# DME CLI 测试执行清单

## 测试环境准备

- [ ] 配置环境变量
  - 配置DME API端点：`export DME_API_ENDPOINT=<your-dme-api-url>`
  - 配置用户名：`export DME_API_USERNAME=<username>`
  - 配置密码：`export DME_API_PASSWORD=<password>`

## aiops AIOps 智能运维相关操作

### alarm

- [ ] **aiops alarm ack**
  - 描述：ack
  - 命令：python scripts/dme_cli.py aiops alarm ack --csns <csns>

- [ ] **aiops alarm clear**
  - 描述：clear
  - 命令：python scripts/dme_cli.py aiops alarm clear --csns <csns>

- [ ] **aiops alarm list**
  - 描述：list
  - 命令：python scripts/dme_cli.py aiops alarm list

- [ ] **aiops alarm unack**
  - 描述：unack
  - 命令：python scripts/dme_cli.py aiops alarm unack --csns <csns>

### check_policy

- [ ] **aiops check_policy delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py aiops check_policy delete

- [ ] **aiops check_policy disable**
  - 描述：disable
  - 命令：python scripts/dme_cli.py aiops check_policy disable

- [ ] **aiops check_policy enable**
  - 描述：enable
  - 命令：python scripts/dme_cli.py aiops check_policy enable

- [ ] **aiops check_policy execute**
  - 描述：execute
  - 命令：python scripts/dme_cli.py aiops check_policy execute

- [ ] **aiops check_policy list**
  - 描述：list
  - 命令：python scripts/dme_cli.py aiops check_policy list

### check_result

- [ ] **aiops check_result list**
  - 描述：list
  - 命令：python scripts/dme_cli.py aiops check_result list

- [ ] **aiops check_result show**
  - 描述：show
  - 命令：python scripts/dme_cli.py aiops check_result show

### diagnose_task

- [ ] **aiops diagnose_task create**
  - 描述：create
  - 命令：python scripts/dme_cli.py aiops diagnose_task create --object_ids <object_ids> --object_type <object_type> --begin_time <begin_time> --end_time <end_time> --analysis_types <analysis_types>

- [ ] **aiops diagnose_task status**
  - 描述：status
  - 命令：python scripts/dme_cli.py aiops diagnose_task status --task_id <task_id>

### health

- [ ] **aiops health query_data**
  - 描述：query_data
  - 命令：python scripts/dme_cli.py aiops health query_data --type <type> --object_id <object_id> --begin_time <begin_time> --end_time <end_time> --object_type <object_type> --indicator <indicator>

- [ ] **aiops health show_detail**
  - 描述：show_detail
  - 命令：python scripts/dme_cli.py aiops health show_detail --object_id <object_id> --object_type <object_type> --health_dimension <health_dimension>

- [ ] **aiops health show_score**
  - 描述：show_score
  - 命令：python scripts/dme_cli.py aiops health show_score --object_type <object_type>

### performance

- [ ] **aiops performance create_collect_task**
  - 描述：create_collect_task
  - 命令：python scripts/dme_cli.py aiops performance create_collect_task

- [ ] **aiops performance download_collect_result**
  - 描述：download_collect_result
  - 命令：python scripts/dme_cli.py aiops performance download_collect_result

- [ ] **aiops performance list_indicators**
  - 描述：list_indicators
  - 命令：python scripts/dme_cli.py aiops performance list_indicators

- [ ] **aiops performance list_object_types**
  - 描述：list_object_types
  - 命令：python scripts/dme_cli.py aiops performance list_object_types

- [ ] **aiops performance query**
  - 描述：query
  - 命令：python scripts/dme_cli.py aiops performance query

- [ ] **aiops performance show_indicators**
  - 描述：show_indicators
  - 命令：python scripts/dme_cli.py aiops performance show_indicators

### topology

- [ ] **aiops topology fcsan_query**
  - 描述：fcsan_query
  - 命令：python scripts/dme_cli.py aiops topology fcsan_query --entry_objects <entry_objects>

- [ ] **aiops topology ipsan_query**
  - 描述：ipsan_query
  - 命令：python scripts/dme_cli.py aiops topology ipsan_query --entry_objects <entry_objects>

- [ ] **aiops topology query_graph_path**
  - 描述：query_graph_path
  - 命令：python scripts/dme_cli.py aiops topology query_graph_path --entry_res_type <entry_res_type> --entry_res_id <entry_res_id>

- [ ] **aiops topology query_luns**
  - 描述：query_luns
  - 命令：python scripts/dme_cli.py aiops topology query_luns --entry_objects <entry_objects> --storage_pool_id <storage_pool_id>

- [ ] **aiops topology query_san_path**
  - 描述：query_san_path
  - 命令：python scripts/dme_cli.py aiops topology query_san_path --entry_objects <entry_objects>

- [ ] **aiops topology query_vms**
  - 描述：query_vms
  - 命令：python scripts/dme_cli.py aiops topology query_vms --entry_objects <entry_objects> --host_id <host_id>

## backup 数据备份管理 (Backup) 相关操作

### cluster

- [ ] **backup cluster capacity**
  - 描述：capacity
  - 命令：python scripts/dme_cli.py backup cluster capacity --cluster_id <cluster_id>

- [ ] **backup cluster list**
  - 描述：list
  - 命令：python scripts/dme_cli.py backup cluster list

- [ ] **backup cluster quota**
  - 描述：quota
  - 命令：python scripts/dme_cli.py backup cluster quota --cluster_id <cluster_id>

## cmdb CMDB (Configuration Management Database) 相关操作

### class

- [ ] **cmdb class list**
  - 描述：list
  - 命令：python scripts/dme_cli.py cmdb class list

- [ ] **cmdb class show**
  - 描述：show
  - 命令：python scripts/dme_cli.py cmdb class show --class_name <class_name>

### instance

- [ ] **cmdb instance list**
  - 描述：list
  - 命令：python scripts/dme_cli.py cmdb instance list --condition <condition>

- [ ] **cmdb instance show**
  - 描述：show
  - 命令：python scripts/dme_cli.py cmdb instance show

### relation

- [ ] **cmdb relation list**
  - 描述：list
  - 命令：python scripts/dme_cli.py cmdb relation list --condition <condition>

