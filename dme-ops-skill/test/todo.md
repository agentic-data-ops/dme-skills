# DME CLI 测试执行清单

## 环境准备

- [ ] 配置DME API环境变量
  ```bash
  export DME_API_ENDPOINT="https://<dme-server>:<port>"
  export DME_API_USERNAME="<username>"
  export DME_API_PASSWORD="<password>"
  ```

- [ ] 验证连接
  ```bash
  python scripts/dme_cli.py --list-topics
  ```

- [ ] 验证登录
  ```bash
  python scripts/dme_cli.py system login --help
  ```

### aiops 主题

#### alarm 子主题

- [x] **aiops alarm ack**
  - 描述: ack
  - 命令: `python scripts/dme_cli.py aiops alarm ack`

- [x] **aiops alarm clear**
  - 描述: clear
  - 命令: `python scripts/dme_cli.py aiops alarm clear`

- [x] **aiops alarm list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py aiops alarm list`

- [x] **aiops alarm unack**
  - 描述: unack
  - 命令: `python scripts/dme_cli.py aiops alarm unack`

#### check_policy 子主题

- [x] **aiops check_policy delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py aiops check_policy delete`

- [x] **aiops check_policy disable**
  - 描述: disable
  - 命令: `python scripts/dme_cli.py aiops check_policy disable`

- [x] **aiops check_policy enable**
  - 描述: enable
  - 命令: `python scripts/dme_cli.py aiops check_policy enable`

- [x] **aiops check_policy execute**
  - 描述: execute
  - 命令: `python scripts/dme_cli.py aiops check_policy execute`

- [x] **aiops alarm list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py aiops check_policy list`

#### check_result 子主题

- [x] **aiops alarm list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py aiops check_result list`

- [x] **aiops check_result show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py aiops check_result show`

#### diagnose_task 子主题

- [ ] **aiops diagnose_task create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py aiops diagnose_task create`

- [ ] **aiops diagnose_task status**
  - 描述: status
  - 命令: `python scripts/dme_cli.py aiops diagnose_task status`

#### health 子主题

- [ ] **aiops health query_data**
  - 描述: query_data
  - 命令: `python scripts/dme_cli.py aiops health query_data`

- [ ] **aiops health show_detail**
  - 描述: show_detail
  - 命令: `python scripts/dme_cli.py aiops health show_detail`

- [ ] **aiops health show_score**
  - 描述: show_score
  - 命令: `python scripts/dme_cli.py aiops health show_score`

#### performance 子主题

- [ ] **aiops performance create_collect_task**
  - 描述: create_collect_task
  - 命令: `python scripts/dme_cli.py aiops performance create_collect_task`

- [ ] **aiops performance download_collect_result**
  - 描述: download_collect_result
  - 命令: `python scripts/dme_cli.py aiops performance download_collect_result`

- [ ] **aiops performance list_indicators**
  - 描述: list_indicators
  - 命令: `python scripts/dme_cli.py aiops performance list_indicators`

- [x] **aiops performance list_object_types**
  - 描述: list_object_types
  - 命令: `python scripts/dme_cli.py aiops performance list_object_types`

- [ ] **aiops performance query**
  - 描述: query
  - 命令: `python scripts/dme_cli.py aiops performance query`

- [ ] **aiops performance show_indicators**
  - 描述: show_indicators
  - 命令: `python scripts/dme_cli.py aiops performance show_indicators`

#### topology 子主题

- [ ] **aiops topology fcsan_query**
  - 描述: fcsan_query
  - 命令: `python scripts/dme_cli.py aiops topology fcsan_query`

- [ ] **aiops topology ipsan_query**
  - 描述: ipsan_query
  - 命令: `python scripts/dme_cli.py aiops topology ipsan_query`

- [ ] **aiops topology query_graph_path**
  - 描述: query_graph_path
  - 命令: `python scripts/dme_cli.py aiops topology query_graph_path`

- [ ] **aiops topology query_luns**
  - 描述: query_luns
  - 命令: `python scripts/dme_cli.py aiops topology query_luns`

- [ ] **aiops topology query_san_path**
  - 描述: query_san_path
  - 命令: `python scripts/dme_cli.py aiops topology query_san_path`

