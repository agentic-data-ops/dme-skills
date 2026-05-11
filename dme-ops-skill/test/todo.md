# DME CLI 测试用例

## 测试环境准备

- [ ] 配置环境变量：`export DME_API_URL=<your-dme-api-url>`
- [ ] 配置认证信息：`export DME_API_USERNAME=<username>`
- [ ] 配置认证信息：`export DME_API_PASSWORD=<password>`

---

## aiops AIOps 智能运维相关操作

### alarm

- [ ] **aiops alarm ack**
  - 描述：确认告警
  - 命令：python scripts/dme_cli.py aiops alarm ack --csns <csns>

- [ ] **aiops alarm clear**
  - 描述：清除告警
  - 命令：python scripts/dme_cli.py aiops alarm clear --csns <csns>

- [ ] **aiops alarm list**
  - 描述：查询告警信息(当前告警,可选择是否包含历史告警)
  - 命令：python scripts/dme_cli.py aiops alarm list

- [ ] **aiops alarm unack**
  - 描述：取消确认告警
  - 命令：python scripts/dme_cli.py aiops alarm unack --csns <csns>

### check_policy

- [ ] **aiops check_policy delete**
  - 描述：删除检查策略
  - 命令：python scripts/dme_cli.py aiops check_policy delete

- [ ] **aiops check_policy disable**
  - 描述：禁用检查策略
  - 命令：python scripts/dme_cli.py aiops check_policy disable

- [ ] **aiops check_policy enable**
  - 描述：启用检查策略
  - 命令：python scripts/dme_cli.py aiops check_policy enable

- [ ] **aiops check_policy execute**
  - 描述：执行检查策略
  - 命令：python scripts/dme_cli.py aiops check_policy execute

- [ ] **aiops check_policy list**
  - 描述：查询检查策略列表
  - 命令：python scripts/dme_cli.py aiops check_policy list

### check_result

- [ ] **aiops check_result list**
  - 描述：查询检查策略异常检查结果列表
  - 命令：python scripts/dme_cli.py aiops check_result list

- [ ] **aiops check_result show**
  - 描述：查询检查策略异常检查结果详情
  - 命令：python scripts/dme_cli.py aiops check_result show

### diagnose_task

- [ ] **aiops diagnose_task create**
  - 描述：创建智能分析任务
  - 命令：python scripts/dme_cli.py aiops diagnose_task create --object_ids <object_ids> --object_type <object_type> --begin_time <begin_time> --end_time <end_time> --analysis_types <analysis_types>

- [ ] **aiops diagnose_task status**
  - 描述：查询性能诊断任务状态
  - 命令：python scripts/dme_cli.py aiops diagnose_task status --task_id <task_id>

### health

- [ ] **aiops health query_data**
  - 描述：查询健康度相关数据（容量预测/性能预测/性能异常）
  - 命令：python scripts/dme_cli.py aiops health query_data --type <type> --object_id <object_id> --begin_time <begin_time> --end_time <end_time> --object_type <object_type> --indicator <indicator>

- [ ] **aiops health show_detail**
  - 描述：查询健康维度的扣分详情
  - 命令：python scripts/dme_cli.py aiops health show_detail --object_id <object_id> --object_type <object_type> --health_dimension <health_dimension>

- [ ] **aiops health show_score**
  - 描述：查询对象健康度
  - 命令：python scripts/dme_cli.py aiops health show_score --object_type <object_type>

### performance

- [ ] **aiops performance create_collect_task**
  - 描述：创建性能文件收集任务
  - 命令：python scripts/dme_cli.py aiops performance create_collect_task

- [ ] **aiops performance download_collect_result**
  - 描述：下载性能文件
  - 命令：python scripts/dme_cli.py aiops performance download_collect_result

- [ ] **aiops performance list_indicators**
  - 描述：列出监控对象类型支持的监控指标
  - 命令：python scripts/dme_cli.py aiops performance list_indicators

- [ ] **aiops performance list_object_types**
  - 描述：获取所有监控对象类型
  - 命令：python scripts/dme_cli.py aiops performance list_object_types

- [ ] **aiops performance query**
  - 描述：查询历史性能数据
  - 命令：python scripts/dme_cli.py aiops performance query

- [ ] **aiops performance show_indicators**
  - 描述：显示监控指标详细信息
  - 命令：python scripts/dme_cli.py aiops performance show_indicators

### topology

- [ ] **aiops topology fcsan_query**
  - 描述：查询 FC_SAN 网络从主机到存储池间的拓扑结构
  - 命令：python scripts/dme_cli.py aiops topology fcsan_query --entry_objects <entry_objects>

- [ ] **aiops topology ipsan_query**
  - 描述：查询 IP_SAN 网络从主机到存储池间的拓扑结构
  - 命令：python scripts/dme_cli.py aiops topology ipsan_query --entry_objects <entry_objects>

- [ ] **aiops topology query_graph_path**
  - 描述：查询拓扑图库信息（支持 NAS、K8s、DB 等业务类型）
  - 命令：python scripts/dme_cli.py aiops topology query_graph_path --entry_res_type <entry_res_type> --entry_res_id <entry_res_id>

- [ ] **aiops topology query_luns**
  - 描述：查询拓扑图 LUN 列表
  - 命令：python scripts/dme_cli.py aiops topology query_luns --entry_objects <entry_objects> --storage_pool_id <storage_pool_id>

- [ ] **aiops topology query_san_path**
  - 描述：查询 SAN 路径拓扑结构（支持 IP_SAN 和 FC_SAN）
  - 命令：python scripts/dme_cli.py aiops topology query_san_path --entry_objects <entry_objects>

- [ ] **aiops topology query_vms**
  - 描述：查询拓扑图虚拟机和虚拟磁盘列表，或查询 BMS 下物理磁盘列表
  - 命令：python scripts/dme_cli.py aiops topology query_vms --entry_objects <entry_objects> --host_id <host_id>

## backup 数据备份管理 (Backup) 相关操作

### cluster

- [ ] **backup cluster capacity**
  - 描述：查询备份集群容量
  - 命令：python scripts/dme_cli.py backup cluster capacity --cluster_id <cluster_id>

- [ ] **backup cluster list**
  - 描述：查询备份集群列表
  - 命令：python scripts/dme_cli.py backup cluster list

- [ ] **backup cluster quota**
  - 描述：查询备份集群租户配额列表
  - 命令：python scripts/dme_cli.py backup cluster quota --cluster_id <cluster_id>

## cmdb CMDB (Configuration Management Database) 相关操作

### class

- [ ] **cmdb class list**
  - 描述：查询 CMDB 类列表
  - 命令：python scripts/dme_cli.py cmdb class list

- [ ] **cmdb class show**
  - 描述：查询类属性定义
  - 命令：python scripts/dme_cli.py cmdb class show --class_name <class_name>

### instance

- [ ] **cmdb instance list**
  - 描述：查询指定资源类型的所有实例
  - 命令：python scripts/dme_cli.py cmdb instance list --condition <condition>

- [ ] **cmdb instance show**
  - 描述：查询单个资源实例
  - 命令：python scripts/dme_cli.py cmdb instance show

### relation

- [ ] **cmdb relation list**
  - 描述：条件查询某类型关系的所有实例
  - 命令：python scripts/dme_cli.py cmdb relation list --condition <condition>

- [ ] **cmdb relation show**
  - 描述：查询单个资源关系的实例
  - 命令：python scripts/dme_cli.py cmdb relation show

## fc_switch FC Switch (光纤交换机) 相关操作

### alias

- [ ] **fc_switch alias create**
  - 描述：创建别名
  - 命令：python scripts/dme_cli.py fc_switch alias create --name <name> --fabric_wwn <fabric_wwn> --vsan_wwn <vsan_wwn>

- [ ] **fc_switch alias delete**
  - 描述：删除别名
  - 命令：python scripts/dme_cli.py fc_switch alias delete --alias_id <alias_id>

- [ ] **fc_switch alias list**
  - 描述：批量查询别名
  - 命令：python scripts/dme_cli.py fc_switch alias list --fabric_wwn <fabric_wwn>

- [ ] **fc_switch alias modify**
  - 描述：修改别名
  - 命令：python scripts/dme_cli.py fc_switch alias modify --alias_id <alias_id>

