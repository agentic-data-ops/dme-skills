# DME CLI 测试执行清单

## 测试环境准备

- [x] 配置环境变量：`export DME_API_URL=<your-dme-api-url>`
- [x] 配置认证信息：`export DME_USERNAME=<username>`
- [x] 配置认证信息：`export DME_PASSWORD=<password>`


---

## 主题测试用例

### 1. aiops - AIOps 智能运维相关操作

#### 1.1 alarm 子主题

- [ ] **aiops alarm list**
  - 描述: 查询告警信息(当前告警,可选择是否包含历史告警)
  - 命令: `python scripts/dme_cli.py aiops alarm list`

- [ ] **aiops alarm ack**
  - 描述: 确认告警
  - 命令: `python scripts/dme_cli.py aiops alarm ack --csns <告警流水号列表>`

- [ ] **aiops alarm unack**
  - 描述: 取消确认告警
  - 命令: `python scripts/dme_cli.py aiops alarm unack --csns <告警流水号列表>`

- [ ] **aiops alarm clear**
  - 描述: 清除告警
  - 命令: `python scripts/dme_cli.py aiops alarm clear --csns <告警流水号列表>`

#### 1.2 check_policy 子主题

- [ ] **aiops check_policy list**
  - 描述: 查询检查策略列表
  - 命令: `python scripts/dme_cli.py aiops check_policy list`

- [ ] **aiops check_policy execute**
  - 描述: 执行检查策略
  - 命令: `python scripts/dme_cli.py aiops check_policy execute --policy_id <策略ID>`

- [ ] **aiops check_policy enable**
  - 描述: 启用检查策略
  - 命令: `python scripts/dme_cli.py aiops check_policy enable --policy_id <策略ID>`

- [ ] **aiops check_policy disable**
  - 描述: 禁用检查策略
  - 命令: `python scripts/dme_cli.py aiops check_policy disable --policy_id <策略ID>`

- [ ] **aiops check_policy delete**
  - 描述: 删除检查策略
  - 命令: `python scripts/dme_cli.py aiops check_policy delete --policy_id <策略ID>`

#### 1.3 check_result 子主题

- [ ] **aiops check_result list**
  - 描述: 查询检查策略异常检查结果列表
  - 命令: `python scripts/dme_cli.py aiops check_result list`

- [ ] **aiops check_result show**
  - 描述: 查询检查策略异常检查结果详情
  - 命令: `python scripts/dme_cli.py aiops check_result show --check_id <检查ID>`

#### 1.4 diagnose_task 子主题

- [ ] **aiops diagnose_task status**
  - 描述: 查询性能诊断任务状态
  - 命令: `python scripts/dme_cli.py aiops diagnose_task status --task_id <任务ID>`

#### 1.5 performance 子主题

- [ ] **aiops performance create_collect_task**
  - 描述: 创建性能文件收集任务
  - 命令: `python scripts/dme_cli.py aiops performance create_collect_task --mo_dn <对象DN> --indicators <指标列表> --start_time <开始时间> --end_time <结束时间>`

- [ ] **aiops performance download_collect_result**
  - 描述: 下载性能文件
  - 命令: `python scripts/dme_cli.py aiops performance download_collect_result --task_id <任务ID> --file_path <保存路径>`

- [ ] **aiops performance query**
  - 描述: 查询历史性能数据
  - 命令: `python scripts/dme_cli.py aiops performance query --mo_dn <对象DN> --indicators <指标列表> --start_time <开始时间> --end_time <结束时间>`

- [ ] **aiops performance show_indicators**
  - 描述: 获取监控对象类型支持的监控指标
  - 命令: `python scripts/dme_cli.py aiops performance show_indicators --object_type <对象类型>`

- [ ] **aiops performance list_indicators**
  - 描述: 获取监控指标
  - 命令: `python scripts/dme_cli.py aiops performance list_indicators`

- [ ] **aiops performance list_object_types**
  - 描述: 获取所有监控对象类型
  - 命令: `python scripts/dme_cli.py aiops performance list_object_types`

#### 1.6 topology 子主题

- [ ] **aiops topology query_san_path**
  - 描述: 查询 SAN 路径拓扑结构（支持 IP_SAN 和 FC_SAN）
  - 命令: `python scripts/dme_cli.py aiops topology query_san_path --host_id <主机ID> --lun_id <LUNID>`

- [ ] **aiops topology query_luns**
  - 描述: 查询拓扑图 LUN 列表
  - 命令: `python scripts/dme_cli.py aiops topology query_luns --host_id <主机ID>`

- [ ] **aiops topology query_vms**
  - 描述: 查询拓扑图虚拟机和虚拟磁盘列表，或查询 BMS 下物理磁盘列表
  - 命令: `python scripts/dme_cli.py aiops topology query_vms --host_id <主机ID>`

- [ ] **aiops topology query_graph_path**
  - 描述: 查询拓扑图库信息（支持 NAS、K8s、DB 等业务类型）
  - 命令: `python scripts/dme_cli.py aiops topology query_graph_path --mo_dn <对象DN>`

- [ ] **aiops topology ipsan_query**
  - 描述: 查询 IP_SAN 网络从主机到存储池间的拓扑结构
  - 命令: `python scripts/dme_cli.py aiops topology ipsan_query --host_ip <主机IP> --pool_id <存储池ID>`

- [ ] **aiops topology fcsan_query**
  - 描述: 查询 FC_SAN 网络从主机到存储池间的拓扑结构
  - 命令: `python scripts/dme_cli.py aiops topology fcsan_query --host_wwn <主机WWN> --pool_id <存储池ID>`

---

### 2. backup - 数据备份管理

#### 2.1 cluster 子主题

- [ ] **backup cluster list**
  - 描述: 查询备份集群列表
  - 命令: `python scripts/dme_cli.py backup cluster list`

- [ ] **backup cluster capacity**
  - 描述: 查询备份集群容量
  - 命令: `python scripts/dme_cli.py backup cluster capacity --cluster_id <集群ID>`

- [ ] **backup cluster quota**
  - 描述: 查询备份集群租户配额列表
  - 命令: `python scripts/dme_cli.py backup cluster quota --cluster_id <集群ID>`

---

### 3. cmdb - CMDB 配置管理

#### 3.1 class 子主题

- [ ] **cmdb class list**
  - 描述: 查询 CMDB 类列表
  - 命令: `python scripts/dme_cli.py cmdb class list`

- [ ] **cmdb class show**
  - 描述: 查询类属性定义
  - 命令: `python scripts/dme_cli.py cmdb class show --class_name <类名>`

#### 3.2 instance 子主题

- [ ] **cmdb instance list**
  - 描述: 查询指定资源类型的所有实例
  - 命令: `python scripts/dme_cli.py cmdb instance list --class_name <类名>`

- [ ] **cmdb instance show**
  - 描述: 查询单个资源实例
  - 命令: `python scripts/dme_cli.py cmdb instance show --mo_dn <对象DN>`

#### 3.3 relation 子主题

- [ ] **cmdb relation list**
  - 描述: 条件查询某类型关系的所有实例
  - 命令: `python scripts/dme_cli.py cmdb relation list --relation_name <关系名>`

- [ ] **cmdb relation show**
  - 描述: 查询单个资源关系的实例
  - 命令: `python scripts/dme_cli.py cmdb relation show --relation_id <关系ID>`

---

### 4. fc_switch - FC 光纤交换机

#### 4.1 直接动作

- [ ] **fc_switch list**
  - 描述: 批量查询光纤交换机
  - 命令: `python scripts/dme_cli.py fc_switch list`