- [ ] **aiops topology query_vms**
  - 描述: query_vms
  - 命令: `python scripts/dme_cli.py aiops topology query_vms`

### backup 主题

#### cluster 子主题

- [ ] **backup capacity**
  - 描述: capacity
  - 命令: `python scripts/dme_cli.py backup cluster capacity`

- [ ] **backup cluster list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py backup cluster list`

- [ ] **backup quota**
  - 描述: quota
  - 命令: `python scripts/dme_cli.py backup cluster quota`

### cmdb 主题

#### class 子主题

- [ ] **cmdb class list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py cmdb class list`

- [ ] **cmdb show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py cmdb class show`

#### instance 子主题

- [ ] **cmdb instance list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py cmdb instance list`

- [ ] **cmdb show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py cmdb instance show`

#### relation 子主题

- [ ] **cmdb relation list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py cmdb relation list`

- [ ] **cmdb show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py cmdb relation show`

### fc_switch 主题

#### alias 子主题

- [ ] **fc_switch create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py fc_switch alias create`

- [ ] **fc_switch delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py fc_switch alias delete`

- [x] **fc_switch alias list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch alias list`

- [ ] **fc_switch modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py fc_switch alias modify`

- [ ] **fc_switch show_members**
  - 描述: show_members
  - 命令: `python scripts/dme_cli.py fc_switch alias show_members`

#### controller 子主题

- [x] **fc_switch controller list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch controller list`

#### fabric 子主题

- [ ] **fc_switch backup**
  - 描述: backup
  - 命令: `python scripts/dme_cli.py fc_switch fabric backup`

- [x] **fc_switch fabric list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch fabric list`

- [ ] **fc_switch show_ports**
  - 描述: show_ports
  - 命令: `python scripts/dme_cli.py fc_switch fabric show_ports`

#### port 子主题

- [x] **fc_switch port list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch port list`

#### vsan 子主题

- [x] **fc_switch vsan list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch vsan list`

#### zone 子主题

- [ ] **fc_switch batch_create**
  - 描述: batch_create
  - 命令: `python scripts/dme_cli.py fc_switch zone batch_create`

- [ ] **fc_switch create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py fc_switch zone create`

- [ ] **fc_switch delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py fc_switch zone delete`

- [x] **fc_switch zone list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch zone list`

- [ ] **fc_switch modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py fc_switch zone modify`

- [ ] **fc_switch show_members**
  - 描述: show_members
  - 命令: `python scripts/dme_cli.py fc_switch zone show_members`

#### 直接动作

- [x] **fc_switch zone list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch list`

- [x] **fc_switch sync**
  - 描述: sync
  - 命令: `python scripts/dme_cli.py fc_switch sync`

### gfs 主题

#### dataspace 子主题

- [ ] **gfs dataspace list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py gfs dataspace list`

- [ ] **gfs show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py gfs dataspace show`

- [ ] **gfs site_list**
  - 描述: site_list
  - 命令: `python scripts/dme_cli.py gfs dataspace site_list`

#### migration_task 子主题

- [ ] **gfs create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py gfs migration_task create`

- [ ] **gfs delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py gfs migration_task delete`

- [ ] **gfs migration_task list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py gfs migration_task list`

- [ ] **gfs modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py gfs migration_task modify`

- [ ] **gfs operate**
  - 描述: operate
  - 命令: `python scripts/dme_cli.py gfs migration_task operate`

- [ ] **gfs show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py gfs migration_task show`

#### namespace 子主题

- [ ] **gfs create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py gfs namespace create`

- [ ] **gfs delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py gfs namespace delete`

- [ ] **gfs namespace list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py gfs namespace list`

- [ ] **gfs modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py gfs namespace modify`

- [ ] **gfs show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py gfs namespace show`

### ip_switch 主题

#### board 子主题

- [x] **ip_switch board list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch board list`

#### fan 子主题

- [x] **ip_switch fan list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch fan list`

#### frame 子主题

- [x] **ip_switch frame list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch frame list`

#### port 子主题

- [x] **ip_switch port list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch port list`

#### power 子主题

- [x] **ip_switch power list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch power list`

#### subcard 子主题

- [x] **ip_switch subcard list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch subcard list`

