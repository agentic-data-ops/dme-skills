"""FlashStorageCLI — SSH 远程登录华为闪存存储设备 CLI，交互式执行命令。

通过启动后台 expect 进程实现 SSH 交互，不使用 pexpect 库。
"""

import argparse
import os
import re
import subprocess
import sys
from typing import Dict, List, Optional

# ---------------------------------------------------------------------------
# Expect 守护进程脚本模板
# ---------------------------------------------------------------------------
# 注意：Tcl 的控制结构（while / if / expect 的 action 块）中的 {} 在
# Python .format() 中需要写为 {{ }}；\r 在 Python 字符串中用 \\r 表示。
_EXPECT_DAEMON_TMPL = r"""set timeout {timeout}
spawn ssh -o StrictHostKeyChecking=no {username}@{address}
expect "password:"
send "{password}\r"
expect "{username}:/>"
puts "==LOGIN_OK=="
flush stdout

while {{1}} {{
    expect_user {{
        -re "(.*)\r" {{
            set command $expect_out(1,string)
        }}
        timeout {{
            continue
        }}
        eof {{
            break
        }}
    }}
    if {{![info exists command]}} {{
        continue
    }}
    if {{$command == "__QUIT__"}} {{
        send "exit\r"
        expect "(y/n):"
        send "y\r"
        expect eof
        exit
    }}
    send "$command\r"
    expect {{
        "(y/n)" {{
            send "y\r"
            exp_continue
        }}
        -re "(:/>|/diagnose>|minisystem>)" {{
            puts $expect_out(buffer)
            flush stdout
        }}
        timeout {{
            puts "==TIMEOUTHIT=="
            flush stdout
        }}
    }}
    unset command
}}
"""


# ---------------------------------------------------------------------------
# Prompt 检测
# ---------------------------------------------------------------------------
# 所有可能的命令行提示符模式
_PROMPT_PATTERNS = [
    r"^[^:]+:/>",           # username:/>  或  engineer:/>  或  developer:/>
    r"^[^:]+:/diagnose>",   # username:/diagnose>
    r"^Storage: minisystem>",  # Storage: minisystem>
]
_PROMPT_RE = re.compile("|".join(_PROMPT_PATTERNS))


def _is_prompt_line(line: str) -> bool:
    """判断一行文本是否匹配某个已知的命令行提示符。"""
    return bool(_PROMPT_RE.match(line.strip()))


# ---------------------------------------------------------------------------
# FlashStorageCLI
# ---------------------------------------------------------------------------

