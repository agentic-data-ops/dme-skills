# Storage Domain Management Commands

Storage space management commands functionally involve the entire process of configuring and using storage space. Those commands can create and manage storage pools, create LUNs in storage pools, create mapping views, map LUNs to hosts for utilization, and configure the commands used by the SmartQoS functions.

## GUARANTEED_CAPACITY_INFO

- change effective_capacity general: modify the attributes of the effective capacity.
- show effective_capacity general: query information about the effective capacity.

## TGT

- change mapping general: modify mapping information.
- change mapping host_lun_id: modify IDs of mapped host LUNs.
- change tgt_switch map_foolproof: enable or disable the function of checking whether an operation object has I/Os during mapping removal.
- create mapping general: create a mapping.
- delete mapping general: delete a mapping.
- show mapping general: query mapping information.
- show mapping host_lun_id: query IDs of mapped host LUNs.
- show tgt_switch map_foolproof: query whether the the function of checking whether an operation object has I/Os during mapping removal is enabled or disabled.

## cifs_service

- change service cifs: modify the settings of the CIFS share service.
- change service cifs_config: change the CIFS common configuration.
- clear cifs connection: close the network connection of the specified client or server.
- show service cifs: query information about the CIFS share service.
- show service cifs_config: query the CIFS common configuration.

## disk_destroy_data

- change disk erase: erase data on disks. Data can be erased from only non-member disks or faulty member disks in a disk domain.

## disk_domain

- add disk_domain disk: add disks to a disk domain.
- change disk_domain general: modify the properties of a disk domain, including the disk domain name, hot spare strategy, switch status of the LUN mapping table repair function, and similarity-based deduplication execution level.
- change disk_domain rekey: manually update the AK according to the disk domain.
- create disk_domain: create a disk domain.
- delete disk_domain: delete a disk domain.
- show bst configuration: check the BST switch status.
- show disk_domain available_capacity: query the usable capacity of a specific RAID level in a disk domain.
- show disk_domain general: query information about disk domains.
- show disk_domain redundancy_recovery_task: query status of a redundancy recovery task in a disk domain.
- show disk_domain task: query the status of a reconstruction or pre-copy task in a disk domain.
- show disk_remove_task general: query the status of a capacity reduction task of a disk domain.

## file_system

- add hyper_cdp_schedule fs: add file systems to a HyperCDP schedule.
- change file_system enabled: enable file system related functions, such as to enable checksum, to perform periodic snapshots, and to modify the Atime.
- change file_system general: modify file system parameters such as the name, capacity, block size, and owning controller.
- create file_system general: create a file system.
- create fs_clone general: create a clone file system.
- delete file_system general: delete file systems.
- remove hyper_cdp_schedule fs: remove file systems from a HyperCDP schedule.
- show file_system general: query details about file systems.
- show file_system reduction_info: query capacity reduction information about a file system.
- show fs_clone general: query information about a file system's child clone file system, including its ID, name, status, and associated parent file system snapshot name.
- show hyper_cdp_schedule fs: query information about file systems in a HyperCDP schedule.

## host

- add host initiator: add an initiator to a host.
- change host: modify the attributes of a host, including the host name, location, operating system type, and IP address.
- change host_auto_scan: enable or disable the automatic scan function of a host.
- create host: **create host**s.
- delete host: **delete host**s.
- remove host initiator: remove initiators from a host.
- scan host: scan for application servers where UltraPath is installed.
- show host general: query the information on hosts.
- show host host_group: query information about the host group that is associated with a host.
- show host link: query details on host links configured for the storage system.
- show host lun: query all the LUNs that have been mapped to hosts in the storage system.
- show host mapping_view: query mapping views of a host.
- show host snapshot: query all the snapshots in the storage system that have been mapped to hosts.
- show host_auto_scan: check whether the automatic scan of a host is enabled.
- show lun host: query the host to which a LUN is mapped.

## host_group

- add host_group host: add hosts to a host group.
- change host_group general: change the name of a host group.
- create host_group: create a host group.
- delete host_group: delete a host group.
- remove host_group host: remove a specified host from a host group.
- show host_group general: query basic information about host groups.
- show host_group host: query information about hosts in a host group.
- show host_group mapping_view: query information about a mapping view added to a host group.

## initiator