#### 直接动作

- [x] **ip_switch subcard list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch list`

### kubernetes 主题

#### cluster 子主题

- [ ] **kubernetes cluster list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes cluster list`

#### namespace 子主题

- [ ] **kubernetes namespace list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes namespace list`

#### node 子主题

- [ ] **kubernetes node list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes node list`

#### pod 子主题

- [ ] **kubernetes pod list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes pod list`

#### pv 子主题

- [ ] **kubernetes pv list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes pv list`

#### pvc 子主题

- [ ] **kubernetes pvc list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes pvc list`

### nas 主题

#### cifs_share 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas cifs_share create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas cifs_share delete`

- [ ] **nas cifs_share list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas cifs_share list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas cifs_share modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas cifs_share show`

- [ ] **nas show_permissions**
  - 描述: show_permissions
  - 命令: `python scripts/dme_cli.py nas cifs_share show_permissions`

#### dataturbo_share 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas dataturbo_share create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas dataturbo_share delete`

- [ ] **nas dataturbo_share list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas dataturbo_share list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas dataturbo_share modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas dataturbo_share show`

- [ ] **nas show_permissions**
  - 描述: show_permissions
  - 命令: `python scripts/dme_cli.py nas dataturbo_share show_permissions`

#### dpc 子主题

- [ ] **nas dpc list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas dpc list`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas dpc show`

#### dtree 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas dtree create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas dtree delete`

- [ ] **nas dtree list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas dtree list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas dtree modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas dtree show`

#### filesystem 子主题

- [ ] **nas batch_modify**
  - 描述: batch_modify
  - 命令: `python scripts/dme_cli.py nas filesystem batch_modify`

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas filesystem create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas filesystem delete`

- [ ] **nas filesystem list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas filesystem list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas filesystem modify`

- [ ] **nas query_available**
  - 描述: query_available
  - 命令: `python scripts/dme_cli.py nas filesystem query_available`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas filesystem show`

#### namespace 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas namespace create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas namespace delete`

- [ ] **nas namespace list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas namespace list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas namespace modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas namespace show`

#### nfs_share 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas nfs_share create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas nfs_share delete`

- [ ] **nas nfs_share list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas nfs_share list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas nfs_share modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas nfs_share show`

#### quota 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas quota create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas quota delete`

- [ ] **nas quota list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas quota list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas quota modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas quota show`

### protection 主题

#### clone_group 子主题

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection clone_group create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection clone_group delete`

- [ ] **protection sync**
  - 描述: sync
  - 命令: `python scripts/dme_cli.py protection clone_group sync`

#### device_pair 子主题

- [ ] **protection device_pair list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection device_pair list`

#### group 子主题

- [ ] **protection add_luns**
  - 描述: add_luns
  - 命令: `python scripts/dme_cli.py protection group add_luns`

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection group create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection group delete`

- [ ] **protection group list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection group list`

- [ ] **protection modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py protection group modify`

- [ ] **protection remove_luns**
  - 描述: remove_luns
  - 命令: `python scripts/dme_cli.py protection group remove_luns`

#### hypermetro_domain 子主题

- [ ] **protection hypermetro_domain list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection hypermetro_domain list`

#### hypermetro_group 子主题

- [ ] **protection add_pairs**
  - 描述: add_pairs
  - 命令: `python scripts/dme_cli.py protection hypermetro_group add_pairs`

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection hypermetro_group create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection hypermetro_group delete`

- [ ] **protection force_startup**
  - 描述: force_startup
  - 命令: `python scripts/dme_cli.py protection hypermetro_group force_startup`

- [ ] **protection hypermetro_group list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection hypermetro_group list`

- [ ] **protection modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py protection hypermetro_group modify`

- [ ] **protection pause**
  - 描述: pause
  - 命令: `python scripts/dme_cli.py protection hypermetro_group pause`

- [ ] **protection remove_pairs**
  - 描述: remove_pairs
  - 命令: `python scripts/dme_cli.py protection hypermetro_group remove_pairs`

- [ ] **protection switch_priority**
  - 描述: switch_priority
  - 命令: `python scripts/dme_cli.py protection hypermetro_group switch_priority`