- [ ] **fc_switch sync**
  - 描述: 同步交换机配置
  - 命令: `python scripts/dme_cli.py fc_switch sync --wwn <交换机WWN>`

#### 4.2 alias 子主题

- [ ] **fc_switch alias list**
  - 描述: 批量查询别名
  - 命令: `python scripts/dme_cli.py fc_switch alias list --fabric_id <FabricID>`

- [ ] **fc_switch alias create**
  - 描述: 创建别名
  - 命令: `python scripts/dme_cli.py fc_switch alias create --fabric_id <FabricID> --name <别名名> --members <成员列表>`

- [ ] **fc_switch alias modify**
  - 描述: 修改别名
  - 命令: `python scripts/dme_cli.py fc_switch alias modify --fabric_id <FabricID> --alias_id <别名ID> --name <别名名> --members <成员列表>`

- [ ] **fc_switch alias delete**
  - 描述: 删除别名
  - 命令: `python scripts/dme_cli.py fc_switch alias delete --fabric_id <FabricID> --alias_id <别名ID>`

- [ ] **fc_switch alias show_members**
  - 描述: 查询别名的成员
  - 命令: `python scripts/dme_cli.py fc_switch alias show_members --fabric_id <FabricID> --alias_id <别名ID>`

#### 4.3 controller 子主题

- [ ] **fc_switch controller list**
  - 描述: 查询交换机控制器列表
  - 命令: `python scripts/dme_cli.py fc_switch controller list --wwn <交换机WWN>`

#### 4.4 fabric 子主题

- [ ] **fc_switch fabric list**
  - 描述: 批量查询 fabric
  - 命令: `python scripts/dme_cli.py fc_switch fabric list`

- [ ] **fc_switch fabric backup**
  - 描述: 备份 fabric 配置
  - 命令: `python scripts/dme_cli.py fc_switch fabric backup --fabric_id <FabricID> --file_path <保存路径>`

- [ ] **fc_switch fabric show_ports**
  - 描述: 查询 fabric 的端口列表
  - 命令: `python scripts/dme_cli.py fc_switch fabric show_ports --fabric_id <FabricID>`

#### 4.5 port 子主题

- [ ] **fc_switch port list**
  - 描述: 查询交换机端口列表
  - 命令: `python scripts/dme_cli.py fc_switch port list --wwn <交换机WWN>`

#### 4.6 vsan 子主题

- [ ] **fc_switch vsan list**
  - 描述: 批量查询 vsan
  - 命令: `python scripts/dme_cli.py fc_switch vsan list --fabric_id <FabricID>`

#### 4.7 zone 子主题

- [ ] **fc_switch zone list**
  - 描述: 批量查询 zone
  - 命令: `python scripts/dme_cli.py fc_switch zone list --fabric_id <FabricID>`

- [ ] **fc_switch zone create**
  - 描述: 创建 zone
  - 命令: `python scripts/dme_cli.py fc_switch zone create --fabric_id <FabricID> --name <Zone名> --members <成员列表>`

- [ ] **fc_switch zone modify**
  - 描述: 修改 zone
  - 命令: `python scripts/dme_cli.py fc_switch zone modify --fabric_id <FabricID> --zone_id <ZoneID> --name <Zone名> --members <成员列表>`

- [ ] **fc_switch zone delete**
  - 描述: 删除 zone
  - 命令: `python scripts/dme_cli.py fc_switch zone delete --fabric_id <FabricID> --zone_id <ZoneID>`

- [ ] **fc_switch zone show_members**
  - 描述: 查询 zone 的成员
  - 命令: `python scripts/dme_cli.py fc_switch zone show_members --fabric_id <FabricID> --zone_id <ZoneID>`

- [ ] **fc_switch zone batch_create**
  - 描述: 批量创建 zone
  - 命令: `python scripts/dme_cli.py fc_switch zone batch_create --fabric_id <FabricID> --config <配置文件路径>`

---

### 5. gfs - GFS 全局文件系统

#### 5.1 dataspace 子主题

- [ ] **gfs dataspace list**
  - 描述: 批量查询 Omni-Dataverse
  - 命令: `python scripts/dme_cli.py gfs dataspace list`

- [ ] **gfs dataspace show**
  - 描述: 查询指定 Omni-Dataverse 的容量统计信息
  - 命令: `python scripts/dme_cli.py gfs dataspace show --dataspace_id <数据空间ID>`

- [ ] **gfs dataspace site_list**
  - 描述: 查询 Omni-Dataverse 数据服务站点
  - 命令: `python scripts/dme_cli.py gfs dataspace site_list --dataspace_id <数据空间ID>`

#### 5.2 migration_task 子主题

- [ ] **gfs migration_task list**
  - 描述: 批量查询 Omni-Dataverse 数据迁移任务
  - 命令: `python scripts/dme_cli.py gfs migration_task list`

- [ ] **gfs migration_task create**
  - 描述: 创建 Omni-Dataverse 数据迁移任务
  - 命令: `python scripts/dme_cli.py gfs migration_task create --dataspace_id <数据空间ID> --source_site_id <源站点ID> --target_site_id <目标站点ID> --config <配置>`

- [ ] **gfs migration_task modify**
  - 描述: 修改 Omni-Dataverse 数据迁移任务
  - 命令: `python scripts/dme_cli.py gfs migration_task modify --task_id <任务ID> --config <配置>`

- [ ] **gfs migration_task show**
  - 描述: 查询 Omni-Dataverse 数据迁移任务详情
  - 命令: `python scripts/dme_cli.py gfs migration_task show --task_id <任务ID>`

- [ ] **gfs migration_task operate**
  - 描述: 批量暂停或者启动 Omni-Dataverse 数据迁移任务
  - 命令: `python scripts/dme_cli.py gfs migration_task operate --task_ids <任务ID列表> --operation <操作>`

- [ ] **gfs migration_task delete**
  - 描述: 批量删除 Omni-Dataverse 数据迁移任务
  - 命令: `python scripts/dme_cli.py gfs migration_task delete --task_ids <任务ID列表>`

#### 5.3 namespace 子主题

- [ ] **gfs namespace list**
  - 描述: 批量查询全局命名空间
  - 命令: `python scripts/dme_cli.py gfs namespace list`

- [ ] **gfs namespace create**
  - 描述: 创建全局命名空间
  - 命令: `python scripts/dme_cli.py gfs namespace create --dataspace_id <数据空间ID> --name <命名空间名> --config <配置>`

- [ ] **gfs namespace modify**
  - 描述: 修改指定全局命名空间
  - 命令: `python scripts/dme_cli.py gfs namespace modify --namespace_id <命名空间ID> --name <命名空间名> --config <配置>`

- [ ] **gfs namespace show**
  - 描述: 查询全局命名空间详情
  - 命令: `python scripts/dme_cli.py gfs namespace show --namespace_id <命名空间ID>`

- [ ] **gfs namespace delete**
  - 描述: 删除指定的全局命名空间
  - 命令: `python scripts/dme_cli.py gfs namespace delete --namespace_id <命名空间ID>`

---

### 6. health - 健康度

#### 6.1 data 子主题

- [ ] **health data query**
  - 描述: 查询健康度相关数据（容量预测/性能预测/性能异常）
  - 命令: `python scripts/dme_cli.py health data query --type <数据类型> --object_id <资源ID> --begin_time <开始时间> --end_time <结束时间> --object_type <资源类型> --indicator <指标>`

#### 6.2 score 子主题

- [ ] **health score list**
  - 描述: 查询对象健康度
  - 命令: `python scripts/dme_cli.py health score list --object_type <对象类型>`

