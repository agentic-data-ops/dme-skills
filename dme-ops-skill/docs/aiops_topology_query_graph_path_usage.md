# aiops topology query_graph_path 使用指南

## 错误信息

```
TypeError: graph_query() missing 2 required positional arguments: 'entry_res_type' and 'entry_res_id'
```

## 原因分析

用户使用了错误的参数 `--mo_dn test`，该命令需要使用 `--entry_res_type` 和 `--entry_res_id` 参数。

**错误用法**:
```bash
python scripts/dme_cli.py aiops topology query_graph_path --mo_dn test
```

## 正确用法

### 基本语法

```bash
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type <入口资源类型> \
  --entry_res_id <入口资源ID>
```

### 查看帮助信息

```bash
python scripts/dme_cli.py aiops topology query_graph_path --help
```

## 参数说明

### 必选参数

#### --entry_res_type
入口资源类型（必选），支持以下类型：

| 类型值 | 说明 |
|--------|------|
| `storage_device` | 存储设备 |
| `disk` | 磁盘 |
| `storage_pool` | 存储池 |
| `hyper_scale_pool` | 超大规模池 |
| `file_system` | 文件系统 |
| `controller` | 控制器 |
| `eth_port` | 以太网端口 |
| `ib_port` | InfiniBand 端口 |
| `logic_port` | 逻辑端口 |
| `ip_client` | IP 客户端 |
| `dtree` | Dtree |
| `lun` | LUN |
| `k8s_application` | K8s 应用 |
| `k8s_workload` | K8s 工作负载 |
| `k8s_pod` | K8s Pod |
| `k8s_pvc` | K8s PVC |
| `k8s_pv` | K8s PV |
| `k8s_cluster` | K8s 集群 |
| `k8s_node` | K8s 节点 |
| `k8s_vc_job` | K8s VC 任务 |
| `dturbo_client` | DataTurbo 客户端 |
| `enclosures` | 机柜 |
| `eth_switch` | 以太网交换机 |
| `storage_zone` | 存储区域 |
| `service_network` | 服务网络 |
| `db_instance` | 数据库实例 |
| `db_node` | 数据库节点 |

#### --entry_res_id
入口资源 ID（必选）

### 可选参数

#### --type
业务类型，可选值：
- `nas` - NAS 业务
- `k8s` - Kubernetes 业务
- `db` - 数据库业务

#### --filter
过滤条件列表，最多 10 个

## 使用示例

### 示例 1: 查询存储设备的拓扑

```bash
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type storage_device \
  --entry_res_id "storage_device_id_001"
```

### 示例 2: 查询存储池的拓扑（NAS业务）

```bash
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type storage_pool \
  --entry_res_id "pool_id_123" \
  --type nas
```

### 示例 3: 查询K8s集群的拓扑

```bash
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type k8s_cluster \
  --entry_res_id "cluster_k8s_01" \
  --type k8s
```

### 示例 4: 查询数据库实例的拓扑

```bash
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type db_instance \
  --entry_res_id "db_instance_001" \
  --type db
```

### 示例 5: 查询文件系统的拓扑（带过滤条件）

```bash
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type file_system \
  --entry_res_id "fs_id_456" \
  --type nas \
  --filter '["type:nas"]'
```

### 示例 6: 查询K8s Pod的拓扑

```bash
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type k8s_pod \
  --entry_res_id "pod_abc123" \
  --type k8s
```

### 示例 7: 查询LUN的拓扑

```bash
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type lun \
  --entry_res_id "lun_id_789"
```

## 获取资源ID的方法

### 方法 1: 通过CMDB查询

1. **查看CMDB类定义**:
```bash
python scripts/dme_cli.py cmdb class list
```

2. **查询特定类型的实例**:
```bash
python scripts/dme_cli.py cmdb instance list --class_name <类名>
```

3. **从返回结果中获取 instance_id 作为 entry_res_id**

### 方法 2: 通过其他命令查询

**查询存储池ID**:
```bash
python scripts/dme_cli.py resource storage_pool list
```

**查询文件系统ID**:
```bash
python scripts/dme_cli.py nas filesystem list
```

**查询LUN ID**:
```bash
python scripts/dme_cli.py san lun list
```

## 返回结果说明

命令返回包含以下字段的数据：

