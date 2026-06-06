# Claude Code: dme-ops-skill

This project is a Python-based CLI tool for the operation and maintenance (O&M) of Huawei DME (Data Management Engine) storage management software. It provides a modular framework for managing SAN, NAS, alarms, health status, and other storage-related tasks via the DME REST API.

## Project Overview

- **Core Goal**: Automate and simplify DME storage O&M tasks through a structured CLI.
- **Key Technologies**: Python 3, `argparse`, `requests`.
- **Primary Entry Point**: `scripts/dme_cli.py`.

## Architecture

- **`scripts/dme_cli.py`**: The central controller. It dynamically loads "topics" from the `actions/` directory and dispatches commands to the appropriate action functions.
- **`scripts/dme_api_client.py`**: Handles authentication and REST API communication (GET, POST, PUT, DELETE). It supports automatic login and session management.
- **`scripts/actions/`**: Contains topic-specific modules (e.g., `storage.py`, `nas.py`, `aiops.py`). Each module defines an `ACTIONS` dictionary that maps CLI action names to implementation functions and specifies their parameters.
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
  python scripts/dme_cli.py --list-topics
  ```

- **Check help for a specific topic**:
  ```bash
  python scripts/dme_cli.py storage --help
  ```

- **List storage devices**:
  ```bash
  python scripts/dme_cli.py storage list
  ```

- **Wait for an asynchronous task**:
  ```bash
  python scripts/dme_cli.py task wait --task_id <id>
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

When user ask to finish todo tasks, sequentially execute the unfinished todo tasks step by step. When each task finished, update the todo task checkbox, and execute git commit and push.

### Code Refactoring and Consolidation Tasks

**Notes**:
- Do not create dependencies during migration and consolidation. After each topic migration is completed, test whether the migrated command help is correct.
- List topics: `python scripts/dme_cli.py --list-topics`
- Topic help: `python scripts/dme_cli.py <topic> <subtopic> --help`

#### san topic
- [x] Migrate physical_host topic to san subtopic: physical_host => san physical_host
- [x] Migrate physical_host_group topic to san subtopic: physical_host_group => san physical_host_group
- [x] Migrate lun_group topic to san subtopic: lun_group => san lun_group
- [x] Migrate mapping_view topic to san subtopic: mapping_view => san mapping_view
- [x] Migrate storage host subtopic to san and rename to storage_host: storage host => san storage_host
- [x] Migrate storage host_group subtopic to san and rename to storage_host_group: storage host_group => san storage_host_group
- [x] Migrate storage port_group subtopic to san: storage port_group => san port_group
- [x] Delete migrated topics

#### aiops topic
- [x] Migrate alarm topic to aiops subtopic: alarm => aiops alarm
- [x] Migrate diagnose task to aiops: diagnose task => aiops diagnose_task
- [x] Migrate performance actions to aiops:
  - performance collect_task create/download => aiops performance create_collect_task/download_collect_result
  - performance data query => aiops performance query
  - performance indicator detail/list => aiops performance show_indicators/list_indicators
  - performance object_type list => aiops performance list_object_types
- [x] Migrate policy result to aiops: policy result show/list => aiops check_result show/list, remove migrated functions from policy.py after migration
- [x] Migrate policy topic to aiops subtopic: policy => aiops check_policy
- [x] Migrate topology topic to aiops subtopic: topology => aiops topology
- [x] Migrate health topic to aiops subtopic:
  - health data query => aiops health query_data
  - health score list => aiops health show_score
  - health score detail => aiops health show_detail
- [x] Delete migrated topics
- [x] Remove redundant topology subtopics (topology_fcsan, topology_ipsan, topology_lun, topology_vm, topology_graph) and merge into main topology subtopic

### Testing Tasks

- [ ] 执行测试用例：test/todo.md

**注意**
- 如果测试命令需要参数，请思考并执行依赖命令，获取必要参数取值
- 每执行完一个用例，更新test/report.md记录用例执行结果，如果用例执行失败，记录失败详情
- 如果用例执行成功，更新test/todo.md，标记用例执行完成


### Current Project Status

**Active Topics**: 15
**Total Actions**: 356

**Topic Structure**:
1. aiops (27 actions) - AIOps intelligent operations
2. backup (3 actions) - Data backup management
3. fc_switch (19 actions) - FC fiber switch management
4. gfs (14 actions) - Global file system
5. ip_switch (6 actions) - IP switch management
6. kubernetes (6 actions) - Kubernetes management
7. nas (42 actions) - Network attached storage
8. protection (3 actions) - Protection management
9. san (68 actions) - Storage area network
10. self_service (8 actions) - Tenant self service
11. server (2 actions) - Server management
12. storage (23 actions) - Storage device management
13. system (8 actions) - System management
14. virtualization (14 actions) - Virtualization services
15. workflow (7 actions) - Workflow management

**Documentation**:
- CLAUDE.md - Development guide and task tracking
- SKILL.md - Skill definition for AI agents
- param-doc-format.md - Parameter documentation format conventions (project memory)
- test/todo.md - Executable test checklist with 345 test cases

**Recent Changes**:
- **Parameter format refactoring**: Unified structured parameter docstring format across all action modules (san.py, nas.py, self_service.py, storage.py)
  - Plain text keys without quotes
  - English parentheses `()` for constraints
  - `可选值：enum (desc)` format for enumerations
  - `参数格式如下：[{` / `属性格式如下：{` for nested structures
  - Updated CLI parser (`dme_cli.py`) with format block skip mechanism to prevent internal attributes from being parsed as phantom parameters
- **san.py expansion**: san topic grew from 60 to 68 actions
  - Added: `storage_host_unmap_luns`, `storage_host_group_unmap_luns`, `physical_host_show_mapping_views`, `physical_host_group_show_mapping_views`, `physical_host_group_show_hosts`, `physical_host_modify_access_info`
  - Rewrote: `lun_group_create`, `lun_group_add_luns`, `lun_group_list`, `lun_list`, `mapping_view_create`, `physical_host_create`, `port_group_create/list/show_ports/show_relations`
  - Removed unused: `lun_mapping`, `unmapping_host/group`, `map_host/group`