- [ ] **health score detail**
  - 描述: 查询健康维度的扣分详情
  - 命令: `python scripts/dme_cli.py health score detail --object_id <对象ID> --object_type <对象类型> --health_dimension <健康维度>`

---

### 7. ip_switch - IP 交换机

#### 7.1 直接动作

- [ ] **ip_switch list**
  - 描述: 查询以太网交换机列表信息
  - 命令: `python scripts/dme_cli.py ip_switch list`

#### 7.2 board 子主题

- [ ] **ip_switch board list**
  - 描述: 查询 IP 交换机单板列表信息
  - 命令: `python scripts/dme_cli.py ip_switch board list --switch_id <交换机ID>`

#### 7.3 fan 子主题

- [ ] **ip_switch fan list**
  - 描述: 查询 IP 交换机风扇列表信息
  - 命令: `python scripts/dme_cli.py ip_switch fan list --switch_id <交换机ID>`

#### 7.4 frame 子主题

- [ ] **ip_switch frame list**
  - 描述: 查询 IP 交换机机框列表信息
  - 命令: `python scripts/dme_cli.py ip_switch frame list --switch_id <交换机ID>`

#### 7.5 port 子主题

- [ ] **ip_switch port list**
  - 描述: 查询 IP 交换机端口列表信息
  - 命令: `python scripts/dme_cli.py ip_switch port list --switch_id <交换机ID>`

#### 7.6 power 子主题

- [ ] **ip_switch power list**
  - 描述: 查询 IP 交换机电源列表信息
  - 命令: `python scripts/dme_cli.py ip_switch power list --switch_id <交换机ID>`

#### 7.7 subcard 子主题

- [ ] **ip_switch subcard list**
  - 描述: 查询 IP 交换机子卡列表信息
  - 命令: `python scripts/dme_cli.py ip_switch subcard list --switch_id <交换机ID>`

---

### 8. kubernetes - Kubernetes

#### 8.1 cluster 子主题

- [ ] **kubernetes cluster list**
  - 描述: 查询容器集群列表
  - 命令: `python scripts/dme_cli.py kubernetes cluster list`

#### 8.2 namespace 子主题

- [ ] **kubernetes namespace list**
  - 描述: 查询容器命名空间列表
  - 命令: `python scripts/dme_cli.py kubernetes namespace list --cluster_id <集群ID>`

#### 8.3 node 子主题

- [ ] **kubernetes node list**
  - 描述: 查询容器节点列表
  - 命令: `python scripts/dme_cli.py kubernetes node list --cluster_id <集群ID>`

#### 8.4 pod 子主题

- [ ] **kubernetes pod list**
  - 描述: 查询容器组列表
  - 命令: `python scripts/dme_cli.py kubernetes pod list --cluster_id <集群ID> --namespace <命名空间>`

#### 8.5 pv 子主题

- [ ] **kubernetes pv list**
  - 描述: 查询容器持久卷列表
  - 命令: `python scripts/dme_cli.py kubernetes pv list --cluster_id <集群ID>`

#### 8.6 pvc 子主题

- [ ] **kubernetes pvc list**
  - 描述: 查询容器持久卷声明列表
  - 命令: `python scripts/dme_cli.py kubernetes pvc list --cluster_id <集群ID> --namespace <命名空间>`

---

### 9. nas - NAS

#### 9.1 cifs_share 子主题

- [ ] **nas cifs_share list**
  - 描述: 批量查询 CIFS 共享
  - 命令: `python scripts/dme_cli.py nas cifs_share list`

- [ ] **nas cifs_share create**
  - 描述: 创建单个 CIFS 共享
  - 命令: `python scripts/dme_cli.py nas cifs_share create --fs_id <文件系统ID> --share_name <共享名> --path <共享路径>`

- [ ] **nas cifs_share modify**
  - 描述: 修改 CIFS 共享
  - 命令: `python scripts/dme_cli.py nas cifs_share modify --share_id <共享ID> --config <配置>`

- [ ] **nas cifs_share delete**
  - 描述: 批量删除 CIFS 共享
  - 命令: `python scripts/dme_cli.py nas cifs_share delete --share_ids <共享ID列表>`

- [ ] **nas cifs_share show**
  - 描述: 查询 CIFS 共享详情
  - 命令: `python scripts/dme_cli.py nas cifs_share show --share_id <共享ID>`

- [ ] **nas cifs_share show_permissions**
  - 描述: 查询 CIFS 共享的权限
  - 命令: `python scripts/dme_cli.py nas cifs_share show_permissions --share_id <共享ID>`

#### 9.2 dataturbo_share 子主题

- [ ] **nas dataturbo_share list**
  - 描述: 批量查询 DataTurbo 共享
  - 命令: `python scripts/dme_cli.py nas dataturbo_share list`

- [ ] **nas dataturbo_share create**
  - 描述: 创建单个 DataTurbo 共享
  - 命令: `python scripts/dme_cli.py nas dataturbo_share create --fs_id <文件系统ID> --share_name <共享名> --config <配置>`

- [ ] **nas dataturbo_share modify**
  - 描述: 修改 DataTurbo 共享
  - 命令: `python scripts/dme_cli.py nas dataturbo_share modify --share_id <共享ID> --config <配置>`

- [ ] **nas dataturbo_share delete**
  - 描述: 批量删除 DataTurbo 共享
  - 命令: `python scripts/dme_cli.py nas dataturbo_share delete --share_ids <共享ID列表>`

- [ ] **nas dataturbo_share show**
  - 描述: 查询 DataTurbo 共享详情
  - 命令: `python scripts/dme_cli.py nas dataturbo_share show --share_id <共享ID>`

- [ ] **nas dataturbo_share show_permissions**
  - 描述: 查询 DataTurbo 共享的权限
  - 命令: `python scripts/dme_cli.py nas dataturbo_share show_permissions --share_id <共享ID>`

#### 9.3 dpc 子主题

- [ ] **nas dpc list**
  - 描述: 批量查询 DPC
  - 命令: `python scripts/dme_cli.py nas dpc list`

- [ ] **nas dpc create**
  - 描述: 创建 DPC
  - 命令: `python scripts/dme_cli.py nas dpc create --fs_id <文件系统ID> --name <DPC名> --config <配置>`

- [ ] **nas dpc modify**
  - 描述: 修改 DPC
  - 命令: `python scripts/dme_cli.py nas dpc modify --dpc_id <DPCID> --config <配置>`

- [ ] **nas dpc delete**
  - 描述: 批量删除 DPC
  - 命令: `python scripts/dme_cli.py nas dpc delete --dpc_ids <DPCID列表>`

- [ ] **nas dpc show**
  - 描述: 查询 DPC 详情
  - 命令: `python scripts/dme_cli.py nas dpc show --dpc_id <DPCID>`

#### 9.4 dtree 子主题

- [ ] **nas dtree list**
  - 描述: 批量查询 DTree
  - 命令: `python scripts/dme_cli.py nas dtree list`

- [ ] **nas dtree create**
  - 描述: 创建 DTree
  - 命令: `python scripts/dme_cli.py nas dtree create --dpc_id <DPCID> --name <DTree名> --quota <配额>`

- [ ] **nas dtree modify**
  - 描述: 修改 DTree
  - 命令: `python scripts/dme_cli.py nas dtree modify --dtree_id <DTreeID> --name <DTree名> --quota <配额>`

- [ ] **nas dtree delete**
  - 描述: 批量删除 DTree
  - 命令: `python scripts/dme_cli.py nas dtree delete --dtree_ids <DTreeID列表>`

