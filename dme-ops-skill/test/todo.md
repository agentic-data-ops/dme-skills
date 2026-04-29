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

### 1. aiops 主题

#### 1.2 alarm 子主题

- [ ] **aiops ack**
  - 描述: ack
  - 命令: `python scripts/dme_cli.py aiops alarm ack`

- [ ] **aiops clear**
  - 描述: clear
  - 命令: `python scripts/dme_cli.py aiops alarm clear`

- [ ] **aiops list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py aiops alarm list`

- [ ] **aiops unack**
  - 描述: unack
  - 命令: `python scripts/dme_cli.py aiops alarm unack`

#### 2.3 check_policy 子主题

- [ ] **aiops delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py aiops check_policy delete`

- [ ] **aiops disable**
  - 描述: disable
  - 命令: `python scripts/dme_cli.py aiops check_policy disable`

- [ ] **aiops enable**
  - 描述: enable
  - 命令: `python scripts/dme_cli.py aiops check_policy enable`

- [ ] **aiops execute**
  - 描述: execute
  - 命令: `python scripts/dme_cli.py aiops check_policy execute`

- [ ] **aiops list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py aiops check_policy list`

#### 3.4 check_result 子主题

- [ ] **aiops list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py aiops check_result list`

- [ ] **aiops show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py aiops check_result show`

#### 4.5 diagnose_task 子主题

- [ ] **aiops create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py aiops diagnose_task create`

- [ ] **aiops status**
  - 描述: status
  - 命令: `python scripts/dme_cli.py aiops diagnose_task status`

#### 5.6 health 子主题

- [ ] **aiops query_data**
  - 描述: query_data
  - 命令: `python scripts/dme_cli.py aiops health query_data`

- [ ] **aiops show_detail**
  - 描述: show_detail
  - 命令: `python scripts/dme_cli.py aiops health show_detail`

- [ ] **aiops show_score**
  - 描述: show_score
  - 命令: `python scripts/dme_cli.py aiops health show_score`

#### 6.7 performance 子主题

- [ ] **aiops create_collect_task**
  - 描述: create_collect_task
  - 命令: `python scripts/dme_cli.py aiops performance create_collect_task`

- [ ] **aiops download_collect_result**
  - 描述: download_collect_result
  - 命令: `python scripts/dme_cli.py aiops performance download_collect_result`

- [ ] **aiops list_indicators**
  - 描述: list_indicators
  - 命令: `python scripts/dme_cli.py aiops performance list_indicators`

- [ ] **aiops list_object_types**
  - 描述: list_object_types
  - 命令: `python scripts/dme_cli.py aiops performance list_object_types`

- [ ] **aiops query**
  - 描述: query
  - 命令: `python scripts/dme_cli.py aiops performance query`

- [ ] **aiops show_indicators**
  - 描述: show_indicators
  - 命令: `python scripts/dme_cli.py aiops performance show_indicators`

#### 7.8 topology 子主题

- [ ] **aiops fcsan_query**
  - 描述: fcsan_query
  - 命令: `python scripts/dme_cli.py aiops topology fcsan_query`

- [ ] **aiops ipsan_query**
  - 描述: ipsan_query
  - 命令: `python scripts/dme_cli.py aiops topology ipsan_query`

- [ ] **aiops query_graph_path**
  - 描述: query_graph_path
  - 命令: `python scripts/dme_cli.py aiops topology query_graph_path`

- [ ] **aiops query_luns**
  - 描述: query_luns
  - 命令: `python scripts/dme_cli.py aiops topology query_luns`

- [ ] **aiops query_san_path**
  - 描述: query_san_path
  - 命令: `python scripts/dme_cli.py aiops topology query_san_path`

- [ ] **aiops query_vms**
  - 描述: query_vms
  - 命令: `python scripts/dme_cli.py aiops topology query_vms`

### 2. backup 主题

#### 1.2 cluster 子主题

- [ ] **backup capacity**
  - 描述: capacity
  - 命令: `python scripts/dme_cli.py backup cluster capacity`

- [ ] **backup list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py backup cluster list`

- [ ] **backup quota**
  - 描述: quota
  - 命令: `python scripts/dme_cli.py backup cluster quota`

### 3. cmdb 主题

#### 1.2 class 子主题

- [ ] **cmdb list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py cmdb class list`

- [ ] **cmdb show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py cmdb class show`

#### 2.3 instance 子主题

- [ ] **cmdb list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py cmdb instance list`

- [ ] **cmdb show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py cmdb instance show`

#### 3.4 relation 子主题

- [ ] **cmdb list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py cmdb relation list`

