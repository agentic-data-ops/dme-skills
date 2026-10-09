"""FlashStorageCLI - SSH login to a Huawei flash storage device CLI and execute commands interactively.

Implemented with paramiko (pure-Python SSH library), compatible with both Windows
and Linux - no system `expect` command is required.

Each call to execute_commands establishes an independent SSH connection:
login -> run commands sequentially -> quit, then closes the connection.
"""
from __future__ import annotations

import argparse
import os
import re
import time
from typing import List

import paramiko


# Device CLI prompts:
#   normal    admin:/>            engineer    engineer:/>
#   developer developer:/>        debug       admin:/diagnose>
#   minisystem Storage: minisystem>
_PROMPT_RE = re.compile(r"(?:[\w-]+:/>|/diagnose>|minisystem>)")
# Risk confirmation prompt (Huawei CLI's (y/n) question)
_CONFIRM_RE = re.compile(r"\(y/n\)")

_RECV_CHUNK = 65535


# ---------------------------------------------------------------------------
# FlashStorageCLI
# ---------------------------------------------------------------------------

class FlashStorageCLI:
    """Login to a Huawei flash storage device CLI over SSH (paramiko) and run batch commands."""

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
    # Entry point
    # ------------------------------------------------------------------

    def execute_commands(
        self, commands: List[str], dumpscript: str | None = None
    ) -> str:
        """Execute multiple commands (one per line, sequentially).

        Args:
            commands: The list of commands to execute.
            dumpscript: Write the interaction log to this file (for debugging).

        Returns:
            The device output text.
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
            raise RuntimeError(f"SSH login failed (authentication error): {ex}") from ex
        except Exception as ex:
            raise RuntimeError(f"SSH connection failed: {ex}") from ex

        shell = client.invoke_shell(width=200, height=50)
        shell.settimeout(self._timeout)
        log = open(dumpscript, "w", encoding="utf-8") if dumpscript else None
        try:
            # Login banner + first prompt (kept as part of the output)
            output = self._read_until_prompt(shell, log)
            for cmd in commands:
                if log:
                    log.write(f">>> {cmd}\n")
                shell.send(cmd + "\r")
                output += self._read_until_prompt(shell, log)
            # Quit the device CLI
            self._quit(shell, log)
            return output
        finally:
            if log:
                log.close()
            client.close()

    # ------------------------------------------------------------------
    # Interaction primitives
    # ------------------------------------------------------------------

    def _read_until_prompt(self, shell, log=None) -> str:
        """Read device output until a CLI prompt appears (auto-accepting (y/n) risk prompts)."""
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
            # Risk confirmation prompt: auto-send "y" and continue
            while _CONFIRM_RE.search(buf):
                buf = _CONFIRM_RE.sub("", buf, count=1)
                shell.send("y\r")
            if _PROMPT_RE.search(buf):
                break
        return buf

    def _quit(self, shell, log=None) -> None:
        """Quit the device CLI: send exit, handle (y/n) confirmations, until the connection closes."""
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
# Command-line entry point
# ---------------------------------------------------------------------------

def _parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="SSH login to a Huawei flash storage device CLI and execute commands",
    )
    parser.add_argument(
        "--address",
        default=os.environ.get("STORAGE_ADDRESS", ""),
        help="device IP address (env STORAGE_ADDRESS)",
    )
    parser.add_argument(
        "--username",
        default=os.environ.get("STORAGE_USERNAME", ""),
        help="login username (env STORAGE_USERNAME)",
    )
    parser.add_argument(
        "--password",
        default=os.environ.get("STORAGE_PASSWORD", ""),
        help="login password (env STORAGE_PASSWORD; prefer passing it via the environment)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("STORAGE_TIMEOUT", "60")),
        help="command timeout in seconds, default 60 (env STORAGE_TIMEOUT)",
    )
    parser.add_argument(
        "--dumpscript",
        default=None,
        help="write the interaction log to this file (for debugging)",
    )
    parser.add_argument(
        "commands",
        nargs="?",
        default="",
        help="commands to execute (multiple commands separated by \\n)",
    )
    ns = parser.parse_args(argv)

    missing = [k for k in ("address", "username", "password") if not getattr(ns, k)]
    if missing:
        parser.error(f"missing required arguments: {', '.join(missing)} (can be set via environment variables)")

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
        print("Please provide commands to execute.")
        return

    try:
        results = cli.execute_commands(commands, args.dumpscript)
    except RuntimeError as ex:
        print(f"Error: {ex}")
        return
    print(results)


if __name__ == "__main__":
    main()