#### hypermetro_pair 子主题

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair delete`

- [ ] **protection force_startup**
  - 描述: force_startup
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair force_startup`

- [ ] **protection hypermetro_pair list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair list`

- [ ] **protection modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair modify`

- [ ] **protection pause**
  - 描述: pause
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair pause`

- [ ] **protection switch_priority**
  - 描述: switch_priority
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair switch_priority`

- [ ] **protection sync**
  - 描述: sync
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair sync`

#### replication_group 子主题

- [ ] **protection add_pairs**
  - 描述: add_pairs
  - 命令: `python scripts/dme_cli.py protection replication_group add_pairs`

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection replication_group create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection replication_group delete`

- [ ] **protection modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py protection replication_group modify`

- [ ] **protection remove_pairs**
  - 描述: remove_pairs
  - 命令: `python scripts/dme_cli.py protection replication_group remove_pairs`

- [ ] **protection split**
  - 描述: split
  - 命令: `python scripts/dme_cli.py protection replication_group split`

- [ ] **protection switch**
  - 描述: switch
  - 命令: `python scripts/dme_cli.py protection replication_group switch`

- [ ] **protection switch_write_protection**
  - 描述: switch_write_protection
  - 命令: `python scripts/dme_cli.py protection replication_group switch_write_protection`

- [ ] **protection sync**
  - 描述: sync
  - 命令: `python scripts/dme_cli.py protection replication_group sync`

#### replication_link 子主题

- [ ] **protection replication_link list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection replication_link list`

#### replication_pair 子主题

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection replication_pair create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection replication_pair delete`

- [ ] **protection replication_pair list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection replication_pair list`

- [ ] **protection modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py protection replication_pair modify`

- [ ] **protection split**
  - 描述: split
  - 命令: `python scripts/dme_cli.py protection replication_pair split`

- [ ] **protection switch**
  - 描述: switch
  - 命令: `python scripts/dme_cli.py protection replication_pair switch`

- [ ] **protection switch_write_protection**
  - 描述: switch_write_protection
  - 命令: `python scripts/dme_cli.py protection replication_pair switch_write_protection`

- [ ] **protection sync**
  - 描述: sync
  - 命令: `python scripts/dme_cli.py protection replication_pair sync`

#### snapshot 子主题

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection snapshot create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection snapshot delete`

- [ ] **protection snapshot list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection snapshot list`

- [ ] **protection rollback**
  - 描述: rollback
  - 命令: `python scripts/dme_cli.py protection snapshot rollback`

#### snapshot_group 子主题

- [ ] **protection activate**
  - 描述: activate
  - 命令: `python scripts/dme_cli.py protection snapshot_group activate`

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection snapshot_group create`

- [ ] **protection deactivate**
  - 描述: deactivate
  - 命令: `python scripts/dme_cli.py protection snapshot_group deactivate`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection snapshot_group delete`

- [ ] **protection rollback**
  - 描述: rollback
  - 命令: `python scripts/dme_cli.py protection snapshot_group rollback`

### san 主题

#### lun 子主题

- [ ] **san connection**
  - 描述: connection
  - 命令: `python scripts/dme_cli.py san lun connection`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san lun create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san lun delete`

- [ ] **san expand**
  - 描述: expand
  - 命令: `python scripts/dme_cli.py san lun expand`

- [ ] **san lun list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san lun list`

- [ ] **san mapping**
  - 描述: mapping
  - 命令: `python scripts/dme_cli.py san lun mapping`

- [ ] **san modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py san lun modify`

- [ ] **san modify_name**
  - 描述: modify_name
  - 命令: `python scripts/dme_cli.py san lun modify_name`

- [ ] **san show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py san lun show`

#### lun_group 子主题

- [ ] **san add_luns**
  - 描述: add_luns
  - 命令: `python scripts/dme_cli.py san lun_group add_luns`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san lun_group create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san lun_group delete`

- [ ] **san lun_group list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san lun_group list`

- [ ] **san remove_luns**
  - 描述: remove_luns
  - 命令: `python scripts/dme_cli.py san lun_group remove_luns`

- [ ] **san show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py san lun_group show`