- [ ] **fc_switch alias show_members**
  - 描述：查询别名的成员
  - 命令：python scripts/dme_cli.py fc_switch alias show_members --alias_id <alias_id>

### controller

- [ ] **fc_switch controller list**
  - 描述：查询交换机控制器列表
  - 命令：python scripts/dme_cli.py fc_switch controller list

### fabric

- [ ] **fc_switch fabric backup**
  - 描述：备份 fabric 配置
  - 命令：python scripts/dme_cli.py fc_switch fabric backup --fabric_id <fabric_id> --backup_server_id <backup_server_id>

- [ ] **fc_switch fabric list**
  - 描述：批量查询 fabric
  - 命令：python scripts/dme_cli.py fc_switch fabric list

- [ ] **fc_switch fabric show_ports**
  - 描述：查询 fabric 的端口列表
  - 命令：python scripts/dme_cli.py fc_switch fabric show_ports --fabric_id <fabric_id>

### port

- [ ] **fc_switch port list**
  - 描述：查询交换机端口列表
  - 命令：python scripts/dme_cli.py fc_switch port list

### vsan

- [ ] **fc_switch vsan list**
  - 描述：批量查询 vsan
  - 命令：python scripts/dme_cli.py fc_switch vsan list

### zone

- [ ] **fc_switch zone batch_create**
  - 描述：批量创建 zone
  - 命令：python scripts/dme_cli.py fc_switch zone batch_create --is_active_zone <is_active_zone> --zones <zones>

- [ ] **fc_switch zone create**
  - 描述：创建 zone
  - 命令：python scripts/dme_cli.py fc_switch zone create --name <name> --fabric_wwn <fabric_wwn> --vsan_wwn <vsan_wwn>

- [ ] **fc_switch zone delete**
  - 描述：删除 zone
  - 命令：python scripts/dme_cli.py fc_switch zone delete --zone_id <zone_id>

- [ ] **fc_switch zone list**
  - 描述：批量查询 zone
  - 命令：python scripts/dme_cli.py fc_switch zone list

- [ ] **fc_switch zone modify**
  - 描述：修改 zone
  - 命令：python scripts/dme_cli.py fc_switch zone modify --zone_id <zone_id>

- [ ] **fc_switch zone show_members**
  - 描述：查询 zone 的成员
  - 命令：python scripts/dme_cli.py fc_switch zone show_members --zone_id <zone_id>

### 直接动作

- [ ] **fc_switch list**
  - 描述：批量查询光纤交换机
  - 命令：python scripts/dme_cli.py fc_switch list

- [ ] **fc_switch sync**
  - 描述：同步交换机配置
  - 命令：python scripts/dme_cli.py fc_switch sync --switch_id <switch_id>

## gfs GFS (Global File System) 相关操作

### dataspace

- [ ] **gfs dataspace list**
  - 描述：批量查询 Omni-Dataverse
  - 命令：python scripts/dme_cli.py gfs dataspace list

- [ ] **gfs dataspace show**
  - 描述：查询指定 Omni-Dataverse 的容量统计信息
  - 命令：python scripts/dme_cli.py gfs dataspace show

- [ ] **gfs dataspace site_list**
  - 描述：查询 Omni-Dataverse 数据服务站点
  - 命令：python scripts/dme_cli.py gfs dataspace site_list

### migration_task

- [ ] **gfs migration_task create**
  - 描述：创建 Omni-Dataverse 数据迁移任务
  - 命令：python scripts/dme_cli.py gfs migration_task create

- [ ] **gfs migration_task delete**
  - 描述：批量删除 Omni-Dataverse 数据迁移任务
  - 命令：python scripts/dme_cli.py gfs migration_task delete

- [ ] **gfs migration_task list**
  - 描述：批量查询 Omni-Dataverse 数据迁移任务
  - 命令：python scripts/dme_cli.py gfs migration_task list

- [ ] **gfs migration_task modify**
  - 描述：修改 Omni-Dataverse 数据迁移任务
  - 命令：python scripts/dme_cli.py gfs migration_task modify

- [ ] **gfs migration_task operate**
  - 描述：批量暂停或者启动 Omni-Dataverse 数据迁移任务
  - 命令：python scripts/dme_cli.py gfs migration_task operate

- [ ] **gfs migration_task show**
  - 描述：查询 Omni-Dataverse 数据迁移任务详情
  - 命令：python scripts/dme_cli.py gfs migration_task show

### namespace

- [ ] **gfs namespace create**
  - 描述：创建全局命名空间
  - 命令：python scripts/dme_cli.py gfs namespace create --smart_share_members <smart_share_members>

- [ ] **gfs namespace delete**
  - 描述：删除指定的全局命名空间
  - 命令：python scripts/dme_cli.py gfs namespace delete

- [ ] **gfs namespace list**
  - 描述：批量查询全局命名空间
  - 命令：python scripts/dme_cli.py gfs namespace list

- [ ] **gfs namespace modify**
  - 描述：修改指定全局命名空间
  - 命令：python scripts/dme_cli.py gfs namespace modify

- [ ] **gfs namespace show**
  - 描述：查询全局命名空间详情
  - 命令：python scripts/dme_cli.py gfs namespace show

## ip_switch IP 交换机 (IPSwitch) 管理相关操作

### board

- [ ] **ip_switch board list**
  - 描述：查询 IP 交换机单板列表信息
  - 命令：python scripts/dme_cli.py ip_switch board list --ipswitch_id <ipswitch_id>

### fan

- [ ] **ip_switch fan list**
  - 描述：查询 IP 交换机风扇列表信息
  - 命令：python scripts/dme_cli.py ip_switch fan list --ipswitch_id <ipswitch_id>

### frame

- [ ] **ip_switch frame list**
  - 描述：查询 IP 交换机机框列表信息
  - 命令：python scripts/dme_cli.py ip_switch frame list --ipswitch_id <ipswitch_id>

### port

- [ ] **ip_switch port list**
  - 描述：查询 IP 交换机端口列表信息
  - 命令：python scripts/dme_cli.py ip_switch port list --ipswitch_id <ipswitch_id>

### power

- [ ] **ip_switch power list**
  - 描述：查询 IP 交换机电源列表信息
  - 命令：python scripts/dme_cli.py ip_switch power list --ipswitch_id <ipswitch_id>

### subcard

- [ ] **ip_switch subcard list**
  - 描述：查询 IP 交换机子卡列表信息
  - 命令：python scripts/dme_cli.py ip_switch subcard list --ipswitch_id <ipswitch_id>

### 直接动作

- [ ] **ip_switch list**
  - 描述：查询以太网交换机列表信息
  - 命令：python scripts/dme_cli.py ip_switch list

## kubernetes Kubernetes 相关操作

### cluster

- [ ] **kubernetes cluster list**
  - 描述：查询容器集群列表
  - 命令：python scripts/dme_cli.py kubernetes cluster list

### namespace

- [ ] **kubernetes namespace list**
  - 描述：查询容器命名空间列表
  - 命令：python scripts/dme_cli.py kubernetes namespace list

### node

- [ ] **kubernetes node list**
  - 描述：查询容器节点列表
  - 命令：python scripts/dme_cli.py kubernetes node list

### pod

- [ ] **kubernetes pod list**
  - 描述：查询容器组列表
  - 命令：python scripts/dme_cli.py kubernetes pod list

### pv

- [ ] **kubernetes pv list**
  - 描述：查询容器持久卷列表
  - 命令：python scripts/dme_cli.py kubernetes pv list

### pvc

- [ ] **kubernetes pvc list**
  - 描述：查询容器持久卷声明列表
  - 命令：python scripts/dme_cli.py kubernetes pvc list

## nas NAS 相关操作

### cifs_share

- [ ] **nas cifs_share create**
  - 描述：创建单个 CIFS 共享
  - 命令：python scripts/dme_cli.py nas cifs_share create

- [ ] **nas cifs_share delete**
  - 描述：批量删除 CIFS 共享
  - 命令：python scripts/dme_cli.py nas cifs_share delete

- [ ] **nas cifs_share list**
  - 描述：批量查询 CIFS 共享
  - 命令：python scripts/dme_cli.py nas cifs_share list

