# DME Skills

[English](./README.md) | [简体中文](./README_zh.md)

DME 运维技能集合，用于存储设备的日常运维工作。


## dme-ops-skill

DME 运维技能，覆盖存储设备的**监控、分析和配置操作**。通过 `pydme` CLI 工具与 DME RESTful API 交互，支持：

- **存储设备管理** — 查询/配置存储池、LUN、文件系统、主机等
- **系统管理** — 任务跟踪、系统配置、登录认证
- **告警 & 监控** — 查看设备告警、运行状态、性能数据
- **SAN & NAS** — 块存储和文件存储的统一管理
- **虚拟化 & 容器** — 对接虚拟化和 Kubernetes 环境
- **数据保护** — 备份、容灾策略管理
- **智能运维** — AIOps 异常检测与分析

### 快速开始

#### 1. 安装依赖

```bash
pip install git+https://github.com/agentic-data-ops/dme-python-sdk.git
```

#### 2. 设置环境变量

```bash
export DME_API_ENDPOINT=https://dme-float-ip:26335
export DME_API_USERNAME=your-username
export DME_API_PASSWORD=your-password
```

#### 3. 验证连接

```bash
pydme system show
```

#### 4. 使用技能

```text
安装dme-ops-skill

查询存储设备列表，选择一个最空闲的Dorado存储设备，创建2个100GB LUN
```

## storage-ops-skill

华为闪存存储设备运维技能，通过 SSH 登录设备 CLI 执行批量命令。核心组件：

- `SKILL.md` — 技能定义与标准流程
- `scripts/flash-storage/cli.py` — 基于 Python（paramiko，跨平台 Windows/Linux）的 SSH CLI 执行器

### 标准流程

1. **查询命令帮助**：通过 CLI 脚本获取命令帮助（非英文输入先提取英文关键字搜索，因为命令行帮助仅有英文）
2. **组装批量命令**：组装批量命令行，每个命令 1 行，用 `\n` 分隔
3. **风险检查与确认**：识别风险命令（变更类命令及 High-Risk Command List 中的命令），展示即将执行的命令列表并标注风险命令，征得用户确认
4. **执行**：用户确认后调用 `scripts/flash-storage/cli.py` 执行命令
5. **总结**：根据输出总结执行情况
6. **推荐下一步**：基于结果推荐下一步动作

### 快速开始

#### 1. 设置环境变量（密码建议通过环境变量传入）

```bash
export STORAGE_ADDRESS=192.168.1.10
export STORAGE_USERNAME=admin
export STORAGE_PASSWORD='your-password'
export STORAGE_TIMEOUT=60
```

#### 2. 执行命令

```bash
python3 storage-ops-skill/scripts/flash-storage/cli.py "show version\nshow storage pool"
```

#### 3. 使用技能

```text
安装storage-ops-skill

查询设备版本和存储池信息，检查是否有告警
```

### 注意事项

- **风险确认**：风险命令（如 `delete`、`create`、`modify` 等变更类命令及 High-Risk Command List 中的命令）执行前必须获得用户确认
- **语言**：命令行帮助仅有英文，非英文请求需提取英文关键字搜索；总结响应语言与用户输入语言保持一致
- **密码安全**：强烈建议通过 `STORAGE_PASSWORD` 环境变量传入密码，避免密码出现在命令行参数中

# 免责声明

1. **非官方项目**：本项目非华为 DME 官方提供，由个人维护，仅提供参考样例，不提供技术支持。

2. **AI 生成代码**：本项目依赖的 `dme-python-sdk` 完全由 AI 编码工具开发和测试，仍存在少部分动作因缺乏环境未进行实际测试（动作实现与 API 是一致的），请谨慎评估后使用。

