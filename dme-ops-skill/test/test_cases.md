# DME CLI 测试用例覆盖报告

## 测试环境准备

- [ ] 配置环境变量：`export DME_API_URL=<your-dme-api-url>`
- [ ] 配置认证信息：`export DME_USERNAME=<username>`
- [ ] 配置认证信息：`export DME_PASSWORD=<password>`
- [ ] 验证连接：`python scripts/dme_cli.py --list-topics`

---

## 主题覆盖统计

**总主题数**: 18
**总动作数**: 348

---

## 主题详细测试用例

### 1. aiops (AIOps 智能运维相关操作)

**子主题**: alarm, check_policy, check_result, diagnose_task, performance, topology, topology_fcsan, topology_graph, topology_ipsan, topology_lun, topology_vm

**动作总数**: 27

**测试用例生成命令**:
```bash
# 获取每个动作的帮助信息
python scripts/dme_cli.py aiops alarm list --help
python scripts/dme_cli.py aiops alarm ack --help
python scripts/dme_cli.py aiops alarm unack --help
python scripts/dme_cli.py aiops alarm clear --help
python scripts/dme_cli.py aiops check_policy list --help
python scripts/dme_cli.py aiops check_policy execute --help
python scripts/dme_cli.py aiops check_policy enable --help
python scripts/dme_cli.py aiops check_policy disable --help
python scripts/dme_cli.py aiops check_policy delete --help
python scripts/dme_cli.py aiops check_result list --help
python scripts/dme_cli.py aiops check_result show --help
python scripts/dme_cli.py aiops diagnose_task status --help
python scripts/dme_cli.py aiops performance create_collect_task --help
python scripts/dme_cli.py aiops performance download_collect_result --help
python scripts/dme_cli.py aiops performance query --help
python scripts/dme_cli.py aiops performance show_indicators --help
python scripts/dme_cli.py aiops performance list_indicators --help
python scripts/dme_cli.py aiops performance list_object_types --help
python scripts/dme_cli.py aiops topology query_san_path --help
python scripts/dme_cli.py aiops topology query_luns --help
python scripts/dme_cli.py aiops topology query_vms --help
python scripts/dme_cli.py aiops topology query_graph_path --help
python scripts/dme_cli.py aiops topology_fcsan query --help
python scripts/dme_cli.py aiops topology_ipsan query --help
python scripts/dme_cli.py aiops topology_lun list --help
python scripts/dme_cli.py aiops topology_vm list --help
python scripts/dme_cli.py aiops topology_graph query --help
```

### 2. backup (数据备份管理)

**子主题**: cluster

**动作总数**: 3

**测试用例生成命令**:
```bash
python scripts/dme_cli.py backup cluster list --help
python scripts/dme_cli.py backup cluster capacity --help
python scripts/dme_cli.py backup cluster quota --help
```

### 3. cmdb (CMDB 配置管理)

**子主题**: class, instance, relation

**动作总数**: 6

**测试用例生成命令**:
```bash
python scripts/dme_cli.py cmdb class list --help
python scripts/dme_cli.py cmdb class show --help
python scripts/dme_cli.py cmdb instance list --help
python scripts/dme_cli.py cmdb instance show --help
python scripts/dme_cli.py cmdb relation list --help
python scripts/dme_cli.py cmdb relation show --help
```

### 4. fc_switch (FC 光纤交换机)

**子主题**: alias, controller, fabric, port, vsan, zone

**动作总数**: 19

**测试用例生成命令**:
```bash
python scripts/dme_cli.py fc_switch alias list --help
python scripts/dme_cli.py fc_switch alias create --help
python scripts/dme_cli.py fc_switch alias modify --help
python scripts/dme_cli.py fc_switch alias delete --help
python scripts/dme_cli.py fc_switch alias show_members --help
python scripts/dme_cli.py fc_switch controller list --help
python scripts/dme_cli.py fc_switch fabric list --help
python scripts/dme_cli.py fc_switch fabric backup --help
python scripts/dme_cli.py fc_switch fabric show_ports --help
python scripts/dme_cli.py fc_switch port list --help
python scripts/dme_cli.py fc_switch vsan list --help
python scripts/dme_cli.py fc_switch zone list --help
python scripts/dme_cli.py fc_switch zone create --help
python scripts/dme_cli.py fc_switch zone modify --help
python scripts/dme_cli.py fc_switch zone delete --help
python scripts/dme_cli.py fc_switch zone show_members --help
python scripts/dme_cli.py fc_switch zone batch_create --help
```