- [ ] **cmdb relation show**
  - 描述：show
  - 命令：python scripts/dme_cli.py cmdb relation show

## fc_switch FC Switch (光纤交换机) 相关操作

- [ ] **fc_switch list**
  - 描述：list
  - 命令：python scripts/dme_cli.py fc_switch list

- [ ] **fc_switch sync**
  - 描述：sync
  - 命令：python scripts/dme_cli.py fc_switch sync --switch_id <switch_id>

### alias

- [ ] **fc_switch alias create**
  - 描述：create
  - 命令：python scripts/dme_cli.py fc_switch alias create --name <name> --fabric_wwn <fabric_wwn> --vsan_wwn <vsan_wwn>

- [ ] **fc_switch alias delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py fc_switch alias delete --alias_id <alias_id>

- [ ] **fc_switch alias list**
  - 描述：list
  - 命令：python scripts/dme_cli.py fc_switch alias list --fabric_wwn <fabric_wwn>

- [ ] **fc_switch alias modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py fc_switch alias modify --alias_id <alias_id>

- [ ] **fc_switch alias show_members**
  - 描述：show_members
  - 命令：python scripts/dme_cli.py fc_switch alias show_members --alias_id <alias_id>

### controller

- [ ] **fc_switch controller list**
  - 描述：list
  - 命令：python scripts/dme_cli.py fc_switch controller list

### fabric

- [ ] **fc_switch fabric backup**
  - 描述：backup
  - 命令：python scripts/dme_cli.py fc_switch fabric backup --fabric_id <fabric_id> --backup_server_id <backup_server_id>

- [ ] **fc_switch fabric list**
  - 描述：list
  - 命令：python scripts/dme_cli.py fc_switch fabric list

- [ ] **fc_switch fabric show_ports**
  - 描述：show_ports
  - 命令：python scripts/dme_cli.py fc_switch fabric show_ports --fabric_id <fabric_id>

### port

- [ ] **fc_switch port list**
  - 描述：list
  - 命令：python scripts/dme_cli.py fc_switch port list

### vsan

- [ ] **fc_switch vsan list**
  - 描述：list
  - 命令：python scripts/dme_cli.py fc_switch vsan list

### zone

- [ ] **fc_switch zone batch_create**
  - 描述：batch_create
  - 命令：python scripts/dme_cli.py fc_switch zone batch_create --is_active_zone <is_active_zone> --zones <zones>

- [ ] **fc_switch zone create**
  - 描述：create
  - 命令：python scripts/dme_cli.py fc_switch zone create --name <name> --fabric_wwn <fabric_wwn> --vsan_wwn <vsan_wwn>

- [ ] **fc_switch zone delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py fc_switch zone delete --zone_id <zone_id>

- [ ] **fc_switch zone list**
  - 描述：list
  - 命令：python scripts/dme_cli.py fc_switch zone list

- [ ] **fc_switch zone modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py fc_switch zone modify --zone_id <zone_id>

- [ ] **fc_switch zone show_members**
  - 描述：show_members
  - 命令：python scripts/dme_cli.py fc_switch zone show_members --zone_id <zone_id>

## gfs GFS (Global File System) 相关操作

### dataspace

- [ ] **gfs dataspace list**
  - 描述：list
  - 命令：python scripts/dme_cli.py gfs dataspace list

- [ ] **gfs dataspace show**
  - 描述：show
  - 命令：python scripts/dme_cli.py gfs dataspace show

- [ ] **gfs dataspace site_list**
  - 描述：site_list
  - 命令：python scripts/dme_cli.py gfs dataspace site_list

### migration_task

- [ ] **gfs migration_task create**
  - 描述：create
  - 命令：python scripts/dme_cli.py gfs migration_task create

- [ ] **gfs migration_task delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py gfs migration_task delete

- [ ] **gfs migration_task list**
  - 描述：list
  - 命令：python scripts/dme_cli.py gfs migration_task list

- [ ] **gfs migration_task modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py gfs migration_task modify

- [ ] **gfs migration_task operate**
  - 描述：operate
  - 命令：python scripts/dme_cli.py gfs migration_task operate

- [ ] **gfs migration_task show**
  - 描述：show
  - 命令：python scripts/dme_cli.py gfs migration_task show

### namespace

- [ ] **gfs namespace create**
  - 描述：create
  - 命令：python scripts/dme_cli.py gfs namespace create --smart_share_members <smart_share_members>

- [ ] **gfs namespace delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py gfs namespace delete

- [ ] **gfs namespace list**
  - 描述：list
  - 命令：python scripts/dme_cli.py gfs namespace list

- [ ] **gfs namespace modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py gfs namespace modify

- [ ] **gfs namespace show**
  - 描述：show
  - 命令：python scripts/dme_cli.py gfs namespace show

## ip_switch IP 交换机 (IPSwitch) 管理相关操作

- [ ] **ip_switch list**
  - 描述：list
  - 命令：python scripts/dme_cli.py ip_switch list

### board

- [ ] **ip_switch board list**
  - 描述：list
  - 命令：python scripts/dme_cli.py ip_switch board list --ipswitch_id <ipswitch_id>

### fan

- [ ] **ip_switch fan list**
  - 描述：list
  - 命令：python scripts/dme_cli.py ip_switch fan list --ipswitch_id <ipswitch_id>

### frame

- [ ] **ip_switch frame list**
  - 描述：list
  - 命令：python scripts/dme_cli.py ip_switch frame list --ipswitch_id <ipswitch_id>

### port

- [ ] **ip_switch port list**
  - 描述：list
  - 命令：python scripts/dme_cli.py ip_switch port list --ipswitch_id <ipswitch_id>

### power

- [ ] **ip_switch power list**
  - 描述：list
  - 命令：python scripts/dme_cli.py ip_switch power list --ipswitch_id <ipswitch_id>

### subcard

- [ ] **ip_switch subcard list**
  - 描述：list
  - 命令：python scripts/dme_cli.py ip_switch subcard list --ipswitch_id <ipswitch_id>

## kubernetes Kubernetes 相关操作

### cluster

- [ ] **kubernetes cluster list**
  - 描述：list
  - 命令：python scripts/dme_cli.py kubernetes cluster list

### namespace

- [ ] **kubernetes namespace list**
  - 描述：list
  - 命令：python scripts/dme_cli.py kubernetes namespace list