- [ ] **cmdb show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py cmdb relation show`

### 4. fc_switch 主题

#### 1.2 alias 子主题

- [ ] **fc_switch create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py fc_switch alias create`

- [ ] **fc_switch delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py fc_switch alias delete`

- [ ] **fc_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch alias list`

- [ ] **fc_switch modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py fc_switch alias modify`

- [ ] **fc_switch show_members**
  - 描述: show_members
  - 命令: `python scripts/dme_cli.py fc_switch alias show_members`

#### 2.3 controller 子主题

- [ ] **fc_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch controller list`

#### 3.4 fabric 子主题

- [ ] **fc_switch backup**
  - 描述: backup
  - 命令: `python scripts/dme_cli.py fc_switch fabric backup`

- [ ] **fc_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch fabric list`

- [ ] **fc_switch show_ports**
  - 描述: show_ports
  - 命令: `python scripts/dme_cli.py fc_switch fabric show_ports`

#### 4.5 port 子主题

- [ ] **fc_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch port list`

#### 5.6 vsan 子主题

- [ ] **fc_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch vsan list`

#### 6.7 zone 子主题

- [ ] **fc_switch batch_create**
  - 描述: batch_create
  - 命令: `python scripts/dme_cli.py fc_switch zone batch_create`

- [ ] **fc_switch create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py fc_switch zone create`

- [ ] **fc_switch delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py fc_switch zone delete`

- [ ] **fc_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch zone list`

- [ ] **fc_switch modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py fc_switch zone modify`

- [ ] **fc_switch show_members**
  - 描述: show_members
  - 命令: `python scripts/dme_cli.py fc_switch zone show_members`

#### 7.1 直接动作

- [ ] **fc_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py fc_switch list`

- [ ] **fc_switch sync**
  - 描述: sync
  - 命令: `python scripts/dme_cli.py fc_switch sync`

### 5. gfs 主题

#### 1.2 dataspace 子主题

- [ ] **gfs list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py gfs dataspace list`

- [ ] **gfs show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py gfs dataspace show`

- [ ] **gfs site_list**
  - 描述: site_list
  - 命令: `python scripts/dme_cli.py gfs dataspace site_list`

#### 2.3 migration_task 子主题

- [ ] **gfs create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py gfs migration_task create`

- [ ] **gfs delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py gfs migration_task delete`

- [ ] **gfs list**
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

#### 3.4 namespace 子主题

- [ ] **gfs create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py gfs namespace create`

- [ ] **gfs delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py gfs namespace delete`

- [ ] **gfs list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py gfs namespace list`

- [ ] **gfs modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py gfs namespace modify`

- [ ] **gfs show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py gfs namespace show`

### 6. ip_switch 主题

#### 1.2 board 子主题

- [ ] **ip_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch board list`

#### 2.3 fan 子主题

- [ ] **ip_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch fan list`

#### 3.4 frame 子主题

- [ ] **ip_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch frame list`

#### 4.5 port 子主题

- [ ] **ip_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch port list`

#### 5.6 power 子主题

- [ ] **ip_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch power list`

#### 6.7 subcard 子主题

- [ ] **ip_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch subcard list`

#### 7.1 直接动作

- [ ] **ip_switch list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py ip_switch list`

### 7. kubernetes 主题

#### 1.2 cluster 子主题

- [ ] **kubernetes list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes cluster list`

#### 2.3 namespace 子主题

- [ ] **kubernetes list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes namespace list`

#### 3.4 node 子主题

- [ ] **kubernetes list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes node list`

#### 4.5 pod 子主题

- [ ] **kubernetes list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes pod list`

#### 5.6 pv 子主题

- [ ] **kubernetes list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes pv list`

#### 6.7 pvc 子主题

- [ ] **kubernetes list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py kubernetes pvc list`

### 8. nas 主题

#### 1.2 cifs_share 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas cifs_share create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas cifs_share delete`

- [ ] **nas list**
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

#### 2.3 dataturbo_share 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas dataturbo_share create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas dataturbo_share delete`

- [ ] **nas list**
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

#### 3.4 dpc 子主题

- [ ] **nas list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas dpc list`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas dpc show`

#### 4.5 dtree 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas dtree create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas dtree delete`

- [ ] **nas list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas dtree list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas dtree modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas dtree show`

#### 5.6 filesystem 子主题

- [ ] **nas batch_modify**
  - 描述: batch_modify
  - 命令: `python scripts/dme_cli.py nas filesystem batch_modify`

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas filesystem create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas filesystem delete`

- [ ] **nas list**
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

#### 6.7 namespace 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas namespace create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas namespace delete`

