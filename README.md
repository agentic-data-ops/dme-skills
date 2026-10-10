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

Huawei all-flash storage device operations skill that logs in to the device CLI over SSH and executes batch commands. Core components:

- `SKILL.md` — skill definition and standard workflow
- `scripts/flash-storage/cli.py` — SSH CLI executor built on Python (paramiko, cross-platform Windows/Linux)

### Standard Workflow

1. **Query command help**: Obtain command help from the CLI script (for non-English requests, first extract English keywords to search, as the command-line help is English-only)
2. **Assemble batch commands**: Build the batch command string, one command per line, separated by `\n`
3. **Risk check and confirmation**: Identify risky commands (change-type commands and commands in the High-Risk Command List), show the command list with risky ones annotated, and obtain user confirmation
4. **Execute**: After user confirmation, run `scripts/flash-storage/cli.py` to execute the commands
5. **Summarize**: Summarize the execution results based on the output
6. **Suggest next steps**: Recommend next actions based on the results

### Quick Start

#### 1. Set Environment Variables (password via environment variable is strongly recommended)

```bash
export STORAGE_ADDRESS=192.168.1.10
export STORAGE_USERNAME=admin
export STORAGE_PASSWORD='your-password'
export STORAGE_TIMEOUT=60
```

#### 2. Execute Commands

```bash
python3 storage-ops-skill/scripts/flash-storage/cli.py "show version\nshow storage pool"
```

#### 3. Use the Skill

```text
Install storage-ops-skill

Query the device version and storage pool information, and check for alarms
```

### Notes

- **Risk confirmation**: Risky commands (e.g., change-type commands such as `delete`, `create`, `modify`, and commands in the High-Risk Command List) must be confirmed by the user before execution
- **Language**: The command-line help is English-only; for non-English requests, extract English keywords to search. The final summary should be in the same language as the user's input
- **Password security**: Strongly recommended to pass the password via the `STORAGE_PASSWORD` environment variable to avoid exposing it on the command line

# Disclaimer

1. **Unofficial project**: This project is not officially provided by Huawei DME. It is maintained by individuals and serves only as a reference sample, without technical support.

2. **AI-generated code**: The `dme-python-sdk` this project depends on was fully developed and tested by AI coding tools. A small number of actions have not been actually tested due to lack of environment (the action implementations are consistent with the API). Please evaluate carefully before use.