### 5. gfs (GFS 全局文件系统)

**子主题**: dataspace, migration_task, namespace

**动作总数**: 14

**测试用例生成命令**:
```bash
python scripts/dme_cli.py gfs dataspace list --help
python scripts/dme_cli.py gfs dataspace show --help
python scripts/dme_cli.py gfs dataspace site_list --help
python scripts/dme_cli.py gfs migration_task list --help
python scripts/dme_cli.py gfs migration_task create --help
python scripts/dme_cli.py gfs migration_task modify --help
python scripts/dme_cli.py gfs migration_task show --help
python scripts/dme_cli.py gfs migration_task operate --help
python scripts/dme_cli.py gfs migration_task delete --help
python scripts/dme_cli.py gfs namespace list --help
python scripts/dme_cli.py gfs namespace create --help
python scripts/dme_cli.py gfs namespace modify --help
python scripts/dme_cli.py gfs namespace show --help
python scripts/dme_cli.py gfs namespace delete --help
```

### 6. health (健康度)

**子主题**: data, score

**动作总数**: 3

**测试用例生成命令**:
```bash
python scripts/dme_cli.py health data query --help
python scripts/dme_cli.py health score list --help
python scripts/dme_cli.py health score detail --help
```

### 7. ip_switch (IP 交换机)

**子主题**: board, fan, frame, port, power, subcard

**动作总数**: 6

**测试用例生成命令**:
```bash
python scripts/dme_cli.py ip_switch board list --help
python scripts/dme_cli.py ip_switch fan list --help
python scripts/dme_cli.py ip_switch frame list --help
python scripts/dme_cli.py ip_switch port list --help
python scripts/dme_cli.py ip_switch power list --help
python scripts/dme_cli.py ip_switch subcard list --help
```

### 8. kubernetes (Kubernetes)

**子主题**: cluster, namespace, node, pod, pv, pvc

**动作总数**: 6

**测试用例生成命令**:
```bash
python scripts/dme_cli.py kubernetes cluster list --help
python scripts/dme_cli.py kubernetes namespace list --help
python scripts/dme_cli.py kubernetes node list --help
python scripts/dme_cli.py kubernetes pod list --help
python scripts/dme_cli.py kubernetes pv list --help
python scripts/dme_cli.py kubernetes pvc list --help
```

### 9. nas (NAS)

**子主题**: cifs_share, dataturbo_share, dpc, dtree, filesystem, namespace, nfs_share, quota

**动作总数**: 42

**测试用例生成命令**:
```bash
python scripts/dme_cli.py nas cifs_share list --help
python scripts/dme_cli.py nas cifs_share create --help
python scripts/dme_cli.py nas cifs_share modify --help
python scripts/dme_cli.py nas cifs_share delete --help
python scripts/dme_cli.py nas cifs_share show --help
python scripts/dme_cli.py nas cifs_share show_permissions --help
python scripts/dme_cli.py nas dataturbo_share list --help
python scripts/dme_cli.py nas dataturbo_share create --help
python scripts/dme_cli.py nas dataturbo_share modify --help
python scripts/dme_cli.py nas dataturbo_share delete --help
python scripts/dme_cli.py nas dataturbo_share show --help
python scripts/dme_cli.py nas dataturbo_share show_permissions --help
python scripts/dme_cli.py nas dpc list --help
python scripts/dme_cli.py nas dpc show --help
python scripts/dme_cli.py nas dtree list --help
python scripts/dme_cli.py nas dtree create --help
python scripts/dme_cli.py nas dtree modify --help
python scripts/dme_cli.py nas dtree show --help
python scripts/dme_cli.py nas dtree delete --help
python scripts/dme_cli.py nas filesystem list --help
python scripts/dme_cli.py nas filesystem create --help
python scripts/dme_cli.py nas filesystem modify --help
python scripts/dme_cli.py nas filesystem query_available --help
python scripts/dme_cli.py nas filesystem show --help
python scripts/dme_cli.py nas filesystem delete --help
python scripts/dme_cli.py nas filesystem batch_modify --help
python scripts/dme_cli.py nas namespace list --help
python scripts/dme_cli.py nas namespace create --help
python scripts/dme_cli.py nas namespace modify --help
python scripts/dme_cli.py nas namespace show --help
python scripts/dme_cli.py nas namespace delete --help
python scripts/dme_cli.py nas nfs_share list --help
python scripts/dme_cli.py nas nfs_share create --help
python scripts/dme_cli.py nas nfs_share modify --help
python scripts/dme_cli.py nas nfs_share delete --help
python scripts/dme_cli.py nas nfs_share show --help
python scripts/dme_cli.py nas quota list --help
python scripts/dme_cli.py nas quota create --help
python scripts/dme_cli.py nas quota modify --help
python scripts/dme_cli.py nas quota show --help
python scripts/dme_cli.py nas quota delete --help
```