- add host nvme_over_roce_initiator: add an NVMe over RoCE initiator to a host.
- change initiator: modify the attributes associated with an initiator including the Challenge Handshake Authentication Protocol (CHAP) status, initiator alias, and multipathing mode. Also, it can be used to replace initiators.
- change iscsi initiator_name: change the name of an iSCSI initiator configured for the storage system.
- change iscsi initiator_name_v2: change the name of an iSCSI initiator configured for the storage system.
- change nvme_over_roce_initiator general: modify the attributes of an initiator, including its alias and NVMe qualified name (NQN), as well as replace an initiator.
- create initiator fc: create Fibre Channel initiators. You can enable hosts to access storage resources of the storage system using created initiators.
- create initiator iscsi: create Internet Small Computer System Interface (iSCSI) initiators. You can enable hosts to access storage resources of the storage system using created initiators.
- create nvme_over_roce_initiator general: create an NVMe over RoCE initiator so that a host can access the storage system resources through the initiator.
- delete initiator fc: delete Fibre Channel initiators. You can disable hosts from accessing the storage resources of the storage system by running this command.
- delete initiator iscsi: delete Internet Small Computer Systems Interface (iSCSI) initiators. You can disable hosts from accessing the storage resources of the storage system by running this command.
- delete nvme_over_roce_initiator general: delete an NVMe over RoCE initiator. After the deletion, the host can no longer access the storage system resources through the initiator.
- remove host nvme_over_roce_initiator: remove an NVMe over RoCE initiator from a host.
- show initiator: query details on host initiators configured for the storage system.
- show iscsi initiator_name: query the names of iSCSI initiators configured for the storage system.
- show iscsi initiator_name_v2: query the names of iSCSI initiators configured for the storage system.
- show nvme_over_roce_initiator general: query information about NVMe over RoCE initiators added to hosts in the storage system.
- show port nvme_over_roce_initiator: view the NVMe qualified name (NQN) information about all NVMe over RoCE initiators that are mapped to a port.

## lun

- add lun_consistency_group lun: add a member LUN to a specified LUN consistency group. Use this command if consistency management is required for LUNs.
- change lun: modify LUN settings, including the name and capacity.
- change lun_clone split: start and stop splitting a clone pair or modify the split speed of a clone pair.
- change lun_consistency_group general: modify the properties of a LUN consistency group.
- change lun_takeover disable_switch_path: forbid the specified LUN's paths to be switched back to the source array and to allow the LUN to be used as the source LUN for online takeover.
- change lun_takeover enhance_switch: set the enhanced masquerading switch of a specified LUN.
- change lun_takeover finish_switch_path: confirm that the host paths of the specified LUN have been switched to the paths between the host and the target disk array.
- change lun_workload_type general: modify the settings of an application type, including the name, I/O size, and so on.
- change workload_type general: modify parameters of an application type, including "name", "io_size", and so on.
- create lun: create LUNs. After creating a storage pool, you must divide its storage space into one or multiple LUNs so that resources can be more appropriately allocated to application servers.
- create lun_clone general: create clones. You can create an identical and usable point-in-time duplicate for a data object by running this command.
- create lun_consistency_group: create a LUN consistency group.
- create lun_takeover general: create takeover LUNs.
- create lun_workload_type general: create a workload type for LUNs. After creating a workload type, you can choose it when you are creating LUNs. Through this method the LUN space parameter can be reasonably set.
- create workload_type general: create an application type for LUNs or for file systems.
- delete lun: delete LUNs.
- delete lun_consistency_group: delete a LUN consistency group.
- delete lun_workload_type general: delete an application type.
- delete workload_type general: delete an application type.
- remove lun_consistency_group lun: remove a member LUN from a specified LUN consistency group. Use this command when consistency protection is not required for a specified LUN.
- remove lun_takeover general: delete the information about a takeover LUN.
- show disk_domain lun: query information about LUNs in a specified disk domain.
- show hyper_cdp_schedule lun: query information about LUNs in a HyperCDP schedule.
- show hyper_cdp_schedule lun_consistency_group: query information about LUN consistency groups in a HyperCDP schedule.
- show lun general: query information about LUNs in the storage system.
- show lun hyper_metro_pair: query information about LUNs for which HyperMetro is configured.
- show lun lun_group: query information about the LUN group that is associated with a LUN.
- show lun mapping_view: query information about a mapping view related to a specified LUN.
- show lun protection: query protect information about the specified LUNs of the storage system.
- show lun_clone available_lun: query the information about all LUNs that can serve as clone source LUNs.
- show lun_clone general: query clone information.
- show lun_consistency_group general: query information about LUN consistency groups in the storage system.
- show lun_consistency_group lun: query information about LUNs in a LUN consistency group.
- show lun_consistency_group snapshot_consistency_group: query information about snapshot consistency groups related to LUN consistency groups.
- show lun_takeover general: query information about takeover LUNs of the storage system.
- show lun_workload_type general: query information about application types in the storage system.
- show protect_group lun: query information about LUNs in a protection group.
- show workload_type general: query information about existing application types of the storage system.