- [ ] **nas list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas namespace list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas namespace modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas namespace show`

#### 7.8 nfs_share 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas nfs_share create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas nfs_share delete`

- [ ] **nas list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas nfs_share list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas nfs_share modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas nfs_share show`

#### 8.9 quota 子主题

- [ ] **nas create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py nas quota create`

- [ ] **nas delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py nas quota delete`

- [ ] **nas list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py nas quota list`

- [ ] **nas modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py nas quota modify`

- [ ] **nas show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py nas quota show`

### 9. protection 主题

#### 1.2 clone_group 子主题

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection clone_group create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection clone_group delete`

- [ ] **protection sync**
  - 描述: sync
  - 命令: `python scripts/dme_cli.py protection clone_group sync`

#### 2.3 device_pair 子主题

- [ ] **protection list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection device_pair list`

#### 3.4 group 子主题

- [ ] **protection add_luns**
  - 描述: add_luns
  - 命令: `python scripts/dme_cli.py protection group add_luns`

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection group create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection group delete`

- [ ] **protection list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection group list`

- [ ] **protection modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py protection group modify`

- [ ] **protection remove_luns**
  - 描述: remove_luns
  - 命令: `python scripts/dme_cli.py protection group remove_luns`

#### 4.5 hypermetro_domain 子主题

- [ ] **protection list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection hypermetro_domain list`

#### 5.6 hypermetro_group 子主题

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

- [ ] **protection list**
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

#### 6.7 hypermetro_pair 子主题

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair delete`

- [ ] **protection force_startup**
  - 描述: force_startup
  - 命令: `python scripts/dme_cli.py protection hypermetro_pair force_startup`

- [ ] **protection list**
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

#### 7.8 replication_group 子主题

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

#### 8.9 replication_link 子主题

- [ ] **protection list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection replication_link list`

#### 9.10 replication_pair 子主题

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection replication_pair create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection replication_pair delete`

- [ ] **protection list**
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

#### 10.11 snapshot 子主题

- [ ] **protection create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py protection snapshot create`

- [ ] **protection delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py protection snapshot delete`

- [ ] **protection list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py protection snapshot list`

- [ ] **protection rollback**
  - 描述: rollback
  - 命令: `python scripts/dme_cli.py protection snapshot rollback`

#### 11.12 snapshot_group 子主题

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

### 10. san 主题

#### 1.2 lun 子主题

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

- [ ] **san list**
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

#### 2.3 lun_group 子主题

- [ ] **san add_luns**
  - 描述: add_luns
  - 命令: `python scripts/dme_cli.py san lun_group add_luns`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san lun_group create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san lun_group delete`

- [ ] **san list**
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

#### 3.4 mapping_view 子主题

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san mapping_view create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san mapping_view delete`

- [ ] **san list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san mapping_view list`

- [ ] **san query**
  - 描述: query
  - 命令: `python scripts/dme_cli.py san mapping_view query`

#### 4.5 physical_host 子主题

- [ ] **san add_initiators**
  - 描述: add_initiators
  - 命令: `python scripts/dme_cli.py san physical_host add_initiators`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san physical_host create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san physical_host delete`

- [ ] **san list**
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

#### 5.6 physical_host_group 子主题

- [ ] **san add_hosts**
  - 描述: add_hosts
  - 命令: `python scripts/dme_cli.py san physical_host_group add_hosts`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san physical_host_group create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san physical_host_group delete`

- [ ] **san list**
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

#### 6.7 port_group 子主题

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san port_group create`

- [ ] **san list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san port_group list`

- [ ] **san show_ports**
  - 描述: show_ports
  - 命令: `python scripts/dme_cli.py san port_group show_ports`

- [ ] **san show_relations**
  - 描述: show_relations
  - 命令: `python scripts/dme_cli.py san port_group show_relations`

#### 7.8 storage_host 子主题

- [ ] **san batch_query**
  - 描述: batch_query
  - 命令: `python scripts/dme_cli.py san storage_host batch_query`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san storage_host create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san storage_host delete`

- [ ] **san list**
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

#### 8.9 storage_host_group 子主题

- [ ] **san add_hosts**
  - 描述: add_hosts
  - 命令: `python scripts/dme_cli.py san storage_host_group add_hosts`

- [ ] **san create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py san storage_host_group create`

- [ ] **san delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py san storage_host_group delete`

