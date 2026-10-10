# flash-storage-cli

An SSH command-line client for managing Huawei flash storage devices.

`flash-storage-cli` logs into a Huawei storage device CLI over SSH (via [paramiko](https://github.com/paramiko/paramiko), a pure-Python SSH library) and executes commands interactively. It works on both Windows and Linux — no system `expect` tool is required.

Key features:

- **Command execution** — run one or more device CLI commands in a single session: SSH login → run commands sequentially → quit.
- **Offline validation** — `--dry-run` checks command existence, required parameters, and high-risk level before touching the device; the same validation runs automatically before every execution.
- **Risk protection** — commands that match the bundled high-risk command list are blocked by default; `--accept-risk` accepts the risk explicitly.
- **Risk prompt handling** — `(y/n)` confirmation prompts raised by the device CLI are auto-accepted.
- **Offline command help** — browse command topics, groups, and per-command help (Format, Parameters, Example) locally from bundled docs, with **no device connection needed**.
- **Environment-variable based configuration** — credentials and options can be supplied via environment variables.

## Directory structure

```
flash-storage-cli/
├── pyproject.toml                  # Packaging & build config (pip package: flash-storage-cli)
├── MANIFEST.in                     # sdist exclusions (reference/, .reasonix/, .git/)
├── .gitignore
├── flash_storage/                  # Python package
│   ├── __init__.py
│   ├── cli.py                      # CLI entry point (flash-storage-cli command)
│   ├── gen_help_docs.py            # Helper: generate docs/ + config/high-risk-commands.json
│   ├── config/
│   │   ├── command-group-description.json   # Topic descriptions
│   │   └── high-risk-commands.json          # High-risk command list ({command: function})
│   └── docs/                       # Bundled command help docs (packaged into the wheel)
│       ├── _topics.md              # All topics overview
│       └── <topic>/                # One dir per topic, e.g. base/, storage_pool/
│           ├── _index.md           # Command list of the topic
│           └── <command>.md        # Per-command help, e.g. show-system-general.md
└── reference/                      # Command reference source (NOT packaged)
    └── flash-storage/
        └── command-reference.md
```

## Installation

Install the package directly from the Git repository with pip:

```bash
pip install git+https://github.com/agentic-data-ops/flash-storage-cli.git
```

This installs the `flash-storage-cli` console command (entry point: `flash_storage.cli:main`) together with the code, `config/` and `docs/` files.

## Usage

### Command-line options

```
flash-storage-cli [options] [commands]
```

| Option | Description |
|---|---|
| `--address ADDRESS` | Device IP address. Env: `STORAGE_ADDRESS`. |
| `--username USERNAME` | Login username. Env: `STORAGE_USERNAME`. |
| `--password PASSWORD` | Login password. Env: `STORAGE_PASSWORD` (prefer the environment variable). |
| `--timeout TIMEOUT` | Command timeout in seconds (default `60`). Env: `STORAGE_TIMEOUT`. |
| `--logfile LOGFILE` | Write the interaction log to this file (debugging). |
| `--accept-risk` | Accept high-risk commands: print warnings and continue instead of rejecting. Env: `STORAGE_ACCEPT_RISK=true`. |
| `--dry-run` | Validate commands (existence, required parameters, risk) without executing them. |
| `--list-topics` | List all command topics (offline help, no device connection). |
| `--list-commands GROUP` | List the commands of a topic, e.g. `base` (offline help). |
| `--show-command-help COMMAND` | Show the help of a command, e.g. `"create lun"` (offline help). |
| `commands` | Commands to execute, multiple commands separated by `\n`. |

Credentials are required unless one of the offline help options (`--list-topics`, `--list-commands`, `--show-command-help`) or `--dry-run` is used.

### Dry-run validation

Validate a batch of commands **without connecting to the device** — checks command existence, required parameters, and risk level:

```bash
flash-storage-cli --dry-run "show system general\ncreate lun name=LUN1"
```

```
Dry-run validation (no command will be executed):
[#]  valid   risk    command
---  ------  ------  ------------------------
[1]  OK      LOW     show system general
[2]  FAIL    LOW     create lun name=LUN1
                     missing required parameter(s): capacity, one of: pool_id, pool_name
```

- `valid`: `OK` means the command exists and all required parameters are present; `FAIL` means the command was not found or required parameters are missing (the missing ones are listed under the row).
- `risk`: `HIGH` means the command matches the bundled high-risk command list; `LOW` otherwise.

The same validation also runs **before every real execution**: execution stops if any command is invalid, and stops on `HIGH`-risk commands unless `--accept-risk` is given.

### Risk check

Commands that match the bundled high-risk command list are marked `HIGH` in the validation table. By default execution is blocked when the batch contains `HIGH`-risk commands:

```
Contains HIGH-risk command(s). Specify --accept-risk to accept the risk and proceed.
```

Pass `--accept-risk` (or set `STORAGE_ACCEPT_RISK=true`) to accept the risk and continue execution.

### Examples

Execute a single command:

```bash
flash-storage-cli --address 192.168.1.10 --username admin --password 'P@ssw0rd' "show system general"
```

Execute multiple commands in one session (separated by `\n`):

```bash
flash-storage-cli --address 192.168.1.10 --username admin --password 'P@ssw0rd' "show system general\nshow storage_pool general"
```

The same via environment variables:

```bash
export STORAGE_ADDRESS=192.168.1.10
export STORAGE_USERNAME=admin
export STORAGE_PASSWORD='P@ssw0rd'

flash-storage-cli "show system general\nshow storage_pool general"
```

Browse offline command help (no device connection required):

```bash
flash-storage-cli --list-topics
flash-storage-cli --list-commands base
flash-storage-cli --show-command-help "show system general"
flash-storage-cli --show-command-help "show storage_pool general"
```

## Disclaimer

1. **Unofficial project**: This project is not officially provided by Huawei Storage. It is maintained by individuals, provides reference samples only, and offers no technical support.

2. **AI-generated code**: The code in this project is fully developed and tested by AI coding tools. Please evaluate carefully before use.