- [ ] **nas dtree show**
  - 描述: 查询 DTree 详情
  - 命令: `python scripts/dme_cli.py nas dtree show --dtree_id <DTreeID>`

#### 9.5 filesystem 子主题

- [ ] **nas filesystem list**
  - 描述: 批量查询文件系统
  - 命令: `python scripts/dme_cli.py nas filesystem list`

- [ ] **nas filesystem create**
  - 描述: 创建文件系统
  - 命令: `python scripts/dme_cli.py nas filesystem create --storage_pool_id <存储池ID> --name <文件系统名> --capacity <容量>`

- [ ] **nas filesystem modify**
  - 描述: 修改文件系统
  - 命令: `python scripts/dme_cli.py nas filesystem modify --fs_id <文件系统ID> --config <配置>`

- [ ] **nas filesystem delete**
  - 描述: 批量删除文件系统
  - 命令: `python scripts/dme_cli.py nas filesystem delete --fs_ids <文件系统ID列表>`

- [ ] **nas filesystem show**
  - 描述: 查询文件系统详情
  - 命令: `python scripts/dme_cli.py nas filesystem show --fs_id <文件系统ID>`

#### 9.6 namespace 子主题

- [ ] **nas namespace list**
  - 描述: 批量查询命名空间
  - 命令: `python scripts/dme_cli.py nas namespace list`

- [ ] **nas namespace create**
  - 描述: 创建命名空间
  - 命令: `python scripts/dme_cli.py nas namespace create --name <命名空间名> --config <配置>`

- [ ] **nas namespace modify**
  - 描述: 修改命名空间
  - 命令: `python scripts/dme_cli.py nas namespace modify --namespace_id <命名空间ID> --config <配置>`

- [ ] **nas namespace delete**
  - 描述: 批量删除命名空间
  - 命令: `python scripts/dme_cli.py nas namespace delete --namespace_ids <命名空间ID列表>`

- [ ] **nas namespace show**
  - 描述: 查询命名空间详情
  - 命令: `python scripts/dme_cli.py nas namespace show --namespace_id <命名空间ID>`

#### 9.7 nfs_share 子主题

- [ ] **nas nfs_share list**
  - 描述: 批量查询 NFS 共享
  - 命令: `python scripts/dme_cli.py nas nfs_share list`

- [ ] **nas nfs_share create**
  - 描述: 创建单个 NFS 共享
  - 命令: `python scripts/dme_cli.py nas nfs_share create --fs_id <文件系统ID> --share_name <共享名> --path <共享路径>`

- [ ] **nas nfs_share modify**
  - 描述: 修改 NFS 共享
  - 命令: `python scripts/dme_cli.py nas nfs_share modify --share_id <共享ID> --config <配置>`

- [ ] **nas nfs_share delete**
  - 描述: 批量删除 NFS 共享
  - 命令: `python scripts/dme_cli.py nas nfs_share delete --share_ids <共享ID列表>`

- [ ] **nas nfs_share show**
  - 描述: 查询 NFS 共享详情
  - 命令: `python scripts/dme_cli.py nas nfs_share show --share_id <共享ID>`

- [ ] **nas nfs_share show_permissions**
  - 描述: 查询 NFS 共享的权限
  - 命令: `python scripts/dme_cli.py nas nfs_share show_permissions --share_id <共享ID>`

#### 9.8 quota 子主题

- [ ] **nas quota list**
  - 描述: 批量查询配额
  - 命令: `python scripts/dme_cli.py nas quota list --fs_id <文件系统ID>`

- [ ] **nas quota create**
  - 描述: 创建配额
  - 命令: `python scripts/dme_cli.py nas quota create --fs_id <文件系统ID> --path <路径> --config <配置>`

- [ ] **nas quota modify**
  - 描述: 修改配额
  - 命令: `python scripts/dme_cli.py nas quota modify --quota_id <配额ID> --config <配置>`

- [ ] **nas quota delete**
  - 描述: 批量删除配额
  - 命令: `python scripts/dme_cli.py nas quota delete --quota_ids <配额ID列表>`

- [ ] **nas quota show**
  - 描述: 查询配额详情
  - 命令: `python scripts/dme_cli.py nas quota show --quota_id <配额ID>`

---

### 10. resource - 资源管理

#### 10.1 storage_pool 子主题

- [ ] **resource storage_pool list**
  - 描述: 批量查询存储池
  - 命令: `python scripts/dme_cli.py resource storage_pool list`

- [ ] **resource storage_pool show**
  - 描述: 查询存储池详情
  - 命令: `python scripts/dme_cli.py resource storage_pool show --pool_id <存储池ID>`

#### 10.2 volume_group 子主题

- [ ] **resource volume_group list**
  - 描述: 批量查询卷组
  - 命令: `python scripts/dme_cli.py resource volume_group list`

- [ ] **resource volume_group show**
  - 描述: 查询卷组详情
  - 命令: `python scripts/dme_cli.py resource volume_group show --vg_id <卷组ID>`

#### 10.3 disk_domain 子主题

- [ ] **resource disk_domain list**
  - 描述: 批量查询硬盘域
  - 命令: `python scripts/dme_cli.py resource disk_domain list`

- [ ] **resource disk_domain show**
  - 描述: 查询硬盘域详情
  - 命令: `python scripts/dme_cli.py resource disk_domain show --domain_id <硬盘域ID>`

#### 10.4 qos_policy 子主题

- [ ] **resource qos_policy list**
  - 描述: 批量查询 QoS 策略
  - 命令: `python scripts/dme_cli.py resource qos_policy list`

- [ ] **resource qos_policy create**
  - 描述: 创建 QoS 策略
  - 命令: `python scripts/dme_cli.py resource qos_policy create --name <策略名> --config <配置>`

- [ ] **resource qos_policy modify**
  - 描述: 修改 QoS 策略
  - 命令: `python scripts/dme_cli.py resource qos_policy modify --policy_id <策略ID> --config <配置>`

- [ ] **resource qos_policy delete**
  - 描述: 批量删除 QoS 策略
  - 命令: `python scripts/dme_cli.py resource qos_policy delete --policy_ids <策略ID列表>`

- [ ] **resource qos_policy show**
  - 描述: 查询 QoS 策略详情
  - 命令: `python scripts/dme_cli.py resource qos_policy show --policy_id <策略ID>`

#### 10.5 hypermetro_domain 子主题

- [ ] **resource hypermetro_domain list**
  - 描述: 批量查询双活域
  - 命令: `python scripts/dme_cli.py resource hypermetro_domain list`

- [ ] **resource hypermetro_domain show**
  - 描述: 查询双活域详情
  - 命令: `python scripts/dme_cli.py resource hypermetro_domain show --domain_id <双活域ID>`

#### 10.6 hypermetro_pair 子主题

- [ ] **resource hypermetro_pair list**
  - 描述: 批量查询双活 pair
  - 命令: `python scripts/dme_cli.py resource hypermetro_pair list`

- [ ] **resource hypermetro_pair show**
  - 描述: 查询双活 pair 详情
  - 命令: `python scripts/dme_cli.py resource hypermetro_pair show --pair_id <PairID>`

#### 10.7 replication_pair 子主题

- [ ] **resource replication_pair list**
  - 描述: 批量查询复制 pair
  - 命令: `python scripts/dme_cli.py resource replication_pair list`

- [ ] **resource replication_pair show**
  - 描述: 查询复制 pair 详情
  - 命令: `python scripts/dme_cli.py resource replication_pair show --pair_id <PairID>`

#### 10.8 smart_partition 子主题

- [ ] **resource smart_partition list**
  - 描述: 批量查询分区
  - 命令: `python scripts/dme_cli.py resource smart_partition list`

