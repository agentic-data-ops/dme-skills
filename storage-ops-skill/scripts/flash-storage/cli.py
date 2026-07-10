"""FlashStorageCLI — SSH 远程登录华为闪存存储设备 CLI，交互式执行命令。

每次执行命令时构建独立的 expect 脚本，通过 subprocess.run 运行。
不使用后台守护进程，不维护持久连接。
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
from typing import Dict, List

# ---------------------------------------------------------------------------
# Prompt 检测 — 所有模式下的提示符行
# ---------------------------------------------------------------------------
_PROMPT_PATTERNS = [
    r"^[^:]+:/>",           # username:/>  或  engineer:/>  或  developer:/>
    r"^[^:]+:/diagnose>",   # username:/diagnose>
    r"^Storage: minisystem>",  # Storage: minisystem>
]
_PROMPT_RE = re.compile("|".join(_PROMPT_PATTERNS))


def _is_prompt_line(line: str) -> bool:
    return bool(_PROMPT_RE.match(line.strip()))


# ---------------------------------------------------------------------------
# FlashStorageCLI
# ---------------------------------------------------------------------------

class FlashStorageCLI:
    """SSH 远程登录华为闪存存储设备 CLI 并执行命令。

    每次执行命令生成一个完整的 expect 脚本（登录 → 模式切换 → 命令 → 退出），
    通过 subprocess.run 一次性运行。
    """

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
        password: [redacted],
        mode: str = "normal",
        timeout: int = 60,
    ) -> None:
        self._address = address
        self._username = username
        self._password = password
        self._default_mode = mode
        self._timeout = timeout

    # ------------------------------------------------------------------
    # 脚本生成
    # ------------------------------------------------------------------

    @staticmethod
    def _escape_tcl(text: str) -> str:
        """转义 Tcl 双引号字符串中的特殊字符。"""
        return (
            text.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("$", "\\$")
            .replace("[", "\\[")
            .replace("]", "\\]")
        )

    def _prompt_for(self, mode: str) -> str:
        """返回指定模式的实际提示符文本。"""
        m = self.MODE_PROMPT[mode]
        return m.replace("{username}", self._username)

    def _enter_mode_script(self, mode: str) -> List[str]:
        """生成从 normal 进入指定模式的 Tcl 脚本段。"""
        lines: List[str] = []
        target_prompt = self._prompt_for(mode)

        if mode == "engineer":
            lines.append(
                'send "change user_mode current_mode user_mode=engineer\\r"'
            )
            lines.append(f'expect "{target_prompt}"')

        elif mode == "developer":
            lines.append(
                'send "change user_mode current_mode user_mode=developer\\r"'
            )
            lines.append("expect {")
            lines.append('    "(y/n)" { send "y\\r"; exp_continue }')
            lines.append(f'    "{target_prompt}" {{ }}')
            lines.append("}")

        elif mode == "debug":
            dev_prompt = self._prompt_for("developer")
            lines.append(
                'send "change user_mode current_mode user_mode=developer\\r"'
            )
            lines.append("expect {")
            lines.append('    "(y/n)" { send "y\\r"; exp_continue }')
            lines.append(f'    "{dev_prompt}" {{ }}')
            lines.append("}")
            lines.append('send "debug\\r"')
            lines.append(f'expect "{target_prompt}"')

        elif mode == "minisystem":
            dev_prompt = self._prompt_for("developer")
            lines.append(
                'send "change user_mode current_mode user_mode=developer\\r"'
            )
            lines.append("expect {")
            lines.append('    "(y/n)" { send "y\\r"; exp_continue }')
            lines.append(f'    "{dev_prompt}" {{ }}')
            lines.append("}")
            lines.append('send "minisystem\\r"')
            lines.append(f'expect "{target_prompt}"')

        return lines

    def _build_script(self, commands: List[str], mode: str) -> str:
        """生成完整的 expect 脚本。

        登录 → 模式切换（如需）→ 顺序执行命令 → 退出。
        每条命令的输出后跟随提示符行，作为 Python 侧的分隔标记。
        """
        escaped_pass = self._escape_tcl(self._password)
        login_prompt = self._prompt_for("normal")
        cmd_prompt = self._prompt_for(mode)

        parts: List[str] = []

        # 超时
        parts.append(f"set timeout {self._timeout}")

        # 登录
        parts.append(
            f"spawn ssh -o StrictHostKeyChecking=no "
            f"{self._username}@{self._address}"
        )
        parts.append('expect "password:"')
        parts.append(f'send "{escaped_pass}\\r"')
        parts.append(f'expect "{login_prompt}"')

        # 模式切换（从 normal 进入目标模式）
        if mode != "normal":
            parts.extend(self._enter_mode_script(mode))

        # 命令执行
        for cmd in commands:
            escaped_cmd = self._escape_tcl(cmd)
            parts.append(f'send "{escaped_cmd}\\r"')
            parts.append("expect {")
            parts.append('    "(y/n)" { send "y\\r"; exp_continue }')
            parts.append(
                '    -re "(:/>|/diagnose>|minisystem>)" {'
                " puts $expect_out(buffer);"
                " puts $expect_out(0,string)"
                " }"
            )
            parts.append('    timeout { puts "==TIMEOUT==" }')
            parts.append("}")

        # 退出
        if mode != "normal":
            normal_prompt = self._prompt_for("normal")
            parts.append(f'expect "{normal_prompt}"')
        parts.append('send "exit\\r"')
        parts.append('expect "(y/n):"')
        parts.append('send "y\\r"')
        parts.append("expect eof")

        return "\n".join(parts)

    def _parse_results(self, output: str) -> List[str]:
        """从 expect 的 stdout 中分离每条命令的输出。

        输出格式为每条命令：<echo + 输出> + <提示符行> + <下一条...>。
        以提示符行为分隔，剥离首行回显后得到纯结果。
        """
        lines = output.splitlines()
        results: List[str] = []
        current: List[str] = []

        for line in lines:
            if line == "==TIMEOUT==":
                raise TimeoutError("命令执行超时")
            if _is_prompt_line(line):
                if current:
                    # 去掉第一行（命令回显）
                    results.append("\n".join(current[1:]) if len(current) > 1 else "")
                    current = []
                else:
                    results.append("")
                continue
            current.append(line)

        # 末尾可能还有未闭合的输出
        if current:
            results.append("\n".join(current[1:]) if len(current) > 1 else "")

        return results

    # ------------------------------------------------------------------
    # 命令执行
    # ------------------------------------------------------------------

    def execute_command(self, command: str, mode: str | None = None) -> str:
        """执行一条命令。mode 默认使用构造时指定的模式。"""
        results = self.execute_commands([command], mode)
        return results[0] if results else ""

    def execute_commands(
        self, commands: List[str], mode: str | None = None
    ) -> List[str]:
        """执行多条命令（同一 SSH 会话中顺序执行）。

        Args:
            commands: 要执行的命令列表
            mode: 执行模式，None 表示使用 __init__ 时指定的默认模式

        Returns:
            每条命令的输出文本列表
        """
        target_mode = mode if mode is not None else self._default_mode
        if target_mode not in self.MODE_PROMPT:
            raise ValueError(f"不支持的模式：{target_mode}")

        script = self._build_script(commands, target_mode)
        result = subprocess.run(
            ["expect", "-c", script],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            stderr = result.stderr.strip()
            if stderr:
                raise RuntimeError(f"expect 执行失败：{stderr}")

        return self._parse_results(result.stdout)


# ---------------------------------------------------------------------------
# 命令行入口
# ---------------------------------------------------------------------------


def _parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="SSH 远程登录华为闪存存储设备 CLI 并执行命令",
    )
    parser.add_argument(
        "--address",
        default=os.environ.get("STORAGE_ADDRESS", ""),
        help="设备 IP 地址（环境变量 STORAGE_ADDRESS）",
    )
    parser.add_argument(
        "--username",
        default=os.environ.get("STORAGE_USERNAME", ""),
        help="登录用户名（环境变量 STORAGE_USERNAME）",
    )
    parser.add_argument(
        "--password",
        default=os.environ.get("STORAGE_PASSWORD", ""),
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


def main(argv: List[str] | None = None) -> None:
    ns = _parse_args(argv)
    raw_commands = ns.command.split(r"\n") if ns.command else []
    commands = [c for c in raw_commands if c.strip()]

    cli = FlashStorageCLI(
        address=ns.address,
        username=ns.username,
        password=[redacted],
        mode=ns.mode,
        timeout=ns.timeout,
    )
    if not commands:
        print("请输入要执行的命令。")
        return

    results = cli.execute_commands(commands)
    for i, result in enumerate(results):
        if result:
            print(result)
        if i < len(results) - 1 and result:
            print()


if __name__ == "__main__":
    main()
