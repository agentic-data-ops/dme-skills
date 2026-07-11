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
# FlashStorageCLI
# ---------------------------------------------------------------------------

class FlashStorageCLI:
    """SSH 远程登录华为闪存存储设备 CLI 并执行命令。

    每次执行命令生成一个完整的 expect 脚本（登录 → 模式切换 → 命令 → 退出），
    通过 subprocess.run 一次性运行。
    """

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

    def _build_script(self, commands: List[str]) -> str:
        """生成完整的 expect 脚本。

        登录 → 模式切换（如需）→ 顺序命令执行 → 退出模式 → 退出 CLI。
        """
        blocks: List[str] = []

        blocks.append(f"""
        set timeout {self._timeout}
        spawn ssh -o StrictHostKeyChecking=no {self._username}@{self._address}
        expect "password:"
        send "{self._password}\r"
        expect ":/>"
        """.replace("        ", ""))
        
        for command in commands:
            blocks.append(f"""
            send "{command}\r"
            expect {{ 
                "(y/n):" {{ send "y\r"; exp_continue }}
                -re ":/>|:/diagnose>|minisystem>" {{ }}
            }}
            """.replace("            ", ""))
        
        blocks.append(f"""
        send "exit\r"
        expect {{ 
            "(y/n):" {{ send "y\r"; exp_continue }}
            -re ":/>|:/diagnose>|minisystem>" {{ send "exit\r"; exp_continue }}
            eof {{ }}
        }}
        """.replace("        ", ""))

        return "\n".join(blocks)

    def execute_commands(
        self, commands: List[str], dumpscript: str | None = None
    ) -> List[str]:
        """执行多条命令。

        Args:
            commands: 要执行的命令列表

        Returns:
            输出文本
        """
        script = self._build_script(commands)
        if dumpscript:
            with open(dumpscript, "w", encoding="utf-8") as f:
                f.write(script)
        
        result = subprocess.run(
            ["expect", "-c", script],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            stderr = result.stderr.strip()
            if stderr:
                raise RuntimeError(f"expect 执行失败：{stderr}")

        return result.stdout


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
        "--dumpscript",
        default=None,
        help="导出 expect 脚本到指定文件（用于调试）",
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

    results = cli.execute_commands(commands, args.dumpscript)
    print(results)

if __name__ == "__main__":
    main()