- [ ] **san show_luns**
  - 描述: show_luns
  - 命令: `python scripts/dme_cli.py san lun_group show_luns`

#### mapping_view 子主题

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san mapping_view create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san mapping_view delete`

- [ ] **san mapping_view list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san mapping_view list`

- [ ] **san query**
  - 描述: query
  - 命令: `python scripts/dme_cli.py san mapping_view query`

#### physical_host 子主题

- [ ] **san add_initiators**
  - 描述: add_initiators
  - 命令: `python scripts/dme_cli.py san physical_host add_initiators`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san physical_host create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san physical_host delete`

- [ ] **san physical_host list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san physical_host list`

- [ ] **san map_luns**
  - 描述: map_luns
  - 命令: `python scripts/dme_cli.py san physical_host map_luns`

- [ ] **san modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py san physical_host modify`

- [ ] **san query_by_initiator**
  - 描述: query_by_initiator
  - 命令: `python scripts/dme_cli.py san physical_host query_by_initiator`

- [ ] **san query_sshkey**
  - 描述: query_sshkey
  - 命令: `python scripts/dme_cli.py san physical_host query_sshkey`

- [ ] **san remove_initiators**
  - 描述: remove_initiators
  - 命令: `python scripts/dme_cli.py san physical_host remove_initiators`

- [ ] **san save_sshkey**
  - 描述: save_sshkey
  - 命令: `python scripts/dme_cli.py san physical_host save_sshkey`

- [ ] **san show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py san physical_host show`

- [ ] **san show_initiators**
  - 描述: show_initiators
  - 命令: `python scripts/dme_cli.py san physical_host show_initiators`

- [ ] **san test**
  - 描述: test
  - 命令: `python scripts/dme_cli.py san physical_host test`

- [ ] **san unmap_luns**
  - 描述: unmap_luns
  - 命令: `python scripts/dme_cli.py san physical_host unmap_luns`

#### physical_host_group 子主题

- [ ] **san add_hosts**
  - 描述: add_hosts
  - 命令: `python scripts/dme_cli.py san physical_host_group add_hosts`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san physical_host_group create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san physical_host_group delete`

- [ ] **san physical_host_group list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san physical_host_group list`

- [ ] **san map_luns**
  - 描述: map_luns
  - 命令: `python scripts/dme_cli.py san physical_host_group map_luns`

- [ ] **san modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py san physical_host_group modify`

- [ ] **san remove_hosts**
  - 描述: remove_hosts
  - 命令: `python scripts/dme_cli.py san physical_host_group remove_hosts`

- [ ] **san show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py san physical_host_group show`

- [ ] **san unmap_luns**
  - 描述: unmap_luns
  - 命令: `python scripts/dme_cli.py san physical_host_group unmap_luns`

#### port_group 子主题

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san port_group create`

- [ ] **san port_group list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san port_group list`

- [ ] **san show_ports**
  - 描述: show_ports
  - 命令: `python scripts/dme_cli.py san port_group show_ports`

- [ ] **san show_relations**
  - 描述: show_relations
  - 命令: `python scripts/dme_cli.py san port_group show_relations`

#### storage_host 子主题

- [ ] **san batch_query**
  - 描述: batch_query
  - 命令: `python scripts/dme_cli.py san storage_host batch_query`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san storage_host create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san storage_host delete`

- [ ] **san storage_host list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san storage_host list`

- [ ] **san modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py san storage_host modify`

- [ ] **san show_luns**
  - 描述: show_luns
  - 命令: `python scripts/dme_cli.py san storage_host show_luns`

- [ ] **san show_paths**
  - 描述: show_paths
  - 命令: `python scripts/dme_cli.py san storage_host show_paths`

#### storage_host_group 子主题

- [ ] **san add_hosts**
  - 描述: add_hosts
  - 命令: `python scripts/dme_cli.py san storage_host_group add_hosts`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san storage_host_group create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san storage_host_group delete`