### 10. protection (保护策略)

**子主题**: clone_group, device_pair, group, hypermetro_domain, hypermetro_group, hypermetro_pair, replication_group, replication_link, replication_pair, snapshot, snapshot_group

**动作总数**: 37

**测试用例生成命令**:
```bash
python scripts/dme_cli.py protection clone_group create --help
python scripts/dme_cli.py protection clone_group delete --help
python scripts/dme_cli.py protection clone_group sync --help
python scripts/dme_cli.py protection device_pair list --help
python scripts/dme_cli.py protection group list --help
python scripts/dme_cli.py protection group create --help
python scripts/dme_cli.py protection group modify --help
python scripts/dme_cli.py protection group delete --help
python scripts/dme_cli.py protection group add_luns --help
python scripts/dme_cli.py protection group remove_luns --help
python scripts/dme_cli.py protection hypermetro_domain list --help
python scripts/dme_cli.py protection hypermetro_group list --help
python scripts/dme_cli.py protection hypermetro_group create --help
python scripts/dme_cli.py protection hypermetro_group modify --help
python scripts/dme_cli.py protection hypermetro_group delete --help
python scripts/dme_cli.py protection hypermetro_group pause --help
python scripts/dme_cli.py protection hypermetro_group switch_priority --help
python scripts/dme_cli.py protection hypermetro_group force_startup --help
python scripts/dme_cli.py protection hypermetro_group add_pairs --help
python scripts/dme_cli.py protection hypermetro_group remove_pairs --help
python scripts/dme_cli.py protection hypermetro_pair list --help
python scripts/dme_cli.py protection hypermetro_pair create --help
python scripts/dme_cli.py protection hypermetro_pair modify --help
python scripts/dme_cli.py protection hypermetro_pair delete --help
python scripts/dme_cli.py protection hypermetro_pair sync --help
python scripts/dme_cli.py protection hypermetro_pair pause --help
python scripts/dme_cli.py protection hypermetro_pair switch_priority --help
python scripts/dme_cli.py protection hypermetro_pair force_startup --help
python scripts/dme_cli.py protection replication_group list --help
python scripts/dme_cli.py protection replication_group create --help
python scripts/dme_cli.py protection replication_group modify --help
python scripts/dme_cli.py protection replication_group delete --help
python scripts/dme_cli.py protection replication_group sync --help
python scripts/dme_cli.py protection replication_group split --help
python scripts/dme_cli.py protection replication_group switch --help
python scripts/dme_cli.py protection replication_group switch_write_protection --help
python scripts/dme_cli.py protection replication_group add_pairs --help
python scripts/dme_cli.py protection replication_group remove_pairs --help
python scripts/dme_cli.py protection replication_link list --help
python scripts/dme_cli.py protection replication_pair list --help
python scripts/dme_cli.py protection replication_pair create --help
python scripts/dme_cli.py protection replication_pair modify --help
python scripts/dme_cli.py protection replication_pair delete --help
python scripts/dme_cli.py protection replication_pair sync --help
python scripts/dme_cli.py protection replication_pair split --help
python scripts/dme_cli.py protection replication_pair switch --help
python scripts/dme_cli.py protection replication_pair switch_write_protection --help
python scripts/dme_cli.py protection snapshot list --help
python scripts/dme_cli.py protection snapshot create --help
python scripts/dme_cli.py protection snapshot delete --help
python scripts/dme_cli.py protection snapshot rollback --help
python scripts/dme_cli.py protection snapshot_group list --help
python scripts/dme_cli.py protection snapshot_group create --help
python scripts/dme_cli.py protection snapshot_group activate --help
python scripts/dme_cli.py protection snapshot_group deactivate --help
python scripts/dme_cli.py protection snapshot_group rollback --help
python scripts/dme_cli.py protection snapshot_group delete --help
```

### 11. san (SAN 存储区域网络)

**子主题**: lun, lun_group, mapping_view, physical_host, physical_host_group, port_group, storage_host, storage_host_group

**动作总数**: 60