```json
{
  "nodes": [
    {
      "id": "节点ID",
      "type": "节点类型",
      "label": "节点标签",
      "sub_type": "子类型"
    }
  ],
  "edges": [
    {
      "source": "源节点ID",
      "target": "目标节点ID",
      "edge_type": "边类型"
    }
  ]
}
```

## 环境配置

执行命令前需要配置环境变量：

```bash
export DME_API_ENDPOINT="https://your-dme-ip:port"
export DME_API_USERNAME="admin"
export DME_API_PASSWORD="your-password"
```

或者使用命令行参数：

```bash
python scripts/dme_cli.py \
  --endpoint "https://your-dme-ip:port" \
  --user "admin" \
  --password "your-password" \
  aiops topology query_graph_path \
  --entry_res_type storage_pool \
  --entry_res_id "pool_id_123"
```

## 注意事项

1. **必选参数**: `--entry_res_type` 和 `--entry_res_id` 是必选参数，必须提供
2. **参数顺序**: 参数顺序不影响执行效果
3. **资源类型**: 确保使用正确的资源类型值，参考上述表格
4. **资源ID**: 确保资源ID在系统中存在，否则查询结果为空
5. **业务类型**: `--type` 参数是可选的，但建议根据实际业务类型提供，以获得更精确的结果
6. **过滤条件**: `--filter` 参数需要使用JSON数组格式

## 故障排查

### 问题 1: TypeError: graph_query() missing 2 required positional arguments

**原因**: 使用了不存在的参数 `--mo_dn`

**解决**: 使用正确的必选参数

```bash
# 错误
python scripts/dme_cli.py aiops topology query_graph_path --mo_dn test

# 正确
python scripts/dme_cli.py aiops topology query_graph_path \
  --entry_res_type storage_device \
  --entry_res_id "storage_id_001"
```

### 问题 2: 返回结果为空

**原因**: 提供的资源ID不存在或资源类型不匹配

**解决**:
1. 确认资源ID是否正确
2. 确认资源类型是否匹配
3. 使用CMDB查询资源是否存在

```bash
python scripts/dme_cli.py cmdb instance list --class_name <类名>
```

### 问题 3: Invalid entry_res_type value

**原因**: 提供的资源类型值不支持

**解决**: 使用上述表格中的正确值

```bash
# 错误
--entry_res_type "storage"

# 正确
--entry_res_type "storage_device"
```

### 问题 4: 必须提供 endpoint、user 和 password 参数

**解决**: 配置环境变量或使用命令行参数

```bash
# 方式 1: 环境变量
export DME_API_ENDPOINT="https://your-dme-ip:port"
export DME_API_USERNAME="admin"
export DME_API_PASSWORD="your-password"
python scripts/dme_cli.py aiops topology query_graph_path --entry_res_type storage_device --entry_res_id "id"

# 方式 2: 命令行参数
python scripts/dme_cli.py \
  --endpoint "https://your-dme-ip:port" \
  --user "admin" \
  --password "your-password" \
  aiops topology query_graph_path \
  --entry_res_type storage_device \
  --entry_res_id "id"
```

## 与其他拓扑查询命令的对比

| 命令 | 用途 | 必选参数 |
|------|------|----------|
| `aiops topology query_san_path` | 查询 SAN 路径拓扑 | `--host_id`, `--lun_id` |
| `aiops topology query_luns` | 查询拓扑图 LUN 列表 | `--host_id` |
| `aiops topology query_vms` | 查询拓扑图虚拟机列表 | `--host_id` |
| `aiops topology query_graph_path` | 查询拓扑图库信息 | `--entry_res_type`, `--entry_res_id` |
| `aiops topology ipsan_query` | 查询 IP_SAN 网络拓扑 | `--host_ip`, `--pool_id` |
| `aiops topology fcsan_query` | 查询 FC_SAN 网络拓扑 | `--host_wwn`, `--pool_id` |

**使用建议**:
- 查询SAN存储路径：使用 `query_san_path`
- 查询主机关联的LUN/VM：使用 `query_luns` / `query_vms`
- 查询IP/FC网络拓扑：使用 `ipsan_query` / `fcsan_query`
- 查询复杂的业务拓扑（NAS/K8s/DB）：使用 `query_graph_path`
