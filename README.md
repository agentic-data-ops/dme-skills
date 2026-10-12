# DME Skills

[English](./README.md) | [简体中文](./README_zh.md)

A collection of DME operations skills for day-to-day storage device administration.

## dme-ops-skill

DME operations skill covering **monitoring, analysis, and configuration operations** for storage devices. It interacts with the DME RESTful API through the `pydme` CLI tool and supports:

- **Storage device management** — query/configure storage pools, LUNs, file systems, hosts, etc.
- **System management** — task tracking, system configuration, login authentication
- **Alarms & monitoring** — view device alarms, running status, performance data
- **SAN & NAS** — unified management of block storage and file storage
- **Virtualization & containers** — integration with virtualization and Kubernetes environments
- **Data protection** — backup and disaster recovery policy management
- **Intelligent operations** — AIOps anomaly detection and analysis

### Quick Start

#### 1. Install Dependencies

```bash
pip install git+https://github.com/agentic-data-ops/dme-python-sdk.git
```

#### 2. Set Environment Variables

```bash
export DME_API_ENDPOINT=https://dme-float-ip:26335
export DME_API_USERNAME=your-username
export DME_API_PASSWORD=your-password
```

#### 3. Verify the Connection

```bash
pydme system show
```

#### 4. Use the Skill

```text
Install dme-ops-skill

List storage devices, select the most idle Dorado storage device, and create two 100GB LUNs
```

## storage-ops-skill

Huawei all-flash storage device operations skill that logs in to the device CLI over SSH and executes batch commands. It depends on the standalone [`flash-storage-cli`](https://github.com/agentic-data-ops/flash-storage-cli) command-line tool (pure Python/paramiko, cross-platform Windows/Linux).

Core components:

- `SKILL.md` — skill definition and standard workflow
- `reference/flash-storage-cli/` — reference docs: README, glossary, acronyms and abbreviations

### Standard Workflow

1. **Install flash-storage-cli**: `pip install git+https://github.com/agentic-data-ops/flash-storage-cli.git`
2. **Query command help**: Use `flash-storage-cli --list-topics`, `--list-commands <group>[,<group>...]` and `--show-command-help <command>[,<command>...]` (for non-English requests, first extract English keywords to search, as the command-line help is English-only)
3. **Assemble batch commands**: Build the batch command string, one command per line, separated by `\n`
4. **Validate with `--dry-run`**: Run `flash-storage-cli --dry-run "<commands>"` to check command existence, required parameters and risk level (`LOW`/`HIGH`) without touching the device; fix invalid commands via command help and repeat until all are `OK`
5. **Risk confirmation**: If any command is `HIGH` risk, present the risky commands to the user and ask whether to accept the risk
6. **Execute**: After user confirmation, run `flash-storage-cli "<commands>"` (append `--accept-risk` if the user accepted the risk); the same validation runs again before execution and stops on invalid or unaccepted `HIGH`-risk commands
7. **Summarize**: Summarize the execution results based on the output
8. **Suggest next steps**: Recommend next actions based on the results

### Quick Start

#### 1. Install flash-storage-cli

```bash
pip install git+https://github.com/agentic-data-ops/flash-storage-cli.git
```

#### 2. Set Environment Variables (password via environment variable is strongly recommended)

```bash
export STORAGE_ADDRESS=192.168.1.10
export STORAGE_USERNAME=admin
export STORAGE_PASSWORD='your-password'
export STORAGE_TIMEOUT=60
```

#### 3. Execute Commands

```bash
flash-storage-cli "show system general\nshow storage_pool general"
```

#### 4. Use the Skill

```text
Install storage-ops-skill

Query the device version and storage pool information, and check for alarms
```

### Notes

- **Risk confirmation**: Risky commands (e.g., change-type commands such as `delete`, `create`, `modify`, and commands in the High-Risk Command List) are marked `HIGH` by the CLI; execution requires the user to accept the risk via `--accept-risk`
- **Language**: The command-line help is English-only; for non-English requests, extract English keywords to search. The final summary should be in the same language as the user's input
- **Password security**: Strongly recommended to pass the password via the `STORAGE_PASSWORD` environment variable to avoid exposing it on the command line

# Disclaimer

1. **Unofficial project**: This project is not officially provided by Huawei DME. It is maintained by individuals and serves only as a reference sample, without technical support.

2. **AI-generated code**: The `dme-python-sdk` this project depends on was fully developed and tested by AI coding tools. A small number of actions have not been actually tested due to lack of environment (the action implementations are consistent with the API). Please evaluate carefully before use.