## lun_group

- add lun_group lun: add LUNs to a specified LUN group.
- change lun_group: change the name of a LUN group.
- create lun_group: create a LUN group.
- delete lun_group: delete a specified LUN group.
- remove lun_group lun: remove LUNs from a specified LUN group.
- show lun_group general: query information about LUN groups.
- show lun_group lun: query information about LUNs in a specified LUN group.
- show lun_group mapping_view: query information about a mapping view related to a specified LUN group.
- show lun_group snapshot: query information about snapshots in a specified LUN group.

## mapping_view

- add mapping_view host_group: add a host group to a mapping view.
- add mapping_view lun_group: add a LUN group to a mapping view.
- add mapping_view port_group: add a port group to a mapping view.
- change mapping_view: modify the settings of a mapping view including the view name and the function switch for in-band commands. Also, it can be used to change the host LUN IDs of the LUNs in mapping_view.
- create mapping_view: create a mapping view.
- delete mapping_view: delete mapping views.
- remove mapping_view host_group: remove a host group from a mapping view.
- remove mapping_view lun_group: remove a LUN group from a mapping view.
- remove mapping_view port_group: remove a port group from a mapping view.
- show mapping_view general: query information about mapping views of a storage system.
- show mapping_view host_group: query host groups in a mapping view.
- show mapping_view lun_group: query LUN groups in a mapping view.
- show mapping_view port_group: query port groups in a mapping view.

## ndmp_service

- change service ndmp_config: modify NDMP configurations.
- change service ndmp_reset_password: reset the NDMP password.
- change service ndmp_restart_service: restart the NDMP service.
- change service ndmp_scanbus: execute the scanbus command.
- change service ndmp_user: change the NDMP user name and password.
- show service ndmp: view NDMP configurations.
- show service ndmp_tape: query information about an NDMP tape library.

## nfs_service

- change service nfs_config: modify the NFS common configuration.
- show service nfs_config: query the NFS common configuration.

## port_group

- add port_group port: add ports to a port group. The ID varies depending on a specific product.
- add rep_port_group port: add ports to a replication port group.
- change port_group general: change the name of a port group.
- change rep_port_group: modify the information about a replication port group.
- create port_group: create a port group.
- create rep_port_group: create a replication port group.
- delete port_group: delete a port group.
- delete rep_port_group: delete a replication port group.
- remove port_group port: remove a specified port from a port group.
- remove rep_port_group port: remove ports from a replication port group.
- show port_group general: query information about port groups.
- show port_group mapping_view: query information about a mapping view of a port group.
- show port_group port: query information about ports in a port group.
- show rep_port_group general: query information about replication port groups.
- show rep_port_group port: query information about ports in a replication port group.

## qos

- change smartqos_policy min_goal_reserved: modify the minimum performance of LUNs that have not been added to a lower limit guarantee policy.
- show smartqos_policy min_goal_reserved: query the minimum performance of LUNs that have not been added to a lower limit guarantee policy.

## quota

- change quota general: change a specified quota of a file system.
- create quota dtree: create a quota for a specified dtree.
- create quota file_system: create a quota for a file system.
- delete quota general: delete a quota of a file system, or a quota of a specified dtree.
- show quota general: query quotas.

## quota_tree

- change dtree: modify dtree information in a file system.
- create dtree general: create a dtree.
- delete dtree general: delete a dtree.
- show dtree count: query the number of dtrees.
- show dtree general: query information about dtrees.

## remote_resource

- scan remote_lun: scan for LUNs on a third-party storage system. When a LUN mapping is added to or deleted from a remote disk array, or an initiator is added to or deleted from a host group, you must manually run this command.
- show remote_lun count: query the number of LUNs in a remote device.
- show remote_lun general: query basic information about remote LUNs in a remote device.
- show remote_lun path: query information about the paths on a remote LUN.
- show remote_lun path_status: query the path that corresponds to the remote LUN in use.
- show remote_lun single_link: check whether a remote LUN in use is connected by a single link.
- show remote_lun status: query a remote LUN in use.
- show remote_replication available_file_system: query the information on available file system tasks.

## resource_user

