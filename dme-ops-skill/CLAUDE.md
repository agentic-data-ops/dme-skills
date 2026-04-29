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

**注意**
- 待执行用例见文件：test/todo.md
- 每执行完一个用例，更新test/report.md，记录执行结果总结
- 如果用例执行成功，更新test/todo.md，将用例标记为完成

- [ ] 执行测试用例：test/todo.md

### Current Project Status

**Active Topics**: 17
**Total Actions**: 307

**Topic Structure**:
1. aiops (27 actions) - AIOps intelligent operations
2. backup (3 actions) - Data backup management
3. cmdb (6 actions) - Configuration management database
4. fc_switch (19 actions) - FC fiber switch management
5. gfs (14 actions) - Global file system
6. ip_switch (6 actions) - IP switch management
7. kubernetes (6 actions) - Kubernetes management
8. nas (42 actions) - Network attached storage
9. resource (22 actions) - Resource management
10. san (60 actions) - Storage area network
11. server (2 actions) - Server management
12. storage (23 actions) - Storage device management
13. system (8 actions) - System management
14. task (18 actions) - Task management
15. user (45 actions) - User management
16. virtualization (14 actions) - Virtualization services
17. workflow (7 actions) - Workflow management

**Documentation**:
- CLAUDE.md - Development guide and task tracking
- SKILL.md - Skill definition for AI agents
- test/todo.md - Executable test checklist with 345 test cases

**Recent Changes**:
- Migrated health topic to aiops subtopic
- aiops now has 7 subtopics including health
- aiops actions increased from 24 to 27
- All Python references updated from python3 to python
- Removed health.py, consolidated into aiops.py
