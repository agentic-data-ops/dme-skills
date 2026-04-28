# DME CLI 测试用例

本文档包含 dme_cli.py 的所有主题、子主题、动作的测试用例。

## 测试环境准备

- [ ] 配置环境变量：`export DME_API_URL=<your-dme-api-url>`
- [ ] 配置认证信息：`export DME_USERNAME=<username>`
- [ ] 配置认证信息：`export DME_PASSWORD=<password>`
- [ ] 验证连接：`python scripts/dme_cli.py --list-topics`

---

## 1. AIOps 智能运维相关操作 (aiops)

### 1.1 alarm 子主题 - 告警管理

- [ ] **查询告警信息**
  - **描述**: 查询当前告警信息，可选择是否包含历史告警
  - **前置条件**: 系统中存在告警数据
  - **执行命令**:
    ```bash
    # 查询当前告警
    python scripts/dme_cli.py aiops alarm list

    # 查询包含历史告警
    python scripts/dme_cli.py aiops alarm list --include_history true

    # 按告警级别过滤
    python scripts/dme_cli.py aiops alarm list --level "critical"

    # 按对象名称过滤
    python scripts/dme_cli.py aiops alarm list --object_name "storage_001"

    # 分页查询
    python scripts/dme_cli.py aiops alarm list --page_size 20 --page_no 1
    ```

- [ ] **确认告警**
  - **描述**: 确认指定的告警
  - **前置条件**: 存在未确认的告警，需要告警ID
  - **执行命令**:
    ```bash
    # 确认单个告警
    python scripts/dme_cli.py aiops alarm ack --alarm_id "<alarm_id>"

    # 确认多个告警
    python scripts/dme_cli.py aiops alarm ack --alarm_id "id1,id2,id3"
    ```

- [ ] **取消确认告警**
  - **描述**: 取消确认指定的告警
  - **前置条件**: 存在已确认的告警，需要告警ID
  - **执行命令**:
    ```bash
    # 取消确认单个告警
    python scripts/dme_cli.py aiops alarm unack --alarm_id "<alarm_id>"

    # 取消确认多个告警
    python scripts/dme_cli.py aiops alarm unack --alarm_id "id1,id2,id3"
    ```

- [ ] **清除告警**
  - **描述**: 清除指定的告警
  - **前置条件**: 存在告警，需要告警ID
  - **执行命令**:
    ```bash
    # 清除单个告警
    python scripts/dme_cli.py aiops alarm clear --alarm_id "<alarm_id>"

    # 清除多个告警
    python scripts/dme_cli.py aiops alarm clear --alarm_id "id1,id2,id3"
    ```

### 1.2 check_policy 子主题 - 检查策略管理

- [ ] **查询检查策略列表**
  - **描述**: 查询系统中的检查策略列表
  - **前置条件**: 系统中存在检查策略
  - **执行命令**:
    ```bash
    # 查询所有检查策略
    python scripts/dme_cli.py aiops check_policy list

    # 按策略名称过滤
    python scripts/dme_cli.py aiops check_policy list --policy_name "health_check"

    # 按状态过滤
    python scripts/dme_cli.py aiops check_policy list --status "enabled"

    # 按策略类型过滤
    python scripts/dme_cli.py aiops check_policy list --policy_type "storage_health"

    # 分页查询
    python scripts/dme_cli.py aiops check_policy list --page_size 20 --page_no 1
    ```

- [ ] **执行检查策略**
  - **描述**: 手动执行指定的检查策略
  - **前置条件**: 存在检查策略，需要策略ID
  - **执行命令**:
    ```bash
    # 执行单个策略
    python scripts/dme_cli.py aiops check_policy execute --policy_id "<policy_id>"
    ```

- [ ] **启用检查策略**
  - **描述**: 启用指定的检查策略
  - **前置条件**: 存在已禁用的检查策略，需要策略ID
  - **执行命令**:
    ```bash
    # 启用策略
    python scripts/dme_cli.py aiops check_policy enable --policy_id "<policy_id>"
    ```

- [ ] **禁用检查策略**
  - **描述**: 禁用指定的检查策略
  - **前置条件**: 存在已启用的检查策略，需要策略ID
  - **执行命令**:
    ```bash
    # 禁用策略
    python scripts/dme_cli.py aiops check_policy disable --policy_id "<policy_id>"
    ```

- [ ] **删除检查策略**
  - **描述**: 删除指定的检查策略
  - **前置条件**: 存在检查策略，需要策略ID
  - **执行命令**:
    ```bash
    # 删除单个策略
    python scripts/dme_cli.py aiops check_policy delete --policy_id "<policy_id>"
    ```

### 1.3 check_result 子主题 - 检查结果管理

- [ ] **查询检查策略异常检查结果列表**
  - **描述**: 查询检查策略的异常检查结果列表
  - **前置条件**: 检查策略已执行
  - **执行命令**:
    ```bash
    # 查询所有异常结果
    python scripts/dme_cli.py aiops check_result list

    # 按对象名称过滤
    python scripts/dme_cli.py aiops check_result list --object_name "storage_001"

    # 按严重级别过滤
    python scripts/dme_cli.py aiops check_result list --level "critical"

    # 按策略ID过滤
    python scripts/dme_cli.py aiops check_result list --policy_id "<policy_id>"

    # 分页查询
    python scripts/dme_cli.py aiops check_result list --page_size 20 --page_no 1
    ```

- [ ] **查询检查策略异常检查结果详情**
  - **描述**: 查询指定检查结果的详细信息
  - **前置条件**: 存在检查结果，需要结果ID
  - **执行命令**:
    ```bash
    # 查询结果详情
    python scripts/dme_cli.py aiops check_result show --check_result_id "<result_id>"
    ```

### 1.4 diagnose_task 子主题 - 诊断任务管理

- [ ] **查询性能诊断任务状态**
  - **描述**: 查询性能诊断任务的状态和结果
  - **前置条件**: 存在诊断任务
  - **执行命令**:
    ```bash
    # 查询诊断任务状态
    python scripts/dme_cli.py aiops diagnose_task status --task_id "<task_id>"
    ```

### 1.5 performance 子主题 - 性能监控管理

- [ ] **创建性能文件收集任务**
  - **描述**: 创建性能数据收集任务
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 创建收集任务
    python scripts/dme_cli.py aiops performance create_collect_task \
      --collect_period "24h" \
      --collect_scope "all" \
      --description "性能数据收集"
    ```

- [ ] **下载性能文件**
  - **描述**: 下载已收集的性能数据文件
  - **前置条件**: 存在已完成的收集任务，需要任务ID
  - **执行命令**:
    ```bash
    # 下载性能文件
    python scripts/dme_cli.py aiops performance download_collect_result \
      --task_id "<task_id>" \
      --output_path "/tmp/performance_data.zip"
    ```

- [ ] **查询历史性能数据**
  - **描述**: 查询历史性能监控数据
  - **前置条件**: 系统中存在性能数据
  - **执行命令**:
    ```bash
    # 查询性能数据
    python scripts/dme_cli.py aiops performance query \
      --object_id "<object_id>" \
      --indicator_name "iops" \
      --start_time "2024-01-01T00:00:00Z" \
      --end_time "2024-01-02T00:00:00Z"
    ```

- [ ] **获取监控对象类型支持的监控指标**
  - **描述**: 获取指定监控对象类型支持的监控指标列表
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 查询存储池的监控指标
    python scripts/dme_cli.py aiops performance show_indicators --object_type "storage_pool"
    ```

- [ ] **获取监控指标**
  - **描述**: 获取系统中的所有监控指标
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 查询所有监控指标
    python scripts/dme_cli.py aiops performance list_indicators

    # 按对象类型过滤
    python scripts/dme_cli.py aiops performance list_indicators --object_type "storage_pool"
    ```

- [ ] **获取所有监控对象类型**
  - **描述**: 获取系统中所有可监控的对象类型
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 查询所有监控对象类型
    python scripts/dme_cli.py aiops performance list_object_types
    ```

### 1.6 topology 子主题 - 拓扑管理

- [ ] **查询 SAN 路径拓扑结构**
  - **描述**: 查询 SAN 路径拓扑结构（支持 IP_SAN 和 FC_SAN）
  - **前置条件**: 系统中存在 SAN 网络配置
  - **执行命令**:
    ```bash
    # 查询 IP_SAN 拓扑
    python scripts/dme_cli.py aiops topology query_san_path \
      --entry_objects '{"host_ids": ["host_001"]}' \
      --san_type "ip_san"

    # 查询 FC_SAN 拓扑
    python scripts/dme_cli.py aiops topology query_san_path \
      --entry_objects '{"host_ids": ["host_001"]}' \
      --san_type "fc_san"
    ```

- [ ] **查询拓扑图 LUN 列表**
  - **描述**: 查询拓扑图中的 LUN 列表
  - **前置条件**: 系统中存在 LUN
  - **执行命令**:
    ```bash
    # 查询所有 LUN
    python scripts/dme_cli.py aiops topology query_luns \
      --entry_objects '{"storage_ids": ["storage_001"]}'

    # 按存储池过滤
    python scripts/dme_cli.py aiops topology query_luns \
      --entry_objects '{"storage_ids": ["storage_001"]}' \
      --storage_pool_id "pool_001"
    ```

- [ ] **查询拓扑图虚拟机和虚拟磁盘列表**
  - **描述**: 查询拓扑图中的虚拟机和虚拟磁盘列表，或查询 BMS 下物理磁盘列表
  - **前置条件**: 系统中存在虚拟机或裸金属服务器
  - **执行命令**:
    ```bash
    # 查询虚拟机和虚拟磁盘
    python scripts/dme_cli.py aiops topology query_vms \
      --entry_objects '{"host_ids": ["host_001"]}'

    # 按主机过滤
    python scripts/dme_cli.py aiops topology query_vms \
      --entry_objects '{"host_ids": ["host_001"]}' \
      --host_id "host_001"
    ```

- [ ] **查询拓扑图库信息**
  - **描述**: 查询拓扑图库信息（支持 NAS、K8s、DB 等业务类型）
  - **前置条件**: 系统中存在拓扑图库数据
  - **执行命令**:
    ```bash
    # 查询 NAS 拓扑
    python scripts/dme_cli.py aiops topology query_graph_path \
      --entry_res_type "nas_share" \
      --entry_res_id "share_001" \
      --type "query"

    # 查询 K8s 拓扑
    python scripts/dme_cli.py aiops topology query_graph_path \
      --entry_res_type "k8s_pod" \
      --entry_res_id "pod_001" \
      --type "query"
    ```

### 1.7 topology_fcsan 子主题 - FC_SAN 拓扑管理

- [ ] **查询 FC_SAN 网络拓扑结构**
  - **描述**: 查询 FC_SAN 网络从主机到存储池间的拓扑结构
  - **前置条件**: 系统中存在 FC_SAN 网络
  - **执行命令**:
    ```bash
    # 查询 FC_SAN 拓扑
    python scripts/dme_cli.py aiops topology_fcsan query \
      --entry_objects '{"host_ids": ["host_001"]}'
    ```

### 1.8 topology_graph 子主题 - 拓扑图库管理

- [ ] **查询拓扑图库信息**
  - **描述**: 查询拓扑图库信息（支持 NAS、K8s、DB 等业务类型）
  - **前置条件**: 系统中存在拓扑图库数据
  - **执行命令**:
    ```bash
    # 查询图库信息
    python scripts/dme_cli.py aiops topology_graph query \
      --entry_res_type "nas_share" \
      --entry_res_id "share_001" \
      --type "query"
    ```

### 1.9 topology_ipsan 子主题 - IP_SAN 拓扑管理

