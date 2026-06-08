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

## 函数参数帮助文档格式约定

对于具有内部结构的复杂参数（列表/字典），在 docstring 中使用以下格式描述。

### 模板

```
param_key: <param_description> (<param_restrictions>)。可选值：<param_option_enum> (<param_option_description>), ...。参数格式如下：[{
                attr_key1: <attr_description> (<attr_restrictions>)。可选值：<enum> (<desc>), ...。属性格式如下：{
                    sub_key1: <sub_description> (<sub_restrictions>)。可选值：<enum> (<desc>), ...。
                    sub_key2: ...
                },
                attr_key2: ...
             }, ...]
```

### 规则

1. **无引号** — attribute_key 和 description 不使用双引号，纯文本格式
2. **约束** — 使用英文括号 `()` 包裹，如 `(1~255个字符)`
3. **枚举值** — `可选值：enum1 (desc1), enum2 (desc2)`（英文括号）
4. **嵌套对象** — 使用 `属性格式如下：{ ... }` 递归表达
5. **外层包裹** — 列表用 `[{ ... }, ...]`，字典用 `{ ... }`
6. **句号结尾** — 每个参数描述以中文句号 `。` 结尾
7. **关键词约定** — 必须使用 `参数格式如下：[{` 或 `参数格式如下：{` 作为格式块入口标记，CLI 解析器依赖此关键词跳过内部 `key: desc` 行，避免误解析为函数参数
8. **嵌套关键词** — 内部嵌套对象必须使用 `属性格式如下：{` 作为入口标记
9. **大括号平衡** — `{` 和 `}` 必须匹配，解析器通过计数自动退出格式块

### 示例

```
volumes: 待创建 LUN 基本参数列表 (List<ServiceVolumeBasicParams>, 数组最大成员个数: 1000)。参数格式如下：[{
        name: LUN名称 (1~255个字符, 支持字母数字._-和中文字符),
        capacity: 容量GB (1~262144),
        count: 创建数量 (1~500),
        description: 描述 (0~255个字符),
        start_suffix: 起始后缀编号 (0~9999),
        suffix_length: 后缀长度规则 (1~4, 名称长度+后缀长度<=255)
     }, ...]

scheduler_hints: 调度策略 (可选, SchedulerHints 对象)。参数格式如下：{
        affinity: 是否开启亲和性。可选值：true (开启), false (不开启)。默认不开启,
        affinity_volume: 待亲和的 LUN ID (可选, 0~64个字符)
     }

tuning: 调优属性 (可选), CustomizeLunTuning 对象。参数格式如下：{
        smart_tier: 数据迁移策略。可选值：no_migration (不迁移), automatic_migration (自动迁移), migration_to_higher (向高性能层迁移), migration_to_lower (向低性能层迁移)。默认no_migration,
        deduplication_enabled: 重复数据删除 (仅Thin LUN支持)。可选值：true (开启), false (关闭),
        compression_enabled: 数据压缩 (仅Thin LUN支持)。可选值：true (开启), false (关闭),
        alloction_type: LUN分配类型。可选值：thin, thick,
        smart_qos: Smart QoS对象。属性格式如下：{
                max_bandwidth: 最大带宽 (1~999999999Mbit/s; 与min_bandwidth/min_iops互斥),
                max_iops: 最大IOPS (1~999999999; 与min_bandwidth/min_iops互斥),
                min_bandwidth: 最小带宽 (1~999999999Mbit/s; 与max_bandwidth/max_iops互斥),
                min_iops: 最小IOPS (1~999999999; 与max_bandwidth/max_iops互斥),
                latency: 时延 (1~999999999ms; Dorado V6系列单位为us, 可选值为500/1500; 与max_bandwidth/max_iops互斥)
        },
        workload_type_raw_id: 应用类型ID (0~4294967295; 通过查询指定存储设备上应用类型接口获取)
     }
```

### ⚠️ 常见错误（务必避免）

```diff
- BAD: 格式：{  或  格式：[{    ← 内部字段会泄露为顶层 CLI 参数（如 --name、--type）
+ GOOD: 参数格式如下：{  或  参数格式如下：[{   ← 解析器自动跳过内部字段
```

**错误后果**：使用 `格式：{` 时，`parse_docstring` 会把内部的 `key: desc` 行解析为顶层参数，
在 `--help` 中出现 `--name`、`--type`、`--mode`、`--tag_ids` 等不应出现的参数名。
修复方法：将 `格式：{` 替换为 `参数格式如下：{`，将 `格式：[{` 替换为 `参数格式如下：[{`。

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

### Code Review & Fix Task

- [x] san.py: 完成检查和修复
- [ ] nas.py: 已完成检查和修复：创建/修改文件系统、命名空间、NFS共享、CIFS共享、DataTurbo共享
- [ ] storage.py: 已完成检查和修复：启动器相关动作
- [ ] self_service.py: 已完成检查和修复：服务化创建LUN

**注意**
- 保证动作代码实现与API文档定义完全一致
- 保证命令行参数解释包含全部格式和约束说明

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