### node

- [ ] **kubernetes node list**
  - 描述：list
  - 命令：python scripts/dme_cli.py kubernetes node list

### pod

- [ ] **kubernetes pod list**
  - 描述：list
  - 命令：python scripts/dme_cli.py kubernetes pod list

### pv

- [ ] **kubernetes pv list**
  - 描述：list
  - 命令：python scripts/dme_cli.py kubernetes pv list

### pvc

- [ ] **kubernetes pvc list**
  - 描述：list
  - 命令：python scripts/dme_cli.py kubernetes pvc list

## nas NAS 相关操作

### cifs_share

- [ ] **nas cifs_share create**
  - 描述：create
  - 命令：python scripts/dme_cli.py nas cifs_share create

- [ ] **nas cifs_share delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py nas cifs_share delete

- [ ] **nas cifs_share list**
  - 描述：list
  - 命令：python scripts/dme_cli.py nas cifs_share list

- [ ] **nas cifs_share modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py nas cifs_share modify

- [ ] **nas cifs_share show**
  - 描述：show
  - 命令：python scripts/dme_cli.py nas cifs_share show

- [ ] **nas cifs_share show_permissions**
  - 描述：show_permissions
  - 命令：python scripts/dme_cli.py nas cifs_share show_permissions

### dataturbo_share

- [ ] **nas dataturbo_share create**
  - 描述：create
  - 命令：python scripts/dme_cli.py nas dataturbo_share create

- [ ] **nas dataturbo_share delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py nas dataturbo_share delete

- [ ] **nas dataturbo_share list**
  - 描述：list
  - 命令：python scripts/dme_cli.py nas dataturbo_share list

- [ ] **nas dataturbo_share modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py nas dataturbo_share modify

- [ ] **nas dataturbo_share show**
  - 描述：show
  - 命令：python scripts/dme_cli.py nas dataturbo_share show

- [ ] **nas dataturbo_share show_permissions**
  - 描述：show_permissions
  - 命令：python scripts/dme_cli.py nas dataturbo_share show_permissions

### dpc

- [ ] **nas dpc list**
  - 描述：list
  - 命令：python scripts/dme_cli.py nas dpc list

- [ ] **nas dpc show**
  - 描述：show
  - 命令：python scripts/dme_cli.py nas dpc show

### dtree

- [ ] **nas dtree create**
  - 描述：create
  - 命令：python scripts/dme_cli.py nas dtree create

- [ ] **nas dtree delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py nas dtree delete

- [ ] **nas dtree list**
  - 描述：list
  - 命令：python scripts/dme_cli.py nas dtree list

- [ ] **nas dtree modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py nas dtree modify

- [ ] **nas dtree show**
  - 描述：show
  - 命令：python scripts/dme_cli.py nas dtree show

### filesystem

- [ ] **nas filesystem batch_modify**
  - 描述：batch_modify
  - 命令：python scripts/dme_cli.py nas filesystem batch_modify

- [ ] **nas filesystem create**
  - 描述：create
  - 命令：python scripts/dme_cli.py nas filesystem create

- [ ] **nas filesystem delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py nas filesystem delete

- [ ] **nas filesystem list**
  - 描述：list
  - 命令：python scripts/dme_cli.py nas filesystem list

- [ ] **nas filesystem modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py nas filesystem modify

- [ ] **nas filesystem query_available**
  - 描述：query_available
  - 命令：python scripts/dme_cli.py nas filesystem query_available --remote_storage_id <remote_storage_id>

- [ ] **nas filesystem show**
  - 描述：show
  - 命令：python scripts/dme_cli.py nas filesystem show

### namespace

- [ ] **nas namespace create**
  - 描述：create
  - 命令：python scripts/dme_cli.py nas namespace create

- [ ] **nas namespace delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py nas namespace delete --namespace_ids <namespace_ids>

- [ ] **nas namespace list**
  - 描述：list
  - 命令：python scripts/dme_cli.py nas namespace list

- [ ] **nas namespace modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py nas namespace modify --namespace_id <namespace_id>

- [ ] **nas namespace show**
  - 描述：show
  - 命令：python scripts/dme_cli.py nas namespace show --namespace_id <namespace_id>

### nfs_share

- [ ] **nas nfs_share create**
  - 描述：create
  - 命令：python scripts/dme_cli.py nas nfs_share create

- [ ] **nas nfs_share delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py nas nfs_share delete

- [ ] **nas nfs_share list**
  - 描述：list
  - 命令：python scripts/dme_cli.py nas nfs_share list

- [ ] **nas nfs_share modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py nas nfs_share modify

- [ ] **nas nfs_share show**
  - 描述：show
  - 命令：python scripts/dme_cli.py nas nfs_share show

### quota

- [ ] **nas quota create**
  - 描述：create
  - 命令：python scripts/dme_cli.py nas quota create

- [ ] **nas quota delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py nas quota delete

- [ ] **nas quota list**
  - 描述：list
  - 命令：python scripts/dme_cli.py nas quota list

- [ ] **nas quota modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py nas quota modify

- [ ] **nas quota show**
  - 描述：show
  - 命令：python scripts/dme_cli.py nas quota show

## protection 保护 (Protection) 相关操作

### clone_group

- [ ] **protection clone_group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py protection clone_group create --clone_pairs <clone_pairs>

- [ ] **protection clone_group delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py protection clone_group delete

- [ ] **protection clone_group sync**
  - 描述：sync
  - 命令：python scripts/dme_cli.py protection clone_group sync --clone_pairs <clone_pairs>

### device_pair

- [ ] **protection device_pair list**
  - 描述：list
  - 命令：python scripts/dme_cli.py protection device_pair list

### group

- [ ] **protection group add_luns**
  - 描述：add_luns
  - 命令：python scripts/dme_cli.py protection group add_luns

- [ ] **protection group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py protection group create --lun_ids <lun_ids> --lun_group_id <lun_group_id>

- [ ] **protection group delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py protection group delete

- [ ] **protection group list**
  - 描述：list
  - 命令：python scripts/dme_cli.py protection group list

- [ ] **protection group modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py protection group modify

- [ ] **protection group remove_luns**
  - 描述：remove_luns
  - 命令：python scripts/dme_cli.py protection group remove_luns