- [ ] **查询 IP_SAN 网络拓扑结构**
  - **描述**: 查询 IP_SAN 网络从主机到存储池间的拓扑结构
  - **前置条件**: 系统中存在 IP_SAN 网络
  - **执行命令**:
    ```bash
    # 查询 IP_SAN 拓扑
    python scripts/dme_cli.py aiops topology_ipsan query \
      --entry_objects '{"host_ids": ["host_001"]}'
    ```

### 1.10 topology_lun 子主题 - LUN 拓扑管理

- [ ] **查询拓扑图 LUN 列表**
  - **描述**: 查询拓扑图中的 LUN 列表
  - **前置条件**: 系统中存在 LUN
  - **执行命令**:
    ```bash
    # 查询 LUN 列表
    python scripts/dme_cli.py aiops topology_lun list \
      --entry_objects '{"storage_ids": ["storage_001"]}' \
      --san_type "ip_san"

    # 分页查询
    python scripts/dme_cli.py aiops topology_lun list \
      --entry_objects '{"storage_ids": ["storage_001"]}' \
      --page_size 20 --page_no 1
    ```

### 1.11 topology_vm 子主题 - 虚拟机拓扑管理

- [ ] **查询拓扑图虚拟机和虚拟磁盘列表**
  - **描述**: 查询拓扑图中的虚拟机和虚拟磁盘列表
  - **前置条件**: 系统中存在虚拟机
  - **执行命令**:
    ```bash
    # 查询虚拟机列表
    python scripts/dme_cli.py aiops topology_vm list \
      --entry_objects '{"host_ids": ["host_001"]}'

    # 按主机过滤
    python scripts/dme_cli.py aiops topology_vm list \
      --entry_objects '{"host_ids": ["host_001"]}' \
      --host_id "host_001"

    # 分页查询
    python scripts/dme_cli.py aiops topology_vm list \
      --entry_objects '{"host_ids": ["host_001"]}' \
      --page_size 20 --page_no 1
    ```

---

## 2. 数据备份管理 (backup)

### 2.1 cluster 子主题 - 备份集群管理

- [ ] **查询备份集群列表**
  - **描述**: 查询系统中的备份集群列表
  - **前置条件**: 系统中存在备份集群
  - **执行命令**:
    ```bash
    # 查询所有备份集群
    python scripts/dme_cli.py backup cluster list

    # 分页查询
    python scripts/dme_cli.py backup cluster list --page_size 20 --page_no 1
    ```

- [ ] **查询备份集群容量**
  - **描述**: 查询备份集群的容量信息
  - **前置条件**: 存在备份集群
  - **执行命令**:
    ```bash
    # 查询集群容量
    python scripts/dme_cli.py backup cluster capacity --cluster_id "<cluster_id>"
    ```

- [ ] **查询备份集群租户配额列表**
  - **描述**: 查询备份集群的租户配额列表
  - **前置条件**: 存在备份集群
  - **执行命令**:
    ```bash
    # 查询租户配额
    python scripts/dme_cli.py backup cluster quota --cluster_id "<cluster_id>"
    ```

---

## 3. CMDB 配置管理 (cmdb)

### 3.1 class 子主题 - CMDB 类管理

- [ ] **查询 CMDB 类列表**
  - **描述**: 查询 CMDB 中的所有类
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 查询所有类
    python scripts/dme_cli.py cmdb class list

    # 按类型过滤
    python scripts/dme_cli.py cmdb class list --type "resource"
    ```

- [ ] **查询类属性定义**
  - **描述**: 查询指定类的属性定义
  - **前置条件**: 类名存在
  - **执行命令**:
    ```bash
    # 查询类属性
    python scripts/dme_cli.py cmdb class show --class_name "storage_pool"
    ```

### 3.2 instance 子主题 - CMDB 实例管理

- [ ] **查询指定资源类型的所有实例**
  - **描述**: 查询指定资源类型的所有实例
  - **前置条件**: 资源类型存在
  - **执行命令**:
    ```bash
    # 查询所有实例
    python scripts/dme_cli.py cmdb instance list --class_name "storage_pool"

    # 按属性过滤
    python scripts/dme_cli.py cmdb instance list \
      --class_name "storage_pool" \
      --filter '{"name": "pool_001"}'

    # 分页查询
    python scripts/dme_cli.py cmdb instance list \
      --class_name "storage_pool" \
      --page_size 20 --page_no 1
    ```

- [ ] **查询单个资源实例**
  - **描述**: 查询单个资源实例的详细信息
  - **前置条件**: 实例ID存在
  - **执行命令**:
    ```bash
    # 查询实例详情
    python scripts/dme_cli.py cmdb instance show \
      --class_name "storage_pool" \
      --instance_id "<instance_id>"
    ```

### 3.3 relation 子主题 - CMDB 关系管理

- [ ] **条件查询某类型关系的所有实例**
  - **描述**: 查询指定类型的所有关系实例
  - **前置条件**: 关系类型存在
  - **执行命令**:
    ```bash
    # 查询所有关系实例
    python scripts/dme_cli.py cmdb relation list --relation_name "host_to_pool"

    # 按源实例过滤
    python scripts/dme_cli.py cmdb relation list \
      --relation_name "host_to_pool" \
      --source_id "<source_id>"
    ```

- [ ] **查询单个资源关系的实例**
  - **描述**: 查询单个关系实例的详细信息
  - **前置条件**: 关系ID存在
  - **执行命令**:
    ```bash
    # 查询关系实例
    python scripts/dme_cli.py cmdb relation show \
      --relation_name "host_to_pool" \
      --relation_id "<relation_id>"
    ```

---

## 4. FC 光纤交换机 (fc_switch)

### 4.1 直接动作

- [ ] **批量查询光纤交换机**
  - **描述**: 查询系统中的所有光纤交换机
  - **前置条件**: 系统中存在光纤交换机
  - **执行命令**:
    ```bash
    # 查询所有交换机
    python scripts/dme_cli.py fc_switch list

    # 按名称过滤
    python scripts/dme_cli.py fc_switch list --name "sw_001"

    # 按厂商过滤
    python scripts/dme_cli.py fc_switch list --manufacturer "brocade"
    ```

- [ ] **同步交换机配置**
  - **描述**: 同步交换机的配置信息
  - **前置条件**: 交换机ID存在
  - **执行命令**:
    ```bash
    # 同步单个交换机
    python scripts/dme_cli.py fc_switch sync --switch_id "<switch_id>"

    # 同步多个交换机
    python scripts/dme_cli.py fc_switch sync --switch_id "sw_001,sw_002"
    ```

### 4.2 alias 子主题 - 别名管理

- [ ] **批量查询别名**
  - **描述**: 查询交换机上的所有别名
  - **前置条件**: 系统中存在别名
  - **执行命令**:
    ```bash
    # 查询所有别名
    python scripts/dme_cli.py fc_switch alias list

    # 按交换机过滤
    python scripts/dme_cli.py fc_switch alias list --switch_id "<switch_id>"
    ```

- [ ] **创建别名**
  - **描述**: 在交换机上创建新的别名
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 创建别名
    python scripts/dme_cli.py fc_switch alias create \
      --switch_id "<switch_id>" \
      --alias_name "host_alias" \
      --members "wwn_001,wwn_002"
    ```

- [ ] **修改别名**
  - **描述**: 修改已存在的别名
  - **前置条件**: 别名存在
  - **执行命令**:
    ```bash
    # 修改别名
    python scripts/dme_cli.py fc_switch alias modify \
      --switch_id "<switch_id>" \
      --alias_id "<alias_id>" \
      --alias_name "new_alias" \
      --members "wwn_001,wwn_002,wwn_003"
    ```

- [ ] **删除别名**
  - **描述**: 删除指定的别名
  - **前置条件**: 别名存在
  - **执行命令**:
    ```bash
    # 删除单个别名
    python scripts/dme_cli.py fc_switch alias delete \
      --switch_id "<switch_id>" \
      --alias_id "<alias_id>"

    # 删除多个别名
    python scripts/dme_cli.py fc_switch alias delete \
      --switch_id "<switch_id>" \
      --alias_id "alias_001,alias_002"
    ```

- [ ] **查询别名的成员**
  - **描述**: 查询别名包含的成员列表
  - **前置条件**: 别名存在
  - **执行命令**:
    ```bash
    # 查询别名成员
    python scripts/dme_cli.py fc_switch alias show_members \
      --switch_id "<switch_id>" \
      --alias_id "<alias_id>"
    ```

### 4.3 controller 子主题 - 控制器管理

- [ ] **查询交换机控制器列表**
  - **描述**: 查询交换机的控制器列表
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 查询控制器列表
    python scripts/dme_cli.py fc_switch controller list --switch_id "<switch_id>"
    ```

### 4.4 fabric 子主题 - Fabric 管理

- [ ] **批量查询 fabric**
  - **描述**: 查询系统中的所有 fabric
  - **前置条件**: 系统中存在 fabric
  - **执行命令**:
    ```bash
    # 查询所有 fabric
    python scripts/dme_cli.py fc_switch fabric list

    # 按名称过滤
    python scripts/dme_cli.py fc_switch fabric list --name "fabric_001"
    ```

- [ ] **备份 fabric 配置**
  - **描述**: 备份指定 fabric 的配置
  - **前置条件**: Fabric 存在
  - **执行命令**:
    ```bash
    # 备份 fabric 配置
    python scripts/dme_cli.py fc_switch fabric backup --fabric_id "<fabric_id>"
    ```

- [ ] **查询 fabric 的端口列表**
  - **描述**: 查询 fabric 包含的所有端口
  - **前置条件**: Fabric 存在
  - **执行命令**:
    ```bash
    # 查询 fabric 端口
    python scripts/dme_cli.py fc_switch fabric show_ports --fabric_id "<fabric_id>"
    ```

### 4.5 port 子主题 - 端口管理

- [ ] **查询交换机端口列表**
  - **描述**: 查询交换机的所有端口
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 查询所有端口
    python scripts/dme_cli.py fc_switch port list --switch_id "<switch_id>"

    # 按端口类型过滤
    python scripts/dme_cli.py fc_switch port list \
      --switch_id "<switch_id>" \
      --port_type "fc_port"
    ```

### 4.6 vsan 子主题 - VSAN 管理

- [ ] **批量查询 vsan**
  - **描述**: 查询系统中的所有 VSAN
  - **前置条件**: 系统中存在 VSAN
  - **执行命令**:
    ```bash
    # 查询所有 VSAN
    python scripts/dme_cli.py fc_switch vsan list

    # 按交换机过滤
    python scripts/dme_cli.py fc_switch vsan list --switch_id "<switch_id>"
    ```

### 4.7 zone 子主题 - Zone 管理

- [ ] **批量查询 zone**
  - **描述**: 查询系统中的所有 zone
  - **前置条件**: 系统中存在 zone
  - **执行命令**:
    ```bash
    # 查询所有 zone
    python scripts/dme_cli.py fc_switch zone list

    # 按 fabric 过滤
    python scripts/dme_cli.py fc_switch zone list --fabric_id "<fabric_id>"
    ```

- [ ] **创建 zone**
  - **描述**: 在 fabric 上创建新的 zone
  - **前置条件**: Fabric 存在
  - **执行命令**:
    ```bash
    # 创建 zone
    python scripts/dme_cli.py fc_switch zone create \
      --fabric_id "<fabric_id>" \
      --zone_name "zone_001" \
      --members "wwn_001,wwn_002"
    ```

- [ ] **修改 zone**
  - **描述**: 修改已存在的 zone
  - **前置条件**: Zone 存在
  - **执行命令**:
    ```bash
    # 修改 zone
    python scripts/dme_cli.py fc_switch zone modify \
      --fabric_id "<fabric_id>" \
      --zone_id "<zone_id>" \
      --zone_name "new_zone" \
      --members "wwn_001,wwn_002,wwn_003"
    ```