- [ ] **nas cifs_share modify**
  - 描述：修改指定 CIFS 共享
  - 命令：python scripts/dme_cli.py nas cifs_share modify

- [ ] **nas cifs_share show**
  - 描述：查询指定 CIFS 共享详情
  - 命令：python scripts/dme_cli.py nas cifs_share show

- [ ] **nas cifs_share show_permissions**
  - 描述：查询单个 CIFS 共享的权限列表（用户/IP/文件过滤）
  - 命令：python scripts/dme_cli.py nas cifs_share show_permissions

### dataturbo_share

- [ ] **nas dataturbo_share create**
  - 描述：创建 DataTurbo 共享
  - 命令：python scripts/dme_cli.py nas dataturbo_share create

- [ ] **nas dataturbo_share delete**
  - 描述：批量删除 DataTurbo 共享
  - 命令：python scripts/dme_cli.py nas dataturbo_share delete

- [ ] **nas dataturbo_share list**
  - 描述：查询 DataTurbo 共享列表
  - 命令：python scripts/dme_cli.py nas dataturbo_share list

- [ ] **nas dataturbo_share modify**
  - 描述：修改指定 DataTurbo 共享
  - 命令：python scripts/dme_cli.py nas dataturbo_share modify

- [ ] **nas dataturbo_share show**
  - 描述：查询指定 DataTurbo 共享详情
  - 命令：python scripts/dme_cli.py nas dataturbo_share show

- [ ] **nas dataturbo_share show_permissions**
  - 描述：查询 DataTurbo 共享管理员权限列表
  - 命令：python scripts/dme_cli.py nas dataturbo_share show_permissions

### dpc

- [ ] **nas dpc list**
  - 描述：批量查询并行客户端列表
  - 命令：python scripts/dme_cli.py nas dpc list

- [ ] **nas dpc show**
  - 描述：查询并行客户端详情
  - 命令：python scripts/dme_cli.py nas dpc show

### dtree

- [ ] **nas dtree create**
  - 描述：创建并共享 Dtree
  - 命令：python scripts/dme_cli.py nas dtree create

- [ ] **nas dtree delete**
  - 描述：批量删除 Dtree
  - 命令：python scripts/dme_cli.py nas dtree delete

- [ ] **nas dtree list**
  - 描述：查询 Dtree 列表
  - 命令：python scripts/dme_cli.py nas dtree list

- [ ] **nas dtree modify**
  - 描述：修改指定 Dtree
  - 命令：python scripts/dme_cli.py nas dtree modify

- [ ] **nas dtree show**
  - 描述：查询指定 Dtree 详情
  - 命令：python scripts/dme_cli.py nas dtree show

### filesystem

- [ ] **nas filesystem batch_modify**
  - 描述：批量修改文件系统（支持批量修改名称）
  - 命令：python scripts/dme_cli.py nas filesystem batch_modify

- [ ] **nas filesystem create**
  - 描述：自定义创建文件系统
  - 命令：python scripts/dme_cli.py nas filesystem create

- [ ] **nas filesystem delete**
  - 描述：批量删除文件系统
  - 命令：python scripts/dme_cli.py nas filesystem delete

- [ ] **nas filesystem list**
  - 描述：批量查询文件系统
  - 命令：python scripts/dme_cli.py nas filesystem list

- [ ] **nas filesystem modify**
  - 描述：修改指定文件系统（完整参数）
  - 命令：python scripts/dme_cli.py nas filesystem modify

- [ ] **nas filesystem query_available**
  - 描述：查询可用的文件系统（支持远程复制）
  - 命令：python scripts/dme_cli.py nas filesystem query_available --remote_storage_id <remote_storage_id>

- [ ] **nas filesystem show**
  - 描述：查询指定文件系统详情
  - 命令：python scripts/dme_cli.py nas filesystem show

### namespace

- [ ] **nas namespace create**
  - 描述：批量创建命名空间
  - 命令：python scripts/dme_cli.py nas namespace create

- [ ] **nas namespace delete**
  - 描述：批量删除命名空间
  - 命令：python scripts/dme_cli.py nas namespace delete --namespace_ids <namespace_ids>

- [ ] **nas namespace list**
  - 描述：批量查询命名空间
  - 命令：python scripts/dme_cli.py nas namespace list

- [ ] **nas namespace modify**
  - 描述：修改指定命名空间
  - 命令：python scripts/dme_cli.py nas namespace modify --namespace_id <namespace_id>

- [ ] **nas namespace show**
  - 描述：查询指定命名空间详情
  - 命令：python scripts/dme_cli.py nas namespace show --namespace_id <namespace_id>

### nfs_share

- [ ] **nas nfs_share create**
  - 描述：创建 NFS 共享
  - 命令：python scripts/dme_cli.py nas nfs_share create

- [ ] **nas nfs_share delete**
  - 描述：批量删除 NFS 共享
  - 命令：python scripts/dme_cli.py nas nfs_share delete

- [ ] **nas nfs_share list**
  - 描述：查询 NFS 共享列表
  - 命令：python scripts/dme_cli.py nas nfs_share list

- [ ] **nas nfs_share modify**
  - 描述：修改指定 NFS 共享
  - 命令：python scripts/dme_cli.py nas nfs_share modify

- [ ] **nas nfs_share show**
  - 描述：查询指定 NFS 共享详情
  - 命令：python scripts/dme_cli.py nas nfs_share show

### quota

- [ ] **nas quota create**
  - 描述：创建配额
  - 命令：python scripts/dme_cli.py nas quota create

- [ ] **nas quota delete**
  - 描述：批量删除配额
  - 命令：python scripts/dme_cli.py nas quota delete

- [ ] **nas quota list**
  - 描述：查询配额列表
  - 命令：python scripts/dme_cli.py nas quota list

- [ ] **nas quota modify**
  - 描述：更新指定配额
  - 命令：python scripts/dme_cli.py nas quota modify

- [ ] **nas quota show**
  - 描述：查询指定配额详情
  - 命令：python scripts/dme_cli.py nas quota show

## protection 保护 (Protection) 相关操作

### clone_group

- [ ] **protection clone_group create**
  - 描述：创建克隆一致性组
  - 命令：python scripts/dme_cli.py protection clone_group create --clone_pairs <clone_pairs>

- [ ] **protection clone_group delete**
  - 描述：批量删除克隆一致性组
  - 命令：python scripts/dme_cli.py protection clone_group delete

- [ ] **protection clone_group sync**
  - 描述：同步克隆一致性组
  - 命令：python scripts/dme_cli.py protection clone_group sync --clone_pairs <clone_pairs>

### device_pair

- [ ] **protection device_pair list**
  - 描述：查询设备 Pairs
  - 命令：python scripts/dme_cli.py protection device_pair list

### group

- [ ] **protection group add_luns**
  - 描述：保护组中添加成员 LUN
  - 命令：python scripts/dme_cli.py protection group add_luns

- [ ] **protection group create**
  - 描述：创建保护组
  - 命令：python scripts/dme_cli.py protection group create --lun_ids <lun_ids> --lun_group_id <lun_group_id>

- [ ] **protection group delete**
  - 描述：批量删除保护组
  - 命令：python scripts/dme_cli.py protection group delete

- [ ] **protection group list**
  - 描述：批量查询保护组
  - 命令：python scripts/dme_cli.py protection group list

- [ ] **protection group modify**
  - 描述：修改保护组
  - 命令：python scripts/dme_cli.py protection group modify

- [ ] **protection group remove_luns**
  - 描述：移除保护组中的成员 LUN
  - 命令：python scripts/dme_cli.py protection group remove_luns

### hypermetro_domain

- [ ] **protection hypermetro_domain list**
  - 描述：批量查询双活域
  - 命令：python scripts/dme_cli.py protection hypermetro_domain list

### hypermetro_group

- [ ] **protection hypermetro_group add_pairs**
  - 描述：双活一致性组添加成员 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_group add_pairs

- [ ] **protection hypermetro_group create**
  - 描述：创建双活一致性组
  - 命令：python scripts/dme_cli.py protection hypermetro_group create --local_pg_id <local_pg_id> --remote_vstore_id <remote_vstore_id> --remote_storage_pool_id <remote_storage_pool_id>