### hypermetro_domain

- [ ] **protection hypermetro_domain list**
  - 描述：list
  - 命令：python scripts/dme_cli.py protection hypermetro_domain list

### hypermetro_group

- [ ] **protection hypermetro_group add_pairs**
  - 描述：add_pairs
  - 命令：python scripts/dme_cli.py protection hypermetro_group add_pairs

- [ ] **protection hypermetro_group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py protection hypermetro_group create --local_pg_id <local_pg_id> --remote_vstore_id <remote_vstore_id> --remote_storage_pool_id <remote_storage_pool_id>

- [ ] **protection hypermetro_group delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py protection hypermetro_group delete

- [ ] **protection hypermetro_group force_startup**
  - 描述：force_startup
  - 命令：python scripts/dme_cli.py protection hypermetro_group force_startup

- [ ] **protection hypermetro_group list**
  - 描述：list
  - 命令：python scripts/dme_cli.py protection hypermetro_group list

- [ ] **protection hypermetro_group modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py protection hypermetro_group modify --bandwidth <bandwidth> --isolation_threshold_time <isolation_threshold_time>

- [ ] **protection hypermetro_group pause**
  - 描述：pause
  - 命令：python scripts/dme_cli.py protection hypermetro_group pause

- [ ] **protection hypermetro_group remove_pairs**
  - 描述：remove_pairs
  - 命令：python scripts/dme_cli.py protection hypermetro_group remove_pairs

- [ ] **protection hypermetro_group switch_priority**
  - 描述：switch_priority
  - 命令：python scripts/dme_cli.py protection hypermetro_group switch_priority

### hypermetro_pair

- [ ] **protection hypermetro_pair create**
  - 描述：create
  - 命令：python scripts/dme_cli.py protection hypermetro_pair create

- [ ] **protection hypermetro_pair delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py protection hypermetro_pair delete

- [ ] **protection hypermetro_pair force_startup**
  - 描述：force_startup
  - 命令：python scripts/dme_cli.py protection hypermetro_pair force_startup

- [ ] **protection hypermetro_pair list**
  - 描述：list
  - 命令：python scripts/dme_cli.py protection hypermetro_pair list

- [ ] **protection hypermetro_pair modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py protection hypermetro_pair modify --bandwidth <bandwidth> --isolation_threshold_time <isolation_threshold_time>

- [ ] **protection hypermetro_pair pause**
  - 描述：pause
  - 命令：python scripts/dme_cli.py protection hypermetro_pair pause

- [ ] **protection hypermetro_pair switch_priority**
  - 描述：switch_priority
  - 命令：python scripts/dme_cli.py protection hypermetro_pair switch_priority

- [ ] **protection hypermetro_pair sync**
  - 描述：sync
  - 命令：python scripts/dme_cli.py protection hypermetro_pair sync

### replication_group

- [ ] **protection replication_group add_pairs**
  - 描述：add_pairs
  - 命令：python scripts/dme_cli.py protection replication_group add_pairs

- [ ] **protection replication_group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py protection replication_group create

- [ ] **protection replication_group delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py protection replication_group delete

- [ ] **protection replication_group modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py protection replication_group modify --bandwidth <bandwidth> --enable_compress <enable_compress> --timing_value_in_sec <timing_value_in_sec> --sync_schedule <sync_schedule>

- [ ] **protection replication_group remove_pairs**
  - 描述：remove_pairs
  - 命令：python scripts/dme_cli.py protection replication_group remove_pairs

- [ ] **protection replication_group split**
  - 描述：split
  - 命令：python scripts/dme_cli.py protection replication_group split

- [ ] **protection replication_group switch**
  - 描述：switch
  - 命令：python scripts/dme_cli.py protection replication_group switch

- [ ] **protection replication_group switch_write_protection**
  - 描述：switch_write_protection
  - 命令：python scripts/dme_cli.py protection replication_group switch_write_protection

- [ ] **protection replication_group sync**
  - 描述：sync
  - 命令：python scripts/dme_cli.py protection replication_group sync

### replication_link

- [ ] **protection replication_link list**
  - 描述：list
  - 命令：python scripts/dme_cli.py protection replication_link list

### replication_pair

- [ ] **protection replication_pair create**
  - 描述：create
  - 命令：python scripts/dme_cli.py protection replication_pair create --bandwidth <bandwidth> --timing_value_in_sec <timing_value_in_sec> --sync_schedule <sync_schedule> --enable_compress <enable_compress>

- [ ] **protection replication_pair delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py protection replication_pair delete

- [ ] **protection replication_pair list**
  - 描述：list
  - 命令：python scripts/dme_cli.py protection replication_pair list

- [ ] **protection replication_pair modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py protection replication_pair modify --bandwidth <bandwidth> --enable_compress <enable_compress> --timing_value_in_sec <timing_value_in_sec> --sync_schedule <sync_schedule>

- [ ] **protection replication_pair split**
  - 描述：split
  - 命令：python scripts/dme_cli.py protection replication_pair split

- [ ] **protection replication_pair switch**
  - 描述：switch
  - 命令：python scripts/dme_cli.py protection replication_pair switch

- [ ] **protection replication_pair switch_write_protection**
  - 描述：switch_write_protection
  - 命令：python scripts/dme_cli.py protection replication_pair switch_write_protection

- [ ] **protection replication_pair sync**
  - 描述：sync
  - 命令：python scripts/dme_cli.py protection replication_pair sync

### snapshot

- [ ] **protection snapshot create**
  - 描述：create
  - 命令：python scripts/dme_cli.py protection snapshot create

- [ ] **protection snapshot delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py protection snapshot delete

- [ ] **protection snapshot list**
  - 描述：list
  - 命令：python scripts/dme_cli.py protection snapshot list

- [ ] **protection snapshot rollback**
  - 描述：rollback
  - 命令：python scripts/dme_cli.py protection snapshot rollback

### snapshot_group

- [ ] **protection snapshot_group activate**
  - 描述：activate
  - 命令：python scripts/dme_cli.py protection snapshot_group activate

- [ ] **protection snapshot_group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py protection snapshot_group create

- [ ] **protection snapshot_group deactivate**
  - 描述：deactivate
  - 命令：python scripts/dme_cli.py protection snapshot_group deactivate