- [ ] **san list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py san storage_host_group list`

- [ ] **san remove_hosts**
  - 描述: remove_hosts
  - 命令: `python scripts/dme_cli.py san storage_host_group remove_hosts`

- [ ] **san show_luns**
  - 描述: show_luns
  - 命令: `python scripts/dme_cli.py san storage_host_group show_luns`

### 11. self_service 主题

#### 1.2 lun 子主题

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

#### 2.3 project 子主题

- [ ] **self_service list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py self_service project list`

- [ ] **self_service show_tiers**
  - 描述: show_tiers
  - 命令: `python scripts/dme_cli.py self_service project show_tiers`

#### 3.4 tier 子主题

- [ ] **self_service list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py self_service tier list`

- [ ] **self_service show_projects**
  - 描述: show_projects
  - 命令: `python scripts/dme_cli.py self_service tier show_projects`

### 12. server 主题

#### 1.2 cpu 子主题

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server cpu list`

#### 2.3 disk 子主题

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server disk list`

#### 3.4 fan 子主题

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server fan list`

#### 4.5 memory 子主题

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server memory list`

#### 5.6 nic 子主题

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server nic list`

#### 6.7 pcie_card 子主题

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server pcie_card list`

#### 7.8 power 子主题

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server power list`

#### 8.9 raid_card 子主题

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server raid_card list`

#### 9.1 直接动作

- [ ] **server list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py server list`

- [ ] **server show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py server show`

### 13. storage 主题

#### 1.2 account 子主题

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

#### 2.3 app_type 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage app_type list`

#### 3.4 bbu 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage bbu list`

#### 4.5 controller 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage controller list`

#### 5.6 disk 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage disk list`

#### 6.7 disk_pool 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage disk_pool list`

#### 7.8 enclosure 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage enclosure list`

#### 8.9 failover_group 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage failover_group list`

- [ ] **storage show_ports**
  - 描述: show_ports
  - 命令: `python scripts/dme_cli.py storage failover_group show_ports`

- [ ] **storage show_vlans**
  - 描述: show_vlans
  - 命令: `python scripts/dme_cli.py storage failover_group show_vlans`

#### 9.10 fan 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage fan list`

#### 10.11 hyperscale_pool 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage hyperscale_pool list`

#### 11.12 initiator 子主题

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage initiator delete`

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage initiator list`

- [ ] **storage modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py storage initiator modify`

#### 12.13 logic_port 子主题

- [ ] **storage create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py storage logic_port create`

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage logic_port delete`

- [ ] **storage failback**
  - 描述: failback
  - 命令: `python scripts/dme_cli.py storage logic_port failback`

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage logic_port list`

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage logic_port show`

- [ ] **storage update**
  - 描述: update
  - 命令: `python scripts/dme_cli.py storage logic_port update`

#### 13.14 node 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage node list`

#### 14.15 pool 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage pool list`

#### 15.16 port 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage port list`

- [ ] **storage show_bond_members**
  - 描述: show_bond_members
  - 命令: `python scripts/dme_cli.py storage port show_bond_members`

#### 16.17 power 子主题

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage power show`

#### 17.18 psu 子主题

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage psu list`

#### 18.19 qos 子主题

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

- [ ] **storage list**
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

#### 19.20 token 子主题

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage token show`

#### 20.21 vlan 子主题

- [ ] **storage create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py storage vlan create`

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage vlan delete`

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage vlan list`

- [ ] **storage modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py storage vlan modify`

#### 21.22 vstore 子主题

- [ ] **storage create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py storage vstore create`

- [ ] **storage delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py storage vstore delete`

- [ ] **storage list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py storage vstore list`

- [ ] **storage modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py storage vstore modify`

- [ ] **storage show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py storage vstore show`

#### 22.1 直接动作

- [ ] **storage add**
  - 描述: add
  - 命令: `python scripts/dme_cli.py storage add`

- [ ] **storage list**
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

### 14. system 主题

#### 1.2 az 子主题

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system az list`

#### 2.3 backup_server 子主题

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system backup_server list`

#### 3.4 dc 子主题

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system dc list`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system dc show`

- [ ] **system show_devices**
  - 描述: show_devices
  - 命令: `python scripts/dme_cli.py system dc show_devices`

#### 4.5 role 子主题

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system role list`

#### 5.6 tag 子主题

- [ ] **system bind**
  - 描述: bind
  - 命令: `python scripts/dme_cli.py system tag bind`

- [ ] **system create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py system tag create`

- [ ] **system delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py system tag delete`

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system tag list`

- [ ] **system modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py system tag modify`

- [ ] **system unbind**
  - 描述: unbind
  - 命令: `python scripts/dme_cli.py system tag unbind`

#### 6.7 tag_type 子主题

- [ ] **system create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py system tag_type create`