- [ ] **protection hypermetro_group delete**
  - 描述：批量删除双活一致性组
  - 命令：python scripts/dme_cli.py protection hypermetro_group delete

- [ ] **protection hypermetro_group force_startup**
  - 描述：强制启动双活一致性组
  - 命令：python scripts/dme_cli.py protection hypermetro_group force_startup

- [ ] **protection hypermetro_group list**
  - 描述：批量查询双活一致性组
  - 命令：python scripts/dme_cli.py protection hypermetro_group list

- [ ] **protection hypermetro_group modify**
  - 描述：修改双活一致性组
  - 命令：python scripts/dme_cli.py protection hypermetro_group modify --bandwidth <bandwidth> --isolation_threshold_time <isolation_threshold_time>

- [ ] **protection hypermetro_group pause**
  - 描述：暂停双活一致性组
  - 命令：python scripts/dme_cli.py protection hypermetro_group pause

- [ ] **protection hypermetro_group remove_pairs**
  - 描述：双活一致性组移除成员 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_group remove_pairs

- [ ] **protection hypermetro_group switch_priority**
  - 描述：双活一致性组优先站点切换
  - 命令：python scripts/dme_cli.py protection hypermetro_group switch_priority

### hypermetro_pair

- [ ] **protection hypermetro_pair create**
  - 描述：创建双活 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_pair create

- [ ] **protection hypermetro_pair delete**
  - 描述：批量删除双活 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_pair delete

- [ ] **protection hypermetro_pair force_startup**
  - 描述：强制启动双活 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_pair force_startup

- [ ] **protection hypermetro_pair list**
  - 描述：批量查询 LUN 双活 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_pair list

- [ ] **protection hypermetro_pair modify**
  - 描述：修改双活 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_pair modify --bandwidth <bandwidth> --isolation_threshold_time <isolation_threshold_time>

- [ ] **protection hypermetro_pair pause**
  - 描述：暂停双活 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_pair pause

- [ ] **protection hypermetro_pair switch_priority**
  - 描述：双活 Pair 优先站点切换
  - 命令：python scripts/dme_cli.py protection hypermetro_pair switch_priority

- [ ] **protection hypermetro_pair sync**
  - 描述：同步双活 Pair
  - 命令：python scripts/dme_cli.py protection hypermetro_pair sync

### replication_group

- [ ] **protection replication_group add_pairs**
  - 描述：远程复制一致性组添加成员 Pair
  - 命令：python scripts/dme_cli.py protection replication_group add_pairs

- [ ] **protection replication_group create**
  - 描述：创建远程复制一致性组
  - 命令：python scripts/dme_cli.py protection replication_group create

- [ ] **protection replication_group delete**
  - 描述：批量删除远程复制一致性组
  - 命令：python scripts/dme_cli.py protection replication_group delete

- [ ] **protection replication_group modify**
  - 描述：修改远程复制一致性组
  - 命令：python scripts/dme_cli.py protection replication_group modify --bandwidth <bandwidth> --enable_compress <enable_compress> --timing_value_in_sec <timing_value_in_sec> --sync_schedule <sync_schedule>

- [ ] **protection replication_group remove_pairs**
  - 描述：远程复制一致性组移除成员 Pair
  - 命令：python scripts/dme_cli.py protection replication_group remove_pairs

- [ ] **protection replication_group split**
  - 描述：批量分裂远程复制一致性组
  - 命令：python scripts/dme_cli.py protection replication_group split

- [ ] **protection replication_group switch**
  - 描述：远程复制一致性组批量主从切换
  - 命令：python scripts/dme_cli.py protection replication_group switch

- [ ] **protection replication_group switch_write_protection**
  - 描述：远程复制一致性组从资源写保护状态切换
  - 命令：python scripts/dme_cli.py protection replication_group switch_write_protection

- [ ] **protection replication_group sync**
  - 描述：批量同步远程复制一致性组
  - 命令：python scripts/dme_cli.py protection replication_group sync

### replication_link

- [ ] **protection replication_link list**
  - 描述：查询复制链路
  - 命令：python scripts/dme_cli.py protection replication_link list

### replication_pair

- [ ] **protection replication_pair create**
  - 描述：创建远程复制 Pair
  - 命令：python scripts/dme_cli.py protection replication_pair create --bandwidth <bandwidth> --timing_value_in_sec <timing_value_in_sec> --sync_schedule <sync_schedule> --enable_compress <enable_compress>

- [ ] **protection replication_pair delete**
  - 描述：批量删除远程复制 Pair
  - 命令：python scripts/dme_cli.py protection replication_pair delete

- [ ] **protection replication_pair list**
  - 描述：批量查询复制 Pair
  - 命令：python scripts/dme_cli.py protection replication_pair list

- [ ] **protection replication_pair modify**
  - 描述：修改复制 Pair
  - 命令：python scripts/dme_cli.py protection replication_pair modify --bandwidth <bandwidth> --enable_compress <enable_compress> --timing_value_in_sec <timing_value_in_sec> --sync_schedule <sync_schedule>

- [ ] **protection replication_pair split**
  - 描述：批量分裂远程复制 Pair
  - 命令：python scripts/dme_cli.py protection replication_pair split

- [ ] **protection replication_pair switch**
  - 描述：远程复制 Pair 批量主从切换
  - 命令：python scripts/dme_cli.py protection replication_pair switch

- [ ] **protection replication_pair switch_write_protection**
  - 描述：远程复制 Pair 从资源保护状态切换
  - 命令：python scripts/dme_cli.py protection replication_pair switch_write_protection

- [ ] **protection replication_pair sync**
  - 描述：批量同步远程复制 Pair
  - 命令：python scripts/dme_cli.py protection replication_pair sync

### snapshot

- [ ] **protection snapshot create**
  - 描述：批量创建 LUN 快照
  - 命令：python scripts/dme_cli.py protection snapshot create

- [ ] **protection snapshot delete**
  - 描述：批量删除 LUN 快照
  - 命令：python scripts/dme_cli.py protection snapshot delete

- [ ] **protection snapshot list**
  - 描述：批量查询 LUN 快照
  - 命令：python scripts/dme_cli.py protection snapshot list

- [ ] **protection snapshot rollback**
  - 描述：批量回滚 LUN 快照
  - 命令：python scripts/dme_cli.py protection snapshot rollback

### snapshot_group

- [ ] **protection snapshot_group activate**
  - 描述：激活快照一致性组
  - 命令：python scripts/dme_cli.py protection snapshot_group activate

- [ ] **protection snapshot_group create**
  - 描述：创建快照一致性组
  - 命令：python scripts/dme_cli.py protection snapshot_group create

- [ ] **protection snapshot_group deactivate**
  - 描述：批量取消激活快照一致性组
  - 命令：python scripts/dme_cli.py protection snapshot_group deactivate

- [ ] **protection snapshot_group delete**
  - 描述：批量删除快照一致性组
  - 命令：python scripts/dme_cli.py protection snapshot_group delete

- [ ] **protection snapshot_group rollback**
  - 描述：回滚快照一致性组
  - 命令：python scripts/dme_cli.py protection snapshot_group rollback

## san SAN (Storage Area Network) 相关操作

### lun

- [ ] **san lun connection**
  - 描述：查询指定 LUN ID 的连接信息
  - 命令：python scripts/dme_cli.py san lun connection

- [ ] **san lun create**
  - 描述：自定义创建 LUN
  - 命令：python scripts/dme_cli.py san lun create --name <name> --host_ids <host_ids>

- [ ] **san lun delete**
  - 描述：批量删除 LUN
  - 命令：python scripts/dme_cli.py san lun delete --hostgroup_id <hostgroup_id>

- [ ] **san lun expand**
  - 描述：批量扩容 LUN
  - 命令：python scripts/dme_cli.py san lun expand

- [ ] **san lun list**
  - 描述：批量查询 LUN
  - 命令：python scripts/dme_cli.py san lun list

- [ ] **san lun mapping**
  - 描述：指定存储主机或存储主机组查询映射 LUN 信息列表
  - 命令：python scripts/dme_cli.py san lun mapping