- [ ] **protection snapshot_group delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py protection snapshot_group delete

- [ ] **protection snapshot_group rollback**
  - 描述：rollback
  - 命令：python scripts/dme_cli.py protection snapshot_group rollback

## san SAN (Storage Area Network) 相关操作

### lun

- [ ] **san lun connection**
  - 描述：connection
  - 命令：python scripts/dme_cli.py san lun connection

- [ ] **san lun create**
  - 描述：create
  - 命令：python scripts/dme_cli.py san lun create --name <name> --host_ids <host_ids>

- [ ] **san lun delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py san lun delete --hostgroup_id <hostgroup_id>

- [ ] **san lun expand**
  - 描述：expand
  - 命令：python scripts/dme_cli.py san lun expand

- [ ] **san lun list**
  - 描述：list
  - 命令：python scripts/dme_cli.py san lun list

- [ ] **san lun mapping**
  - 描述：mapping
  - 命令：python scripts/dme_cli.py san lun mapping

- [ ] **san lun modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py san lun modify --hostgroup_id <hostgroup_id>

- [ ] **san lun modify_name**
  - 描述：modify_name
  - 命令：python scripts/dme_cli.py san lun modify_name

- [ ] **san lun show**
  - 描述：show
  - 命令：python scripts/dme_cli.py san lun show --hostgroup_id <hostgroup_id>

### lun_group

- [ ] **san lun_group add_luns**
  - 描述：add_luns
  - 命令：python scripts/dme_cli.py san lun_group add_luns

- [ ] **san lun_group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py san lun_group create --name <name>

- [ ] **san lun_group delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py san lun_group delete

- [ ] **san lun_group list**
  - 描述：list
  - 命令：python scripts/dme_cli.py san lun_group list

- [ ] **san lun_group remove_luns**
  - 描述：remove_luns
  - 命令：python scripts/dme_cli.py san lun_group remove_luns

- [ ] **san lun_group show**
  - 描述：show
  - 命令：python scripts/dme_cli.py san lun_group show

- [ ] **san lun_group show_luns**
  - 描述：show_luns
  - 命令：python scripts/dme_cli.py san lun_group show_luns

### mapping_view

- [ ] **san mapping_view create**
  - 描述：create
  - 命令：python scripts/dme_cli.py san mapping_view create

- [ ] **san mapping_view delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py san mapping_view delete

- [ ] **san mapping_view list**
  - 描述：list
  - 命令：python scripts/dme_cli.py san mapping_view list

- [ ] **san mapping_view query**
  - 描述：query
  - 命令：python scripts/dme_cli.py san mapping_view query

### physical_host

- [ ] **san physical_host add_initiators**
  - 描述：add_initiators
  - 命令：python scripts/dme_cli.py san physical_host add_initiators --host_id <host_id> --initiators <initiators>

- [ ] **san physical_host create**
  - 描述：create
  - 命令：python scripts/dme_cli.py san physical_host create --access_mode <access_mode> --type <type> --host_name <host_name> --ip <ip> --port <port> --host_username <host_username> --host_password <host_password> --initiator <initiator>

- [ ] **san physical_host delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py san physical_host delete --host_id <host_id>

- [ ] **san physical_host list**
  - 描述：list
  - 命令：python scripts/dme_cli.py san physical_host list

- [ ] **san physical_host map_luns**
  - 描述：map_luns
  - 命令：python scripts/dme_cli.py san physical_host map_luns

- [ ] **san physical_host modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py san physical_host modify --host_id <host_id>

- [ ] **san physical_host query_by_initiator**
  - 描述：query_by_initiator
  - 命令：python scripts/dme_cli.py san physical_host query_by_initiator

- [ ] **san physical_host query_sshkey**
  - 描述：query_sshkey
  - 命令：python scripts/dme_cli.py san physical_host query_sshkey --ip <ip>

- [ ] **san physical_host remove_initiators**
  - 描述：remove_initiators
  - 命令：python scripts/dme_cli.py san physical_host remove_initiators --host_id <host_id> --initiators <initiators>

- [ ] **san physical_host save_sshkey**
  - 描述：save_sshkey
  - 命令：python scripts/dme_cli.py san physical_host save_sshkey --ip <ip> --key <key>

- [ ] **san physical_host show**
  - 描述：show
  - 命令：python scripts/dme_cli.py san physical_host show --host_id <host_id>

- [ ] **san physical_host show_initiators**
  - 描述：show_initiators
  - 命令：python scripts/dme_cli.py san physical_host show_initiators --host_id <host_id>

- [ ] **san physical_host test**
  - 描述：test
  - 命令：python scripts/dme_cli.py san physical_host test --storage_id <storage_id>

- [ ] **san physical_host unmap_luns**
  - 描述：unmap_luns
  - 命令：python scripts/dme_cli.py san physical_host unmap_luns

### physical_host_group

- [ ] **san physical_host_group add_hosts**
  - 描述：add_hosts
  - 命令：python scripts/dme_cli.py san physical_host_group add_hosts --hostgroup_id <hostgroup_id> --host_ids <host_ids>

- [ ] **san physical_host_group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py san physical_host_group create --name <name> --host_ids <host_ids>

- [ ] **san physical_host_group delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py san physical_host_group delete --hostgroup_id <hostgroup_id>

- [ ] **san physical_host_group list**
  - 描述：list
  - 命令：python scripts/dme_cli.py san physical_host_group list

- [ ] **san physical_host_group map_luns**
  - 描述：map_luns
  - 命令：python scripts/dme_cli.py san physical_host_group map_luns

- [ ] **san physical_host_group modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py san physical_host_group modify --hostgroup_id <hostgroup_id>

- [ ] **san physical_host_group remove_hosts**
  - 描述：remove_hosts
  - 命令：python scripts/dme_cli.py san physical_host_group remove_hosts --hostgroup_id <hostgroup_id> --host_ids <host_ids>

- [ ] **san physical_host_group show**
  - 描述：show
  - 命令：python scripts/dme_cli.py san physical_host_group show --hostgroup_id <hostgroup_id>

- [ ] **san physical_host_group unmap_luns**
  - 描述：unmap_luns
  - 命令：python scripts/dme_cli.py san physical_host_group unmap_luns

