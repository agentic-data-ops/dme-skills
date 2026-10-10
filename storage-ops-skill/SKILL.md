---
name: storage-ops-skill
description: Huawei storage device operations skill, currently supporting Huawei all-flash storage devices. Executes CLI commands on the device via SSH (scripts/flash-storage/cli.py).
---

# Huawei Storage Operations Skill

Huawei storage device operations skill. It currently supports **Huawei all-flash (flash) storage devices** (e.g., OceanStor Dorado V6 series) by logging in to the device CLI over SSH and executing commands through `scripts/flash-storage/cli.py`.

## Prerequisites

- Python 3 with the `paramiko` library installed: `pip install paramiko`
- Network reachability from the execution host to the storage device management port (SSH)

> Note: The CLI is implemented purely in Python (paramiko) and works on both Windows and Linux — no system `expect` command is required.

## Setting Environment Variables

The CLI reads connection settings from environment variables. **Strongly recommended: set the password via the `STORAGE_PASSWORD` environment variable instead of passing it as a command-line argument**, because command-line arguments may leak the password into shell history, process lists, and logs.

```bash
export STORAGE_ADDRESS=192.168.1.10        # device IP address
export STORAGE_USERNAME=admin              # login username
export STORAGE_PASSWORD='your-password'    # login password (prefer environment variable)
export STORAGE_TIMEOUT=60                  # command timeout in seconds (default 60)
```

Then run commands without putting any secret on the command line:

```bash
python3 scripts/flash-storage/cli.py "show version\nshow storage pool"
```

## Command Line Interface

Run `scripts/flash-storage/cli.py` to execute one or more commands on the device:

```bash
python3 scripts/flash-storage/cli.py --address <IP> --username <user> "cmd1\ncmd2\ncmd3"
```

### Arguments

| Argument | Description | Environment Variable |
|---|---|---|
| `--address` | Device IP address | `STORAGE_ADDRESS` |
| `--username` | Login username | `STORAGE_USERNAME` |
| `--password` | Login password (prefer environment variable) | `STORAGE_PASSWORD` |
| `--timeout` | Command timeout in seconds, default 60 | `STORAGE_TIMEOUT` |
| `--logfile` | Write the interaction log to a file (for debugging) | — |
| `commands` | Positional argument: batch commands separated by literal `\n`, **one command per line** | — |

### Notes

- Batch commands are separated by the literal two-character sequence `\n` (backslash-n). Pass them inside double quotes, e.g. `"show version\nshow alarm"`, or build the string with `printf`.
- The CLI connects via SSH, enters the device CLI, executes the commands sequentially, and prints the device output.

> Note: The command-line help is available in English only. If the user asks in another language, **extract the English keywords** of the intended commands (e.g., translate "创建LUN" → `create lun`) and search the help with those English keywords.

## Standard Workflow

1. **Query command help**: Obtain the command help (Format, Parameters, Example) provided by the CLI script. If the user's request is not in English, extract the English keywords first and use them to look up the help.
2. **Assemble the batch commands**: Build the batch command string, **one command per line**, joined with `\n`.
3. **Risk check and confirmation**: Determine whether any command is a risky command (see [Risk Commands](#risk-commands)). Show the full command list that is about to run, mark the risky ones, and ask the user whether to continue.
4. **Execute**: After the user confirms, run `python3 scripts/flash-storage/cli.py "cmd1\ncmd2\n..."` and capture the output.
5. **Summarize**: Summarize the execution results based on the output (success/failure per command, returned data, task status).
6. **Suggest next steps**: Recommend the next actions based on the results and the available command help.

## Risk Commands

A command is considered **risky** if:

- It is a high-risk operation (e.g., destructive or irreversible operations listed in the device's high-risk command list), or
- It is a change-type operation: `create`, `delete`, `modify`, `add`, `remove`, `change`, `set`, `reset`, `clear`, `enable`, `disable`, etc.

Read-only query commands (`show`, `display`, `list`, `get`, `query`) are generally **not** risky and may be executed without confirmation when the user has already asked for the information.

Before executing any batch that contains risky commands, present the full command list with the risky commands annotated, and ask the user for explicit confirmation.

## Notes

- **Response language**: Keep the final summary and recommendations in the **same language the user used** in their request.
- **Async operations**: Some commands return asynchronous task results; if the output indicates an ongoing task, suggest following up with the corresponding query commands.
- **Large outputs**: Prefer query commands with filters/conditions from the command help to avoid huge output.
- **Failure handling**: If execution fails, inspect the output and retry with corrected parameters rather than inventing new commands.