- [ ] **system delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py system tag_type delete`

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system tag_type list`

- [ ] **system modify**
  - 描述: modify
  - 命令: `python scripts/dme_cli.py system tag_type modify`

#### 7.8 task 子主题

- [ ] **system list**
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

#### 8.9 todo_task 子主题

- [ ] **system audit**
  - 描述: audit
  - 命令: `python scripts/dme_cli.py system todo_task audit`

- [ ] **system close**
  - 描述: close
  - 命令: `python scripts/dme_cli.py system todo_task close`

- [ ] **system execute**
  - 描述: execute
  - 命令: `python scripts/dme_cli.py system todo_task execute`

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system todo_task list`

- [ ] **system revoke**
  - 描述: revoke
  - 命令: `python scripts/dme_cli.py system todo_task revoke`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system todo_task show`

#### 9.10 todo_task_group 子主题

- [ ] **system confirm**
  - 描述: confirm
  - 命令: `python scripts/dme_cli.py system todo_task_group confirm`

- [ ] **system execute**
  - 描述: execute
  - 命令: `python scripts/dme_cli.py system todo_task_group execute`

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system todo_task_group list`

#### 10.11 user 子主题

- [ ] **system create**
  - 描述: create
  - 命令: `python scripts/dme_cli.py system user create`

- [ ] **system delete**
  - 描述: delete
  - 命令: `python scripts/dme_cli.py system user delete`

- [ ] **system list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py system user list`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system user show`

#### 11.1 直接动作

- [ ] **system certificate**
  - 描述: certificate
  - 命令: `python scripts/dme_cli.py system certificate`

- [ ] **system login**
  - 描述: login
  - 命令: `python scripts/dme_cli.py system login`

- [ ] **system logout**
  - 描述: logout
  - 命令: `python scripts/dme_cli.py system logout`

- [ ] **system show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py system show`

### 15. virtualization 主题

#### 1.1 直接动作

- [ ] **virtualization cluster list**
  - 描述: cluster list
  - 命令: `python scripts/dme_cli.py virtualization cluster list`

- [ ] **virtualization cluster show**
  - 描述: cluster show
  - 命令: `python scripts/dme_cli.py virtualization cluster show`

- [ ] **virtualization datastore list**
  - 描述: datastore list
  - 命令: `python scripts/dme_cli.py virtualization datastore list`

- [ ] **virtualization datastore show**
  - 描述: datastore show
  - 命令: `python scripts/dme_cli.py virtualization datastore show`

- [ ] **virtualization disk list**
  - 描述: disk list
  - 命令: `python scripts/dme_cli.py virtualization disk list`

- [ ] **virtualization host adapter_list**
  - 描述: host adapter_list
  - 命令: `python scripts/dme_cli.py virtualization host adapter_list`

- [ ] **virtualization host list**
  - 描述: host list
  - 命令: `python scripts/dme_cli.py virtualization host list`

- [ ] **virtualization host show**
  - 描述: host show
  - 命令: `python scripts/dme_cli.py virtualization host show`

- [ ] **virtualization site list**
  - 描述: site list
  - 命令: `python scripts/dme_cli.py virtualization site list`

- [ ] **virtualization site show**
  - 描述: site show
  - 命令: `python scripts/dme_cli.py virtualization site show`

- [ ] **virtualization vdisk list**
  - 描述: vdisk list
  - 命令: `python scripts/dme_cli.py virtualization vdisk list`

- [ ] **virtualization vdisk show**
  - 描述: vdisk show
  - 命令: `python scripts/dme_cli.py virtualization vdisk show`

- [ ] **virtualization vm list**
  - 描述: vm list
  - 命令: `python scripts/dme_cli.py virtualization vm list`

- [ ] **virtualization vm show**
  - 描述: vm show
  - 命令: `python scripts/dme_cli.py virtualization vm show`

### 16. workflow 主题

#### 1.2 instance 子主题

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

#### 2.3 template 子主题

- [ ] **workflow groups**
  - 描述: groups
  - 命令: `python scripts/dme_cli.py workflow template groups`

- [ ] **workflow list**
  - 描述: list
  - 命令: `python scripts/dme_cli.py workflow template list`

- [ ] **workflow show**
  - 描述: show
  - 命令: `python scripts/dme_cli.py workflow template show`

#### 3.1 直接动作

- [ ] **workflow 直接动作**
  - 描述: 直接动作
  - 命令: `python scripts/dme_cli.py workflow 直接动作`

## 测试执行统计

- 总主题数: 16
- 总测试用例数: 376
- 已执行用例: 0
- 未执行用例: 376
- 执行进度: 0%