- [ ] **san lun modify**
  - 描述：修改指定 LUN
  - 命令：python scripts/dme_cli.py san lun modify --hostgroup_id <hostgroup_id>

- [ ] **san lun modify_name**
  - 描述：批量修改 LUN 名称
  - 命令：python scripts/dme_cli.py san lun modify_name

- [ ] **san lun show**
  - 描述：查询指定 LUN
  - 命令：python scripts/dme_cli.py san lun show --hostgroup_id <hostgroup_id>

### lun_group

- [ ] **san lun_group add_luns**
  - 描述：向 LUN 组添加 LUN
  - 命令：python scripts/dme_cli.py san lun_group add_luns

- [ ] **san lun_group create**
  - 描述：创建 LUN 组
  - 命令：python scripts/dme_cli.py san lun_group create --name <name>

- [ ] **san lun_group delete**
  - 描述：删除 LUN 组
  - 命令：python scripts/dme_cli.py san lun_group delete

- [ ] **san lun_group list**
  - 描述：批量查询 LUN 组
  - 命令：python scripts/dme_cli.py san lun_group list

- [ ] **san lun_group remove_luns**
  - 描述：从 LUN 组移除 LUN
  - 命令：python scripts/dme_cli.py san lun_group remove_luns

- [ ] **san lun_group show**
  - 描述：查询指定 LUN 组详情
  - 命令：python scripts/dme_cli.py san lun_group show

- [ ] **san lun_group show_luns**
  - 描述：查询 LUN 组中的 LUN
  - 命令：python scripts/dme_cli.py san lun_group show_luns

### mapping_view

- [ ] **san mapping_view create**
  - 描述：创建映射视图
  - 命令：python scripts/dme_cli.py san mapping_view create

- [ ] **san mapping_view delete**
  - 描述：批量删除映射视图
  - 命令：python scripts/dme_cli.py san mapping_view delete

- [ ] **san mapping_view list**
  - 描述：批量查询映射视图列表
  - 命令：python scripts/dme_cli.py san mapping_view list

- [ ] **san mapping_view query**
  - 描述：查询物理主机（组）关联的映射关系
  - 命令：python scripts/dme_cli.py san mapping_view query

### physical_host

- [ ] **san physical_host add_initiators**
  - 描述：为物理主机添加启动器
  - 命令：python scripts/dme_cli.py san physical_host add_initiators --host_id <host_id> --initiators <initiators>

- [ ] **san physical_host create**
  - 描述：接入物理主机
  - 命令：python scripts/dme_cli.py san physical_host create --access_mode <access_mode> --type <type> --host_name <host_name> --ip <ip> --port <port> --host_username <host_username> --host_password <host_password> --initiator <initiator>

- [ ] **san physical_host delete**
  - 描述：移除物理主机
  - 命令：python scripts/dme_cli.py san physical_host delete --host_id <host_id>

- [ ] **san physical_host list**
  - 描述：批量查询物理主机
  - 命令：python scripts/dme_cli.py san physical_host list

- [ ] **san physical_host map_luns**
  - 描述：LUN映射给物理主机
  - 命令：python scripts/dme_cli.py san physical_host map_luns

- [ ] **san physical_host modify**
  - 描述：修改物理主机基本信息
  - 命令：python scripts/dme_cli.py san physical_host modify --host_id <host_id>

- [ ] **san physical_host query_by_initiator**
  - 描述：根据启动器查询关联的物理主机
  - 命令：python scripts/dme_cli.py san physical_host query_by_initiator

- [ ] **san physical_host query_sshkey**
  - 描述：查询指定物理主机SSH公钥
  - 命令：python scripts/dme_cli.py san physical_host query_sshkey --ip <ip>

- [ ] **san physical_host remove_initiators**
  - 描述：从物理主机移除启动器
  - 命令：python scripts/dme_cli.py san physical_host remove_initiators --host_id <host_id> --initiators <initiators>

- [ ] **san physical_host save_sshkey**
  - 描述：保存指定物理主机SSH公钥
  - 命令：python scripts/dme_cli.py san physical_host save_sshkey --ip <ip> --key <key>

- [ ] **san physical_host show**
  - 描述：查询指定物理主机
  - 命令：python scripts/dme_cli.py san physical_host show --host_id <host_id>

- [ ] **san physical_host show_initiators**
  - 描述：查询指定物理主机的启动器
  - 命令：python scripts/dme_cli.py san physical_host show_initiators --host_id <host_id>

- [ ] **san physical_host test**
  - 描述：检测存储设备和物理主机连通性
  - 命令：python scripts/dme_cli.py san physical_host test --storage_id <storage_id>

- [ ] **san physical_host unmap_luns**
  - 描述：解除主机映射
  - 命令：python scripts/dme_cli.py san physical_host unmap_luns

### physical_host_group

- [ ] **san physical_host_group add_hosts**
  - 描述：向物理主机组中增加物理主机
  - 命令：python scripts/dme_cli.py san physical_host_group add_hosts --hostgroup_id <hostgroup_id> --host_ids <host_ids>

- [ ] **san physical_host_group create**
  - 描述：创建物理主机组
  - 命令：python scripts/dme_cli.py san physical_host_group create --name <name> --host_ids <host_ids>

- [ ] **san physical_host_group delete**
  - 描述：删除指定物理主机组
  - 命令：python scripts/dme_cli.py san physical_host_group delete --hostgroup_id <hostgroup_id>

- [ ] **san physical_host_group list**
  - 描述：批量查询物理主机组
  - 命令：python scripts/dme_cli.py san physical_host_group list

- [ ] **san physical_host_group map_luns**
  - 描述：LUN映射给物理主机组
  - 命令：python scripts/dme_cli.py san physical_host_group map_luns

- [ ] **san physical_host_group modify**
  - 描述：修改物理主机组基本信息
  - 命令：python scripts/dme_cli.py san physical_host_group modify --hostgroup_id <hostgroup_id>

- [ ] **san physical_host_group remove_hosts**
  - 描述：物理主机组移除物理主机
  - 命令：python scripts/dme_cli.py san physical_host_group remove_hosts --hostgroup_id <hostgroup_id> --host_ids <host_ids>

- [ ] **san physical_host_group show**
  - 描述：查询指定物理主机组
  - 命令：python scripts/dme_cli.py san physical_host_group show --hostgroup_id <hostgroup_id>

- [ ] **san physical_host_group unmap_luns**
  - 描述：解除物理主机组映射
  - 命令：python scripts/dme_cli.py san physical_host_group unmap_luns

### port_group

- [ ] **san port_group create**
  - 描述：创建端口组
  - 命令：python scripts/dme_cli.py san port_group create --storage_id <storage_id> --name <name>

- [ ] **san port_group list**
  - 描述：批量查询端口组
  - 命令：python scripts/dme_cli.py san port_group list --storage_id <storage_id>

- [ ] **san port_group show_ports**
  - 描述：批量查询指定端口组的端口
  - 命令：python scripts/dme_cli.py san port_group show_ports

- [ ] **san port_group show_relations**
  - 描述：批量查询端口组与端口关联关系
  - 命令：python scripts/dme_cli.py san port_group show_relations

### storage_host

- [ ] **san storage_host batch_query**
  - 描述：根据存储主机 ID 列表批量查询存储主机
  - 命令：python scripts/dme_cli.py san storage_host batch_query --ids <ids>

- [ ] **san storage_host create**
  - 描述：创建存储主机
  - 命令：python scripts/dme_cli.py san storage_host create --storage_id <storage_id> --name <name> --os_type <os_type>

- [ ] **san storage_host delete**
  - 描述：批量删除存储主机
  - 命令：python scripts/dme_cli.py san storage_host delete --host_ids <host_ids>

- [ ] **san storage_host list**
  - 描述：批量查询存储主机
  - 命令：python scripts/dme_cli.py san storage_host list

- [ ] **san storage_host modify**
  - 描述：修改存储主机
  - 命令：python scripts/dme_cli.py san storage_host modify --storage_host_id <storage_host_id>

- [ ] **san storage_host show_luns**
  - 描述：查询存储主机映射的 LUN 信息列表
  - 命令：python scripts/dme_cli.py san storage_host show_luns --storage_host_id <storage_host_id>

