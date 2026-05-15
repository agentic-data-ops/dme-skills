---
name: dme-actions
description: DME 运维动作，用于存储设备的日常运维工作，包括存储监控、分析和配置操作。
---

# DME 运维动作

DME 运维动作，用于存储设备的日常运维工作，包括存储监控、分析和配置操作。

## 标准流程

1. **获取帮助信息**：调用 `dme_cli.py --list-topics` 获取所有可用的主题和动作
2. **规划执行步骤**：根据用户请求规划执行步骤
3. **执行动作步骤**：
   - 调用 `dme_cli.py <topic> <subtopic> <action> --help` 获取动作参数帮助
   - 调用 `dme_cli.py <topic> <subtopic> <action> --param1 value1 --param2 value2` 执行具体动作
   - 如果动作返回异步任务ID，调用 `dme_cli.py task show` 查询任务状态，等待任务完成
   - 规划后续要执行的动作
4. **总结输出**：格式化输出信息，并进行总结
5. **提示下一步**：根据输出信息和相关主题的帮助信息，提示用户下一步操作

## 依赖脚本

### dme_cli.py

存储运维操作命令行入口，提供参数解析和帮助。

**位置**: `scripts/dme_cli.py`

## 注意事项

1. **认证**: 如果 DME_API_AUTH_TOKEN 环境变量为空，或执行动作时提示会话超时，则调用 system login 动作登录，获取 accessSession，设置环境变量 DME_API_AUTH_TOKEN=<accessSession>
2. **分页**: 部分接口支持分页查询，注意设置合适的 `page_size`
3. **异步任务**: 某些操作（如添加、删除、修改）会返回异步任务 ID，可以使用 `task wait` 等待任务完成
4. **环境变量**: 可以通过环境变量设置 DME 连接信息，避免每次输入

## 参考信息

- `reference/dme_api_reference/目录.md` - DME API 参考文档目录
- `reference/dme_api_reference/<API>.md` - 具体 API 的详细定义和调用示例

## 命令行工具

### 命令格式

CLI 支持两种命令格式，根据 API URI 的层级自动判断：

**两级结构**（直接动作）：
```bash
python dme_cli.py <topic> <action> --param1 value1 --param2 value2
```

**三级结构**（子主题动作）：
```bash
python dme_cli.py <topic> <subtopic> <action> --param1 value1 --param2 value2
```

### 参数说明

**全局参数**：
- `--endpoint` / `-e`: DME API 的访问地址，格式：`https://<dme_ip_address>:<dme_port>`，可通过 `DME_API_ENDPOINT` 环境变量传入
- `--user` / `-u`: DME API 的用户名，可通过 `DME_API_USERNAME` 环境变量传入
- `--password` / `-p`: DME API 的密码，可通过 `DME_API_PASSWORD` 环境变量传入
- `--token`: DME API 的认证密钥，提供则跳过登录，可通过 `DME_API_AUTH_TOKEN` 环境变量传入
- `--timeout`: API 请求超时时间（秒），默认 10 秒
- `--list-topics`: 列出所有可用的主题（树形结构展示）

**位置参数**：
- `topic`: 动作主题，例如：`storage`, `storagepool`, `lun`, `filesystem`, `host`, `task`, `system`
- `subtopic`: 子主题（可选），例如：`disk`, `fan`, `node`, `pool`, `snapshot`, `initiator`
- `action`: 动作名称，例如：`list`, `create`, `delete`, `show`, `modify`

### 帮助信息

```bash
# 查看所有主题（树形结构）
python dme_cli.py --list-topics

# 查看主题帮助（显示所有直接动作和子主题）
python dme_cli.py storage --help

# 查看子主题帮助
python dme_cli.py storage disk --help

# 查看动作参数帮助
python dme_cli.py storage list --help
python dme_cli.py storage disk list --help
```