- [ ] **删除 zone**
  - **描述**: 删除指定的 zone
  - **前置条件**: Zone 存在
  - **执行命令**:
    ```bash
    # 删除单个 zone
    python scripts/dme_cli.py fc_switch zone delete \
      --fabric_id "<fabric_id>" \
      --zone_id "<zone_id>"

    # 删除多个 zone
    python scripts/dme_cli.py fc_switch zone delete \
      --fabric_id "<fabric_id>" \
      --zone_id "zone_001,zone_002"
    ```

- [ ] **批量创建 zone**
  - **描述**: 批量创建多个 zone
  - **前置条件**: Fabric 存在
  - **执行命令**:
    ```bash
    # 批量创建 zone
    python scripts/dme_cli.py fc_switch zone batch_create \
      --fabric_id "<fabric_id>" \
      --zones '[{"zone_name":"zone1","members":["wwn1","wwn2"]},{"zone_name":"zone2","members":["wwn3","wwn4"]}]'
    ```

- [ ] **查询 zone 的成员**
  - **描述**: 查询 zone 包含的成员列表
  - **前置条件**: Zone 存在
  - **执行命令**:
    ```bash
    # 查询 zone 成员
    python scripts/dme_cli.py fc_switch zone show_members \
      --fabric_id "<fabric_id>" \
      --zone_id "<zone_id>"
    ```

---

## 5. GFS 全局文件系统 (gfs)

### 5.1 dataspace 子主题 - 数据空间管理

- [ ] **批量查询 Omni-Dataverse**
  - **描述**: 查询系统中的所有数据空间
  - **前置条件**: 系统中存在数据空间
  - **执行命令**:
    ```bash
    # 查询所有数据空间
    python scripts/dme_cli.py gfs dataspace list

    # 分页查询
    python scripts/dme_cli.py gfs dataspace list --page_size 20 --page_no 1
    ```

- [ ] **查询指定 Omni-Dataverse 的容量统计信息**
  - **描述**: 查询数据空间的容量统计信息
  - **前置条件**: 数据空间存在
  - **执行命令**:
    ```bash
    # 查询容量统计
    python scripts/dme_cli.py gfs dataspace show --dataspace_id "<dataspace_id>"
    ```

- [ ] **查询 Omni-Dataverse 数据服务站点**
  - **描述**: 查询数据空间的数据服务站点列表
  - **前置条件**: 数据空间存在
  - **执行命令**:
    ```bash
    # 查询数据服务站点
    python scripts/dme_cli.py gfs dataspace site_list --dataspace_id "<dataspace_id>"
    ```

### 5.2 migration_task 子主题 - 迁移任务管理

- [ ] **批量查询 Omni-Dataverse 数据迁移任务**
  - **描述**: 查询数据空间的数据迁移任务列表
  - **前置条件**: 系统中存在迁移任务
  - **执行命令**:
    ```bash
    # 查询所有迁移任务
    python scripts/dme_cli.py gfs migration_task list

    # 按数据空间过滤
    python scripts/dme_cli.py gfs migration_task list --dataspace_id "<dataspace_id>"
    ```

- [ ] **创建 Omni-Dataverse 数据迁移任务**
  - **描述**: 创建新的数据迁移任务
  - **前置条件**: 数据空间存在
  - **执行命令**:
    ```bash
    # 创建迁移任务
    python scripts/dme_cli.py gfs migration_task create \
      --dataspace_id "<dataspace_id>" \
      --source_site_id "<source_site>" \
      --target_site_id "<target_site>" \
      --description "数据迁移任务"
    ```

- [ ] **修改 Omni-Dataverse 数据迁移任务**
  - **描述**: 修改已存在的迁移任务
  - **前置条件**: 迁移任务存在
  - **执行命令**:
    ```bash
    # 修改迁移任务
    python scripts/dme_cli.py gfs migration_task modify \
      --task_id "<task_id>" \
      --description "更新后的描述"
    ```

- [ ] **查询 Omni-Dataverse 数据迁移任务详情**
  - **描述**: 查询迁移任务的详细信息
  - **前置条件**: 迁移任务ID存在
  - **执行命令**:
    ```bash
    # 查询任务详情
    python scripts/dme_cli.py gfs migration_task show --task_id "<task_id>"
    ```

- [ ] **批量暂停或者启动 Omni-Dataverse 数据迁移任务**
  - **描述**: 暂停或启动迁移任务
  - **前置条件**: 迁移任务存在
  - **执行命令**:
    ```bash
    # 暂停任务
    python scripts/dme_cli.py gfs migration_task operate \
      --task_id "<task_id>" \
      --operation "pause"

    # 启动任务
    python scripts/dme_cli.py gfs migration_task operate \
      --task_id "<task_id>" \
      --operation "resume"
    ```

- [ ] **批量删除 Omni-Dataverse 数据迁移任务**
  - **描述**: 删除指定的迁移任务
  - **前置条件**: 迁移任务存在
  - **执行命令**:
    ```bash
    # 删除单个任务
    python scripts/dme_cli.py gfs migration_task delete --task_id "<task_id>"

    # 删除多个任务
    python scripts/dme_cli.py gfs migration_task delete --task_id "task1,task2"
    ```

### 5.3 namespace 子主题 - 命名空间管理

- [ ] **批量查询全局命名空间**
  - **描述**: 查询系统中的所有全局命名空间
  - **前置条件**: 系统中存在命名空间
  - **执行命令**:
    ```bash
    # 查询所有命名空间
    python scripts/dme_cli.py gfs namespace list

    # 分页查询
    python scripts/dme_cli.py gfs namespace list --page_size 20 --page_no 1
    ```

- [ ] **创建全局命名空间**
  - **描述**: 创建新的全局命名空间
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 创建命名空间
    python scripts/dme_cli.py gfs namespace create \
      --name "namespace_001" \
      --description "全局命名空间"
    ```

- [ ] **修改指定全局命名空间**
  - **描述**: 修改已存在的命名空间
  - **前置条件**: 命名空间存在
  - **执行命令**:
    ```bash
    # 修改命名空间
    python scripts/dme_cli.py gfs namespace modify \
      --namespace_id "<namespace_id>" \
      --name "new_name" \
      --description "更新后的描述"
    ```

- [ ] **查询全局命名空间详情**
  - **描述**: 查询命名空间的详细信息
  - **前置条件**: 命名空间ID存在
  - **执行命令**:
    ```bash
    # 查询命名空间详情
    python scripts/dme_cli.py gfs namespace show --namespace_id "<namespace_id>"
    ```

- [ ] **删除指定的全局命名空间**
  - **描述**: 删除指定的命名空间
  - **前置条件**: 命名空间存在
  - **执行命令**:
    ```bash
    # 删除命名空间
    python scripts/dme_cli.py gfs namespace delete --namespace_id "<namespace_id>"
    ```

---

## 6. 健康度 (health)

### 6.1 data 子主题 - 健康度数据管理

- [ ] **查询健康度相关数据**
  - **描述**: 查询健康度相关数据（容量预测/性能预测/性能异常）
  - **前置条件**: 系统中存在健康度数据
  - **执行命令**:
    ```bash
    # 查询容量预测数据
    python scripts/dme_cli.py health data query \
      --type "capacity_forecast" \
      --object_id "<object_id>"

    # 查询性能预测数据
    python scripts/dme_cli.py health data query \
      --type "performance_forecast" \
      --object_id "<object_id>"

    # 查询性能异常数据
    python scripts/dme_cli.py health data query \
      --type "performance_anomaly" \
      --object_id "<object_id>"
    ```

### 6.2 score 子主题 - 健康度评分管理

- [ ] **查询对象健康度**
  - **描述**: 查询对象的健康度评分
  - **前置条件**: 系统中存在健康度评分
  - **执行命令**:
    ```bash
    # 查询所有对象健康度
    python scripts/dme_cli.py health score list

    # 按对象ID过滤
    python scripts/dme_cli.py health score list --object_id "<object_id>"

    # 按对象类型过滤
    python scripts/dme_cli.py health score list --object_type "storage_pool"
    ```

- [ ] **查询健康维度的扣分详情**
  - **描述**: 查询对象各健康维度的扣分详情
  - **前置条件**: 对象存在
  - **执行命令**:
    ```bash
    # 查询扣分详情
    python scripts/dme_cli.py health score detail --object_id "<object_id>"
    ```

---

## 7. IP 交换机 (ip_switch)

### 7.1 直接动作

- [ ] **查询以太网交换机列表信息**
  - **描述**: 查询系统中的所有以太网交换机
  - **前置条件**: 系统中存在以太网交换机
  - **执行命令**:
    ```bash
    # 查询所有交换机
    python scripts/dme_cli.py ip_switch list

    # 按名称过滤
    python scripts/dme_cli.py ip_switch list --name "sw_001"

    # 按厂商过滤
    python scripts/dme_cli.py ip_switch list --manufacturer "cisco"
    ```

### 7.2 board 子主题 - 单板管理

- [ ] **查询 IP 交换机单板列表信息**
  - **描述**: 查询交换机的单板列表
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 查询单板列表
    python scripts/dme_cli.py ip_switch board list --switch_id "<switch_id>"
    ```

### 7.3 fan 子主题 - 风扇管理

- [ ] **查询 IP 交换机风扇列表信息**
  - **描述**: 查询交换机的风扇列表
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 查询风扇列表
    python scripts/dme_cli.py ip_switch fan list --switch_id "<switch_id>"
    ```

### 7.4 frame 子主题 - 机框管理

- [ ] **查询 IP 交换机机框列表信息**
  - **描述**: 查询交换机的机框列表
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 查询机框列表
    python scripts/dme_cli.py ip_switch frame list --switch_id "<switch_id>"
    ```

### 7.5 port 子主题 - 端口管理

- [ ] **查询 IP 交换机端口列表信息**
  - **描述**: 查询交换机的端口列表
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 查询所有端口
    python scripts/dme_cli.py ip_switch port list --switch_id "<switch_id>"

    # 按端口类型过滤
    python scripts/dme_cli.py ip_switch port list \
      --switch_id "<switch_id>" \
      --port_type "ethernet"
    ```

### 7.6 power 子主题 - 电源管理

- [ ] **查询 IP 交换机电源列表信息**
  - **描述**: 查询交换机的电源列表
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 查询电源列表
    python scripts/dme_cli.py ip_switch power list --switch_id "<switch_id>"
    ```

### 7.7 subcard 子主题 - 子卡管理

- [ ] **查询 IP 交换机子卡列表信息**
  - **描述**: 查询交换机的子卡列表
  - **前置条件**: 交换机存在
  - **执行命令**:
    ```bash
    # 查询子卡列表
    python scripts/dme_cli.py ip_switch subcard list --switch_id "<switch_id>"
    ```

---

## 8. Kubernetes (kubernetes)

### 8.1 cluster 子主题 - 集群管理

- [ ] **查询容器集群列表**
  - **描述**: 查询系统中的所有容器集群
  - **前置条件**: 系统中存在容器集群
  - **执行命令**:
    ```bash
    # 查询所有集群
    python scripts/dme_cli.py kubernetes cluster list

    # 分页查询
    python scripts/dme_cli.py kubernetes cluster list --page_size 20 --page_no 1
    ```

### 8.2 namespace 子主题 - 命名空间管理

- [ ] **查询容器命名空间列表**
  - **描述**: 查询容器集群的命名空间列表
  - **前置条件**: 容器集群存在
  - **执行命令**:
    ```bash
    # 查询所有命名空间
    python scripts/dme_cli.py kubernetes namespace list

    # 按集群过滤
    python scripts/dme_cli.py kubernetes namespace list --cluster_id "<cluster_id>"
    ```

### 8.3 node 子主题 - 节点管理

