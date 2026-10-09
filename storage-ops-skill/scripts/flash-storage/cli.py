"""FlashStorageCLI — SSH 远程登录华为闪存存储设备 CLI，交互式执行命令。

基于 paramiko（纯 Python SSH 库）实现，兼容 Windows 和 Linux，
无需安装系统 expect 命令。

每次 execute_commands 建立独立 SSH 连接：登录 → 顺序执行命令 → 退出，
与设备交互结束后关闭连接。
"""
from __future__ import annotations

import argparse
import os
import re
import time
from typing import List

import paramiko


# 设备 CLI 提示符：
#   normal    admin:/>            engineer    engineer:/>
#   developer developer:/>        debug       admin:/diagnose>
#   minisystem Storage: minisystem>
_PROMPT_RE = re.compile(r"(?:[\w-]+:/>|/diagnose>|minisystem>)")
# 风险确认提示（华为 CLI 的 (y/n) 询问）
_CONFIRM_RE = re.compile(r"\(y/n\)")

_RECV_CHUNK = 65535


# ---------------------------------------------------------------------------
# FlashStorageCLI
# ---------------------------------------------------------------------------

class FlashStorageCLI:
    """通过 paramiko SSH 登录华为闪存存储设备 CLI 并执行批量命令。"""

    def __init__(
        self,
        address: str,
        username: str,
        password: str,
        timeout: int = 60,
    ) -> None:
        self._address = address
        self._username = username
        self._password = password
        self._timeout = timeout

    # ------------------------------------------------------------------
    # 执行入口
    # ------------------------------------------------------------------

    def execute_commands(
        self, commands: List[str], dumpscript: str | None = None
    ) -> str:
        """执行多条命令（每个命令一行，顺序执行）。

        Args:
            commands: 要执行的命令列表
            dumpscript: 导出交互日志到指定文件（用于调试）

        Returns:
            设备输出文本
        """
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(
                self._address,
                username=self._username,
                password=self._password,
                timeout=self._timeout,
                auth_timeout=self._timeout,
                look_for_keys=False,
                allow_agent=False,
            )
        except paramiko.AuthenticationException as ex:
            raise RuntimeError(f"SSH 登录失败（认证错误）：{ex}") from ex
        except Exception as ex:
            raise RuntimeError(f"SSH 连接失败：{ex}") from ex

        shell = client.invoke_shell(width=200, height=50)
        shell.settimeout(self._timeout)
        log = open(dumpscript, "w", encoding="utf-8") if dumpscript else None
        try:
            # 登录横幅 + 首个提示符
            self._read_until_prompt(shell, log)
            outputs: List[str] = []
            for cmd in commands:
                if log:
                    log.write(f">>> {cmd}\n")
                shell.send(cmd + "\r")
                outputs.append(self._read_until_prompt(shell, log))
            # 退出设备 CLI
            self._quit(shell, log)
            return "\n".join(outputs)
        finally:
            if log:
                log.close()
            client.close()

    # ------------------------------------------------------------------
    # 交互原语
    # ------------------------------------------------------------------

    def _read_until_prompt(self, shell, log=None) -> str:
        """读取设备输出直到出现 CLI 提示符（自动接受 (y/n) 风险确认）。"""
        buf = ""
        deadline = time.monotonic() + self._timeout
        while time.monotonic() < deadline:
            try:
                data = shell.recv(_RECV_CHUNK).decode("utf-8", "replace")
            except (TimeoutError, OSError, paramiko.SSHException):
                break
            if not data:
                break
            buf += data
            if log:
                log.write(data)
            # 风险确认提示：自动发送 y 继续执行
            while _CONFIRM_RE.search(buf):
                buf = _CONFIRM_RE.sub("", buf, count=1)
                shell.send("y\r")
            if _PROMPT_RE.search(buf):
                break
        return buf

    def _quit(self, shell, log=None) -> None:
        """退出设备 CLI：发送 exit，处理 (y/n) 确认，直至连接关闭。"""
        try:
            for _ in range(5):
                shell.send("exit\r")
                try:
                    data = shell.recv(_RECV_CHUNK).decode("utf-8", "replace")
                except (TimeoutError, OSError, paramiko.SSHException):
                    break
                if not data:
                    break
                if log:
                    log.write(data)
                if _CONFIRM_RE.search(data):
                    shell.send("y\r")
        except Exception:
            pass


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
        help="登录密码（环境变量 STORAGE_PASSWORD，建议通过环境变量传入）",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("STORAGE_TIMEOUT", "60")),
        help="命令超时秒数，默认 60（环境变量 STORAGE_TIMEOUT）",
    )
    parser.add_argument(
        "--dumpscript",
        default=None,
        help="导出交互日志到指定文件（用于调试）",
    )
    parser.add_argument(
        "commands",
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
    args = _parse_args(argv)
    raw_commands = args.commands.split(r"\n") if args.commands else []
    commands = [c for c in raw_commands if c.strip()]

    cli = FlashStorageCLI(
        address=args.address,
        username=args.username,
        password=args.password,
        timeout=args.timeout,
    )
    if not commands:
        print("请输入要执行的命令。")
        return

    try:
        results = cli.execute_commands(commands, args.dumpscript)
    except RuntimeError as ex:
        print(f"错误：{ex}")
        return
    print(results)


if __name__ == "__main__":
    main()
