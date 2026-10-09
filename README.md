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

# Disclaimer

1. **Unofficial project**: This project is not officially provided by Huawei DME. It is maintained by individuals and serves only as a reference sample, without technical support.

2. **AI-generated code**: The `dme-python-sdk` this project depends on was fully developed and tested by AI coding tools. A small number of actions have not been actually tested due to lack of environment (the action implementations are consistent with the API). Please evaluate carefully before use.