**测试用例生成命令**:
```bash
python scripts/dme_cli.py san lun list --help
python scripts/dme_cli.py san lun show --help
python scripts/dme_cli.py san lun create --help
python scripts/dme_cli.py san lun modify --help
python scripts/dme_cli.py san lun delete --help
python scripts/dme_cli.py san lun modify_name --help
python scripts/dme_cli.py san lun expand --help
python scripts/dme_cli.py san lun connection --help
python scripts/dme_cli.py san lun mapping --help
python scripts/dme_cli.py san lun_group list --help
python scripts/dme_cli.py san lun_group show --help
python scripts/dme_cli.py san lun_group create --help
python scripts/dme_cli.py san lun_group delete --help
python scripts/dme_cli.py san lun_group add_luns --help
python scripts/dme_cli.py san lun_group remove_luns --help
python scripts/dme_cli.py san lun_group show_luns --help
python scripts/dme_cli.py san mapping_view list --help
python scripts/dme_cli.py san mapping_view create --help
python scripts/dme_cli.py san mapping_view delete --help
python scripts/dme_cli.py san mapping_view query --help
python scripts/dme_cli.py san physical_host list --help
python scripts/dme_cli.py san physical_host show --help
python scripts/dme_cli.py san physical_host create --help
python scripts/dme_cli.py san physical_host modify --help
python scripts/dme_cli.py san physical_host delete --help
python scripts/dme_cli.py san physical_host add_initiators --help
python scripts/dme_cli.py san physical_host remove_initiators --help
python scripts/dme_cli.py san physical_host show_initiators --help
python scripts/dme_cli.py san physical_host test --help
python scripts/dme_cli.py san physical_host query_sshkey --help
python scripts/dme_cli.py san physical_host save_sshkey --help
python scripts/dme_cli.py san physical_host query_by_initiator --help
python scripts/dme_cli.py san physical_host map_luns --help
python scripts/dme_cli.py san physical_host unmap_luns --help
python scripts/dme_cli.py san physical_host_group list --help
python scripts/dme_cli.py san physical_host_group show --help
python scripts/dme_cli.py san physical_host_group create --help
python scripts/dme_cli.py san physical_host_group modify --help
python scripts/dme_cli.py san physical_host_group delete --help
python scripts/dme_cli.py san physical_host_group add_hosts --help
python scripts/dme_cli.py san physical_host_group remove_hosts --help
python scripts/dme_cli.py san physical_host_group map_luns --help
python scripts/dme_cli.py san physical_host_group unmap_luns --help
python scripts/dme_cli.py san port_group list --help
python scripts/dme_cli.py san port_group create --help
python scripts/dme_cli.py san port_group show_ports --help
python scripts/dme_cli.py san port_group show_relations --help
python scripts/dme_cli.py san storage_host batch_query --help
python scripts/dme_cli.py san storage_host create --help
python scripts/dme_cli.py san storage_host list --help
python scripts/dme_cli.py san storage_host modify --help
python scripts/dme_cli.py san storage_host delete --help
python scripts/dme_cli.py san storage_host show_paths --help
python scripts/dme_cli.py san storage_host show_luns --help
python scripts/dme_cli.py san storage_host_group list --help
python scripts/dme_cli.py san storage_host_group create --help
python scripts/dme_cli.py san storage_host_group add_hosts --help
python scripts/dme_cli.py san storage_host_group remove_hosts --help
python scripts/dme_cli.py san storage_host_group delete --help
python scripts/dme_cli.py san storage_host_group show_luns --help
```

### 12. self_service (自助服务)

**子主题**: lun, project, tier

**动作总数**: 10

**测试用例生成命令**:
```bash
python scripts/dme_cli.py self_service lun create --help
python scripts/dme_cli.py self_service lun bind_project --help
python scripts/dme_cli.py self_service lun unbind_project --help
python scripts/dme_cli.py self_service lun bind_tier --help
python scripts/dme_cli.py self_service lun unbind_tier --help
python scripts/dme_cli.py self_service lun change_tier --help
python scripts/dme_cli.py self_service project list --help
python scripts/dme_cli.py self_service project show_tiers --help
python scripts/dme_cli.py self_service tier list --help
python scripts/dme_cli.py self_service tier show_projects --help
```

### 13. server (服务器管理)

**子主题**: cpu, disk, fan, memory, nic, pcie_card, power, raid_card

**动作总数**: 8