- [ ] **查询容器节点列表**
  - **描述**: 查询容器集群的节点列表
  - **前置条件**: 容器集群存在
  - **执行命令**:
    ```bash
    # 查询所有节点
    python scripts/dme_cli.py kubernetes node list

    # 按集群过滤
    python scripts/dme_cli.py kubernetes node list --cluster_id "<cluster_id>"

    # 分页查询
    python scripts/dme_cli.py kubernetes node list --page_size 20 --page_no 1
    ```

### 8.4 pod 子主题 - Pod 管理

- [ ] **查询容器 Pod 列表**
  - **描述**: 查询容器集群的 Pod 列表
  - **前置条件**: 容器集群存在
  - **执行命令**:
    ```bash
    # 查询所有 Pod
    python scripts/dme_cli.py kubernetes pod list

    # 按命名空间过滤
    python scripts/dme_cli.py kubernetes pod list --namespace "<namespace>"

    # 按节点过滤
    python scripts/dme_cli.py kubernetes pod list --node_id "<node_id>"

    # 分页查询
    python scripts/dme_cli.py kubernetes pod list --page_size 20 --page_no 1
    ```

### 8.5 volume 子主题 - 卷管理

- [ ] **查询容器卷列表**
  - **描述**: 查询容器集群的卷列表
  - **前置条件**: 容器集群存在
  - **执行命令**:
    ```bash
    # 查询所有卷
    python scripts/dme_cli.py kubernetes volume list

    # 按命名空间过滤
    python scripts/dme_cli.py kubernetes volume list --namespace "<namespace>"

    # 按节点过滤
    python scripts/dme_cli.py kubernetes volume list --node_id "<node_id>"

    # 分页查询
    python scripts/dme_cli.py kubernetes volume list --page_size 20 --page_no 1
    ```

---

## 9. NAS (nas)

### 9.1 nfs_share 子主题 - NFS 共享管理

- [ ] **批量查询 NFS 共享**
  - **描述**: 查询系统中的所有 NFS 共享
  - **前置条件**: 系统中存在 NFS 共享
  - **执行命令**:
    ```bash
    # 查询所有 NFS 共享
    python scripts/dme_cli.py nas nfs_share list

    # 按名称过滤
    python scripts/dme_cli.py nas nfs_share list --share_name "share_001"

    # 分页查询
    python scripts/dme_cli.py nas nfs_share list --page_size 20 --page_no 1
    ```

- [ ] **创建 NFS 共享**
  - **描述**: 创建新的 NFS 共享
  - **前置条件**: 文件系统存在
  - **执行命令**:
    ```bash
    # 创建 NFS 共享
    python scripts/dme_cli.py nas nfs_share create \
      --share_name "nfs_share_001" \
      --file_system_id "<fs_id>" \
      --description "NFS共享"
    ```

- [ ] **修改 NFS 共享**
  - **描述**: 修改已存在的 NFS 共享
  - **前置条件**: NFS 共享存在
  - **执行命令**:
    ```bash
    # 修改 NFS 共享
    python scripts/dme_cli.py nas nfs_share modify \
      --share_id "<share_id>" \
      --share_name "new_share_name" \
      --description "更新后的描述"
    ```

- [ ] **查询 NFS 共享详情**
  - **描述**: 查询 NFS 共享的详细信息
  - **前置条件**: 共享ID存在
  - **执行命令**:
    ```bash
    # 查询共享详情
    python scripts/dme_cli.py nas nfs_share show --share_id "<share_id>"
    ```

- [ ] **删除 NFS 共享**
  - **描述**: 删除指定的 NFS 共享
  - **前置条件**: 共享存在
  - **执行命令**:
    ```bash
    # 删除单个共享
    python scripts/dme_cli.py nas nfs_share delete --share_id "<share_id>"

    # 删除多个共享
    python scripts/dme_cli.py nas nfs_share delete --share_id "share1,share2"
    ```

### 9.2 smb_share 子主题 - SMB 共享管理

- [ ] **批量查询 SMB 共享**
  - **描述**: 查询系统中的所有 SMB 共享
  - **前置条件**: 系统中存在 SMB 共享
  - **执行命令**:
    ```bash
    # 查询所有 SMB 共享
    python scripts/dme_cli.py nas smb_share list

    # 按名称过滤
    python scripts/dme_cli.py nas smb_share list --share_name "share_001"

    # 分页查询
    python scripts/dme_cli.py nas smb_share list --page_size 20 --page_no 1
    ```

- [ ] **创建 SMB 共享**
  - **描述**: 创建新的 SMB 共享
  - **前置条件**: 文件系统存在
  - **执行命令**:
    ```bash
    # 创建 SMB 共享
    python scripts/dme_cli.py nas smb_share create \
      --share_name "smb_share_001" \
      --file_system_id "<fs_id>" \
      --description "SMB共享"
    ```

- [ ] **修改 SMB 共享**
  - **描述**: 修改已存在的 SMB 共享
  - **前置条件**: SMB 共享存在
  - **执行命令**:
    ```bash
    # 修改 SMB 共享
    python scripts/dme_cli.py nas smb_share modify \
      --share_id "<share_id>" \
      --share_name "new_share_name" \
      --description "更新后的描述"
    ```

- [ ] **查询 SMB 共享详情**
  - **描述**: 查询 SMB 共享的详细信息
  - **前置条件**: 共享ID存在
  - **执行命令**:
    ```bash
    # 查询共享详情
    python scripts/dme_cli.py nas smb_share show --share_id "<share_id>"
    ```

- [ ] **删除 SMB 共享**
  - **描述**: 删除指定的 SMB 共享
  - **前置条件**: 共享存在
  - **执行命令**:
    ```bash
    # 删除单个共享
    python scripts/dme_cli.py nas smb_share delete --share_id "<share_id>"

    # 删除多个共享
    python scripts/dme_cli.py nas smb_share delete --share_id "share1,share2"
    ```

---

## 10. 存储池 (pool)

### 10.1 直接动作

- [ ] **批量查询存储池**
  - **描述**: 查询系统中的所有存储池
  - **前置条件**: 系统中存在存储池
  - **执行命令**:
    ```bash
    # 查询所有存储池
    python scripts/dme_cli.py pool list

    # 按名称过滤
    python scripts/dme_cli.py pool list --name "pool_001"

    # 按存储ID过滤
    python scripts/dme_cli.py pool list --storage_id "<storage_id>"

    # 分页查询
    python scripts/dme_cli.py pool list --page_size 20 --page_no 1
    ```

- [ ] **查询指定存储池详情**
  - **描述**: 查询存储池的详细信息
  - **前置条件**: 存储池ID存在
  - **执行命令**:
    ```bash
    # 查询存储池详情
    python scripts/dme_cli.py pool show --pool_id "<pool_id>"
    ```

---

## 11. SAN 存储区域网络 (san)

### 11.1 lun 子主题 - LUN 管理

- [ ] **批量查询 LUN**
  - **描述**: 查询系统中的所有 LUN
  - **前置条件**: 系统中存在 LUN
  - **执行命令**:
    ```bash
    # 查询所有 LUN
    python scripts/dme_cli.py san lun list

    # 按名称过滤
    python scripts/dme_cli.py san lun list --name "lun_001"

    # 按存储ID过滤
    python scripts/dme_cli.py san lun list --storage_id "<storage_id>"

    # 分页查询
    python scripts/dme_cli.py san lun list --page_size 20 --page_no 1
    ```

- [ ] **查询指定 LUN 详情**
  - **描述**: 查询 LUN 的详细信息
  - **前置条件**: LUN ID 存在
  - **执行命令**:
    ```bash
    # 查询 LUN 详情
    python scripts/dme_cli.py san lun show --volume_id "<volume_id>"
    ```

- [ ] **自定义创建 LUN**
  - **描述**: 创建新的 LUN
  - **前置条件**: 存储池存在
  - **执行命令**:
    ```bash
    # 创建 LUN
    python scripts/dme_cli.py san lun create \
      --storage_id "<storage_id>" \
      --lun_specs '{"capacity": "100GB", "name": "lun_001"}' \
      --pool_id "<pool_id>"
    ```

- [ ] **修改指定 LUN**
  - **描述**: 修改已存在的 LUN
  - **前置条件**: LUN 存在
  - **执行命令**:
    ```bash
    # 修改 LUN
    python scripts/dme_cli.py san lun modify \
      --volume_id "<volume_id>" \
      --name "new_lun_name" \
      --description "更新后的描述"
    ```

- [ ] **批量删除 LUN**
  - **描述**: 删除指定的 LUN
  - **前置条件**: LUN 存在
  - **执行命令**:
    ```bash
    # 删除单个 LUN
    python scripts/dme_cli.py san lun delete --volume_ids "<volume_id>"

    # 删除多个 LUN
    python scripts/dme_cli.py san lun delete --volume_ids "vol1,vol2,vol3"
    ```

- [ ] **批量修改 LUN 名称**
  - **描述**: 批量修改 LUN 的名称
  - **前置条件**: LUN 存在
  - **执行命令**:
    ```bash
    # 批量修改名称
    python scripts/dme_cli.py san lun modify_name \
      --volumes '[{"volume_id":"vol1","name":"new_name1"},{"volume_id":"vol2","name":"new_name2"}]'
    ```

- [ ] **批量扩容 LUN**
  - **描述**: 批量扩容 LUN 的容量
  - **前置条件**: LUN 存在
  - **执行命令**:
    ```bash
    # 批量扩容
    python scripts/dme_cli.py san lun expand \
      --volumes '[{"volume_id":"vol1","capacity":"200GB"},{"volume_id":"vol2","capacity":"300GB"}]'
    ```

- [ ] **查询指定 LUN ID 的连接信息**
  - **描述**: 查询 LUN 的连接信息
  - **前置条件**: LUN ID 存在
  - **执行命令**:
    ```bash
    # 查询连接信息
    python scripts/dme_cli.py san lun connection --volume_ids "<volume_id>"
    ```

- [ ] **指定存储主机或存储主机组查询映射 LUN 信息列表**
  - **描述**: 查询主机或主机组映射的 LUN 信息
  - **前置条件**: 主机或主机组存在
  - **执行命令**:
    ```bash
    # 按主机查询
    python scripts/dme_cli.py san lun mapping --storage_host_id "<host_id>"

    # 按主机组查询
    python scripts/dme_cli.py san lun mapping --storage_host_group_id "<group_id>"
    ```

### 11.2 lun_group 子主题 - LUN 组管理

- [ ] **批量查询 LUN 组**
  - **描述**: 查询系统中的所有 LUN 组
  - **前置条件**: 系统中存在 LUN 组
  - **执行命令**:
    ```bash
    # 查询所有 LUN 组
    python scripts/dme_cli.py san lun_group list

    # 按存储ID过滤
    python scripts/dme_cli.py san lun_group list --storage_id "<storage_id>"

    # 按名称过滤
    python scripts/dme_cli.py san lun_group list --name "group_001"

    # 分页查询
    python scripts/dme_cli.py san lun_group list --page_size 20 --page_no 1
    ```

- [ ] **查询指定 LUN 组详情**
  - **描述**: 查询 LUN 组的详细信息
  - **前置条件**: LUN 组 ID 存在
  - **执行命令**:
    ```bash
    # 查询 LUN 组详情
    python scripts/dme_cli.py san lun_group show --group_id "<group_id>" --storage_id "<storage_id>"
    ```

- [ ] **创建 LUN 组**
  - **描述**: 创建新的 LUN 组
  - **前置条件**: 存储存在
  - **执行命令**:
    ```bash
    # 创建 LUN 组
    python scripts/dme_cli.py san lun_group create \
      --storage_id "<storage_id>" \
      --name "lun_group_001" \
      --description "LUN组"
    ```

- [ ] **删除 LUN 组**
  - **描述**: 删除指定的 LUN 组
  - **前置条件**: LUN 组存在
  - **执行命令**:
    ```bash
    # 删除 LUN 组
    python scripts/dme_cli.py san lun_group delete --storage_id "<storage_id>" --group_id "<group_id>"
    ```