- [ ] **san storage_host show_paths**
  - 描述：批量查询存储主机的路径信息
  - 命令：python scripts/dme_cli.py san storage_host show_paths

### storage_host_group

- [ ] **san storage_host_group add_hosts**
  - 描述：添加存储主机到存储主机组
  - 命令：python scripts/dme_cli.py san storage_host_group add_hosts --storage_host_group_id <storage_host_group_id>

- [ ] **san storage_host_group create**
  - 描述：创建存储主机组
  - 命令：python scripts/dme_cli.py san storage_host_group create --storage_id <storage_id> --name <name>

- [ ] **san storage_host_group delete**
  - 描述：批量删除存储主机组
  - 命令：python scripts/dme_cli.py san storage_host_group delete --host_group_ids <host_group_ids>

- [ ] **san storage_host_group list**
  - 描述：批量查询存储主机组
  - 命令：python scripts/dme_cli.py san storage_host_group list

- [ ] **san storage_host_group remove_hosts**
  - 描述：从存储主机组中移除主机
  - 命令：python scripts/dme_cli.py san storage_host_group remove_hosts --storage_host_group_id <storage_host_group_id> --storage_host_ids <storage_host_ids>

- [ ] **san storage_host_group show_luns**
  - 描述：查询存储主机组映射的 LUN 信息列表
  - 命令：python scripts/dme_cli.py san storage_host_group show_luns --storage_host_group_id <storage_host_group_id>

## self_service 租户自助服务 (Self Service) 相关操作

### lun

- [ ] **self_service lun bind_project**
  - 描述：LUN 关联业务群组
  - 命令：python scripts/dme_cli.py self_service lun bind_project

- [ ] **self_service lun bind_tier**
  - 描述：LUN 关联服务等级
  - 命令：python scripts/dme_cli.py self_service lun bind_tier

- [ ] **self_service lun change_tier**
  - 描述：批量更新 LUN 的服务等级
  - 命令：python scripts/dme_cli.py self_service lun change_tier

- [ ] **self_service lun create**
  - 描述：服务化批量创建 LUN
  - 命令：python scripts/dme_cli.py self_service lun create

- [ ] **self_service lun unbind_project**
  - 描述：解除 LUN 与业务群组间关联
  - 命令：python scripts/dme_cli.py self_service lun unbind_project

- [ ] **self_service lun unbind_tier**
  - 描述：解除 LUN 与服务等级关联
  - 命令：python scripts/dme_cli.py self_service lun unbind_tier

### project

- [ ] **self_service project list**
  - 描述：批量查询业务群组
  - 命令：python scripts/dme_cli.py self_service project list

- [ ] **self_service project show_tiers**
  - 描述：批量查询业务群组与服务等级关联关系
  - 命令：python scripts/dme_cli.py self_service project show_tiers

### tier

- [ ] **self_service tier list**
  - 描述：批量查询服务等级
  - 命令：python scripts/dme_cli.py self_service tier list

- [ ] **self_service tier show_projects**
  - 描述：批量查询业务群组与服务等级关联关系
  - 命令：python scripts/dme_cli.py self_service tier show_projects

## server 服务器管理 (Server) 相关操作

### cpu

- [ ] **server cpu list**
  - 描述：查询服务器上的所有 CPU 列表
  - 命令：python scripts/dme_cli.py server cpu list

### disk

- [ ] **server disk list**
  - 描述：查询服务器上的硬盘集合
  - 命令：python scripts/dme_cli.py server disk list

### fan

- [ ] **server fan list**
  - 描述：查询服务器上的风扇
  - 命令：python scripts/dme_cli.py server fan list

### memory

- [ ] **server memory list**
  - 描述：查询服务器上的内存
  - 命令：python scripts/dme_cli.py server memory list

### nic

- [ ] **server nic list**
  - 描述：查询服务器上的网卡集合
  - 命令：python scripts/dme_cli.py server nic list

### pcie_card

- [ ] **server pcie_card list**
  - 描述：查询服务器上的 PCIe 卡信息
  - 命令：python scripts/dme_cli.py server pcie_card list

### power

- [ ] **server power list**
  - 描述：查询服务器上的电源
  - 命令：python scripts/dme_cli.py server power list

### raid_card

- [ ] **server raid_card list**
  - 描述：查询服务器上的 RAID 卡详情
  - 命令：python scripts/dme_cli.py server raid_card list

### 直接动作

- [ ] **server list**
  - 描述：查询服务器列表
  - 命令：python scripts/dme_cli.py server list

- [ ] **server show**
  - 描述：查询指定服务器的概览信息
  - 命令：python scripts/dme_cli.py server show

## storage 存储设备 (Storage) 相关操作

### account

- [ ] **storage account show_dataturbo_admin_users**
  - 描述：批量查询 DataTurbo 管理员
  - 命令：python scripts/dme_cli.py storage account show_dataturbo_admin_users

- [ ] **storage account show_local_user_groups**
  - 描述：查询指定存储设备本地认证用户组的信息
  - 命令：python scripts/dme_cli.py storage account show_local_user_groups

- [ ] **storage account show_local_users**
  - 描述：查询指定存储设备本地认证用户的信息
  - 命令：python scripts/dme_cli.py storage account show_local_users

- [ ] **storage account show_unix_user_groups**
  - 描述：查询指定存储设备 UNIX 认证用户组的信息
  - 命令：python scripts/dme_cli.py storage account show_unix_user_groups

- [ ] **storage account show_unix_users**
  - 描述：查询指定存储设备 UNIX 认证用户的信息
  - 命令：python scripts/dme_cli.py storage account show_unix_users

- [ ] **storage account show_windows_user_groups**
  - 描述：查询指定存储设备 Windows 认证用户组的信息
  - 命令：python scripts/dme_cli.py storage account show_windows_user_groups

- [ ] **storage account show_windows_users**
  - 描述：查询指定存储设备 Windows 认证用户的信息
  - 命令：python scripts/dme_cli.py storage account show_windows_users

### app_type

- [ ] **storage app_type list**
  - 描述：查询指定存储设备的应用类型
  - 命令：python scripts/dme_cli.py storage app_type list --storage_id <storage_id>

### bbu

- [ ] **storage bbu list**
  - 描述：查询存储设备的 BBU 信息列表
  - 命令：python scripts/dme_cli.py storage bbu list

### controller

- [ ] **storage controller list**
  - 描述：查询指定存储设备的控制器信息
  - 命令：python scripts/dme_cli.py storage controller list --storage_id <storage_id>

### disk

- [ ] **storage disk list**
  - 描述：查询存储设备的硬盘信息列表
  - 命令：python scripts/dme_cli.py storage disk list

### disk_pool

- [ ] **storage disk_pool list**
  - 描述：批量查询硬盘域（自动根据存储设备型号选择 API）
  - 命令：python scripts/dme_cli.py storage disk_pool list

### enclosure

- [ ] **storage enclosure list**
  - 描述：批量查询存储设备的机框信息
  - 命令：python scripts/dme_cli.py storage enclosure list

### failover_group

- [ ] **storage failover_group list**
  - 描述：查询漂移组列表
  - 命令：python scripts/dme_cli.py storage failover_group list --storage_id <storage_id>

- [ ] **storage failover_group show_ports**
  - 描述：查询漂移组下的端口（支持 bond、eth、ib 三种类型）
  - 命令：python scripts/dme_cli.py storage failover_group show_ports

- [ ] **storage failover_group show_vlans**
  - 描述：查询漂移组下的 VLAN
  - 命令：python scripts/dme_cli.py storage failover_group show_vlans

### fan

- [ ] **storage fan list**
  - 描述：查询存储设备的风扇信息
  - 命令：python scripts/dme_cli.py storage fan list

### hyperscale_pool

- [ ] **storage hyperscale_pool list**
  - 描述：查询 HyperScale 存储池列表
  - 命令：python scripts/dme_cli.py storage hyperscale_pool list

### initiator

- [ ] **storage initiator delete**
  - 描述：批量删除存储设备的启动器对象
  - 命令：python scripts/dme_cli.py storage initiator delete --initiator_ids <initiator_ids>

