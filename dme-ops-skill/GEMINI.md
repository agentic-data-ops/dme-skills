# GEMINI Context: dme-ops-skill

This project is a Python-based CLI tool for the operation and maintenance (O&M) of Huawei DME (Data Management Engine) storage management software. It provides a modular framework for managing SAN, NAS, alarms, health status, and other storage-related tasks via the DME REST API.

## Project Overview

- **Core Goal**: Automate and simplify DME storage O&M tasks through a structured CLI.
- **Key Technologies**: Python 3, `argparse`, `requests`.
- **Primary Entry Point**: `scripts/dme_cli.py`.

## Architecture

- **`scripts/dme_cli.py`**: The central controller. It dynamically loads "topics" from the `actions/` directory and dispatches commands to the appropriate action functions.
- **`scripts/dme_api_client.py`**: Handles authentication and REST API communication (GET, POST, PUT, DELETE). It supports automatic login and session management.
- **`scripts/actions/`**: Contains topic-specific modules (e.g., `storage.py`, `nas.py`, `alarm.py`). Each module defines an `ACTIONS` dictionary that maps CLI action names to implementation functions and specifies their parameters.
- **`scripts/util/`**: Includes utility scripts like `read_api_reference.py` for processing documentation.

## Running the Project

### Environment Setup

Ensure `requests` is installed in your Python environment:
```bash
pip install requests
```

### Configuration

The CLI uses environment variables for authentication. You can export them in your shell:
```bash
export DME_API_ENDPOINT="https://your-dme-ip:port"
export DME_API_USERNAME="admin"
export DME_API_PASSWORD="your-password"
# Optional: export DME_API_AUTH_TOKEN="your-token"
```

### Usage Examples

- **List all available topics and actions**:
  ```bash
  python3 scripts/dme_cli.py --list-topics
  ```

- **Check help for a specific topic**:
  ```bash
  python3 scripts/dme_cli.py storage --help
  ```

- **List storage devices**:
  ```bash
  python3 scripts/dme_cli.py storage list
  ```

- **Wait for an asynchronous task**:
  ```bash
  python3 scripts/dme_cli.py task wait --task_id <id>
  ```

## Development Conventions

- **Action Implementation**:
  - Each action file in `scripts/actions/` should define functions that take a `DMEAPIClient` instance as the first argument.
  - Actions must be registered in a global `ACTIONS` dictionary at the end of the file.
- **Naming Convention**: 
  - Topics correspond to filenames in `scripts/actions/`.
  - Actions within a topic are either "direct" (e.g., `storage list`) or grouped under a "subtopic" (e.g., `storage disk list`).
- **Error Handling**: Use the response from `DMEAPIClient` which returns JSON data from the API. Raise `ValueError` for missing required parameters before making API calls.
- **Documentation**: Use `SKILL.md` for high-level guidance on using this project as a tool for AI agents.

## Todo Tasks

When user ask to finish todo tasks, sequentially execute the unfinished todo tasks step by step. When eath task finished, update the todo task checkbox, and execute git commit and push.

### 代码重构合并任务

**注意**：
- 迁移合并时不要产生依赖关系，每个主题迁移完成后，测试迁移后的命令帮助是否正确。
- 列出主题：python3 scripts/dme_cli.py --list-topics
- 主题帮助：python3 scripts/dme_cli.py <topic> <subtopic> --help

#### san topic
- [x] 将physical_host主题迁移为san主题下的子主题：physical_host => san physical_host
- [x] 将physical_host_group主题迁移为san主题下的子主题：physical_host_group => san physical_host_group
- [x] 将lun_group主题迁移为san主题下的子主题：lun_group => san lun_group
- [x] 将mapping_view主题迁移为san主题下的子主题：mapping_view => san mapping_view
- [x] 将storage主题下的host子主题迁移到san主题下并重命名为storage_host：storage host => san storage_host
- [x] 将storage主题下的host_group子主题迁移到san主题下并重命名为storage_host_group：storage host_group => san storage_host_group
- [x] 将storage主题下的 port_group子主题迁移到san主题下：storage port_group => san port_group
- [x] 删除被迁移的主题

#### aiops topic
- [x] 将alarm主题迁移为aiops主题下的子主题：alarm=> aiops alarm
- [x] 将diagnose task 迁移到aiops主题下：diagnose task => aiops diagnose_task;
- [x] 将performance主题下的动作迁移到aiops主题：performance collect_task create/download => aiops performance create_collect_task/download_collect_result, performance data query => aiops performance query, performance indicator detail/list => aiops performance show_indicators/list_indicators, performance object_type list=> aiops performance list_object_types;
- [x] 将policy result迁移到aiops主题：policy result show/list => aiops check_result show/list，迁移完成后移除policy.py中被迁移到aiops.py的函数
- [x] 将policy主题迁移为aiops子主题：policy => aiops check_policy;
- [x] 将topology主题迁移为aiops子主题：topology => aiops topology.
- [x] 删除被迁移的主题.