- [ ] **向 LUN 组添加 LUN**
  - **描述**: 向 LUN 组添加一个或多个 LUN
  - **前置条件**: LUN 组和 LUN 都存在
  - **执行命令**:
    ```bash
    # 添加 LUN
    python scripts/dme_cli.py san lun_group add_luns \
      --storage_id "<storage_id>" \
      --group_id "<group_id>" \
      --lun_ids "lun1,lun2,lun3"
    ```

- [ ] **从 LUN 组移除 LUN**
  - **描述**: 从 LUN 组移除一个或多个 LUN
  - **前置条件**: LUN 组存在
  - **执行命令**:
    ```bash
    # 移除 LUN
    python scripts/dme_cli.py san lun_group remove_luns \
      --group_id "<group_id>" \
      --lun_ids "lun1,lun2"
    ```

- [ ] **查询 LUN 组中的 LUN**
  - **描述**: 查询 LUN 组包含的所有 LUN
  - **前置条件**: LUN 组存在
  - **执行命令**:
    ```bash
    # 查询 LUN 组中的 LUN
    python scripts/dme_cli.py san lun_group show_luns --group_id "<group_id>" --storage_id "<storage_id>"
    ```

### 11.3 mapping_view 子主题 - 映射视图管理

- [ ] **批量查询映射视图列表**
  - **描述**: 查询系统中的所有映射视图
  - **前置条件**: 系统中存在映射视图
  - **执行命令**:
    ```bash
    # 查询所有映射视图
    python scripts/dme_cli.py san mapping_view list

    # 按名称过滤
    python scripts/dme_cli.py san mapping_view list --name "view_001"

    # 按存储ID过滤
    python scripts/dme_cli.py san mapping_view list --storage_id "<storage_id>"

    # 分页查询
    python scripts/dme_cli.py san mapping_view list --page_size 20 --page_no 1
    ```

- [ ] **创建映射视图**
  - **描述**: 创建新的映射视图
  - **前置条件**: LUN 组、端口组、主机或主机组存在
  - **执行命令**:
    ```bash
    # 创建映射视图（使用主机）
    python scripts/dme_cli.py san mapping_view create \
      --storage_id "<storage_id>" \
      --port_group_id "<port_group_id>" \
      --name "mapping_view_001" \
      --host_id "<host_id>" \
      --lun_group_id "<lun_group_id>"

    # 创建映射视图（使用主机组）
    python scripts/dme_cli.py san mapping_view create \
      --storage_id "<storage_id>" \
      --port_group_id "<port_group_id>" \
      --name "mapping_view_002" \
      --host_group_id "<host_group_id>" \
      --lun_group_id "<lun_group_id>"
    ```

- [ ] **批量删除映射视图**
  - **描述**: 删除指定的映射视图
  - **前置条件**: 映射视图存在
  - **执行命令**:
    ```bash
    # 删除单个映射视图
    python scripts/dme_cli.py san mapping_view delete --mapping_view_ids "<view_id>"

    # 删除多个映射视图
    python scripts/dme_cli.py san mapping_view delete --mapping_view_ids "view1,view2"
    ```

- [ ] **查询物理主机（组）关联的映射关系**
  - **描述**: 查询主机或主机组关联的映射关系
  - **前置条件**: 主机或主机组存在
  - **执行命令**:
    ```bash
    # 查询主机关联的映射
    python scripts/dme_cli.py san mapping_view query --type "host" --request_id "<request_id>" --storage_id "<storage_id>"

    # 查询主机组关联的映射
    python scripts/dme_cli.py san mapping_view query --type "host_group" --request_id "<request_id>" --storage_id "<storage_id>"
    ```

### 11.4 physical_host 子主题 - 物理主机管理

- [ ] **批量查询物理主机**
  - **描述**: 查询系统中的所有物理主机
  - **前置条件**: 系统中存在物理主机
  - **执行命令**:
    ```bash
    # 查询所有物理主机
    python scripts/dme_cli.py san physical_host list

    # 按名称过滤
    python scripts/dme_cli.py san physical_host list --name "host_001"

    # 按IP过滤
    python scripts/dme_cli.py san physical_host list --ip "192.168.1.100"

    # 分页查询
    python scripts/dme_cli.py san physical_host list --page_size 20 --page_no 1
    ```

- [ ] **查询指定物理主机**
  - **描述**: 查询物理主机的详细信息
  - **前置条件**: 主机ID存在
  - **执行命令**:
    ```bash
    # 查询主机详情
    python scripts/dme_cli.py san physical_host show --host_id "<host_id>"
    ```

- [ ] **接入物理主机**
  - **描述**: 将新的物理主机接入系统
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 接入主机
    python scripts/dme_cli.py san physical_host create \
      --access_mode "iscsi" \
      --type "linux" \
      --host_name "host_001" \
      --ip "192.168.1.100" \
      --port "3260" \
      --host_username "admin" \
      --host_password "password"
    ```

- [ ] **修改物理主机基本信息**
  - **描述**: 修改物理主机的基本信息
  - **前置条件**: 物理主机存在
  - **执行命令**:
    ```bash
    # 修改主机信息
    python scripts/dme_cli.py san physical_host modify \
      --host_id "<host_id>" \
      --host_name "new_host_name" \
      --ip "192.168.1.101"
    ```

- [ ] **移除物理主机**
  - **描述**: 从系统中移除物理主机
  - **前置条件**: 物理主机存在
  - **执行命令**:
    ```bash
    # 移除主机
    python scripts/dme_cli.py san physical_host delete --host_id "<host_id>" --sync_to_storage true
    ```

- [ ] **为物理主机添加启动器**
  - **描述**: 为物理主机添加启动器（IQN）
  - **前置条件**: 物理主机存在
  - **执行命令**:
    ```bash
    # 添加启动器
    python scripts/dme_cli.py san physical_host add_initiators \
      --host_id "<host_id>" \
      --initiators "iqn.2024-01.com.example:host001,iqn.2024-01.com.example:host002"
    ```

- [ ] **从物理主机移除启动器**
  - **描述**: 从物理主机移除启动器
  - **前置条件**: 物理主机存在
  - **执行命令**:
    ```bash
    # 移除启动器
    python scripts/dme_cli.py san physical_host remove_initiators \
      --host_id "<host_id>" \
      --initiators "iqn.2024-01.com.example:host001"
    ```

- [ ] **查询指定物理主机的启动器**
  - **描述**: 查询物理主机配置的所有启动器
  - **前置条件**: 物理主机存在
  - **执行命令**:
    ```bash
    # 查询启动器
    python scripts/dme_cli.py san physical_host show_initiators --host_id "<host_id>"

    # 按协议过滤
    python scripts/dme_cli.py san physical_host show_initiators --host_id "<host_id>" --protocol "iscsi"
    ```

- [ ] **检测存储设备和物理主机连通性**
  - **描述**: 测试存储设备与物理主机的连通性
  - **前置条件**: 存储设备和主机都存在
  - **执行命令**:
    ```bash
    # 测试连通性
    python scripts/dme_cli.py san physical_host test \
      --storage_id "<storage_id>" \
      --host_ids "<host_id>" \
      --auto_zoning true
    ```

- [ ] **查询指定物理主机SSH公钥**
  - **描述**: 查询物理主机的SSH公钥
  - **前置条件**: 物理主机存在且可访问
  - **执行命令**:
    ```bash
    # 查询SSH公钥
    python scripts/dme_cli.py san physical_host query_sshkey --ip "192.168.1.100" --port 22
    ```

- [ ] **保存指定物理主机SSH公钥**
  - **描述**: 保存物理主机的SSH公钥到系统
  - **前置条件**: 物理主机存在
  - **执行命令**:
    ```bash
    # 保存SSH公钥
    python scripts/dme_cli.py san physical_host save_sshkey \
      --ip "192.168.1.100" \
      --key "ssh-rsa AAAAB3NzaC1yc2E... root@host" \
      --port 22
    ```

- [ ] **根据启动器查询关联的物理主机**
  - **描述**: 根据启动器IQN查询关联的物理主机
  - **前置条件**: 启动器存在
  - **执行命令**:
    ```bash
    # 查询关联主机
    python scripts/dme_cli.py san physical_host query_by_initiator \
      --initiator_id "<initiator_id>"
    ```

- [ ] **LUN映射给物理主机**
  - **描述**: 将LUN映射给物理主机
  - **前置条件**: LUN和物理主机都存在
  - **执行命令**:
    ```bash
    # 映射LUN
    python scripts/dme_cli.py san physical_host map_luns \
      --volume_ids "lun1,lun2" \
      --host_id "<host_id>" \
      --mapping_policy "automatic"
    ```

- [ ] **解除主机映射**
  - **描述**: 解除物理主机的LUN映射
  - **前置条件**: 主机存在LUN映射
  - **执行命令**:
    ```bash
    # 解除映射
    python scripts/dme_cli.py san physical_host unmap_luns \
      --volume_ids "lun1,lun2" \
      --host_id "<host_id>"
    ```

### 11.5 physical_host_group 子主题 - 物理主机组管理

- [ ] **批量查询物理主机组**
  - **描述**: 查询系统中的所有物理主机组
  - **前置条件**: 系统中存在物理主机组
  - **执行命令**:
    ```bash
    # 查询所有物理主机组
    python scripts/dme_cli.py san physical_host_group list

    # 按名称过滤
    python scripts/dme_cli.py san physical_host_group list --name "group_001"

    # 分页查询
    python scripts/dme_cli.py san physical_host_group list --page_size 20 --page_no 1
    ```

- [ ] **查询指定物理主机组**
  - **描述**: 查询物理主机组的详细信息
  - **前置条件**: 主机组ID存在
  - **执行命令**:
    ```bash
    # 查询主机组详情
    python scripts/dme_cli.py san physical_host_group show --hostgroup_id "<group_id>"
    ```

- [ ] **创建物理主机组**
  - **描述**: 创建新的物理主机组
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 创建主机组
    python scripts/dme_cli.py san physical_host_group create \
      --name "host_group_001" \
      --host_ids "host1,host2" \
      --description "物理主机组"
    ```

- [ ] **修改物理主机组基本信息**
  - **描述**: 修改物理主机组的基本信息
  - **前置条件**: 物理主机组存在
  - **执行命令**:
    ```bash
    # 修改主机组
    python scripts/dme_cli.py san physical_host_group modify \
      --hostgroup_id "<group_id>" \
      --name "new_group_name" \
      --description "更新后的描述"
    ```

- [ ] **删除指定物理主机组**
  - **描述**: 删除指定的物理主机组
  - **前置条件**: 物理主机组存在
  - **执行命令**:
    ```bash
    # 删除主机组
    python scripts/dme_cli.py san physical_host_group delete --hostgroup_id "<group_id>" --sync_to_storage true
    ```

- [ ] **向物理主机组中增加物理主机**
  - **描述**: 向主机组添加物理主机
  - **前置条件**: 物理主机组和物理主机都存在
  - **执行命令**:
    ```bash
    # 添加主机
    python scripts/dme_cli.py san physical_host_group add_hosts \
      --hostgroup_id "<group_id>" \
      --host_ids "host1,host2" \
      --sync_to_storage true
    ```

- [ ] **物理主机组移除物理主机**
  - **描述**: 从主机组移除物理主机
  - **前置条件**: 物理主机组存在
  - **执行命令**:
    ```bash
    # 移除主机
    python scripts/dme_cli.py san physical_host_group remove_hosts \
      --hostgroup_id "<group_id>" \
      --host_ids "host1" \
      --sync_to_storage true
    ```