- [ ] **storage initiator list**
  - 描述：批量查询存储侧启动器对象
  - 命令：python scripts/dme_cli.py storage initiator list

- [ ] **storage initiator modify**
  - 描述：修改存储侧启动器对象
  - 命令：python scripts/dme_cli.py storage initiator modify --initiator_id <initiator_id>

### logic_port

- [ ] **storage logic_port create**
  - 描述：创建存储设备的逻辑端口（仅 OceanStor A800 系列存储支持）
  - 命令：python scripts/dme_cli.py storage logic_port create

- [ ] **storage logic_port delete**
  - 描述：删除存储设备的逻辑端口（仅 OceanStor A800 系列存储支持）
  - 命令：python scripts/dme_cli.py storage logic_port delete

- [ ] **storage logic_port failback**
  - 描述：回切存储设备的逻辑端口（仅 OceanStor A800 系列存储支持）
  - 命令：python scripts/dme_cli.py storage logic_port failback

- [ ] **storage logic_port list**
  - 描述：查询存储设备的逻辑端口列表
  - 命令：python scripts/dme_cli.py storage logic_port list

- [ ] **storage logic_port show**
  - 描述：查询存储设备的逻辑端口详情
  - 命令：python scripts/dme_cli.py storage logic_port show

- [ ] **storage logic_port update**
  - 描述：修改存储设备的逻辑端口（仅 OceanStor A800 系列存储支持）
  - 命令：python scripts/dme_cli.py storage logic_port update

### node

- [ ] **storage node list**
  - 描述：查询存储设备的节点列表
  - 命令：python scripts/dme_cli.py storage node list

### pool

- [ ] **storage pool list**
  - 描述：查询存储设备存储池列表
  - 命令：python scripts/dme_cli.py storage pool list

### port

- [ ] **storage port list**
  - 描述：查询存储设备端口信息，支持 ETH、FC、IB、Bond 四种类型
  - 命令：python scripts/dme_cli.py storage port list

- [ ] **storage port show_bond_members**
  - 描述：查询指定绑定端口的成员列表信息
  - 命令：python scripts/dme_cli.py storage port show_bond_members

### power

- [ ] **storage power show**
  - 描述：获取存储设备功率
  - 命令：python scripts/dme_cli.py storage power show

### psu

- [ ] **storage psu list**
  - 描述：获取存储设备电源（PSU）列表
  - 命令：python scripts/dme_cli.py storage psu list

### qos

- [ ] **storage qos activate**
  - 描述：批量激活 QoS 策略
  - 命令：python scripts/dme_cli.py storage qos activate --qos_policy_ids <qos_policy_ids>

- [ ] **storage qos associate**
  - 描述：QoS 策略关联控制资源
  - 命令：python scripts/dme_cli.py storage qos associate --qos_policy_id <qos_policy_id> --resource_ids <resource_ids> --resource_type <resource_type>

- [ ] **storage qos create**
  - 描述：创建 QoS 策略
  - 命令：python scripts/dme_cli.py storage qos create --name <name> --storage_id <storage_id> --resource_type <resource_type> --resource_ids <resource_ids> --zone_id <zone_id> --vstore_id <vstore_id>

- [ ] **storage qos deactivate**
  - 描述：批量取消激活 QoS 策略
  - 命令：python scripts/dme_cli.py storage qos deactivate --qos_policy_ids <qos_policy_ids>

- [ ] **storage qos delete**
  - 描述：删除 QoS 策略
  - 命令：python scripts/dme_cli.py storage qos delete --qos_policy_ids <qos_policy_ids>

- [ ] **storage qos list**
  - 描述：批量查询 QoS 策略
  - 命令：python scripts/dme_cli.py storage qos list --storage_id <storage_id>

- [ ] **storage qos modify**
  - 描述：修改 QoS 策略
  - 命令：python scripts/dme_cli.py storage qos modify --qos_policy_id <qos_policy_id>

- [ ] **storage qos show**
  - 描述：查询指定 QoS 策略详情
  - 命令：python scripts/dme_cli.py storage qos show --qos_policy_id <qos_policy_id>

- [ ] **storage qos unassociate**
  - 描述：QoS 策略解关联控制资源
  - 命令：python scripts/dme_cli.py storage qos unassociate --qos_policy_id <qos_policy_id> --resource_ids <resource_ids> --resource_type <resource_type>

### token

- [ ] **storage token show**
  - 描述：获取存储设备访问的令牌
  - 命令：python scripts/dme_cli.py storage token show

### vlan

- [ ] **storage vlan create**
  - 描述：创建 VLAN（仅支持 OceanStor A800、A600 系列存储）
  - 命令：python scripts/dme_cli.py storage vlan create --name <name> --vlan_id <vlan_id> --storage_id <storage_id>

- [ ] **storage vlan delete**
  - 描述：删除 VLAN（仅支持 OceanStor A800、A600 系列存储）
  - 命令：python scripts/dme_cli.py storage vlan delete

- [ ] **storage vlan list**
  - 描述：批量查询 VLAN 列表
  - 命令：python scripts/dme_cli.py storage vlan list

- [ ] **storage vlan modify**
  - 描述：修改 VLAN（仅支持 OceanStor A800、A600 系列存储）
  - 命令：python scripts/dme_cli.py storage vlan modify

### vstore

- [ ] **storage vstore create**
  - 描述：创建租户
  - 命令：python scripts/dme_cli.py storage vstore create --name <name> --storage_id <storage_id>

- [ ] **storage vstore delete**
  - 描述：批量删除租户
  - 命令：python scripts/dme_cli.py storage vstore delete --vstore_ids <vstore_ids>

- [ ] **storage vstore list**
  - 描述：批量查询存储设备租户信息
  - 命令：python scripts/dme_cli.py storage vstore list

- [ ] **storage vstore modify**
  - 描述：修改指定租户
  - 命令：python scripts/dme_cli.py storage vstore modify --vstore_id <vstore_id>

- [ ] **storage vstore show**
  - 描述：查询租户详情
  - 命令：python scripts/dme_cli.py storage vstore show --vstore_id <vstore_id>

### 直接动作

- [ ] **storage add**
  - 描述：添加存储设备（仅支持录入离线存储设备信息）
  - 命令：python scripts/dme_cli.py storage add

- [ ] **storage list**
  - 描述：批量查询存储设备
  - 命令：python scripts/dme_cli.py storage list

- [ ] **storage modify**
  - 描述：修改存储设备（仅支持修改录入的离线存储设备信息）
  - 命令：python scripts/dme_cli.py storage modify

- [ ] **storage remove**
  - 描述：批量移除存储设备
  - 命令：python scripts/dme_cli.py storage remove

- [ ] **storage show**
  - 描述：查询指定存储设备
  - 命令：python scripts/dme_cli.py storage show --storage_id <storage_id>

- [ ] **storage sync**
  - 描述：同步存储设备信息
  - 命令：python scripts/dme_cli.py storage sync

## system 系统管理 (System) 相关操作

### az

- [ ] **system az list**
  - 描述：批量查询可用分区
  - 命令：python scripts/dme_cli.py system az list

### backup_server

- [ ] **system backup_server list**
  - 描述：批量查询备份服务器
  - 命令：python scripts/dme_cli.py system backup_server list

### dc

- [ ] **system dc list**
  - 描述：获取数据中心列表
  - 命令：python scripts/dme_cli.py system dc list

- [ ] **system dc show**
  - 描述：获取数据中心详情
  - 命令：python scripts/dme_cli.py system dc show --dc_id <dc_id>

- [ ] **system dc show_devices**
  - 描述：查询指定数据中心的设备列表信息
  - 命令：python scripts/dme_cli.py system dc show_devices --dc_id <dc_id>

### role

- [ ] **system role list**
  - 描述：批量查询角色信息
  - 命令：python scripts/dme_cli.py system role list

### tag

- [ ] **system tag bind**
  - 描述：标签关联资源
  - 命令：python scripts/dme_cli.py system tag bind --tag_id <tag_id> --resources <resources>

- [ ] **system tag create**
  - 描述：创建标签
  - 命令：python scripts/dme_cli.py system tag create --name <name> --tag_type_id <tag_type_id>