class FlashStorageCLI:
    """通过后台 expect 进程交互华为闪存存储设备 CLI。"""

    # 模式 → (切换命令, 切换后的提示符)
    MODE_PROMPT: Dict[str, str] = {
        "normal": "{username}:/>",
        "engineer": "engineer:/>",
        "developer": "developer:/>",
        "debug": "{username}:/diagnose>",
        "minisystem": "Storage: minisystem>",
    }

    def __init__(
        self,
        address: str,
        username: str,
        password: str,
        mode: str = "normal",
        timeout: int = 60,
    ) -> None:
        self._address = address
        self._username = username
        self._password = password
        self._timeout = timeout

        # 当前状态
        self._current_mode: str = "normal"
        self._prompt: str = f"{username}:/>"

        # 构建 expect 脚本并启动子进程
        script = _EXPECT_DAEMON_TMPL.format(
            address=address,
            username=username,
            password=password,
            timeout=timeout,
        )
        self._proc = subprocess.Popen(
            ["expect", "-c", script],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        # 读取登录确认标记
        ok = self._proc.stdout.readline()  # type: ignore[union-attr]
        if ok is None or "==LOGIN_OK==" not in ok:
            stderr = self._proc.stderr.read()  # type: ignore[union-attr]
            self._proc.terminate()
            raise RuntimeError(
                f"SSH 登录失败（{address}）：{stderr.strip()}"
            )

        # 如果要求非 normal 模式，立即切换
        if mode != "normal":
            self.switch_mode(mode)

    # ------------------------------------------------------------------
    # 底层读写
    # ------------------------------------------------------------------

    def _send_raw(self, command: str) -> None:
        """向 expect 进程发送一行命令（以 \\r 结尾）。"""
        assert self._proc.stdin is not None
        self._proc.stdin.write(f"{command}\r")
        self._proc.stdin.flush()

    def _read_until_prompt(self) -> List[str]:
        """逐行读取 stdout 直到遇到当前提示符，返回中间内容（不含提示符行）。"""
        assert self._proc.stdout is not None
        lines: List[str] = []
        while True:
            line = self._proc.stdout.readline()
            if not line:
                raise RuntimeError("expect 进程意外退出")
            line = line.rstrip("\r\n")
            if _is_prompt_line(line):
                break
            if line == "==TIMEOUTHIT==":
                raise TimeoutError("命令执行超时")
            lines.append(line)
        return lines

    def _exec(self, command: str) -> List[str]:
        """发送一条命令到设备并返回设备输出（每行一个元素）。"""
        self._send_raw(command)
        lines = self._read_until_prompt()
        if not lines:
            return []
        # 去掉第一行（命令回显），其余为实际输出
        return lines[1:]

    # ------------------------------------------------------------------
    # 模式切换
    # ------------------------------------------------------------------

    @property
    def current_mode(self) -> str:
        return self._current_mode

    def switch_mode(self, mode: str) -> None:
        """将设备 CLI 切换到指定模式。

        严格按照设计文档中的 expect 交互序列执行退出 → 进入。
        """
        if mode == self._current_mode:
            return
        if mode not in self.MODE_PROMPT:
            raise ValueError(f"不支持的模式：{mode}")

        # ---- 退出当前模式到 normal ----
        target_prompt = f"{self._username}:/>"

        if self._current_mode in ("engineer", "developer"):
            # 直接 exit → normal
            self._exec("exit")
        elif self._current_mode == "debug":
            # exit → developer → exit → normal
            self._send_raw("exit")
            # 等待 developer:/>
            self._wait_for_prompt("developer:/>")
            self._send_raw("exit")
            self._wait_for_prompt(target_prompt)
        elif self._current_mode == "minisystem":
            # exit → (y/n) → y → (y/n) → y → developer → exit → normal
            self._send_raw("exit")
            self._wait_for_yn(times=2)
            self._wait_for_prompt("developer:/>")
            self._send_raw("exit")
            self._wait_for_prompt(target_prompt)

        self._current_mode = "normal"
        self._prompt = target_prompt

        # ---- 进入目标模式 ----
        if mode == "normal":
            return

        if mode == "engineer":
            self._send_raw("change user_mode current_mode user_mode=engineer")
            self._wait_for_prompt("engineer:/>")
            self._current_mode = "engineer"
            self._prompt = "engineer:/>"

        elif mode == "developer":
            self._send_raw("change user_mode current_mode user_mode=developer")
            self._wait_for_yn(times=2)
            self._wait_for_prompt("developer:/>")
            self._current_mode = "developer"
            self._prompt = "developer:/>"

        elif mode == "debug":
            # 先进入 developer
            self._send_raw("change user_mode current_mode user_mode=developer")
            self._wait_for_yn(times=2)
            self._wait_for_prompt("developer:/>")
            # 再 debug
            self._send_raw("debug")
            self._wait_for_prompt(f"{self._username}:/diagnose>")
            self._current_mode = "debug"
            self._prompt = f"{self._username}:/diagnose>"

        elif mode == "minisystem":
            # 先进入 developer
            self._send_raw("change user_mode current_mode user_mode=developer")
            self._wait_for_yn(times=2)
            self._wait_for_prompt("developer:/>")
            # 再 minisystem
            self._send_raw("minisystem")
            self._wait_for_prompt("Storage: minisystem>")
            self._current_mode = "minisystem"
            self._prompt = "Storage: minisystem>"

    def _wait_for_prompt(self, prompt: str) -> None:
        """读取 stdout 直到遇到指定的提示符行。"""
        assert self._proc.stdout is not None
        while True:
            line = self._proc.stdout.readline()
            if not line:
                raise RuntimeError("expect 进程意外退出")
            line = line.rstrip("\r\n")
            if _is_prompt_line(line):
                # 确认匹配的是我们期望的提示符
                if prompt in line:
                    break
                # 否则继续读 — 可能有多行输出
                continue
            if line == "==TIMEOUTHIT==":
                raise TimeoutError("等待提示符超时")

    def _wait_for_yn(self, times: int = 1) -> None:
        """读取 stdout 跳过指定次数的 (y/n) 风险提示。

        expect 守护进程遇到 (y/n) 时已经自动发送了 "y"，所以我们
        只需要消费输出，直到遇到提示符或 (y/n) 相关行被消耗完毕。
        """
        assert self._proc.stdout is not None
        consumed = 0
        while consumed < times:
            line = self._proc.stdout.readline()
            if not line:
                raise RuntimeError("expect 进程意外退出")
            line = line.rstrip("\r\n")
            if "(y/n)" in line:
                consumed += 1
            elif _is_prompt_line(line):
                break
            elif line == "==TIMEOUTHIT==":
                raise TimeoutError("等待风险提示超时")

    # ------------------------------------------------------------------
    # 命令执行
    # ------------------------------------------------------------------

    def execute_command(self, command: str, mode: Optional[str] = None) -> str:
        """执行一条命令，可选择先切换到指定模式。返回纯命令输出文本。"""
        if mode is not None and mode != self._current_mode:
            self.switch_mode(mode)
        lines = self._exec(command)
        return "\n".join(lines)

    def execute_commands(
        self, commands: List[str], mode: Optional[str] = None
    ) -> List[str]:
        """执行多条命令（均在同一模式下执行）。返回结果列表。"""
        return [self.execute_command(cmd, mode) for cmd in commands]

    # ------------------------------------------------------------------
    # 关闭连接
    # ------------------------------------------------------------------

    def close(self) -> None:
        """断开与设备的连接。

        严格按设计文档：
          1. 退出当前模式到 normal
          2. 发送 exit → expect (y/n): → send y → expect eof
          3. 关闭 expect 子进程
        """
        if self._proc is None:
            return

        # 1. 退出到 normal
        if self._current_mode != "normal":
            cur = self._current_mode
            self._current_mode = "normal"
            self._prompt = f"{self._username}:/>"

            if cur in ("engineer", "developer"):
                self._send_raw("exit")
                try:
                    self._wait_for_prompt(self._prompt)
                except Exception:
                    pass
            elif cur == "debug":
                self._send_raw("exit")
                try:
                    self._wait_for_prompt("developer:/>")
                except Exception:
                    pass
                self._send_raw("exit")
                try:
                    self._wait_for_prompt(self._prompt)
                except Exception:
                    pass
            elif cur == "minisystem":
                self._send_raw("exit")
                try:
                    self._wait_for_prompt("developer:/>")
                except Exception:
                    pass
                self._send_raw("exit")
                try:
                    self._wait_for_prompt(self._prompt)
                except Exception:
                    pass

        # 2. 发送 QUIT 让 expect 进程处理设备退出
        try:
            self._send_raw("__QUIT__")
            self._proc.wait(timeout=10)
        except Exception:
            self._proc.terminate()
            self._proc.wait(timeout=5)
        finally:
            self._proc = None  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# 命令行入口
# ---------------------------------------------------------------------------


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="SSH 远程登录华为闪存存储设备 CLI 并执行命令",
    )
    parser.add_argument(
        "--address",
        default=os.environ.get("STORAGE_ADDRESS", ""),
        required=False,
        help="设备 IP 地址（环境变量 STORAGE_ADDRESS）",
    )
    parser.add_argument(
        "--username",
        default=os.environ.get("STORAGE_USERNAME", ""),
        required=False,
        help="登录用户名（环境变量 STORAGE_USERNAME）",
    )
    parser.add_argument(
        "--password",
        default=os.environ.get("STORAGE_PASSWORD", ""),
        required=False,
        help="登录密码（环境变量 STORAGE_PASSWORD）",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("STORAGE_TIMEOUT", "60")),
        help="命令超时秒数，默认 60（环境变量 STORAGE_TIMEOUT）",
    )
    parser.add_argument(
        "--mode",
        default="normal",
        choices=list(FlashStorageCLI.MODE_PROMPT),
        help="CLI 命令行模式，默认 normal",
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="",
        help="要执行的命令（多条命令用 \\n 分隔）",
    )
    ns = parser.parse_args(argv)

    missing = [k for k in ("address", "username", "password") if not getattr(ns, k)]
    if missing:
        parser.error(f"缺少必填参数：{', '.join(missing)}（可通过环境变量传入）")

    return ns


def main(argv: Optional[List[str]] = None) -> None:
    ns = _parse_args(argv)
    commands = [c.strip() for c in ns.command.split(r"\n") if c.strip()]

    cli = FlashStorageCLI(
        address=ns.address,
        username=ns.username,
        password=ns.password,
        mode=ns.mode,
        timeout=ns.timeout,
    )
    try:
        if not commands:
            print("已连接到设备，当前模式：", cli.current_mode)
            return

        results = cli.execute_commands(commands)
        for i, result in enumerate(results):
            if result:
                print(result)
            if i < len(results) - 1:
                print()
    finally:
        cli.close()


if __name__ == "__main__":
    main()