- [ ] **LUN映射给物理主机组**
  - **描述**: 将LUN映射给物理主机组
  - **前置条件**: LUN和物理主机组都存在
  - **执行命令**:
    ```bash
    # 映射LUN
    python scripts/dme_cli.py san physical_host_group map_luns \
      --volume_ids "lun1,lun2" \
      --hostgroup_id "<group_id>" \
      --mapping_policy "automatic"
    ```

- [ ] **解除物理主机组映射**
  - **描述**: 解除物理主机组的LUN映射
  - **前置条件**: 主机组存在LUN映射
  - **执行命令**:
    ```bash
    # 解除映射
    python scripts/dme_cli.py san physical_host_group unmap_luns \
      --volume_ids "lun1,lun2" \
      --hostgroup_id "<group_id>"
    ```

### 11.6 port_group 子主题 - 端口组管理

- [ ] **批量查询端口组**
  - **描述**: 查询系统中的所有端口组
  - **前置条件**: 系统中存在端口组
  - **执行命令**:
    ```bash
    # 查询所有端口组
    python scripts/dme_cli.py san port_group list

    # 按存储ID过滤
    python scripts/dme_cli.py san port_group list --storage_id "<storage_id>"

    # 按名称过滤
    python scripts/dme_cli.py san port_group list --name "port_group_001"

    # 分页查询
    python scripts/dme_cli.py san port_group list --page_size 20 --page_no 1
    ```

- [ ] **创建端口组**
  - **描述**: 创建新的端口组
  - **前置条件**: 存储存在
  - **执行命令**:
    ```bash
    # 创建端口组
    python scripts/dme_cli.py san port_group create \
      --storage_id "<storage_id>" \
      --name "port_group_001" \
      --description "端口组"
    ```

- [ ] **批量查询指定端口组的端口**
  - **描述**: 查询端口组包含的所有端口
  - **前置条件**: 端口组存在
  - **执行命令**:
    ```bash
    # 查询端口组端口
    python scripts/dme_cli.py san port_group show_ports \
      --storage_id "<storage_id>" \
      --port_group_id "<port_group_id>"
    ```

- [ ] **批量查询端口组与端口关联关系**
  - **描述**: 查询端口组与端口的关联关系
  - **前置条件**: 端口组存在
  - **执行命令**:
    ```bash
    # 查询关联关系
    python scripts/dme_cli.py san port_group show_relations \
      --storage_id "<storage_id>" \
      --port_group_id "<port_group_id>"
    ```

### 11.7 storage_host 子主题 - 存储主机管理

- [ ] **创建存储主机**
  - **描述**: 在存储设备上创建主机
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 创建存储主机
    python scripts/dme_cli.py san storage_host create \
      --storage_id "<storage_id>" \
      --name "storage_host_001" \
      --os_type "linux" \
      --ip "192.168.1.100" \
      --description "存储主机"
    ```

- [ ] **根据存储主机 ID 列表批量查询存储主机**
  - **描述**: 批量查询存储主机
  - **前置条件**: 存储主机ID存在
  - **执行命令**:
    ```bash
    # 批量查询
    python scripts/dme_cli.py san storage_host batch_query --ids "host1,host2,host3"
    ```

- [ ] **批量查询存储主机**
  - **描述**: 查询存储设备上的所有存储主机
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 查询所有存储主机
    python scripts/dme_cli.py san storage_host list --storage_id "<storage_id>"

    # 按名称过滤
    python scripts/dme_cli.py san storage_host list --name "storage_host_001"

    # 分页查询
    python scripts/dme_cli.py san storage_host list --page_size 20 --page_no 1
    ```

- [ ] **修改存储主机**
  - **描述**: 修改存储主机的配置
  - **前置条件**: 存储主机存在
  - **执行命令**:
    ```bash
    # 修改存储主机
    python scripts/dme_cli.py san storage_host modify \
      --storage_host_id "<host_id>" \
      --storage_host_name "new_name" \
      --storage_host_description "更新后的描述"
    ```

- [ ] **批量删除存储主机**
  - **描述**: 删除存储设备上的存储主机
  - **前置条件**: 存储主机存在
  - **执行命令**:
    ```bash
    # 删除单个存储主机
    python scripts/dme_cli.py san storage_host delete --host_ids "<host_id>"

    # 删除多个存储主机
    python scripts/dme_cli.py san storage_host delete --host_ids "host1,host2"
    ```

- [ ] **批量查询存储主机的路径信息**
  - **描述**: 查询存储主机的多路径信息
  - **前置条件**: 存储主机存在
  - **执行命令**:
    ```bash
    # 查询路径信息
    python scripts/dme_cli.py san storage_host show_paths \
      --storage_id "<storage_id>" \
      --storage_host_ids "<host_id>"

    # 按健康状态过滤
    python scripts/dme_cli.py san storage_host show_paths \
      --storage_id "<storage_id>" \
      --storage_host_ids "<host_id>" \
      --health_status "normal"
    ```

- [ ] **查询存储主机映射的 LUN 信息列表**
  - **描述**: 查询存储主机映射的所有LUN
  - **前置条件**: 存储主机存在
  - **执行命令**:
    ```bash
    # 查询映射的LUN
    python scripts/dme_cli.py san storage_host show_luns --storage_host_id "<host_id>"

    # 按名称过滤
    python scripts/dme_cli.py san storage_host show_luns \
      --storage_host_id "<host_id>" \
      --name "lun_001"

    # 分页查询
    python scripts/dme_cli.py san storage_host show_luns \
      --storage_host_id "<host_id>" \
      --page_size 20 --page_no 1
    ```

### 11.8 storage_host_group 子主题 - 存储主机组管理

- [ ] **创建存储主机组**
  - **描述**: 在存储设备上创建主机组
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 创建存储主机组
    python scripts/dme_cli.py san storage_host_group create \
      --storage_id "<storage_id>" \
      --name "storage_host_group_001" \
      --description "存储主机组"
    ```

- [ ] **批量查询存储主机组**
  - **描述**: 查询存储设备上的所有存储主机组
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 查询所有存储主机组
    python scripts/dme_cli.py san storage_host_group list --storage_id "<storage_id>"

    # 按名称过滤
    python scripts/dme_cli.py san storage_host_group list --name "storage_host_group_001"

    # 分页查询
    python scripts/dme_cli.py san storage_host_group list --page_size 20 --page_no 1
    ```

- [ ] **添加存储主机到存储主机组**
  - **描述**: 向主机组添加存储主机
  - **前置条件**: 存储主机组和存储主机都存在
  - **执行命令**:
    ```bash
    # 添加主机
    python scripts/dme_cli.py san storage_host_group add_hosts \
      --storage_host_group_id "<group_id>" \
      --storage_host_id_ids "host1,host2"
    ```

- [ ] **从存储主机组中移除主机**
  - **描述**: 从主机组移除存储主机
  - **前置条件**: 存储主机组存在
  - **执行命令**:
    ```bash
    # 移除主机
    python scripts/dme_cli.py san storage_host_group remove_hosts \
      --storage_host_group_id "<group_id>" \
      --storage_host_ids "host1"
    ```

- [ ] **批量删除存储主机组**
  - **描述**: 删除存储设备上的存储主机组
  - **前置条件**: 存储主机组存在
  - **执行命令**:
    ```bash
    # 删除单个存储主机组
    python scripts/dme_cli.py san storage_host_group delete --host_group_ids "<group_id>"

    # 删除多个存储主机组
    python scripts/dme_cli.py san storage_host_group delete --host_group_ids "group1,group2"
    ```

- [ ] **查询存储主机组映射的 LUN 信息列表**
  - **描述**: 查询存储主机组映射的所有LUN
  - **前置条件**: 存储主机组存在
  - **执行命令**:
    ```bash
    # 查询映射的LUN
    python scripts/dme_cli.py san storage_host_group show_luns --storage_host_group_id "<group_id>"

    # 按名称过滤
    python scripts/dme_cli.py san storage_host_group show_luns \
      --storage_host_group_id "<group_id>" \
      --name "lun_001"

    # 分页查询
    python scripts/dme_cli.py san storage_host_group show_luns \
      --storage_host_group_id "<group_id>" \
      --page_size 20 --page_no 1
    ```

---

## 12. 存储设备 (storage)

### 12.1 直接动作

- [ ] **批量查询存储设备**
  - **描述**: 查询系统中的所有存储设备
  - **前置条件**: 系统中存在存储设备
  - **执行命令**:
    ```bash
    # 查询所有存储设备
    python scripts/dme_cli.py storage list

    # 按名称过滤
    python scripts/dme_cli.py storage list --name "storage_001"

    # 按厂商过滤
    python scripts/dme_cli.py storage list --manufacturer "huawei"

    # 分页查询
    python scripts/dme_cli.py storage list --page_size 20 --page_no 1
    ```

- [ ] **查询指定存储设备详情**
  - **描述**: 查询存储设备的详细信息
  - **前置条件**: 存储设备ID存在
  - **执行命令**:
    ```bash
    # 查询存储设备详情
    python scripts/dme_cli.py storage show --storage_id "<storage_id>"
    ```

### 12.2 disk 子主题 - 磁盘管理

- [ ] **批量查询磁盘**
  - **描述**: 查询存储设备上的所有磁盘
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 查询所有磁盘
    python scripts/dme_cli.py storage disk list --storage_id "<storage_id>"

    # 按磁盘类型过滤
    python scripts/dme_cli.py storage disk list --storage_id "<storage_id>" --disk_type "ssd"

    # 分页查询
    python scripts/dme_cli.py storage disk list --page_size 20 --page_no 1
    ```

### 12.3 enclosure 子主题 - 机框管理

- [ ] **批量查询机框**
  - **描述**: 查询存储设备上的所有机框
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 查询所有机框
    python scripts/dme_cli.py storage enclosure list --storage_id "<storage_id>"

    # 按机框ID过滤
    python scripts/dme_cli.py storage enclosure list --storage_id "<storage_id>" --enclosure_id "<enclosure_id>"
    ```

### 12.4 file_system 子主题 - 文件系统管理

- [ ] **批量查询文件系统**
  - **描述**: 查询存储设备上的所有文件系统
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 查询所有文件系统
    python scripts/dme_cli.py storage file_system list --storage_id "<storage_id>"

    # 按名称过滤
    python scripts/dme_cli.py storage file_system list --storage_id "<storage_id>" --name "fs_001"

    # 分页查询
    python scripts/dme_cli.py storage file_system list --page_size 20 --page_no 1
    ```

- [ ] **创建文件系统**
  - **描述**: 在存储池上创建文件系统
  - **前置条件**: 存储池存在
  - **执行命令**:
    ```bash
    # 创建文件系统
    python scripts/dme_cli.py storage file_system create \
      --storage_id "<storage_id>" \
      --name "file_system_001" \
      --pool_id "<pool_id>" \
      --capacity "1TB"
    ```

- [ ] **查询指定文件系统详情**
  - **描述**: 查询文件系统的详细信息
  - **前置条件**: 文件系统ID存在
  - **执行命令**:
    ```bash
    # 查询文件系统详情
    python scripts/dme_cli.py storage file_system show --file_system_id "<fs_id>"
    ```

- [ ] **修改文件系统**
  - **描述**: 修改文件系统的配置
  - **前置条件**: 文件系统存在
  - **执行命令**:
    ```bash
    # 修改文件系统
    python scripts/dme_cli.py storage file_system modify \
      --file_system_id "<fs_id>" \
      --name "new_fs_name" \
      --description "更新后的描述"
    ```

- [ ] **扩容文件系统**
  - **描述**: 扩容文件系统的容量
  - **前置条件**: 文件系统存在
  - **执行命令**:
    ```bash
    # 扩容文件系统
    python scripts/dme_cli.py storage file_system expand \
      --file_system_id "<fs_id>" \
      --capacity "2TB"
    ```

- [ ] **删除文件系统**
  - **描述**: 删除指定的文件系统
  - **前置条件**: 文件系统存在
  - **执行命令**:
    ```bash
    # 删除单个文件系统
    python scripts/dme_cli.py storage file_system delete --file_system_ids "<fs_id>"

    # 删除多个文件系统
    python scripts/dme_cli.py storage file_system delete --file_system_ids "fs1,fs2"
    ```

### 12.5 initiator 子主题 - 启动器管理

- [ ] **批量查询启动器**
  - **描述**: 查询存储设备上的所有启动器
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 查询所有启动器
    python scripts/dme_cli.py storage initiator list --storage_id "<storage_id>"

    # 按类型过滤
    python scripts/dme_cli.py storage initiator list --storage_id "<storage_id>" --protocol "iscsi"

    # 分页查询
    python scripts/dme_cli.py storage initiator list --page_size 20 --page_no 1
    ```

