---
name: storage-ops-skill
description: Huawei storage device operations skill, currently supporting Huawei all-flash storage devices. Executes CLI commands on the device via SSH using the flash-storage-cli command.
---

# Huawei Storage Operations Skill

Huawei storage device operations skill. It currently supports **Huawei all-flash (flash) storage devices** (e.g., OceanStor Dorado V6 series) by logging in to the device CLI over SSH and executing commands through the `flash-storage-cli` command.

## Prerequisites

- Python 3 with the `flash-storage-cli` package installed:

  ```bash
  pip install git+https://github.com/agentic-data-ops/flash-storage-cli.git
  ```

  This installs the `flash-storage-cli` console command (together with the bundled command help docs and the high-risk command list).

- Network reachability from the execution host to the storage device management port (SSH)

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
flash-storage-cli "show system general\nshow storage_pool general"
```

## Command Line Interface

Run `flash-storage-cli` to execute one or more commands on the device:

```bash
flash-storage-cli --address <IP> --username <user> "show system general\nshow storage_pool general"
```

### Arguments

| Argument | Description | Environment Variable |
|---|---|---|
| `--address` | Device IP address | `STORAGE_ADDRESS` |
| `--username` | Login username | `STORAGE_USERNAME` |
| `--password` | Login password (prefer environment variable) | `STORAGE_PASSWORD` |
| `--timeout` | Command timeout in seconds, default 60 | `STORAGE_TIMEOUT` |
| `--logfile` | Write the interaction log to a file (for debugging) | — |
| `--accept-risk` | Accept high-risk commands: print warnings and continue instead of rejecting execution | `STORAGE_ACCEPT_RISK=true` |
| `--dry-run` | Validate commands (existence, required parameters, risk) without executing them or connecting to the device | — |
| `--list-topics` | List all command topics (command help, no device connection needed) | — |
| `--list-commands` | List the commands of a command group, e.g. `base` (command help, no device connection needed) | — |
| `--show-command-help` | Show the help of a command, e.g. `"create lun"` (no device connection needed) | — |
| `commands` | Positional argument: batch commands separated by literal `\n`, **one command per line** | — |

### Notes

- Batch commands are separated by the literal two-character sequence `\n` (backslash-n). Pass them inside double quotes, e.g. `"show system general\nshow storage_pool general"`, or build the string with `printf`.
- The CLI connects via SSH, enters the device CLI, executes the commands sequentially, and prints the device output.
- `--dry-run` is a pure offline validation: it reports whether each command exists, whether required parameters are missing, and whether any command hits the high-risk command list — no device connection is made.

> Note: The command-line help is available in English only. If the user asks in another language, **extract the English keywords** of the intended commands (e.g., translate "创建LUN" → `create lun`) and search the help with those English keywords.

## Reference Document Key Sections

`reference/flash-storage-cli/README.md` — the flash-storage-cli project README. Key sections for command-line usage:

| Section | Description |
|---|---|
| Installation | How to install the `flash-storage-cli` package with pip from the Git repository. |
| Command-line options | The full list of `flash-storage-cli` options and their meanings. |
| Examples | Sample invocations: single command, multiple commands, environment-variable based, and offline command help. |

## Command Line Conventions

A command line consists of several segments:

- **Starting segment**: general descriptor of an activity to be performed, such as `change` and `show`.
- **Second segment**: performer of the activity, such as `storage_pool` and `host`.
- **Third segment** (available for certain commands): attribute of the performer, such as `relocation_speed`.
- **Remaining segments**: parameters required for the command.

Command line conventions:

| Pattern | Definition |
|---|---|
| **Bold** | The keywords of a command line, which must not be changed. |
| *Italic* | The parameters of a command line, which will be replaced by actual values. |
| `[ ]` | Items (keywords or parameters) in brackets `[ ]` are optional. |
| `{ x \| y \| ... }` | Optional items are grouped in braces `{}` and separated by vertical bars (`\|`); one item must be selected. |
| `[ x \| y \| ... ]` | Optional items are grouped in brackets `[]` and separated by vertical bars (`\|`); one or no item is selected. |
| `{ x \| y \| ... } *` | Optional items are grouped in braces and separated by vertical bars; at least one item or all items at most are selected. |
| `[ x \| y \| ... ] *` | Optional items are grouped in brackets and separated by vertical bars; more than one or no item is selected. |

Example: the `change user user_name=? { level=? \| action=? }` command implies that `change user` is a fixed keyword, `user_name=?` is required, either `level=?` or `action=?` is used, and the `?` in `level=?` is replaced with an actual value such as `level=admin`.

## CLI Command Filtering

### Column Filtering Command

`show xxx|filterColumn { exclude \| include } columnList=?` is used to filter column information off a command output.

- `xxx` is the ending keywords of the command that you want to query column information for.
- If the name of a selected column field contains a space, replace the space with `\s`. For example, to query the **Write Policy** column for LUNs, run `show lun general|filterColumn include columnList=Write\sPolicy`.

| Parameter | Description |
|---|---|
| `exclude` | Column fields available for filtering that do not need to be displayed. |
| `include` | Column fields available for filtering that need to be displayed. |
| `columnList=?` | Column fields that are available for filtering; separate multiple fields by commas. |

### Row Filtering Command

`show xxx |filterRow column=? predict=? [ predict2=? ] value=? [ logicOp=? ]` is used to filter row information off a command output.

- `xxx` is the ending keywords of the command that you want to query row information for.
- If the name of a selected column field contains a space, replace the space with `\s`. For example, to query the **Write Policy** column for LUNs, run `show lun general|filterRow column=Write\sPolicy`.

| Parameter | Description |
|---|---|
| `column=?` | Column fields that you want to include into a filtering. |
| `predict=?` | A filter condition: `not`, `equal_to`, `greater_than`, `greater_equal`, `less_than`, `less_equal`, or `match` (regular expression match). |
| `predict2=?` | Additional filter condition; required when `predict=?` is set to `not`. |
| `value=?` | Value of a field. |
| `logicOp=?` | Logical relationship between multiple column fields: `and` (match all) or `or` (match any). |

## Standard Workflow

1. **Query command help**: Use the CLI help parameters to look up command help before executing:
   - `--list-topics` — browse all command topics
   - `--list-commands <group>` — list the commands of a command group (e.g. `base`, `lun`, `user`)
   - `--show-command-help <command>` — view the full help (Format, Parameters, Example) of a command
   
   If the user's request is not in English, extract the English keywords first and use them with the help parameters.
2. **Assemble the batch commands**: Build the batch command string, **one command per line**, joined with `\n`.
3. **Validate with `--dry-run`**: Run `flash-storage-cli --dry-run "<commands>"` to check every command offline. The output is an aligned table with columns `[#]`, `valid` (`OK`/`FAIL`), `risk` (`LOW`/`HIGH`) and `command`:
   - `valid = FAIL` means the command does not exist or required parameters are missing (the missing ones are listed under the row),
   - `risk = HIGH` means the command hits the high-risk command list (otherwise `LOW`).
   No device connection is made at this step.
4. **Fix invalid commands**: If the dry-run reports a command as `FAIL`, look up its help with `--show-command-help` (e.g. `flash-storage-cli --show-command-help "create lun"`), determine the required parameters, and rebuild the command. Repeat the dry-run until every command is `OK`.
5. **Risk confirmation**: If the dry-run output shows any `HIGH` risk and ends with "Contains HIGH-risk command(s). Present the risky commands to the user and ask whether to accept the risk.
6. **Execute**: After the user confirms, run `flash-storage-cli "show system general\nshow storage_pool general"` and capture the output. The same dry-run validation runs again before execution: it stops if a command is invalid, and it stops on `HIGH` risk unless `--accept-risk` is given. If the user accepted the risk, append `--accept-risk` to the execution command; otherwise do not execute the risky batch.
7. **Summarize**: Summarize the execution results based on the output (success/failure per command, returned data, task status).
8. **Suggest next steps**: Recommend the next actions based on the results and the available command help.

## Notes

- **Response language**: Keep the final summary and recommendations in the **same language the user used** in their request.
- **Async operations**: Some commands return asynchronous task results; if the output indicates an ongoing task, suggest following up with the corresponding query commands.
- **Large outputs**: Prefer query commands with filters/conditions from the command help to avoid huge output.
- **Failure handling**: If execution fails, inspect the output and retry with corrected parameters rather than inventing new commands.
