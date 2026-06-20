# DME Skills

DME（数据中心管理引擎）运维技能集合，用于存储设备的日常运维工作。


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