- add identity_mapping rule: add user mapping rules.
- add unix_group_member: add a UNIX user to a UNIX group.
- add windows_group ad_group: add a domain user group to a Windows user group.
- add windows_group ad_user: add a domain user to a Windows user group.
- add windows_group windows_user: add a Windows user to a Windows user group.
- change identity_mapping config: change user mapping configurations.
- change identity_mapping rule: change user mapping rules.
- change unix_group general: change the configuration of a UNIX group.
- change unix_user general: change the configuration of a UNIX user.
- change windows_group general: change the configuration of a Windows user group.
- change windows_user general: change the configuration of a Windows user.
- change windows_user password: modify the password of a Windows user.
- change windows_user safe_strategy: change the password and login policies of the Windows user.
- clear identity_mapping cache: clear user mapping caches.
- clear identity_mapping config: clear user mapping configurations.
- create unix_group: create a UNIX group.
- create unix_user general: create a UNIX user.
- create windows_group general: create a Windows group.
- create windows_user general: create a Windows user.
- delete identity_mapping rule: delete the identity_mapping rule.
- delete unix_group: delete a UNIX group.
- delete unix_user: delete a UNIX user.
- delete windows_group: delete a Windows user group.
- delete windows_user: delete a Windows user.
- remove unix_group_member: remove a UNIX user from a UNIX group.
- remove windows_group ad_group: remove an AD domain user group from a Windows user group.
- remove windows_group ad_user: remove an AD domain user from a Windows user group.
- remove windows_group windows_user: remove an Windows user from a Windows user group.
- show identity_mapping config: check user mapping configurations.
- show identity_mapping mapped_user: check whether the user can be found after a mapping.
- show identity_mapping rule: check the identity_mapping rule.
- show unix_group count: query the number of UNIX groups.
- show unix_group general: query the information of UNIX groups.
- show unix_user count: query the number of UNIX users.
- show unix_user general: query the information of UNIX users.
- show windows_group ad_group: show information about AD domain user groups in a Windows user group.
- show windows_group ad_user: show information about AD domain users in a Windows user group.
- show windows_group count: query the number of Windows groups.
- show windows_group general: query information of Windows user groups.
- show windows_group windows_user: show information about Windows users in a Windows user group.
- show windows_user count: query the number of Windows users.
- show windows_user general: query information of Windows users.
- show windows_user safe_strategy: view the password and login policies of the Windows user.

## share

- change share cifs: modify CIFS share configurations.
- change share nfs: modify the configurations of an NFS share.
- change share_homedir_rule cifs: modify the mapping rule of a Homedir share.
- change share_permission cifs: change the type of a CIFS share permission.
- create share cifs: create a CIFS share.
- create share nfs: create an NFS share.
- create share_homedir_rule cifs: create a mapping rule for a Homedir share.
- create share_permission cifs: create a CIFS share permission.
- delete share cifs: delete a CIFS share.
- delete share nfs: delete an NFS share.
- delete share_homedir_rule cifs: delete a mapping rule from a Homedir share.
- delete share_permission cifs: delete a CIFS share permission.
- show share cifs: query a CIFS share.
- show share cifs_count: query the number of CIFS shares.
- show share nfs: query information about NFS shares.
- show share nfs_count: query the number of NFS shares.
- show share_homedir_rule cifs: view the mapping rules of a Homedir share.
- show share_homedir_rule cifs_count: view the number of mapping rules of a Homedir share.
- show share_permission cifs: query the permissions of a CIFS share.
- show share_permission cifs_count: query the number of CIFS share permissions.

## share_permission

- change share_permission nfs: modify NFS share permission settings.
- create share_permission nfs: create an NFS share permission.
- delete share_permission nfs: delete an NFS share permission.
- show share_permission nfs: query information about NFS share permissions.
- show share_permission nfs_count: query the number of NFS share permissions.

## smart_cache

- add smart_cache_partition file_system: add file systems to a SmartCache partition.
- add smart_cache_partition lun: add LUNs to a SmartCache partition.
- add smart_cache_pool: add disks to a specified SmartCache pool.
- change smart_cache_partition general: change the name of a SmartCache partition.
- change smart_cache_pool general: change the name of a SmartCache pool.
- change smart_cache_pool switch: enable or disable a SmartCache pool.
- create smart_cache_partition: create a SmartCache partition.
- create smart_cache_pool: create a SmartCache pool.
- delete smart_cache_partition: delete a SmartCache partition.
- delete smart_cache_pool: delete a SmartCache pool.
- remove smart_cache_partition file_system: remove file systems from a SmartCache partition.
- remove smart_cache_partition lun: remove LUNs from a SmartCache partition.
- show performance smart_cache_pool: query performance information about a SmartCache pool.
- show smart_cache_partition file_system: query file systems in a SmartCache partition.
- show smart_cache_partition general: query SmartCache partitions.
- show smart_cache_partition lun: query LUNs in a SmartCache partition.
- show smart_cache_pool general: query basic information about a SmartCache pool.
- show smart_cache_pool smart_cache_partition: query information about SmartCache partitions in a SmartCache pool.

