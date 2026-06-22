---
name: dme-ops-skill
description: DME 运维技能，用于存储设备的日常运维工作，包括存储监控、分析和配置操作。
---

# DME 运维技能

DME 运维技能，用于存储设备的日常运维工作，包括存储监控、分析和配置操作。

## 安装依赖包

```bash
pip install git+https://github.com/agentic-data-ops/dme-python-sdk.git
```

## 设置环境变量

```
DME_API_ENDPOINT=https://dme-float-ip:26335
DME_API_USERNAME=your-username
DME_API_PASSWORD=your-password
```

## 标准流程

1. **获取帮助信息**：调用 `pydme --list-topics` 获取所有可用的主题和动作
2. **规划执行步骤**：根据用户请求规划执行步骤
3. **执行动作步骤**：
   - 调用 `pydme <topic> <subtopic> <action> --help` 获取动作参数帮助
   - 调用 `pydme <topic> <subtopic> <action> --param1 value1 --param2 value2` 执行具体动作（变更类动作需提示用户确认后执行）
   - 如果动作返回异步任务ID，调用 `pydme system task wait` 等待任务完成
   - 规划后续要执行的动作
4. **总结输出**：格式化输出信息，并进行总结
5. **提示下一步**：根据输出信息和相关主题的帮助信息，提示用户下一步操作

## 注意事项

1. **分页**: 部分接口支持分页查询，注意设置合适的 `page_size`
2. **异步任务**: 某些操作（如添加、删除、修改）会返回异步任务 ID，可以使用 `pydme system task wait` 等待任务完成
3. **环境变量**: 可以通过环境变量设置 DME 连接信息，避免每次输入
4. **风险确认**：风险动作会被pydme命令行拦截，必须获得用户确认后，再追加 `--accept-risk` 参数执行
5. **过滤查询**：查询对象列表前获取动作帮助，尽量使用过滤条件，避免返回大量数据
6. **复杂参数格式**：动作的命令行帮助中如果参数包含内部格式，这指定为JSON字符串，JSON参数需要使用双引号

## 参考信息

- `reference/dme-python-sdk.md` - DME Python SDK 参考文档

## 命令行工具

### 命令格式

CLI 支持两种命令格式，根据 API URI 的层级自动判断：

**两级结构**（直接动作）：
```bash
pydme <topic> <action> --param1 value1 --param2 value2
```

**三级结构**（子主题动作）：
```bash
pydme <topic> <subtopic> <action> --param1 value1 --param2 value2
```

### 参数说明

**全局参数**：
- `--endpoint` / `-e`: DME API 的访问地址，格式：`https://<dme_ip_address>:<dme_port>`，可通过 `DME_API_ENDPOINT` 环境变量传入
- `--user` / `-u`: DME API 的用户名，可通过 `DME_API_USERNAME` 环境变量传入
- `--password` / `-p`: DME API 的密码，可通过 `DME_API_PASSWORD` 环境变量传入
- `--timeout`: API 请求超时时间（秒），默认 90 秒
- `--list-topics`: 列出所有可用的主题（树形结构展示）
- `--accept-risk`: 确认接受风险，可通过`DME_ACCEPT_RISK`环境变量传入（不建议通过环境变量传入）

**位置参数**：
- `topic`: 动作主题，例如：`storage`, `storagepool`, `lun`, `filesystem`, `host`, `task`, `system`
- `subtopic`: 子主题（可选），例如：`disk`, `fan`, `node`, `pool`, `snapshot`, `initiator`
- `action`: 动作名称，例如：`list`, `create`, `delete`, `show`, `modify`

### 帮助信息

```bash
# 查看所有主题动作（树形结构）
pydme --list-topics

# 查看主题帮助（显示所有直接动作和子主题）
pydme <topic> --help

# 查看子主题帮助
pydme <topic> <subtopic> --help

# 查看动作参数帮助
pydme <topic> <action> --help
pydme <topic> <subtopic> <action> --help
```