- [ ] **查询指定启动器详情**
  - **描述**: 查询启动器的详细信息
  - **前置条件**: 启动器ID存在
  - **执行命令**:
    ```bash
    # 查询启动器详情
    python scripts/dme_cli.py storage initiator show --initiator_id "<initiator_id>" --vstore_id "<vstore_id>"
    ```

- [ ] **创建启动器**
  - **描述**: 在存储设备上创建启动器
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 创建启动器
    python scripts/dme_cli.py storage initiator create \
      --initiator_id "iqn.2024-01.com.example:host001" \
      --vstore_id "<vstore_id>" \
      --alias "host_001_initiator" \
      --multipath true
    ```

- [ ] **修改启动器**
  - **描述**: 修改启动器的配置
  - **前置条件**: 启动器存在
  - **执行命令**:
    ```bash
    # 修改启动器
    python scripts/dme_cli.py storage initiator modify \
      --initiator_id "<initiator_id>" \
      --vstore_id "<vstore_id>" \
      --alias "new_alias" \
      --multipath true
    ```

- [ ] **删除启动器**
  - **描述**: 删除存储设备上的启动器
  - **前置条件**: 启动器存在
  - **执行命令**:
    ```bash
    # 删除单个启动器
    python scripts/dme_cli.py storage initiator delete --initiator_ids "<initiator_id>"

    # 删除多个启动器
    python scripts/dme_cli.py storage initiator delete --initiator_ids "init1,init2"
    ```

### 12.6 port 子主题 - 端口管理

- [ ] **批量查询端口**
  - **描述**: 查询存储设备上的所有端口
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 查询所有端口
    python scripts/dme_cli.py storage port list --storage_id "<storage_id>"

    # 按端口类型过滤
    python scripts/dme_cli.py storage port list --storage_id "<storage_id>" --port_type "eth"

    # 分页查询
    python scripts/dme_cli.py storage port list --page_size 20 --page_no 1
    ```

- [ ] **查询指定端口详情**
  - **描述**: 查询端口的详细信息
  - **前置条件**: 端口ID存在
  - **执行命令**:
    ```bash
    # 查询端口详情
    python scripts/dme_cli.py storage port show --port_id "<port_id>"
    ```

- [ ] **查询绑定端口的成员列表信息**
  - **描述**: 查询绑定端口包含的成员
  - **前置条件**: 绑定端口存在
  - **执行命令**:
    ```bash
    # 查询绑定端口成员
    python scripts/dme_cli.py storage port show_members --bond_port_id "<bond_port_id>"
    ```

### 12.7 quorum_server 子主题 - 仲裁服务器管理

- [ ] **批量查询仲裁服务器**
  - **描述**: 查询系统中的所有仲裁服务器
  - **前置条件**: 系统中存在仲裁服务器
  - **执行命令**:
    ```bash
    # 查询所有仲裁服务器
    python scripts/dme_cli.py storage quorum_server list

    # 按IP过滤
    python scripts/dme_cli.py storage quorum_server list --ip "192.168.1.100"
    ```

- [ ] **创建仲裁服务器**
  - **描述**: 创建新的仲裁服务器
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 创建仲裁服务器
    python scripts/dme_cli.py storage quorum_server create \
      --ip "192.168.1.100" \
      --port 30002 \
      --description "仲裁服务器"
    ```

- [ ] **查询指定仲裁服务器详情**
  - **描述**: 查询仲裁服务器的详细信息
  - **前置条件**: 仲裁服务器ID存在
  - **执行命令**:
    ```bash
    # 查询仲裁服务器详情
    python scripts/dme_cli.py storage quorum_server show --server_id "<server_id>"
    ```

- [ ] **修改仲裁服务器**
  - **描述**: 修改仲裁服务器的配置
  - **前置条件**: 仲裁服务器存在
  - **执行命令**:
    ```bash
    # 修改仲裁服务器
    python scripts/dme_cli.py storage quorum_server modify \
      --server_id "<server_id>" \
      --description "更新后的描述"
    ```

- [ ] **删除仲裁服务器**
  - **描述**: 删除指定的仲裁服务器
  - **前置条件**: 仲裁服务器存在
  - **执行命令**:
    ```bash
    # 删除单个仲裁服务器
    python scripts/dme_cli.py storage quorum_server delete --server_ids "<server_id>"

    # 删除多个仲裁服务器
    python scripts/dme_cli.py storage quorum_server delete --server_ids "server1,server2"
    ```

### 12.8 smartq 子主题 - 智能配额管理

- [ ] **批量查询智能配额**
  - **描述**: 查询文件系统的智能配额
  - **前置条件**: 文件系统存在
  - **执行命令**:
    ```bash
    # 查询所有智能配额
    python scripts/dme_cli.py storage smartq list --file_system_id "<fs_id>"

    # 按用户过滤
    python scripts/dme_cli.py storage smartq list --file_system_id "<fs_id>" --user_id "<user_id>"

    # 分页查询
    python scripts/dme_cli.py storage smartq list --page_size 20 --page_no 1
    ```

- [ ] **创建智能配额**
  - **描述**: 为文件系统创建智能配额
  - **前置条件**: 文件系统存在
  - **执行命令**:
    ```bash
    # 创建智能配额
    python scripts/dme_cli.py storage smartq create \
      --file_system_id "<fs_id>" \
      --user_id "<user_id>" \
      --soft_quota "100GB" \
      --hard_quota "150GB"
    ```

- [ ] **查询指定智能配额详情**
  - **描述**: 查询智能配额的详细信息
  - **前置条件**: 智能配额ID存在
  - **执行命令**:
    ```bash
    # 查询智能配额详情
    python scripts/dme_cli.py storage smartq show --quota_id "<quota_id>"
    ```

- [ ] **修改智能配额**
  - **描述**: 修改智能配额的配置
  - **前置条件**: 智能配额存在
  - **执行命令**:
    ```bash
    # 修改智能配额
    python scripts/dme_cli.py storage smartq modify \
      --quota_id "<quota_id>" \
      --soft_quota "200GB" \
      --hard_quota "250GB"
    ```

- [ ] **删除智能配额**
  - **描述**: 删除智能配额
  - **前置条件**: 智能配额存在
  - **执行命令**:
    ```bash
    # 删除智能配额
    python scripts/dme_cli.py storage smartq delete --quota_ids "<quota_id>"

    # 删除多个智能配额
    python scripts/dme_cli.py storage smartq delete --quota_ids "quota1,quota2"
    ```

### 12.9 user 子主题 - 用户管理

- [ ] **批量查询用户**
  - **描述**: 查询存储设备上的所有用户
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 查询所有用户
    python scripts/dme_cli.py storage user list --storage_id "<storage_id>"

    # 按用户名过滤
    python scripts/dme_cli.py storage user list --storage_id "<storage_id>" --name "user_001"

    # 分页查询
    python scripts/dme_cli.py storage user list --page_size 20 --page_no 1
    ```

- [ ] **创建用户**
  - **描述**: 在存储设备上创建用户
  - **前置条件**: 存储设备存在
  - **执行命令**:
    ```bash
    # 创建用户
    python scripts/dme_cli.py storage user create \
      --storage_id "<storage_id>" \
      --name "user_001" \
      --password "password123" \
      --description "存储用户"
    ```

- [ ] **查询指定用户详情**
  - **描述**: 查询用户的详细信息
  - **前置条件**: 用户ID存在
  - **执行命令**:
    ```bash
    # 查询用户详情
    python scripts/dme_cli.py storage user show --user_id "<user_id>"
    ```

- [ ] **修改用户**
  - **描述**: 修改用户的配置
  - **前置条件**: 用户存在
  - **执行命令**:
    ```bash
    # 修改用户
    python scripts/dme_cli.py storage user modify \
      --user_id "<user_id>" \
      --name "new_username" \
      --description "更新后的描述"
    ```

- [ ] **删除用户**
  - **描述**: 删除存储设备上的用户
  - **前置条件**: 用户存在
  - **执行命令**:
    ```bash
    # 删除单个用户
    python scripts/dme_cli.py storage user delete --user_ids "<user_id>"

    # 删除多个用户
    python scripts/dme_cli.py storage user delete --user_ids "user1,user2"
    ```

---

## 13. 任务管理 (task)

### 13.1 直接动作

- [ ] **批量查询任务**
  - **描述**: 查询系统中的所有任务
  - **前置条件**: 系统中存在任务
  - **执行命令**:
    ```bash
    # 查询所有任务
    python scripts/dme_cli.py task list

    # 按任务状态过滤
    python scripts/dme_cli.py task list --status "running"

    # 分页查询
    python scripts/dme_cli.py task list --page_size 20 --page_no 1
    ```

- [ ] **查询指定任务详情**
  - **描述**: 查询任务的详细信息
  - **前置条件**: 任务ID存在
  - **执行命令**:
    ```bash
    # 查询任务详情
    python scripts/dme_cli.py task show --task_id "<task_id>"
    ```

- [ ] **等待任务完成**
  - **描述**: 等待任务执行完成
  - **前置条件**: 任务ID存在且任务正在运行
  - **执行命令**:
    ```bash
    # 等待任务完成
    python scripts/dme_cli.py task wait --task_id "<task_id>"

    # 设置超时时间（秒）
    python scripts/dme_cli.py task wait --task_id "<task_id>" --timeout 300
    ```

- [ ] **重试任务**
  - **描述**: 重试失败的任务
  - **前置条件**: 任务存在且状态为失败
  - **执行命令**:
    ```bash
    # 重试任务
    python scripts/dme_cli.py task retry --task_id "<task_id>"
    ```

---

## 14. 待办任务管理 (todo_task)

### 14.1 list 动作

- [ ] **查询待办任务列表**
  - **描述**: 查询系统中的所有待办任务
  - **前置条件**: 系统中存在待办任务
  - **执行命令**:
    ```bash
    # 查询所有待办任务
    python scripts/dme_cli.py todo_task list

    # 按状态过滤
    python scripts/dme_cli.py todo_task list --status "pending"

    # 按类型过滤
    python scripts/dme_cli.py todo_task list --type "approval"

    # 分页查询
    python scripts/dme_cli.py todo_task list --page_size 20 --page_no 1
    ```

### 14.2 show 动作

- [ ] **查询待办任务详情**
  - **描述**: 查询待办任务的详细信息
  - **前置条件**: 待办任务ID存在
  - **执行命令**:
    ```bash
    # 查询待办任务详情
    python scripts/dme_cli.py todo_task show --task_id "<task_id>"
    ```

### 14.3 execute 动作

- [ ] **执行待办任务**
  - **描述**: 执行待办任务
  - **前置条件**: 待办任务存在且状态为待执行
  - **执行命令**:
    ```bash
    # 执行待办任务
    python scripts/dme_cli.py todo_task execute --task_id "<task_id>"
    ```

### 14.4 audit 动作