## smart_migration

- change lun_migration: change the LUN migration properties.
- change lun_migration_pause: pause the LUN migration.
- change lun_migration_split consistency: split LUN migration tasks.
- change lun_migration_synchronize: start synchronization of the LUN migration.
- create lun_migration: create LUN migration.
- delete lun_migration: delete LUN migration tasks.
- show lun_migration count: calculate the number of migrated LUNs.
- show lun_migration general: query the attributes of LUN migration tasks.

## smart_qos

- add smartqos_policy file_system: add file systems to a SmartQoS policy.
- add smartqos_policy hierarchical: add normal SmartQoS policies to a specified hierarchical SmartQoS policy.
- add smartqos_policy lun: add logical unit numbers (LUNs) to a SmartQoS policy.
- add smartqos_policy lun_group: add LUN groups to a SmartQoS policy.
- change smartqos_policy enabled: enable or disable a specified SmartQoS policy.
- change smartqos_policy general: modify SmartQoS policies.
- change smartqos_policy normalized_io_switch: enable or disable normalized I/O conversion.
- create smartqos_policy: create SmartQoS policies. By using SmartQoS, the storage system can allocate its resources to different types of I/Os on demand.
- delete smartqos_policy: delete one or more specified SmartQoS policies.
- remove smartqos_policy hierarchical: remove normal SmartQoS policies from a specified hierarchical SmartQoS policy.
- remove smartqos_policy host: remove hosts from a specific SmartQoS policy.
- remove smartqos_policy lun: remove LUNs from a specific SmartQoS policy.
- remove smartqos_policy lun_group: remove LUN groups from a specific SmartQoS policy.
- show smartqos_policy file_system: query information about file systems in a specified SmartQoS policy.
- show smartqos_policy general: query details on existing SmartQoS policies of the storage system. By using SmartQoS, the storage system can allocate its resources to different types of I/Os on demand.
- show smartqos_policy hierarchical: query information about SmartQoS policies in a specified hierarchical SmartQoS policy.
- show smartqos_policy host: query information about hosts in a specified SmartQoS policy.
- show smartqos_policy lun: query information about LUNs in a specified SmartQoS policy.
- show smartqos_policy lun_group: query information about LUN groups in a specified SmartQoS policy.
- show smartqos_policy snapshot: query the snapshot information of the specified SmartQoS policy.

## smartqos

- add smartqos_policy host: add hosts to a SmartQoS policy.
- remove smartqos_policy file_system: remove file systems from a specific SmartQoS policy.
- show smartqos_policy normalized_io_switch: query the switch status of normalized I/O conversion.

## space

- add protect_group lun: add a member LUN to a specified protection group.
- change recycle_bin_policy: modify parameters related to the recycle bin policy.
- change protect_group: modify the parameters of a protection group.
- create protect_group: create a protection group.
- delete protect_group: delete specified protected groups.
- delete recycle_bin_view: delete objects from the recycle bin view.
- remove protect_group lun: remove a member LUN from a specified protected group.
- show lun protect_group: query the protection group associated with a LUN.
- show protect_group general: query information about a protection group.
- show recycle_bin_policy general: query the recycle bin configuration policy.
- show recycle_bin_view general: query object information in the recycle bin view.

## storage_pool

- add storage_pool disk: add disks to a storage pool.
- change storage_pool general: modify the attributes of a storage pool, including the name, capacity alarm threshold, capacity exhaustion threshold, capacity, provisioning limit, low threshold of protection capacity, high threshold of protection capacity, and automatic deletion switch.
- create storage_pool: create a storage pool.
- delete storage_pool: delete a specified storage pool.
- show storage_pool general: query information about storage pools.

## vstore

- change vstore info: modify the basic information about a vStore.
- change vstore view: enter the view of a vStore.
- create vstore general: create a vStore.
- delete vstore general: delete a vStore.
- show vstore: query the states of vStores.