- [ ] **san storage_host_group list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san storage_host_group list`

- [ ] **san remove_hosts**
  - 描述: remove_hosts
  - 命令: `python scripts/dme_cli.py san storage_host_group remove_hosts`

- [ ] **san show_luns**
  - 描述: show_luns
  - 命令: `python scripts/dme_cli.py san storage_host_group show_luns`

### self_service 主题

#### lun 子主题

- [ ] **self_service bind_project**
  - 描述: bind_project
  - 命令: `python scripts/dme_cli.py self_service lun bind_project`

- [ ] **self_service bind_tier**
  - 描述: bind_tier
  - 命令: `python scripts/dme_cli.py self_service lun bind_tier`

- [ ] **self_service change_tier**
  - 描述: change_tier
  - 命令: `python scripts/dme_cli.py self_service lun change_tier`

- [ ] **self_service create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py self_service lun create`

- [ ] **self_service unbind_project**
  - 描述: unbind_project
  - 命令: `python scripts/dme_cli.py self_service lun unbind_project`

- [ ] **self_service unbind_tier**
  - 描述: unbind_tier
  - 命令: `python scripts/dme_cli.py self_service lun unbind_tier`

#### project 子主题

- [ ] **self_service project list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py self_service project list`

- [ ] **self_service show_tiers**
  - 描述: show_tiers
  - 命令: `python scripts/dme_cli.py self_service project show_tiers`

#### tier 子主题

- [ ] **self_service tier list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py self_service tier list`

- [ ] **self_service show_projects**
  - 描述: show_projects
  - 命令: `python scripts/dme_cli.py self_service tier show_projects`

### server 主题

#### cpu 子主题

- [x] **server cpu list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server cpu list`

#### disk 子主题

- [x] **server disk list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server disk list`

#### fan 子主题

- [x] **server fan list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server fan list`

#### memory 子主题

- [x] **server memory list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server memory list`

#### nic 子主题

- [x] **server nic list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server nic list`

#### pcie_card 子主题

- [x] **server pcie_card list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server pcie_card list`

#### power 子主题

- [x] **server power list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server power list`

#### raid_card 子主题

- [x] **server raid_card list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server raid_card list`

#### 直接动作

- [x] **server raid_card list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server list`

- [x] **server show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py server show`

### storage 主题

#### account 子主题

- [ ] **storage show_dataturbo_admin_users**
  - 描述: show_dataturbo_admin_users
  - 命令: `python scripts/dme_cli.py storage account show_dataturbo_admin_users`

- [ ] **storage show_local_user_groups**
  - 描述: show_local_user_groups
  - 命令: `python scripts/dme_cli.py storage account show_local_user_groups`

- [ ] **storage show_local_users**
  - 描述: show_local_users
  - 命令: `python scripts/dme_cli.py storage account show_local_users`

- [ ] **storage show_unix_user_groups**
  - 描述: show_unix_user_groups
  - 命令: `python scripts/dme_cli.py storage account show_unix_user_groups`

- [ ] **storage show_unix_users**
  - 描述: show_unix_users
  - 命令: `python scripts/dme_cli.py storage account show_unix_users`

- [ ] **storage show_windows_user_groups**
  - 描述: show_windows_user_groups
  - 命令: `python scripts/dme_cli.py storage account show_windows_user_groups`

- [ ] **storage show_windows_users**
  - 描述: show_windows_users
  - 命令: `python scripts/dme_cli.py storage account show_windows_users`

#### app_type 子主题

- [x] **storage app_type list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage app_type list`

#### bbu 子主题

- [x] **storage bbu list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage bbu list`

#### controller 子主题

- [x] **storage controller list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage controller list`

#### disk 子主题

- [x] **storage disk list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage disk list`

#### disk_pool 子主题

- [x] **storage disk_pool list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage disk_pool list`

#### enclosure 子主题

- [x] **storage enclosure list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage enclosure list`

#### failover_group 子主题

- [x] **storage failover_group list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage failover_group list`

- [ ] **storage show_ports**
  - 描述: show_ports
  - 命令: `python scripts/dme_cli.py storage failover_group show_ports`

- [ ] **storage show_vlans**
  - 描述: show_vlans
  - 命令: `python scripts/dme_cli.py storage failover_group show_vlans`

#### fan 子主题

- [x] **storage fan list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage fan list`

#### hyperscale_pool 子主题