**测试用例生成命令**:
```bash
python scripts/dme_cli.py server cpu list --help
python scripts/dme_cli.py server disk list --help
python scripts/dme_cli.py server fan list --help
python scripts/dme_cli.py server memory list --help
python scripts/dme_cli.py server nic list --help
python scripts/dme_cli.py server pcie_card list --help
python scripts/dme_cli.py server power list --help
python scripts/dme_cli.py server raid_card list --help
```

### 14. storage (存储设备)

**子主题**: account, app_type, bbu, controller, disk, disk_pool, enclosure, failover_group, fan, hyperscale_pool, initiator, logic_port, node, pool, port, power, psu, qos, token, vlan, vstore

**动作总数**: 45

**测试用例生成命令**:
```bash
python scripts/dme_cli.py storage account show_local_users --help
python scripts/dme_cli.py storage account show_local_user_groups --help
python scripts/dme_cli.py storage account show_unix_users --help
python scripts/dme_cli.py storage account show_unix_user_groups --help
python scripts/dme_cli.py storage account show_windows_users --help
python scripts/dme_cli.py storage account show_windows_user_groups --help
python scripts/dme_cli.py storage account show_dataturbo_admin_users --help
python scripts/dme_cli.py storage app_type list --help
python scripts/dme_cli.py storage bbu list --help
python scripts/dme_cli.py storage controller list --help
python scripts/dme_cli.py storage disk list --help
python scripts/dme_cli.py storage disk_pool list --help
python scripts/dme_cli.py storage enclosure list --help
python scripts/dme_cli.py storage failover_group list --help
python scripts/dme_cli.py storage failover_group show_ports --help
python scripts/dme_cli.py storage failover_group show_vlans --help
python scripts/dme_cli.py storage fan list --help
python scripts/dme_cli.py storage hyperscale_pool list --help
python scripts/dme_cli.py storage initiator list --help
python scripts/dme_cli.py storage initiator modify --help
python scripts/dme_cli.py storage initiator delete --help
python scripts/dme_cli.py storage logic_port list --help
python scripts/dme_cli.py storage logic_port create --help
python scripts/dme_cli.py storage logic_port show --help
python scripts/dme_cli.py storage logic_port update --help
python scripts/dme_cli.py storage logic_port failback --help
python scripts/dme_cli.py storage logic_port delete --help
python scripts/dme_cli.py storage node list --help
python scripts/dme_cli.py storage pool list --help
python scripts/dme_cli.py storage port list --help
python scripts/dme_cli.py storage port show_bond_members --help
python scripts/dme_cli.py storage power show --help
python scripts/dme_cli.py storage psu list --help
python scripts/dme_cli.py storage qos list --help
python scripts/dme_cli.py storage qos create --help
python scripts/dme_cli.py storage qos modify --help
python scripts/dme_cli.py storage qos show --help
python scripts/dme_cli.py storage qos activate --help
python scripts/dme_cli.py storage qos deactivate --help
python scripts/dme_cli.py storage qos associate --help
python scripts/dme_cli.py storage qos unassociate --help
python scripts/dme_cli.py storage qos delete --help
python scripts/dme_cli.py storage token show --help
python scripts/dme_cli.py storage vlan list --help
python scripts/dme_cli.py storage vlan create --help
python scripts/dme_cli.py storage vlan modify --help
python scripts/dme_cli.py storage vlan delete --help
python scripts/dme_cli.py storage vstore list --help
python scripts/dme_cli.py storage vstore create --help
python scripts/dme_cli.py storage vstore modify --help
python scripts/dme_cli.py storage vstore show --help
python scripts/dme_cli.py storage vstore delete --help
```

### 15. system (系统管理)

**子主题**: az, backup_server, dc, role, tag, tag_type, task, todo_task, todo_task_group, user

**动作总数**: 23

