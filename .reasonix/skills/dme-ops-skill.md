---
name: dme-ops-skill
description: DME 运维技能 — 通过 pydme CLI 管理存储设备（监控/分析/配置），支持存储池、LUN、告警、SAN/NAS、虚拟化、数据保护等
---
# DME 运维技能

通过 `pydme` CLI 工具与 DME RESTful API 交互，用于存储设备的日常运维工作。

## 前提条件

确保已安装 pydme：
```bash
pip install git+https://github.com/agentic-data-ops/dme-python-sdk.git
```

并设置环境变量：
- `DME_API_ENDPOINT` — DME 访问地址，格式 `https://<ip>:<port>`
- `DME_API_USERNAME` / `DME_API_PASSWORD`

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

## 命令格式

**两级结构**（直接动作）：
```bash
pydme <topic> <action> --param1 value1 --param2 value2
```

**三级结构**（子主题动作）：
```bash
pydme <topic> <subtopic> <action> --param1 value1 --param2 value2
```

## 注意事项

1. **分页**: 部分接口支持分页查询，注意设置合适的 `page_size`
3. **异步任务**: 某些操作（添加、删除、修改）会返回异步任务 ID，可使用 `pydme system task wait` 等待任务完成
4. **环境变量**: 可通过环境变量设置 DME 连接信息，避免每次输入
5. **风险确认**: 风险动作会被 pydme 命令行拦截，必须获得用户确认后，再追加 `--accept-risk` 参数执行
6. **过滤查询**: 查询对象列表前获取动作帮助，尽量使用过滤条件，避免返回大量数据
7. **复杂参数格式**: JSON 参数必须使用**双引号**，且通过 pydme CLI 传递 JSON 参数时部分三级结构命令可能无法正确解析，可改用 Python 脚本直接调用 SDK


## 参考信息

- `reference/dme-python-sdk.md` - DME Python SDK 参考文档
- 使用 `pydme <topic> <subtopic> <action> --help` 查看具体动作参数