### port_group

- [ ] **san port_group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py san port_group create --storage_id <storage_id> --name <name>

- [ ] **san port_group list**
  - 描述：list
  - 命令：python scripts/dme_cli.py san port_group list --storage_id <storage_id>

- [ ] **san port_group show_ports**
  - 描述：show_ports
  - 命令：python scripts/dme_cli.py san port_group show_ports

- [ ] **san port_group show_relations**
  - 描述：show_relations
  - 命令：python scripts/dme_cli.py san port_group show_relations

### storage_host

- [ ] **san storage_host batch_query**
  - 描述：batch_query
  - 命令：python scripts/dme_cli.py san storage_host batch_query --ids <ids>

- [ ] **san storage_host create**
  - 描述：create
  - 命令：python scripts/dme_cli.py san storage_host create --storage_id <storage_id> --name <name> --os_type <os_type>

- [ ] **san storage_host delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py san storage_host delete --host_ids <host_ids>

- [ ] **san storage_host list**
  - 描述：list
  - 命令：python scripts/dme_cli.py san storage_host list

- [ ] **san storage_host modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py san storage_host modify --storage_host_id <storage_host_id>

- [ ] **san storage_host show_luns**
  - 描述：show_luns
  - 命令：python scripts/dme_cli.py san storage_host show_luns --storage_host_id <storage_host_id>

- [ ] **san storage_host show_paths**
  - 描述：show_paths
  - 命令：python scripts/dme_cli.py san storage_host show_paths

### storage_host_group

- [ ] **san storage_host_group add_hosts**
  - 描述：add_hosts
  - 命令：python scripts/dme_cli.py san storage_host_group add_hosts --storage_host_group_id <storage_host_group_id>

- [ ] **san storage_host_group create**
  - 描述：create
  - 命令：python scripts/dme_cli.py san storage_host_group create --storage_id <storage_id> --name <name>

- [ ] **san storage_host_group delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py san storage_host_group delete --host_group_ids <host_group_ids>

- [ ] **san storage_host_group list**
  - 描述：list
  - 命令：python scripts/dme_cli.py san storage_host_group list

- [ ] **san storage_host_group remove_hosts**
  - 描述：remove_hosts
  - 命令：python scripts/dme_cli.py san storage_host_group remove_hosts --storage_host_group_id <storage_host_group_id> --storage_host_ids <storage_host_ids>

- [ ] **san storage_host_group show_luns**
  - 描述：show_luns
  - 命令：python scripts/dme_cli.py san storage_host_group show_luns --storage_host_group_id <storage_host_group_id>

## self_service 租户自助服务 (Self Service) 相关操作

### lun

- [ ] **self_service lun bind_project**
  - 描述：bind_project
  - 命令：python scripts/dme_cli.py self_service lun bind_project

- [ ] **self_service lun bind_tier**
  - 描述：bind_tier
  - 命令：python scripts/dme_cli.py self_service lun bind_tier

- [ ] **self_service lun change_tier**
  - 描述：change_tier
  - 命令：python scripts/dme_cli.py self_service lun change_tier

- [ ] **self_service lun create**
  - 描述：create
  - 命令：python scripts/dme_cli.py self_service lun create

- [ ] **self_service lun unbind_project**
  - 描述：unbind_project
  - 命令：python scripts/dme_cli.py self_service lun unbind_project

- [ ] **self_service lun unbind_tier**
  - 描述：unbind_tier
  - 命令：python scripts/dme_cli.py self_service lun unbind_tier

### project

- [ ] **self_service project list**
  - 描述：list
  - 命令：python scripts/dme_cli.py self_service project list

- [ ] **self_service project show_tiers**
  - 描述：show_tiers
  - 命令：python scripts/dme_cli.py self_service project show_tiers

### tier

- [ ] **self_service tier list**
  - 描述：list
  - 命令：python scripts/dme_cli.py self_service tier list

- [ ] **self_service tier show_projects**
  - 描述：show_projects
  - 命令：python scripts/dme_cli.py self_service tier show_projects

## server 服务器管理 (Server) 相关操作

- [ ] **server list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server list

- [ ] **server show**
  - 描述：show
  - 命令：python scripts/dme_cli.py server show

### cpu

- [ ] **server cpu list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server cpu list

### disk

- [ ] **server disk list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server disk list

### fan

- [ ] **server fan list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server fan list

### memory

- [ ] **server memory list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server memory list

### nic

- [ ] **server nic list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server nic list

### pcie_card

- [ ] **server pcie_card list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server pcie_card list

### power

- [ ] **server power list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server power list

### raid_card

- [ ] **server raid_card list**
  - 描述：list
  - 命令：python scripts/dme_cli.py server raid_card list

## storage 存储设备 (Storage) 相关操作

- [ ] **storage add**
  - 描述：add
  - 命令：python scripts/dme_cli.py storage add

- [ ] **storage list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage list

- [ ] **storage modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py storage modify

- [ ] **storage remove**
  - 描述：remove
  - 命令：python scripts/dme_cli.py storage remove

- [ ] **storage show**
  - 描述：show
  - 命令：python scripts/dme_cli.py storage show --storage_id <storage_id>

- [ ] **storage sync**
  - 描述：sync
  - 命令：python scripts/dme_cli.py storage sync

### account

- [ ] **storage account show_dataturbo_admin_users**
  - 描述：show_dataturbo_admin_users
  - 命令：python scripts/dme_cli.py storage account show_dataturbo_admin_users

- [ ] **storage account show_local_user_groups**
  - 描述：show_local_user_groups
  - 命令：python scripts/dme_cli.py storage account show_local_user_groups

- [ ] **storage account show_local_users**
  - 描述：show_local_users
  - 命令：python scripts/dme_cli.py storage account show_local_users

- [ ] **storage account show_unix_user_groups**
  - 描述：show_unix_user_groups
  - 命令：python scripts/dme_cli.py storage account show_unix_user_groups

- [ ] **storage account show_unix_users**
  - 描述：show_unix_users
  - 命令：python scripts/dme_cli.py storage account show_unix_users

- [ ] **storage account show_windows_user_groups**
  - 描述：show_windows_user_groups
  - 命令：python scripts/dme_cli.py storage account show_windows_user_groups