- [ ] **审核待办任务**
  - **描述**: 审核待办任务
  - **前置条件**: 待办任务存在且状态为待审核
  - **执行命令**:
    ```bash
    # 通过审核
    python scripts/dme_cli.py todo_task audit --task_id "<task_id>" --approved true

    # 拒绝审核
    python scripts/dme_cli.py todo_task audit --task_id "<task_id>" --approved false --comment "需要补充信息"
    ```

### 14.5 revoke 动作

- [ ] **撤销审核待办项**
  - **描述**: 撤销待办任务的审核
  - **前置条件**: 待办任务存在且已审核
  - **执行命令**:
    ```bash
    # 撤销审核
    python scripts/dme_cli.py todo_task revoke --task_id "<task_id>"
    ```

### 14.6 close 动作

- [ ] **关闭待办任务**
  - **描述**: 关闭待办任务
  - **前置条件**: 待办任务存在
  - **执行命令**:
    ```bash
    # 关闭待办任务
    python scripts/dme_cli.py todo_task close --task_id "<task_id>"
    ```

---

## 15. 虚拟化服务 (virtualization)

### 15.1 cluster 子主题 - 集群管理

- [ ] **查询集群列表**
  - **描述**: 查询虚拟化平台中的所有集群
  - **前置条件**: 系统中存在集群
  - **执行命令**:
    ```bash
    # 查询所有集群
    python scripts/dme_cli.py virtualization cluster list

    # 按名称过滤
    python scripts/dme_cli.py virtualization cluster list --name "cluster_001"

    # 分页查询
    python scripts/dme_cli.py virtualization cluster list --page_size 20 --page_no 1
    ```

- [ ] **查询指定集群详情**
  - **描述**: 查询集群的详细信息
  - **前置条件**: 集群ID存在
  - **执行命令**:
    ```bash
    # 查询集群详情
    python scripts/dme_cli.py virtualization cluster show --cluster_id "<cluster_id>"
    ```

### 15.2 datastore 子主题 - 数据存储管理

- [ ] **查询数据存储列表**
  - **描述**: 查询虚拟化平台中的所有数据存储
  - **前置条件**: 系统中存在数据存储
  - **执行命令**:
    ```bash
    # 查询所有数据存储
    python scripts/dme_cli.py virtualization datastore list

    # 按名称过滤
    python scripts/dme_cli.py virtualization datastore list --name "datastore_001"

    # 按集群过滤
    python scripts/dme_cli.py virtualization datastore list --cluster_id "<cluster_id>"

    # 分页查询
    python scripts/dme_cli.py virtualization datastore list --page_size 20 --page_no 1
    ```

- [ ] **查询指定数据存储详情**
  - **描述**: 查询数据存储的详细信息
  - **前置条件**: 数据存储ID存在
  - **执行命令**:
    ```bash
    # 查询数据存储详情
    python scripts/dme_cli.py virtualization datastore show --datastore_id "<datastore_id>"
    ```

### 15.3 host 子主题 - 主机管理

- [ ] **查询主机列表**
  - **描述**: 查询虚拟化平台中的所有主机
  - **前置条件**: 系统中存在主机
  - **执行命令**:
    ```bash
    # 查询所有主机
    python scripts/dme_cli.py virtualization host list

    # 按名称过滤
    python scripts/dme_cli.py virtualization host list --name "host_001"

    # 按集群过滤
    python scripts/dme_cli.py virtualization host list --cluster_id "<cluster_id>"

    # 分页查询
    python scripts/dme_cli.py virtualization host list --page_size 20 --page_no 1
    ```

- [ ] **查询指定主机详情**
  - **描述**: 查询主机的详细信息
  - **前置条件**: 主机ID存在
  - **执行命令**:
    ```bash
    # 查询主机详情
    python scripts/dme_cli.py virtualization host show --host_id "<host_id>"
    ```

- [ ] **查询指定主机存储适配器列表**
  - **描述**: 查询主机的存储适配器
  - **前置条件**: 主机存在
  - **执行命令**:
    ```bash
    # 查询存储适配器
    python scripts/dme_cli.py virtualization host adapter_list --host_id "<host_id>"
    ```

### 15.4 site 子主题 - 站点管理

- [ ] **查询站点列表**
  - **描述**: 查询虚拟化平台中的所有站点
  - **前置条件**: 系统中存在站点
  - **执行命令**:
    ```bash
    # 查询所有站点
    python scripts/dme_cli.py virtualization site list

    # 按名称过滤
    python scripts/dme_cli.py virtualization site list --name "site_001"

    # 分页查询
    python scripts/dme_cli.py virtualization site list --page_size 20 --page_no 1
    ```

- [ ] **查询指定站点详情**
  - **描述**: 查询站点的详细信息
  - **前置条件**: 站点ID存在
  - **执行命令**:
    ```bash
    # 查询站点详情
    python scripts/dme_cli.py virtualization site show --site_id "<site_id>"
    ```

### 15.5 vm 子主题 - 虚拟机管理

- [ ] **查询虚拟机列表**
  - **描述**: 查询虚拟化平台中的所有虚拟机
  - **前置条件**: 系统中存在虚拟机
  - **执行命令**:
    ```bash
    # 查询所有虚拟机
    python scripts/dme_cli.py virtualization vm list

    # 按名称过滤
    python scripts/dme_cli.py virtualization vm list --name "vm_001"

    # 按主机过滤
    python scripts/dme_cli.py virtualization vm list --host_id "<host_id>"

    # 按集群过滤
    python scripts/dme_cli.py virtualization vm list --cluster_id "<cluster_id>"

    # 分页查询
    python scripts/dme_cli.py virtualization vm list --page_size 20 --page_no 1
    ```

- [ ] **查询指定虚拟机详情**
  - **描述**: 查询虚拟机的详细信息
  - **前置条件**: 虚拟机ID存在
  - **执行命令**:
    ```bash
    # 查询虚拟机详情
    python scripts/dme_cli.py virtualization vm show --vm_id "<vm_id>"
    ```

### 15.6 vdisk 子主题 - 虚拟磁盘管理

- [ ] **查询虚拟磁盘信息列表**
  - **描述**: 查询虚拟化平台中的所有虚拟磁盘
  - **前置条件**: 系统中存在虚拟磁盘
  - **执行命令**:
    ```bash
    # 查询所有虚拟磁盘
    python scripts/dme_cli.py virtualization vdisk list

    # 按虚拟机过滤
    python scripts/dme_cli.py virtualization vdisk list --vm_id "<vm_id>"

    # 按名称过滤
    python scripts/dme_cli.py virtualization vdisk list --name "vdisk_001"

    # 分页查询
    python scripts/dme_cli.py virtualization vdisk list --page_size 20 --page_no 1
    ```

- [ ] **查询指定虚拟磁盘信息**
  - **描述**: 查询虚拟磁盘的详细信息
  - **前置条件**: 虚拟磁盘ID存在
  - **执行命令**:
    ```bash
    # 查询虚拟磁盘详情
    python scripts/dme_cli.py virtualization vdisk show --vdisk_id "<vdisk_id>"
    ```

### 15.7 disk 子主题 - 物理盘管理

- [ ] **查询物理盘信息**
  - **描述**: 查询主机上的物理盘信息
  - **前置条件**: 主机存在
  - **执行命令**:
    ```bash
    # 查询物理盘
    python scripts/dme_cli.py virtualization disk list

    # 按主机过滤
    python scripts/dme_cli.py virtualization disk list --host_id "<host_id>"
    ```

---

## 16. 工作流 (workflow)

### 16.1 instance 子主题 - 工作流实例管理

- [ ] **创建并执行实例**
  - **描述**: 基于模板创建工作流实例并执行
  - **前置条件**: 工作流模板存在
  - **执行命令**:
    ```bash
    # 创建并执行实例
    python scripts/dme_cli.py workflow instance create \
      --template_id "<template_id>" \
      --input_params '{"param1":"value1","param2":"value2"}'
    ```

- [ ] **查询实例详情**
  - **描述**: 查询工作流实例的详细信息
  - **前置条件**: 实例ID存在
  - **执行命令**:
    ```bash
    # 查询实例详情
    python scripts/dme_cli.py workflow instance show --instance_id "<instance_id>"
    ```

- [ ] **查询步骤日志**
  - **描述**: 查询工作流实例的步骤日志
  - **前置条件**: 实例存在
  - **执行命令**:
    ```bash
    # 查询步骤日志
    python scripts/dme_cli.py workflow instance step_log --instance_id "<instance_id>"

    # 按步骤ID过滤
    python scripts/dme_cli.py workflow instance step_log --instance_id "<instance_id>" --step_id "<step_id>"
    ```

- [ ] **停止实例**
  - **描述**: 停止正在运行的工作流实例
  - **前置条件**: 实例存在且正在运行
  - **执行命令**:
    ```bash
    # 停止实例
    python scripts/dme_cli.py workflow instance stop --instance_id "<instance_id>"
    ```

### 16.2 template 子主题 - 工作流模板管理

- [ ] **分页查询模板列表**
  - **描述**: 查询系统中的所有工作流模板
  - **前置条件**: 系统中存在工作流模板
  - **执行命令**:
    ```bash
    # 查询所有模板
    python scripts/dme_cli.py workflow template list

    # 按名称过滤
    python scripts/dme_cli.py workflow template list --name "template_001"

    # 按分组过滤
    python scripts/dme_cli.py workflow template list --group_id "<group_id>"

    # 分页查询
    python scripts/dme_cli.py workflow template list --page_size 20 --page_no 1
    ```

- [ ] **查询模板详细信息**
  - **描述**: 查询工作流模板的详细信息
  - **前置条件**: 模板ID存在
  - **执行命令**:
    ```bash
    # 查询模板详情
    python scripts/dme_cli.py workflow template show --template_id "<template_id>"
    ```

- [ ] **查询所有模板分组**
  - **描述**: 查询工作流模板的所有分组
  - **前置条件**: 无
  - **执行命令**:
    ```bash
    # 查询所有模板分组
    python scripts/dme_cli.py workflow template groups
    ```

---

## 测试执行说明

### 测试环境要求

1. **环境变量配置**
   ```bash
   export DME_API_URL=<your-dme-api-url>
   export DME_USERNAME=<username>
   export DME_PASSWORD=<password>
   ```

2. **Python环境**
   - Python 3.6+
   - 已安装必要的依赖包

3. **网络连接**
   - 可访问DME API服务
   - 网络延迟在可接受范围内

### 测试执行流程

1. **基础测试**（优先执行）
   - 测试环境准备
   - 连接测试
   - 基本查询功能

2. **核心功能测试**
   - 按主题顺序执行
   - 每个主题先执行查询类操作
   - 再执行创建/修改类操作
   - 最后执行删除类操作

3. **依赖关系处理**
   - 某些操作有前置依赖，需按顺序执行
   - 例如：创建存储池 → 创建文件系统 → 创建共享

### 测试结果记录

对于每个测试用例，记录以下信息：
- [ ] 执行状态（通过/失败/跳过）
- [ ] 执行时间
- [ ] 错误信息（如果有）
- [ ] 备注

### 测试覆盖率统计

- [ ] 主题覆盖率：__/16
- [ ] 子主题覆盖率：__/__
- [ ] 动作覆盖率：__/__

---

## 附录

### 常见错误及处理

1. **连接错误**
   ```
   Error: Failed to connect to DME API
   解决：检查DME_API_URL和网络连接
   ```

2. **认证错误**
   ```
   Error: Authentication failed
   解决：检查用户名和密码
   ```

3. **参数错误**
   ```
   Error: Invalid parameter
   解决：检查参数格式和必需性
   ```

### 测试数据清理

测试完成后，清理测试数据：
- [ ] 删除测试创建的资源
- [ ] 恢复测试修改的配置
- [ ] 检查系统状态是否正常

---

**文档版本**: 1.0  
**最后更新**: 2024年  
**维护者**: DME CLI Team