- [ ] **resource smart_partition show**
  - 描述: 查询分区详情
  - 命令: `python scripts/dme_cli.py resource smart_partition show --partition_id <分区ID>`

#### 10.9 smart_cache_partition 子主题

- [ ] **resource smart_cache_partition list**
  - 描述: 批量查询缓存分区
  - 命令: `python scripts/dme_cli.py resource smart_cache_partition list`

- [ ] **resource smart_cache_partition show**
  - 描述: 查询缓存分区详情
  - 命令: `python scripts/dme_cli.py resource smart_cache_partition show --partition_id <分区ID>`

#### 10.10 dedup_cache 子主题

- [ ] **resource dedup_cache list**
  - 描述: 批量查询重删缓存
  - 命令: `python scripts/dme_cli.py resource dedup_cache list`

- [ ] **resource dedup_cache show**
  - 描述: 查询重删缓存详情
  - 命令: `python scripts/dme_cli.py resource dedup_cache show --cache_id <缓存ID>`

#### 10.11 compression_pool 子主题

- [ ] **resource compression_pool list**
  - 描述: 批量查询压缩池
  - 命令: `python scripts/dme_cli.py resource compression_pool list`

- [ ] **resource compression_pool show**
  - 描述: 查询压缩池详情
  - 命令: `python scripts/dme_cli.py resource compression_pool show --pool_id <池ID>`

---

### 11. san - SAN 存储区域网络

#### 11.1 lun 子主题

- [ ] **san lun list**
  - 描述: 批量查询 LUN
  - 命令: `python scripts/dme_cli.py san lun list`

- [ ] **san lun create**
  - 描述: 创建 LUN
  - 命令: `python scripts/dme_cli.py san lun create --pool_id <存储池ID> --name <LUN名> --capacity <容量> --config <配置>`

- [ ] **san lun modify**
  - 描述: 修改 LUN
  - 命令: `python scripts/dme_cli.py san lun modify --lun_id <LUNID> --config <配置>`

- [ ] **san lun delete**
  - 描述: 批量删除 LUN
  - 命令: `python scripts/dme_cli.py san lun delete --lun_ids <LUNID列表>`

- [ ] **san lun show**
  - 描述: 查询 LUN 详情
  - 命令: `python scripts/dme_cli.py san lun show --lun_id <LUNID>`

- [ ] **san lun expand**
  - 描述: 扩容 LUN
  - 命令: `python scripts/dme_cli.py san lun expand --lun_id <LUNID> --capacity <容量>`

#### 11.2 lun_group 子主题

- [ ] **san lun_group list**
  - 描述: 批量查询 LUN 组
  - 命令: `python scripts/dme_cli.py san lun_group list`

- [ ] **san lun_group create**
  - 描述: 创建 LUN 组
  - 命令: `python scripts/dme_cli.py san lun_group create --name <LUN组名> --description <描述>`

- [ ] **san lun_group modify**
  - 描述: 修改 LUN 组
  - 命令: `python scripts/dme_cli.py san lun_group modify --lun_group_id <LUN组ID> --name <LUN组名> --description <描述>`

- [ ] **san lun_group delete**
  - 描述: 批量删除 LUN 组
  - 命令: `python scripts/dme_cli.py san lun_group delete --lun_group_ids <LUN组ID列表>`

- [ ] **san lun_group show**
  - 描述: 查询 LUN 组详情
  - 命令: `python scripts/dme_cli.py san lun_group show --lun_group_id <LUN组ID>`

- [ ] **san lun_group add_lun**
  - 描述: 添加 LUN 到 LUN 组
  - 命令: `python scripts/dme_cli.py san lun_group add_lun --lun_group_id <LUN组ID> --lun_ids <LUNID列表>`

- [ ] **san lun_group remove_lun**
  - 描述: 从 LUN 组移除 LUN
  - 命令: `python scripts/dme_cli.py san lun_group remove_lun --lun_group_id <LUN组ID> --lun_ids <LUNID列表>`

#### 11.3 mapping_view 子主题

- [ ] **san mapping_view list**
  - 描述: 批量查询映射视图
  - 命令: `python scripts/dme_cli.py san mapping_view list`

- [ ] **san mapping_view create**
  - 描述: 创建映射视图
  - 命令: `python scripts/dme_cli.py san mapping_view create --name <视图名> --description <描述>`

- [ ] **san mapping_view modify**
  - 描述: 修改映射视图
  - 命令: `python scripts/dme_cli.py san mapping_view modify --view_id <视图ID> --name <视图名> --description <描述>`

- [ ] **san mapping_view delete**
  - 描述: 批量删除映射视图
  - 命令: `python scripts/dme_cli.py san mapping_view delete --view_ids <视图ID列表>`

- [ ] **san mapping_view show**
  - 描述: 查询映射视图详情
  - 命令: `python scripts/dme_cli.py san mapping_view show --view_id <视图ID>`

- [ ] **san mapping_view associate**
  - 描述: 关联映射视图
  - 命令: `python scripts/dme_cli.py san mapping_view associate --view_id <视图ID> --host_group_id <主机组ID> --lun_group_id <LUN组ID>`

- [ ] **san mapping_view disassociate**
  - 描述: 解除映射视图关联
  - 命令: `python scripts/dme_cli.py san mapping_view disassociate --view_id <视图ID> --host_group_id <主机组ID> --lun_group_id <LUN组ID>`

#### 11.4 physical_host 子主题

- [ ] **san physical_host list**
  - 描述: 批量查询物理主机
  - 命令: `python scripts/dme_cli.py san physical_host list`

- [ ] **san physical_host create**
  - 描述: 创建物理主机
  - 命令: `python scripts/dme_cli.py san physical_host create --name <主机名> --ip <IP地址> --os <操作系统>`

- [ ] **san physical_host modify**
  - 描述: 修改物理主机
  - 命令: `python scripts/dme_cli.py san physical_host modify --host_id <主机ID> --config <配置>`

- [ ] **san physical_host delete**
  - 描述: 批量删除物理主机
  - 命令: `python scripts/dme_cli.py san physical_host delete --host_ids <主机ID列表>`

- [ ] **san physical_host show**
  - 描述: 查询物理主机详情
  - 命令: `python scripts/dme_cli.py san physical_host show --host_id <主机ID>`

- [ ] **san physical_host add_initiator**
  - 描述: 添加启动器
  - 命令: `python scripts/dme_cli.py san physical_host add_initiator --host_id <主机ID> --initiator <启动器>`

- [ ] **san physical_host remove_initiator**
  - 描述: 移除启动器
  - 命令: `python scripts/dme_cli.py san physical_host remove_initiator --host_id <主机ID> --initiator <启动器>`

#### 11.5 physical_host_group 子主题

- [ ] **san physical_host_group list**
  - 描述: 批量查询物理主机组
  - 命令: `python scripts/dme_cli.py san physical_host_group list`

- [ ] **san physical_host_group create**
  - 描述: 创建物理主机组
  - 命令: `python scripts/dme_cli.py san physical_host_group create --name <主机组名> --description <描述>`

- [ ] **san physical_host_group modify**
  - 描述: 修改物理主机组
  - 命令: `python scripts/dme_cli.py san physical_host_group modify --host_group_id <主机组ID> --name <主机组名> --description <描述>`

- [ ] **san physical_host_group delete**
  - 描述: 批量删除物理主机组
  - 命令: `python scripts/dme_cli.py san physical_host_group delete --host_group_ids <主机组ID列表>`