- [x] **storage hyperscale_pool list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage hyperscale_pool list`

#### initiator 子主题

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage initiator delete`

- [x] **storage initiator list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage initiator list`

- [ ] **storage modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py storage initiator modify`

#### logic_port 子主题

- [ ] **storage create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py storage logic_port create`

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage logic_port delete`

- [ ] **storage failback**
  - 描述: failback
  - 命令: `python scripts/dme_cli.py storage logic_port failback`

- [x] **storage logic_port list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage logic_port list`

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage logic_port show`

- [ ] **storage update**
  - 描述: update
  - 命令: `python scripts/dme_cli.py storage logic_port update`

#### node 子主题

- [x] **storage node list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage node list`

#### pool 子主题

- [x] **storage pool list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage pool list`

#### port 子主题

- [x] **storage port list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage port list`

- [ ] **storage show_bond_members**
  - 描述: show_bond_members
  - 命令: `python scripts/dme_cli.py storage port show_bond_members`

#### power 子主题

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage power show`

#### psu 子主题

- [x] **storage psu list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage psu list`

#### qos 子主题

- [ ] **storage activate**
  - 描述: activate
  - 命令: `python scripts/dme_cli.py storage qos activate`

- [ ] **storage associate**
  - 描述: associate
  - 命令: `python scripts/dme_cli.py storage qos associate`

- [ ] **storage create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py storage qos create`

- [ ] **storage deactivate**
  - 描述: deactivate
  - 命令: `python scripts/dme_cli.py storage qos deactivate`

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage qos delete`

- [x] **storage qos list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage qos list`

- [ ] **storage modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py storage qos modify`

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage qos show`

- [ ] **storage unassociate**
  - 描述: unassociate
  - 命令: `python scripts/dme_cli.py storage qos unassociate`

#### token 子主题

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage token show`

#### vlan 子主题

- [ ] **storage create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py storage vlan create`

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage vlan delete`

- [x] **storage vlan list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage vlan list`

- [ ] **storage modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py storage vlan modify`

#### vstore 子主题

- [ ] **storage create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py storage vstore create`

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage vstore delete`

- [x] **storage vstore list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage vstore list`

- [ ] **storage modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py storage vstore modify`

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage vstore show`

#### 直接动作

- [ ] **storage add**
  - 描述: add
  - 命令: `python scripts/dme_cli.py storage add`

- [x] **storage vstore list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage list`

- [ ] **storage modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py storage modify`

- [ ] **storage remove**
  - 描述: remove
  - 命令: `python scripts/dme_cli.py storage remove`

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage show`

- [ ] **storage sync**
  - 描述: sync
  - 命令: `python scripts/dme_cli.py storage sync`

### system 主题

#### az 子主题

- [ ] **system az list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system az list`

#### backup_server 子主题

- [ ] **system backup_server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system backup_server list`

#### dc 子主题

- [ ] **system dc list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system dc list`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system dc show`

- [ ] **system show_devices**
  - 描述: show_devices
  - 命令: `python scripts/dme_cli.py system dc show_devices`

#### role 子主题

- [ ] **system role list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system role list`

#### tag 子主题

- [ ] **system bind**
  - 描述: bind
  - 命令: `python scripts/dme_cli.py system tag bind`

- [ ] **system create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py system tag create`

- [ ] **system delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py system tag delete`

- [ ] **system tag list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system tag list`

- [ ] **system modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py system tag modify`

- [ ] **system unbind**
  - 描述: unbind
  - 命令: `python scripts/dme_cli.py system tag unbind`

#### tag_type 子主题

- [ ] **system create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py system tag_type create`

- [ ] **system delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py system tag_type delete`

- [ ] **system tag_type list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system tag_type list`

- [ ] **system modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py system tag_type modify`

#### task 子主题

- [ ] **system task list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system task list`

- [ ] **system retry**
  - 描述: retry
  - 命令: `python scripts/dme_cli.py system task retry`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system task show`

- [ ] **system wait**
  - 描述: wait
  - 命令: `python scripts/dme_cli.py system task wait`

#### todo_task 子主题

- [ ] **system audit**
  - 描述: audit
  - 命令: `python scripts/dme_cli.py system todo_task audit`