- [ ] **storage account show_windows_users**
  - 描述：show_windows_users
  - 命令：python scripts/dme_cli.py storage account show_windows_users

### app_type

- [ ] **storage app_type list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage app_type list --storage_id <storage_id>

### bbu

- [ ] **storage bbu list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage bbu list

### controller

- [ ] **storage controller list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage controller list --storage_id <storage_id>

### disk

- [ ] **storage disk list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage disk list

### disk_pool

- [ ] **storage disk_pool list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage disk_pool list

### enclosure

- [ ] **storage enclosure list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage enclosure list

### failover_group

- [ ] **storage failover_group list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage failover_group list --storage_id <storage_id>

- [ ] **storage failover_group show_ports**
  - 描述：show_ports
  - 命令：python scripts/dme_cli.py storage failover_group show_ports

- [ ] **storage failover_group show_vlans**
  - 描述：show_vlans
  - 命令：python scripts/dme_cli.py storage failover_group show_vlans

### fan

- [ ] **storage fan list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage fan list

### hyperscale_pool

- [ ] **storage hyperscale_pool list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage hyperscale_pool list

### initiator

- [ ] **storage initiator delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py storage initiator delete --initiator_ids <initiator_ids>

- [ ] **storage initiator list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage initiator list

- [ ] **storage initiator modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py storage initiator modify --initiator_id <initiator_id>

### logic_port

- [ ] **storage logic_port create**
  - 描述：create
  - 命令：python scripts/dme_cli.py storage logic_port create

- [ ] **storage logic_port delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py storage logic_port delete

- [ ] **storage logic_port failback**
  - 描述：failback
  - 命令：python scripts/dme_cli.py storage logic_port failback

- [ ] **storage logic_port list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage logic_port list

- [ ] **storage logic_port show**
  - 描述：show
  - 命令：python scripts/dme_cli.py storage logic_port show

- [ ] **storage logic_port update**
  - 描述：update
  - 命令：python scripts/dme_cli.py storage logic_port update

### node

- [ ] **storage node list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage node list

### pool

- [ ] **storage pool list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage pool list

### port

- [ ] **storage port list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage port list

- [ ] **storage port show_bond_members**
  - 描述：show_bond_members
  - 命令：python scripts/dme_cli.py storage port show_bond_members

### power

- [ ] **storage power show**
  - 描述：show
  - 命令：python scripts/dme_cli.py storage power show

### psu

- [ ] **storage psu list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage psu list

### qos

- [ ] **storage qos activate**
  - 描述：activate
  - 命令：python scripts/dme_cli.py storage qos activate --qos_policy_ids <qos_policy_ids>

- [ ] **storage qos associate**
  - 描述：associate
  - 命令：python scripts/dme_cli.py storage qos associate --qos_policy_id <qos_policy_id> --resource_ids <resource_ids> --resource_type <resource_type>

- [ ] **storage qos create**
  - 描述：create
  - 命令：python scripts/dme_cli.py storage qos create --name <name> --storage_id <storage_id> --resource_type <resource_type> --resource_ids <resource_ids> --zone_id <zone_id> --vstore_id <vstore_id>

- [ ] **storage qos deactivate**
  - 描述：deactivate
  - 命令：python scripts/dme_cli.py storage qos deactivate --qos_policy_ids <qos_policy_ids>

- [ ] **storage qos delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py storage qos delete --qos_policy_ids <qos_policy_ids>

- [ ] **storage qos list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage qos list --storage_id <storage_id>

- [ ] **storage qos modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py storage qos modify --qos_policy_id <qos_policy_id>

- [ ] **storage qos show**
  - 描述：show
  - 命令：python scripts/dme_cli.py storage qos show --qos_policy_id <qos_policy_id>

- [ ] **storage qos unassociate**
  - 描述：unassociate
  - 命令：python scripts/dme_cli.py storage qos unassociate --qos_policy_id <qos_policy_id> --resource_ids <resource_ids> --resource_type <resource_type>

### token

- [ ] **storage token show**
  - 描述：show
  - 命令：python scripts/dme_cli.py storage token show

### vlan

- [ ] **storage vlan create**
  - 描述：create
  - 命令：python scripts/dme_cli.py storage vlan create --name <name> --vlan_id <vlan_id> --storage_id <storage_id>

- [ ] **storage vlan delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py storage vlan delete

- [ ] **storage vlan list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage vlan list

- [ ] **storage vlan modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py storage vlan modify

### vstore

- [ ] **storage vstore create**
  - 描述：create
  - 命令：python scripts/dme_cli.py storage vstore create --name <name> --storage_id <storage_id>

- [ ] **storage vstore delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py storage vstore delete --vstore_ids <vstore_ids>

- [ ] **storage vstore list**
  - 描述：list
  - 命令：python scripts/dme_cli.py storage vstore list

- [ ] **storage vstore modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py storage vstore modify --vstore_id <vstore_id>

- [ ] **storage vstore show**
  - 描述：show
  - 命令：python scripts/dme_cli.py storage vstore show --vstore_id <vstore_id>

## system 系统管理 (System) 相关操作

- [ ] **system certificate**
  - 描述：certificate
  - 命令：python scripts/dme_cli.py system certificate

- [ ] **system login**
  - 描述：login
  - 命令：python scripts/dme_cli.py system login

- [ ] **system logout**
  - 描述：logout
  - 命令：python scripts/dme_cli.py system logout

- [ ] **system show**
  - 描述：show
  - 命令：python scripts/dme_cli.py system show

### az

- [ ] **system az list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system az list

### backup_server

- [ ] **system backup_server list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system backup_server list

### dc

- [ ] **system dc list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system dc list

- [ ] **system dc show**
  - 描述：show
  - 命令：python scripts/dme_cli.py system dc show --dc_id <dc_id>

- [ ] **system dc show_devices**
  - 描述：show_devices
  - 命令：python scripts/dme_cli.py system dc show_devices --dc_id <dc_id>

### role

- [ ] **system role list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system role list

### tag

- [ ] **system tag bind**
  - 描述：bind
  - 命令：python scripts/dme_cli.py system tag bind --tag_id <tag_id> --resources <resources>

- [ ] **system tag create**
  - 描述：create
  - 命令：python scripts/dme_cli.py system tag create --name <name> --tag_type_id <tag_type_id>