- [ ] **san physical_host_group show**
  - 描述: 查询物理主机组详情
  - 命令: `python scripts/dme_cli.py san physical_host_group show --host_group_id <主机组ID>`

- [ ] **san physical_host_group add_host**
  - 描述: 添加主机到主机组
  - 命令: `python scripts/dme_cli.py san physical_host_group add_host --host_group_id <主机组ID> --host_ids <主机ID列表>`

- [ ] **san physical_host_group remove_host**
  - 描述: 从主机组移除主机
  - 命令: `python scripts/dme_cli.py san physical_host_group remove_host --host_group_id <主机组ID> --host_ids <主机ID列表>`

#### 11.6 port_group 子主题

- [ ] **san port_group list**
  - 描述: 批量查询端口组
  - 命令: `python scripts/dme_cli.py san port_group list`

- [ ] **san port_group create**
  - 描述: 创建端口组
  - 命令: `python scripts/dme_cli.py san port_group create --name <端口组名> --description <描述>`

- [ ] **san port_group modify**
  - 描述: 修改端口组
  - 命令: `python scripts/dme_cli.py san port_group modify --port_group_id <端口组ID> --name <端口组名> --description <描述>`

- [ ] **san port_group delete**
  - 描述: 批量删除端口组
  - 命令: `python scripts/dme_cli.py san port_group delete --port_group_ids <端口组ID列表>`

- [ ] **san port_group show**
  - 描述: 查询端口组详情
  - 命令: `python scripts/dme_cli.py san port_group show --port_group_id <端口组ID>`

- [ ] **san port_group add_port**
  - 描述: 添加端口到端口组
  - 命令: `python scripts/dme_cli.py san port_group add_port --port_group_id <端口组ID> --port_wwns <端口WWN列表>`

- [ ] **san port_group remove_port**
  - 描述: 从端口组移除端口
  - 命令: `python scripts/dme_cli.py san port_group remove_port --port_group_id <端口组ID> --port_wwns <端口WWN列表>`

#### 11.7 storage_host 子主题

- [ ] **san storage_host list**
  - 描述: 批量查询存储主机
  - 命令: `python scripts/dme_cli.py san storage_host list`

- [ ] **san storage_host create**
  - 描述: 创建存储主机
  - 命令: `python scripts/dme_cli.py san storage_host create --name <主机名> --ip <IP地址> --os <操作系统>`

- [ ] **san storage_host modify**
  - 描述: 修改存储主机
  - 命令: `python scripts/dme_cli.py san storage_host modify --host_id <主机ID> --config <配置>`

- [ ] **san storage_host delete**
  - 描述: 批量删除存储主机
  - 命令: `python scripts/dme_cli.py san storage_host delete --host_ids <主机ID列表>`

- [ ] **san storage_host show**
  - 描述: 查询存储主机详情
  - 命令: `python scripts/dme_cli.py san storage_host show --host_id <主机ID>`

- [ ] **san storage_host add_initiator**
  - 描述: 添加启动器
  - 命令: `python scripts/dme_cli.py san storage_host add_initiator --host_id <主机ID> --initiator <启动器>`

- [ ] **san storage_host remove_initiator**
  - 描述: 移除启动器
  - 命令: `python scripts/dme_cli.py san storage_host remove_initiator --host_id <主机ID> --initiator <启动器>`

#### 11.8 storage_host_group 子主题

- [ ] **san storage_host_group list**
  - 描述: 批量查询存储主机组
  - 命令: `python scripts/dme_cli.py san storage_host_group list`

- [ ] **san storage_host_group create**
  - 描述: 创建存储主机组
  - 命令: `python scripts/dme_cli.py san storage_host_group create --name <主机组名> --description <描述>`

- [ ] **san storage_host_group modify**
  - 描述: 修改存储主机组
  - 命令: `python scripts/dme_cli.py san storage_host_group modify --host_group_id <主机组ID> --name <主机组名> --description <描述>`

- [ ] **san storage_host_group delete**
  - 描述: 批量删除存储主机组
  - 命令: `python scripts/dme_cli.py san storage_host_group delete --host_group_ids <主机组ID列表>`

- [ ] **san storage_host_group show**
  - 描述: 查询存储主机组详情
  - 命令: `python scripts/dme_cli.py san storage_host_group show --host_group_id <主机组ID>`

- [ ] **san storage_host_group add_host**
  - 描述: 添加主机到主机组
  - 命令: `python scripts/dme_cli.py san storage_host_group add_host --host_group_id <主机组ID> --host_ids <主机ID列表>`

- [ ] **san storage_host_group remove_host**
  - 描述: 从主机组移除主机
  - 命令: `python scripts/dme_cli.py san storage_host_group remove_host --host_group_id <主机组ID> --host_ids <主机ID列表>`

---

### 12. server - 服务器

#### 12.1 直接动作

- [ ] **server list**
  - 描述: 批量查询服务器
  - 命令: `python scripts/dme_cli.py server list`

- [ ] **server show**
  - 描述: 查询指定服务器的概览信息
  - 命令: `python scripts/dme_cli.py server show --server_id <服务器ID>`

---

### 13. storage - 存储

#### 13.1 直接动作

- [ ] **storage add**
  - 描述: 添加存储设备（仅支持录入离线存储设备信息）
  - 命令: `python scripts/dme_cli.py storage add --sn <序列号> --name <设备名> --model <型号> --ip <IP地址>`

- [ ] **storage list**
  - 描述: 批量查询存储设备
  - 命令: `python scripts/dme_cli.py storage list`

#### 13.2 controller 子主题

- [ ] **storage controller list**
  - 描述: 批量查询控制器
  - 命令: `python scripts/dme_cli.py storage controller list --storage_id <存储设备ID>`

- [ ] **storage controller show**
  - 描述: 查询控制器详情
  - 命令: `python scripts/dme_cli.py storage controller show --controller_id <控制器ID>`

#### 13.3 disk 子主题

- [ ] **storage disk list**
  - 描述: 批量查询硬盘
  - 命令: `python scripts/dme_cli.py storage disk list --storage_id <存储设备ID>`

- [ ] **storage disk show**
  - 描述: 查询硬盘详情
  - 命令: `python scripts/dme_cli.py storage disk show --disk_id <硬盘ID>`

#### 13.4 enclosure 子主题

- [ ] **storage enclosure list**
  - 描述: 批量查询机框
  - 命令: `python scripts/dme_cli.py storage enclosure list --storage_id <存储设备ID>`

- [ ] **storage enclosure show**
  - 描述: 查询机框详情
  - 命令: `python scripts/dme_cli.py storage enclosure show --enclosure_id <机框ID>`

#### 13.5 interface_module 子主题

- [ ] **storage interface_module list**
  - 描述: 批量查询接口模块
  - 命令: `python scripts/dme_cli.py storage interface_module list --storage_id <存储设备ID>`

- [ ] **storage interface_module show**
  - 描述: 查询接口模块详情
  - 命令: `python scripts/dme_cli.py storage interface_module show --module_id <模块ID>`

#### 13.6 expansion_module 子主题

- [ ] **storage expansion_module list**
  - 描述: 批量查询扩展模块
  - 命令: `python scripts/dme_cli.py storage expansion_module list --storage_id <存储设备ID>`

- [ ] **storage expansion_module show**
  - 描述: 查询扩展模块详情
  - 命令: `python scripts/dme_cli.py storage expansion_module show --module_id <模块ID>`

#### 13.7 fan 子主题

- [ ] **storage fan list**
  - 描述: 批量查询风扇
  - 命令: `python scripts/dme_cli.py storage fan list --storage_id <存储设备ID>`