- [ ] **system tag delete**
  - 描述：批量删除标签
  - 命令：python scripts/dme_cli.py system tag delete --tag_ids <tag_ids>

- [ ] **system tag list**
  - 描述：批量查询标签
  - 命令：python scripts/dme_cli.py system tag list

- [ ] **system tag modify**
  - 描述：修改标签
  - 命令：python scripts/dme_cli.py system tag modify --tag_id <tag_id>

- [ ] **system tag unbind**
  - 描述：标签取消关联资源
  - 命令：python scripts/dme_cli.py system tag unbind --tag_id <tag_id> --resources <resources>

### tag_type

- [ ] **system tag_type create**
  - 描述：创建标签类型
  - 命令：python scripts/dme_cli.py system tag_type create --name <name>

- [ ] **system tag_type delete**
  - 描述：批量删除标签类型
  - 命令：python scripts/dme_cli.py system tag_type delete --tag_type_ids <tag_type_ids>

- [ ] **system tag_type list**
  - 描述：批量查询标签类型
  - 命令：python scripts/dme_cli.py system tag_type list

- [ ] **system tag_type modify**
  - 描述：修改标签类型
  - 命令：python scripts/dme_cli.py system tag_type modify --tag_type_id <tag_type_id>

### task

- [ ] **system task list**
  - 描述：批量查询任务
  - 命令：python scripts/dme_cli.py system task list

- [ ] **system task retry**
  - 描述：重试任务
  - 命令：python scripts/dme_cli.py system task retry --task_id <task_id>

- [ ] **system task show**
  - 描述：查询指定任务详情
  - 命令：python scripts/dme_cli.py system task show --task_id <task_id>

- [ ] **system task wait**
  - 描述：等待任务完成
  - 命令：python scripts/dme_cli.py system task wait

### todo_task

- [ ] **system todo_task audit**
  - 描述：审核待办任务
  - 命令：python scripts/dme_cli.py system todo_task audit --item_id <item_id> --is_approval <is_approval>

- [ ] **system todo_task close**
  - 描述：关闭待办任务
  - 命令：python scripts/dme_cli.py system todo_task close --item_id <item_id> --reason <reason>

- [ ] **system todo_task execute**
  - 描述：执行待办任务
  - 命令：python scripts/dme_cli.py system todo_task execute --item_id <item_id>

- [ ] **system todo_task list**
  - 描述：查询待办任务列表
  - 命令：python scripts/dme_cli.py system todo_task list --service_type <service_type>

- [ ] **system todo_task revoke**
  - 描述：撤销审核待办项
  - 命令：python scripts/dme_cli.py system todo_task revoke --item_id <item_id>

- [ ] **system todo_task show**
  - 描述：查询待办任务详情
  - 命令：python scripts/dme_cli.py system todo_task show --item_id <item_id>

### todo_task_group

- [ ] **system todo_task_group confirm**
  - 描述：确认执行定时待办任务组
  - 命令：python scripts/dme_cli.py system todo_task_group confirm --group_id <group_id>

- [ ] **system todo_task_group execute**
  - 描述：执行待办任务组
  - 命令：python scripts/dme_cli.py system todo_task_group execute --group_id <group_id>

- [ ] **system todo_task_group list**
  - 描述：查询待办任务组列表
  - 命令：python scripts/dme_cli.py system todo_task_group list

### user

- [ ] **system user create**
  - 描述：创建用户
  - 命令：python scripts/dme_cli.py system user create

- [ ] **system user delete**
  - 描述：删除用户
  - 命令：python scripts/dme_cli.py system user delete

- [ ] **system user list**
  - 描述：批量查询用户信息
  - 命令：python scripts/dme_cli.py system user list

- [ ] **system user show**
  - 描述：查询指定用户信息
  - 命令：python scripts/dme_cli.py system user show

### 直接动作

- [ ] **system certificate**
  - 描述：获取 DME 证书
  - 命令：python scripts/dme_cli.py system certificate

- [ ] **system login**
  - 描述：认证用户登录
  - 命令：python scripts/dme_cli.py system login

- [ ] **system logout**
  - 描述：注销会话
  - 命令：python scripts/dme_cli.py system logout

- [ ] **system show**
  - 描述：查询产品系统信息
  - 命令：python scripts/dme_cli.py system show

## virtualization 虚拟化服务 (Virtualization) 相关操作

### cluster

- [ ] **virtualization cluster list**
  - 描述：查询集群列表
  - 命令：python scripts/dme_cli.py virtualization cluster list

- [ ] **virtualization cluster show**
  - 描述：查询指定集群详情
  - 命令：python scripts/dme_cli.py virtualization cluster show --cluster_id <cluster_id>

### datastore

- [ ] **virtualization datastore list**
  - 描述：查询数据存储列表
  - 命令：python scripts/dme_cli.py virtualization datastore list

- [ ] **virtualization datastore show**
  - 描述：查询指定数据存储详情
  - 命令：python scripts/dme_cli.py virtualization datastore show --datastore_id <datastore_id>

### disk

- [ ] **virtualization disk list**
  - 描述：查询物理盘信息
  - 命令：python scripts/dme_cli.py virtualization disk list

### host

- [ ] **virtualization host adapter_list**
  - 描述：查询指定主机存储适配器列表
  - 命令：python scripts/dme_cli.py virtualization host adapter_list --host_id <host_id>

- [ ] **virtualization host list**
  - 描述：查询主机列表
  - 命令：python scripts/dme_cli.py virtualization host list

- [ ] **virtualization host show**
  - 描述：查询指定主机详情
  - 命令：python scripts/dme_cli.py virtualization host show --host_id <host_id>

### site

- [ ] **virtualization site list**
  - 描述：查询站点列表
  - 命令：python scripts/dme_cli.py virtualization site list

- [ ] **virtualization site show**
  - 描述：查询指定站点详情
  - 命令：python scripts/dme_cli.py virtualization site show --site_id <site_id>

### vdisk

- [ ] **virtualization vdisk list**
  - 描述：查询虚拟磁盘信息列表
  - 命令：python scripts/dme_cli.py virtualization vdisk list

- [ ] **virtualization vdisk show**
  - 描述：查询指定虚拟磁盘信息
  - 命令：python scripts/dme_cli.py virtualization vdisk show --virtual_disk_id <virtual_disk_id>

### vm

- [ ] **virtualization vm list**
  - 描述：查询虚拟机列表
  - 命令：python scripts/dme_cli.py virtualization vm list

- [ ] **virtualization vm show**
  - 描述：查询指定虚拟机详情
  - 命令：python scripts/dme_cli.py virtualization vm show --vm_id <vm_id>

## workflow 工作流 (Workflow) 相关操作

### instance

- [ ] **workflow instance create**
  - 描述：创建并执行实例
  - 命令：python scripts/dme_cli.py workflow instance create

- [ ] **workflow instance show**
  - 描述：查询实例详情
  - 命令：python scripts/dme_cli.py workflow instance show --instance_id <instance_id>

- [ ] **workflow instance step_log**
  - 描述：查询步骤日志
  - 命令：python scripts/dme_cli.py workflow instance step_log --instance_id <instance_id> --step_id <step_id>

- [ ] **workflow instance stop**
  - 描述：停止实例
  - 命令：python scripts/dme_cli.py workflow instance stop --instance_id <instance_id>

### template

- [ ] **workflow template groups**
  - 描述：查询所有模板分组
  - 命令：python scripts/dme_cli.py workflow template groups

- [ ] **workflow template list**
  - 描述：分页查询模板列表
  - 命令：python scripts/dme_cli.py workflow template list --page_no <page_no> --page_size <page_size>

- [ ] **workflow template show**
  - 描述：查询模板详细信息
  - 命令：python scripts/dme_cli.py workflow template show --template_id <template_id>

### 直接动作

- [ ] **workflow 直接动作**
  - 描述：动作描述
  - 命令：python scripts/dme_cli.py workflow 直接动作

---

## 测试执行统计

- **主题数**：16
- **测试用例数**：376
- **已完成**：0
- **通过率**：0%

## 注意事项

1. 执行前请先配置环境变量
2. 命令中的 `<...>` 需替换为实际值
3. 部分命令需要管理员权限
4. 测试完成后请更新checkbox状态