- [ ] **system tag delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py system tag delete --tag_ids <tag_ids>

- [ ] **system tag list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system tag list

- [ ] **system tag modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py system tag modify --tag_id <tag_id>

- [ ] **system tag unbind**
  - 描述：unbind
  - 命令：python scripts/dme_cli.py system tag unbind --tag_id <tag_id> --resources <resources>

### tag_type

- [ ] **system tag_type create**
  - 描述：create
  - 命令：python scripts/dme_cli.py system tag_type create --name <name>

- [ ] **system tag_type delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py system tag_type delete --tag_type_ids <tag_type_ids>

- [ ] **system tag_type list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system tag_type list

- [ ] **system tag_type modify**
  - 描述：modify
  - 命令：python scripts/dme_cli.py system tag_type modify --tag_type_id <tag_type_id>

### task

- [ ] **system task list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system task list

- [ ] **system task retry**
  - 描述：retry
  - 命令：python scripts/dme_cli.py system task retry --task_id <task_id>

- [ ] **system task show**
  - 描述：show
  - 命令：python scripts/dme_cli.py system task show --task_id <task_id>

- [ ] **system task wait**
  - 描述：wait
  - 命令：python scripts/dme_cli.py system task wait

### todo_task

- [ ] **system todo_task audit**
  - 描述：audit
  - 命令：python scripts/dme_cli.py system todo_task audit --item_id <item_id> --is_approval <is_approval>

- [ ] **system todo_task close**
  - 描述：close
  - 命令：python scripts/dme_cli.py system todo_task close --item_id <item_id> --reason <reason>

- [ ] **system todo_task execute**
  - 描述：execute
  - 命令：python scripts/dme_cli.py system todo_task execute --item_id <item_id>

- [ ] **system todo_task list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system todo_task list --service_type <service_type>

- [ ] **system todo_task revoke**
  - 描述：revoke
  - 命令：python scripts/dme_cli.py system todo_task revoke --item_id <item_id>

- [ ] **system todo_task show**
  - 描述：show
  - 命令：python scripts/dme_cli.py system todo_task show --item_id <item_id>

### todo_task_group

- [ ] **system todo_task_group confirm**
  - 描述：confirm
  - 命令：python scripts/dme_cli.py system todo_task_group confirm --group_id <group_id>

- [ ] **system todo_task_group execute**
  - 描述：execute
  - 命令：python scripts/dme_cli.py system todo_task_group execute --group_id <group_id>

- [ ] **system todo_task_group list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system todo_task_group list

### user

- [ ] **system user create**
  - 描述：create
  - 命令：python scripts/dme_cli.py system user create

- [ ] **system user delete**
  - 描述：delete
  - 命令：python scripts/dme_cli.py system user delete

- [ ] **system user list**
  - 描述：list
  - 命令：python scripts/dme_cli.py system user list

- [ ] **system user show**
  - 描述：show
  - 命令：python scripts/dme_cli.py system user show

## virtualization 虚拟化服务 (Virtualization) 相关操作

- [ ] **virtualization cluster list**
  - 描述：cluster list
  - 命令：python scripts/dme_cli.py virtualization cluster list

- [ ] **virtualization cluster show**
  - 描述：cluster show
  - 命令：python scripts/dme_cli.py virtualization cluster show --cluster_id <cluster_id>

- [ ] **virtualization datastore list**
  - 描述：datastore list
  - 命令：python scripts/dme_cli.py virtualization datastore list

- [ ] **virtualization datastore show**
  - 描述：datastore show
  - 命令：python scripts/dme_cli.py virtualization datastore show --datastore_id <datastore_id>

- [ ] **virtualization disk list**
  - 描述：disk list
  - 命令：python scripts/dme_cli.py virtualization disk list

- [ ] **virtualization host adapter_list**
  - 描述：host adapter_list
  - 命令：python scripts/dme_cli.py virtualization host adapter_list --host_id <host_id>

- [ ] **virtualization host list**
  - 描述：host list
  - 命令：python scripts/dme_cli.py virtualization host list

- [ ] **virtualization host show**
  - 描述：host show
  - 命令：python scripts/dme_cli.py virtualization host show --host_id <host_id>

- [ ] **virtualization site list**
  - 描述：site list
  - 命令：python scripts/dme_cli.py virtualization site list

- [ ] **virtualization site show**
  - 描述：site show
  - 命令：python scripts/dme_cli.py virtualization site show --site_id <site_id>

- [ ] **virtualization vdisk list**
  - 描述：vdisk list
  - 命令：python scripts/dme_cli.py virtualization vdisk list

- [ ] **virtualization vdisk show**
  - 描述：vdisk show
  - 命令：python scripts/dme_cli.py virtualization vdisk show --virtual_disk_id <virtual_disk_id>

- [ ] **virtualization vm list**
  - 描述：vm list
  - 命令：python scripts/dme_cli.py virtualization vm list

- [ ] **virtualization vm show**
  - 描述：vm show
  - 命令：python scripts/dme_cli.py virtualization vm show --vm_id <vm_id>

## workflow 工作流 (Workflow) 相关操作

- [ ] **workflow 直接动作**
  - 描述：直接动作
  - 命令：python scripts/dme_cli.py workflow 直接动作

### instance

- [ ] **workflow instance create**
  - 描述：create
  - 命令：python scripts/dme_cli.py workflow instance create

- [ ] **workflow instance show**
  - 描述：show
  - 命令：python scripts/dme_cli.py workflow instance show --instance_id <instance_id>

- [ ] **workflow instance step_log**
  - 描述：step_log
  - 命令：python scripts/dme_cli.py workflow instance step_log --instance_id <instance_id> --step_id <step_id>

- [ ] **workflow instance stop**
  - 描述：stop
  - 命令：python scripts/dme_cli.py workflow instance stop --instance_id <instance_id>

### template

- [ ] **workflow template groups**
  - 描述：groups
  - 命令：python scripts/dme_cli.py workflow template groups

- [ ] **workflow template list**
  - 描述：list
  - 命令：python scripts/dme_cli.py workflow template list --page_no <page_no> --page_size <page_size>

- [ ] **workflow template show**
  - 描述：show
  - 命令：python scripts/dme_cli.py workflow template show --template_id <template_id>