- [ ] **storage fan show**
  - 描述: 查询风扇详情
  - 命令: `python scripts/dme_cli.py storage fan show --fan_id <风扇ID>`

#### 13.8 power 子主题

- [ ] **storage power list**
  - 描述: 批量查询电源
  - 命令: `python scripts/dme_cli.py storage power list --storage_id <存储设备ID>`

- [ ] **storage power show**
  - 描述: 查询电源详情
  - 命令: `python scripts/dme_cli.py storage power show --power_id <电源ID>`

#### 13.9 port 子主题

- [ ] **storage port list**
  - 描述: 批量查询端口
  - 命令: `python scripts/dme_cli.py storage port list --storage_id <存储设备ID>`

- [ ] **storage port show**
  - 描述: 查询端口详情
  - 命令: `python scripts/dme_cli.py storage port show --port_id <端口ID>`

---

### 14. system - 系统

#### 14.1 直接动作

- [ ] **system certificate**
  - 描述: 获取 DME 证书
  - 命令: `python scripts/dme_cli.py system certificate`

- [ ] **system login**
  - 描述: 认证用户登录
  - 命令: `python scripts/dme_cli.py system login --username <用户名> --password <密码>`

#### 14.2 account 子主题

- [ ] **system account list**
  - 描述: 批量查询用户信息
  - 命令: `python scripts/dme_cli.py system account list`

- [ ] **system account create**
  - 描述: 创建用户
  - 命令: `python scripts/dme_cli.py system account create --username <用户名> --password <密码> --role <角色>`

- [ ] **system account delete**
  - 描述: 删除用户
  - 命令: `python scripts/dme_cli.py system account delete --user_ids <用户ID列表>`

- [ ] **system account show**
  - 描述: 查询指定用户信息
  - 命令: `python scripts/dme_cli.py system account show --user_id <用户ID>`

#### 14.3 dc 子主题

- [ ] **system dc list**
  - 描述: 批量查询数据中心
  - 命令: `python scripts/dme_cli.py system dc list`

- [ ] **system dc show**
  - 描述: 查询数据中心详情
  - 命令: `python scripts/dme_cli.py system dc show --dc_id <数据中心ID>`

#### 14.4 device 子主题

- [ ] **system device list**
  - 描述: 批量查询设备
  - 命令: `python scripts/dme_cli.py system device list`

- [ ] **system device show**
  - 描述: 查询设备详情
  - 命令: `python scripts/dme_cli.py system device show --device_id <设备ID>`

#### 14.5 role 子主题

- [ ] **system role list**
  - 描述: 批量查询角色
  - 命令: `python scripts/dme_cli.py system role list`

- [ ] **system role show**
  - 描述: 查询角色详情
  - 命令: `python scripts/dme_cli.py system role show --role_id <角色ID>`

---

### 15. task - 任务

#### 15.1 async_task 子主题

- [ ] **task async_task list**
  - 描述: 批量查询异步任务
  - 命令: `python scripts/dme_cli.py task async_task list`

- [ ] **task async_task show**
  - 描述: 查询异步任务详情
  - 命令: `python scripts/dme_cli.py task async_task show --task_id <任务ID>`

#### 15.2 resource_task 子主题

- [ ] **task resource_task list**
  - 描述: 批量查询资源任务
  - 命令: `python scripts/dme_cli.py task resource_task list`

- [ ] **task resource_task show**
  - 描述: 查询资源任务详情
  - 命令: `python scripts/dme_cli.py task resource_task show --task_id <任务ID>`

#### 15.3 smartx_task 子主题

- [ ] **task smartx_task list**
  - 描述: 批量查询 SmartX 任务
  - 命令: `python scripts/dme_cli.py task smartx_task list`

- [ ] **task smartx_task show**
  - 描述: 查询 SmartX 任务详情
  - 命令: `python scripts/dme_cli.py task smartx_task show --task_id <任务ID>`

#### 15.4 migration_task 子主题

- [ ] **task migration_task list**
  - 描述: 批量查询迁移任务
  - 命令: `python scripts/dme_cli.py task migration_task list`

- [ ] **task migration_task show**
  - 描述: 查询迁移任务详情
  - 命令: `python scripts/dme_cli.py task migration_task show --task_id <任务ID>`

#### 15.5 rescue_task 子主题

- [ ] **task rescue_task list**
  - 描述: 批量查询救援任务
  - 命令: `python scripts/dme_cli.py task rescue_task list`

- [ ] **task rescue_task show**
  - 描述: 查询救援任务详情
  - 命令: `python scripts/dme_cli.py task rescue_task show --task_id <任务ID>`

#### 15.6 update_task 子主题

- [ ] **task update_task list**
  - 描述: 批量查询升级任务
  - 命令: `python scripts/dme_cli.py task update_task list`

- [ ] **task update_task show**
  - 描述: 查询升级任务详情
  - 命令: `python scripts/dme_cli.py task update_task show --task_id <任务ID>`

#### 15.7 expand_task 子主题

- [ ] **task expand_task list**
  - 描述: 批量查询扩容任务
  - 命令: `python scripts/dme_cli.py task expand_task list`

- [ ] **task expand_task show**
  - 描述: 查询扩容任务详情
  - 命令: `python scripts/dme_cli.py task expand_task show --task_id <任务ID>`

#### 15.8 import_resource 子主题

- [ ] **task import_resource list**
  - 描述: 批量查询资源导入任务
  - 命令: `python scripts/dme_cli.py task import_resource list`

- [ ] **task import_resource show**
  - 描述: 查询资源导入任务详情
  - 命令: `python scripts/dme_cli.py task import_resource show --task_id <任务ID>`

#### 15.9 sync_resource 子主题

- [ ] **task sync_resource list**
  - 描述: 批量查询资源同步任务
  - 命令: `python scripts/dme_cli.py task sync_resource list`

- [ ] **task sync_resource show**
  - 描述: 查询资源同步任务详情
  - 命令: `python scripts/dme_cli.py task sync_resource show --task_id <任务ID>`

---

### 16. user - 用户

#### 16.1 task 子主题

- [ ] **user task list**
  - 描述: 批量查询任务
  - 命令: `python scripts/dme_cli.py user task list`

- [ ] **user task show**
  - 描述: 查询指定任务详情
  - 命令: `python scripts/dme_cli.py user task show --task_id <任务ID>`

- [ ] **user task retry**
  - 描述: 重试任务
  - 命令: `python scripts/dme_cli.py user task retry --task_id <任务ID>`

- [ ] **user task wait**
  - 描述: 等待任务完成
  - 命令: `python scripts/dme_cli.py user task wait --task_id <任务ID> --timeout <超时时间>`

#### 16.2 user 子主题

- [ ] **user user list**
  - 描述: 批量查询用户信息
  - 命令: `python scripts/dme_cli.py user user list`

- [ ] **user user create**
  - 描述: 创建用户
  - 命令: `python scripts/dme_cli.py user user create --username <用户名> --password <密码> --email <邮箱>`

- [ ] **user user delete**
  - 描述: 删除用户
  - 命令: `python scripts/dme_cli.py user user delete --user_ids <用户ID列表>`

- [ ] **user user show**
  - 描述: 查询指定用户信息
  - 命令: `python scripts/dme_cli.py user user show --user_id <用户ID>`

#### 16.3 todo_task 子主题

- [ ] **user todo_task list**
  - 描述: 查询待办任务列表
  - 命令: `python scripts/dme_cli.py user todo_task list`

- [ ] **user todo_task show**
  - 描述: 查询待办任务详情
  - 命令: `python scripts/dme_cli.py user todo_task show --task_id <任务ID>`