**测试用例生成命令**:
```bash
python scripts/dme_cli.py system az list --help
python scripts/dme_cli.py system backup_server list --help
python scripts/dme_cli.py system dc list --help
python scripts/dme_cli.py system dc show --help
python scripts/dme_cli.py system dc show_devices --help
python scripts/dme_cli.py system role list --help
python scripts/dme_cli.py system tag list --help
python scripts/dme_cli.py system tag create --help
python scripts/dme_cli.py system tag modify --help
python scripts/dme_cli.py system tag delete --help
python scripts/dme_cli.py system tag bind --help
python scripts/dme_cli.py system tag unbind --help
python scripts/dme_cli.py system tag_type list --help
python scripts/dme_cli.py system tag_type create --help
python scripts/dme_cli.py system tag_type modify --help
python scripts/dme_cli.py system tag_type delete --help
python scripts/dme_cli.py system task list --help
python scripts/dme_cli.py system task show --help
python scripts/dme_cli.py system task wait --help
python scripts/dme_cli.py system task retry --help
python scripts/dme_cli.py system todo_task list --help
python scripts/dme_cli.py system todo_task show --help
python scripts/dme_cli.py system todo_task execute --help
python scripts/dme_cli.py system todo_task audit --help
python scripts/dme_cli.py system todo_task revoke --help
python scripts/dme_cli.py system todo_task close --help
python scripts/dme_cli.py system todo_task_group list --help
python scripts/dme_cli.py system todo_task_group execute --help
python scripts/dme_cli.py system todo_task_group confirm --help
python scripts/dme_cli.py system user list --help
python scripts/dme_cli.py system user show --help
python scripts/dme_cli.py system user create --help
python scripts/dme_cli.py system user delete --help
```

### 16. virtualization (虚拟化服务)

**子主题**: 无（全部为直接动作）

**动作总数**: 13

**测试用例生成命令**:
```bash
python scripts/dme_cli.py virtualization cluster list --help
python scripts/dme_cli.py virtualization cluster show --help
python scripts/dme_cli.py virtualization datastore list --help
python scripts/dme_cli.py virtualization datastore show --help
python scripts/dme_cli.py virtualization disk list --help
python scripts/dme_cli.py virtualization host list --help
python scripts/dme_cli.py virtualization host show --help
python scripts/dme_cli.py virtualization host adapter_list --help
python scripts/dme_cli.py virtualization site list --help
python scripts/dme_cli.py virtualization site show --help
python scripts/dme_cli.py virtualization vm list --help
python scripts/dme_cli.py virtualization vm show --help
python scripts/dme_cli.py virtualization vdisk list --help
python scripts/dme_cli.py virtualization vdisk show --help
```

### 17. workflow (工作流)

**子主题**: instance, template

**动作总数**: 7

**测试用例生成命令**:
```bash
python scripts/dme_cli.py workflow instance create --help
python scripts/dme_cli.py workflow instance show --help
python scripts/dme_cli.py workflow instance step_log --help
python scripts/dme_cli.py workflow instance stop --help
python scripts/dme_cli.py workflow template list --help
python scripts/dme_cli.py workflow template show --help
python scripts/dme_cli.py workflow template groups --help
```

### 18. pool (存储池)

**动作**: list, show (作为直接动作)

**动作总数**: 2

**测试用例生成命令**:
```bash
python scripts/dme_cli.py pool list --help
python scripts/dme_cli.py pool show --help
```

---

## 自动化测试脚本

使用以下脚本自动生成详细的测试用例：

```bash
#!/bin/bash
# generate_test_cases.sh

cd /workspace/projects/dme-skills/dme-ops-skill

# 主题列表
topics=("aiops" "backup" "cmdb" "fc_switch" "gfs" "health" "ip_switch" "kubernetes" "nas" "protection" "san" "self_service" "server" "storage" "system" "virtualization" "workflow" "pool")

# 为每个主题生成测试用例
for topic in "${topics[@]}"; do
    echo "=== 生成 $topic 测试用例 ==="
    
    # 获取主题帮助
    python scripts/dme_cli.py $topic --help > "test/${topic}_help.txt"
    
    # 提取所有子主题和动作
    # 这里需要根据实际输出解析
done

echo "测试用例生成完成"
```

---

## 测试执行建议

1. **优先级排序**:
   - P0: 列表和查询类动作（list, show）
   - P1: 创建类动作（create）
   - P2: 修改类动作（modify）
   - P3: 删除类动作（delete）

2. **依赖关系**:
   - 先测试基础资源（pool, storage）
   - 再测试依赖资源（lun, filesystem）
   - 最后测试业务逻辑（mapping_view, backup）

3. **数据准备**:
   - 准备测试用的存储设备
   - 准备测试用的存储池
   - 准备测试用的LUN

---

## 测试结果记录模板

| 主题 | 子主题 | 动作 | 执行状态 | 执行时间 | 备注 |
|------|--------|------|----------|----------|------|
| san | lun | list | [ ] | | |
| san | lun | create | [ ] | | |
| ... | ... | ... | [ ] | | |

---

**文档版本**: 2.0  
**最后更新**: 2024年  
**总动作数**: 348