- [ ] **system close**
  - 描述: close
  - 命令: `python scripts/dme_cli.py system todo_task close`

- [ ] **system execute**
  - 描述: execute
  - 命令: `python scripts/dme_cli.py system todo_task execute`

- [ ] **system todo_task list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system todo_task list`

- [ ] **system revoke**
  - 描述: revoke
  - 命令: `python scripts/dme_cli.py system todo_task revoke`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system todo_task show`

#### todo_task_group 子主题

- [ ] **system confirm**
  - 描述: confirm
  - 命令: `python scripts/dme_cli.py system todo_task_group confirm`

- [ ] **system execute**
  - 描述: execute
  - 命令: `python scripts/dme_cli.py system todo_task_group execute`

- [ ] **system todo_task_group list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system todo_task_group list`

#### user 子主题

- [ ] **system create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py system user create`

- [ ] **system delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py system user delete`

- [ ] **system user list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system user list`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system user show`

#### 直接动作

- [x] **system certificate**
  - 描述: certificate
  - 命令: `python scripts/dme_cli.py system certificate`

- [x] **system login**
  - 描述: login
  - 命令: `python scripts/dme_cli.py system login`

- [ ] **system logout**
  - 描述: logout
  - 命令: `python scripts/dme_cli.py system logout`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system show`

### virtualization 主题

#### 直接动作

- [x] **virtualization cluster list**
  - 描述: cluster list
  - 命令: `python scripts/dme_cli.py virtualization cluster list`

- [ ] **virtualization cluster show**
  - 描述: cluster show
  - 命令: `python scripts/dme_cli.py virtualization cluster show`

- [x] **virtualization datastore list**
  - 描述: datastore list
  - 命令: `python scripts/dme_cli.py virtualization datastore list`

- [ ] **virtualization datastore show**
  - 描述: datastore show
  - 命令: `python scripts/dme_cli.py virtualization datastore show`

- [x] **virtualization disk list**
  - 描述: disk list
  - 命令: `python scripts/dme_cli.py virtualization disk list`

- [ ] **virtualization host adapter_list**
  - 描述: host adapter_list
  - 命令: `python scripts/dme_cli.py virtualization host adapter_list`

- [x] **virtualization host list**
  - 描述: host list
  - 命令: `python scripts/dme_cli.py virtualization host list`

- [ ] **virtualization host show**
  - 描述: host show
  - 命令: `python scripts/dme_cli.py virtualization host show`

- [x] **virtualization site list**
  - 描述: site list
  - 命令: `python scripts/dme_cli.py virtualization site list`

- [ ] **virtualization site show**
  - 描述: site show
  - 命令: `python scripts/dme_cli.py virtualization site show`

- [x] **virtualization vdisk list**
  - 描述: vdisk list
  - 命令: `python scripts/dme_cli.py virtualization vdisk list`

- [ ] **virtualization vdisk show**
  - 描述: vdisk show
  - 命令: `python scripts/dme_cli.py virtualization vdisk show`

- [x] **virtualization vm list**
  - 描述: vm list
  - 命令: `python scripts/dme_cli.py virtualization vm list`

- [ ] **virtualization vm show**
  - 描述: vm show
  - 命令: `python scripts/dme_cli.py virtualization vm show`

### workflow 主题

#### instance 子主题

- [ ] **workflow create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py workflow instance create`

- [ ] **workflow show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py workflow instance show`

- [ ] **workflow step_log**
  - 描述: step_log
  - 命令: `python scripts/dme_cli.py workflow instance step_log`

- [ ] **workflow stop**
  - 描述: stop
  - 命令: `python scripts/dme_cli.py workflow instance stop`

#### template 子主题

- [ ] **workflow groups**
  - 描述: groups
  - 命令: `python scripts/dme_cli.py workflow template groups`

- [ ] **workflow template list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py workflow template list`

- [ ] **workflow show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py workflow template show`

#### 直接动作

- [ ] **workflow 直接动作**
  - 描述: 直接动作
  - 命令: `python scripts/dme_cli.py workflow 直接动作`

## 测试执行统计

- 总主题数: 16
- 总测试用例数: 376
- 已执行用例: 0
- 未执行用例: 376
- 执行进度: 0%