- [ ] **user todo_task execute**
  - 描述: 执行待办任务
  - 命令: `python scripts/dme_cli.py user todo_task execute --task_id <任务ID> --comment <评论>`

- [ ] **user todo_task audit**
  - 描述: 审核待办任务
  - 命令: `python scripts/dme_cli.py user todo_task audit --task_id <任务ID> --approved <是否批准> --comment <评论>`

- [ ] **user todo_task revoke**
  - 描述: 撤销审核待办项
  - 命令: `python scripts/dme_cli.py user todo_task revoke --task_id <任务ID> --comment <评论>`

- [ ] **user todo_task close**
  - 描述: 关闭待办任务
  - 命令: `python scripts/dme_cli.py user todo_task close --task_id <任务ID> --comment <评论>`

#### 16.4 todo_task_group 子主题

- [ ] **user todo_task_group list**
  - 描述: 查询待办任务组列表
  - 命令: `python scripts/dme_cli.py user todo_task_group list`

- [ ] **user todo_task_group execute**
  - 描述: 执行待办任务组
  - 命令: `python scripts/dme_cli.py user todo_task_group execute --group_id <组ID> --comment <评论>`

- [ ] **user todo_task_group confirm**
  - 描述: 确认执行定时待办任务组
  - 命令: `python scripts/dme_cli.py user todo_task_group confirm --group_id <组ID>`

#### 16.5 role 子主题

- [ ] **user role list**
  - 描述: 批量查询角色
  - 命令: `python scripts/dme_cli.py user role list`

- [ ] **user role show**
  - 描述: 查询角色详情
  - 命令: `python scripts/dme_cli.py user role show --role_id <角色ID>`

#### 16.6 role_permission 子主题

- [ ] **user role_permission list**
  - 描述: 批量查询角色权限
  - 命令: `python scripts/dme_cli.py user role_permission list --role_id <角色ID>`

#### 16.7 tag_type 子主题

- [ ] **user tag_type list**
  - 描述: 批量查询标签类型
  - 命令: `python scripts/dme_cli.py user tag_type list`

- [ ] **user tag_type create**
  - 描述: 创建标签类型
  - 命令: `python scripts/dme_cli.py user tag_type create --name <类型名> --description <描述>`

- [ ] **user tag_type modify**
  - 描述: 修改标签类型
  - 命令: `python scripts/dme_cli.py user tag_type modify --type_id <类型ID> --name <类型名> --description <描述>`

- [ ] **user tag_type delete**
  - 描述: 批量删除标签类型
  - 命令: `python scripts/dme_cli.py user tag_type delete --type_ids <类型ID列表>`

#### 16.8 tag 子主题

- [ ] **user tag list**
  - 描述: 批量查询标签
  - 命令: `python scripts/dme_cli.py user tag list`

- [ ] **user tag create**
  - 描述: 创建标签
  - 命令: `python scripts/dme_cli.py user tag create --type_id <类型ID> --name <标签名> --value <值>`

- [ ] **user tag modify**
  - 描述: 修改标签
  - 命令: `python scripts/dme_cli.py user tag modify --tag_id <标签ID> --name <标签名> --value <值>`

- [ ] **user tag delete**
  - 描述: 批量删除标签
  - 命令: `python scripts/dme_cli.py user tag delete --tag_ids <标签ID列表>`

---

### 17. virtualization - 虚拟化服务

#### 17.1 直接动作

- [ ] **virtualization cluster list**
  - 描述: 查询集群列表
  - 命令: `python scripts/dme_cli.py virtualization cluster list`

- [ ] **virtualization cluster show**
  - 描述: 查询指定集群详情
  - 命令: `python scripts/dme_cli.py virtualization cluster show --cluster_id <集群ID>`

- [ ] **virtualization datastore list**
  - 描述: 查询数据存储列表
  - 命令: `python scripts/dme_cli.py virtualization datastore list`

- [ ] **virtualization datastore show**
  - 描述: 查询指定数据存储详情
  - 命令: `python scripts/dme_cli.py virtualization datastore show --datastore_id <数据存储ID>`

- [ ] **virtualization host list**
  - 描述: 查询主机列表
  - 命令: `python scripts/dme_cli.py virtualization host list`

- [ ] **virtualization host show**
  - 描述: 查询指定主机详情
  - 命令: `python scripts/dme_cli.py virtualization host show --host_id <主机ID>`

- [ ] **virtualization vm list**
  - 描述: 查询虚拟机列表
  - 命令: `python scripts/dme_cli.py virtualization vm list`

- [ ] **virtualization vm show**
  - 描述: 查询指定虚拟机详情
  - 命令: `python scripts/dme_cli.py virtualization vm show --vm_id <虚拟机ID>`

- [ ] **virtualization vdisk list**
  - 描述: 查询虚拟磁盘信息列表
  - 命令: `python scripts/dme_cli.py virtualization vdisk list`

- [ ] **virtualization vdisk show**
  - 描述: 查询指定虚拟磁盘信息
  - 命令: `python scripts/dme_cli.py virtualization vdisk show --vdisk_id <虚拟磁盘ID>`

- [ ] **virtualization disk list**
  - 描述: 查询物理盘信息
  - 命令: `python scripts/dme_cli.py virtualization disk list`

- [ ] **virtualization site list**
  - 描述: 查询站点列表
  - 命令: `python scripts/dme_cli.py virtualization site list`

- [ ] **virtualization site show**
  - 描述: 查询指定站点详情
  - 命令: `python scripts/dme_cli.py virtualization site show --site_id <站点ID>`

- [ ] **virtualization host adapter_list**
  - 描述: 查询指定主机存储适配器列表
  - 命令: `python scripts/dme_cli.py virtualization host adapter_list --host_id <主机ID>`

---

### 18. workflow - 工作流

#### 18.1 instance 子主题

- [ ] **workflow instance create**
  - 描述: 创建并执行实例
  - 命令: `python scripts/dme_cli.py workflow instance create --template_id <模板ID> --parameters <参数>`

- [ ] **workflow instance show**
  - 描述: 查询实例详情
  - 命令: `python scripts/dme_cli.py workflow instance show --instance_id <实例ID>`

- [ ] **workflow instance stop**
  - 描述: 停止实例
  - 命令: `python scripts/dme_cli.py workflow instance stop --instance_id <实例ID> --reason <原因>`

- [ ] **workflow instance step_log**
  - 描述: 查询步骤日志
  - 命令: `python scripts/dme_cli.py workflow instance step_log --instance_id <实例ID> --step_id <步骤ID>`

#### 18.2 template 子主题

- [ ] **workflow template list**
  - 描述: 分页查询模板列表
  - 命令: `python scripts/dme_cli.py workflow template list`

- [ ] **workflow template show**
  - 描述: 查询模板详细信息
  - 命令: `python scripts/dme_cli.py workflow template show --template_id <模板ID>`

- [ ] **workflow template groups**
  - 描述: 查询所有模板分组
  - 命令: `python scripts/dme_cli.py workflow template groups`

---

## 测试执行统计

- **总测试用例数**: 345
- **已执行**: 0
- **待执行**: 345
- **通过**: 0
- **失败**: 0

## 注意事项

1. 所有命令中的 `<参数>` 都需要替换为实际值
2. 执行前请确保已正确配置环境变量和认证信息
3. 某些操作可能需要管理员权限
4. 建议先执行 `list` 类型的命令了解数据结构
5. 带有 `--help` 的命令可以查看详细的参数说明
6. 删除操作请谨慎执行，建议先查询确认
7. 执行完成后请及时勾选对应的 checkbox
