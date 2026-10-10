# High-Risk Command List

The following commands are highly risky. An improper execution of any of the commands may interrupt ongoing services and cause storage system failures.When executing a command, carefully read the high-risk prompt that is displayed and execute the command as prompted.
Table 13-1 High-risk command list
| Format | Function |
|---|---|
| remove bond_port ipv6_address | The remove bond_port ipv6_address command is used to delete the IPv6 address of a bond port. |
| remove bond_port ipv4_route | The remove bond_port ipv4_route command is used to delete the IPv4 route of a host bond port. |
| remove bond_port ipv6_route | The remove bond_port ipv6_route command is used to delete the IPv6 route of a host bond port. |
| change bond_port ipv6_address | The change bond_port ipv6_address command is used to change the IPv6 address of the bond port. |
| change bond_port ipv4_address | The change bond_port ipv4_address command is used to change the IPv4 address of the bond port. |
| remove bond_port ipv4_address | The remove bond_port ipv4_address command is used to delete the IPv4 address of a bond port. |
| add bond_port ipv4_route | The add bond_port ipv4_route command is used to add an IPv4 route to the bond port. You can run this command to add a route to connect the storage system to the application server when their IPv4 addresses are not at the same network segment. |
| add bond_port ipv6_route | The add bond_port ipv6_route command is used to add an IPv6 route to the bond port. You can run this command to add a route to connect the storage system to the application server when their IPv6 addresses are not at the same network segment. |
| delete ssh known_hosts | The delete ssh known_hosts command is used to delete the server "known_hosts" file or a certain record in the file that is saved by the SSH client. |
| import ssh_host_key_file | The import ssh_host_key_file command is used to replace the public key file and private key file on the SSH server. |
| delete user | The delete user command is used to delete a user or user group. You can delete the users that are no longer required for managing and maintaining the storage system by running this command. |
| change user | The change user command is used to operate users, including resetting users' login passwords, changing user role IDs, forcing users offline, modifying a user's login method, modifying a user's authentication factors, and setting a specified user's password to never expire. |
| import weak_password_dictionary | The import weak_password_dictionary command is used to import and overwrite a complete weak password dictionary. |
| import license | The import license command is used to import license files. You can activate or update license files by running this command. |
| add smartqos_policy host | The add smartqos_policy host command is used to add hosts to a SmartQoS policy. |
| remove smartqos_policy file_system | The remove smartqos_policy file_system command is used to remove file systems from a specific SmartQoS policy. |
| change service ndmp_restart_service | The change service ndmp_restart_service command is used to restart the NDMP service. |
| change service ndmp_config | The change service ndmp_config command is used to modify NDMP configurations. |
| change service nfs_config | The change service nfs_config command is used to modify the NFS common configuration. |
| change disk erase | The change disk erase command is used to erase data on disks. Data can be erased from only non-member disks or faulty member disks in a disk domain. |
| delete protect_group | The delete protect_group command is used to delete specified protected groups. |
| change recycle_bin_policy | The change recycle_bin_policy command is used to modify parameters related to the recycle bin policy. |
| delete recycle_bin_view | The delete recycle_bin_view command is used to delete objects from the recycle bin view. |
| remove protect_group lun | The remove protect_group lun command is used to remove a member LUN from a specified protected group. |
| change disk_domain rekey | The change disk_domain rekey command is used to manually update the AK according to the disk domain. |
| delete disk_domain | The delete disk_domain command is used to delete a disk domain. |
| change disk_domain general | The change disk_domain general command is used to modify the properties of a disk domain, including the disk domain name, hot spare strategy, switch status of the LUN mapping table repair function, and similarity-based deduplication execution level. |
| create disk_domain | The create disk_domain command is used to create a disk domain. |
| add disk_domain disk | The add disk_domain disk command is used to add disks to a disk domain. |
| change storage_pool general | The change storage_pool general command is used to modify the attributes of a storage pool, including the name, capacity alarm threshold, capacity exhaustion threshold, capacity, provisioning limit, low threshold of protection capacity, high threshold of protection capacity, and automatic deletion switch. |
| delete storage_pool | The delete storage_pool command is used to delete a specified storage pool. |
| add storage_pool disk | The add storage_pool disk command is used to add disks to a storage pool. |
| change lun_takeover finish_switch_path | The change lun_takeover finish_switch_path command is used to confirm that the host paths of the specified LUN have been switched to the paths between the host and the target disk array. |
| change lun_takeover enhance_switch | The change lun_takeover enhance_switch is used to set the enhanced masquerading switch of a specified LUN. |
| change lun_takeover disable_switch_path | The change lun_takeover disable_switch_path command is used to forbid the specified LUN's paths to be switched back to the source array and to allow the LUN to be used as the source LUN for online takeover. |
| create lun_takeover general | The create lun_takeover general command is used to create takeover LUNs. |
| create lun_workload_type general | The create lun_workload_type general command is used to create a workload type for LUNs. After creating a workload type, you can choose it when you are creating LUNs. Through this method the LUN space parameter can be reasonably set. |
| remove lun_consistency_group lun | The remove lun_consistency_group lun command is used to remove a member LUN from a specified LUN consistency group. Use this command when consistency protection is not required for a specified LUN. |
| remove lun_takeover general | The remove lun_takeover general command is used to delete the information about a takeover LUN. |
| delete lun | The delete lun command is used to delete LUNs. |
| change lun | The change lun command is used to modify LUN settings, including the name and capacity. |
| add host initiator | The add host initiator command is used to add an initiator to a host. |
| create host | The create host command is used to create hosts. |
| delete host | The delete host command is used to delete hosts. |
| remove lun_group lun | The remove lun_group lun command is used to remove LUNs from a specified LUN group. |
| delete lun_group | The delete lun_group command is used to delete a specified LUN group. |
| remove host_group host | The remove host_group host command is used to remove a specified host from a host group. |
| remove port_group port | The remove port_group port command is used to remove a specified port from a port group. |
| add rep_port_group port | The add rep_port_group port command is used to add ports to a replication port group. |
| delete mapping_view | The delete mapping_view command is used to delete mapping views. |
| add mapping_view port_group | The add mapping_view port_group command is used to add a port group to a mapping view. |
| remove mapping_view lun_group | The remove mapping_view lun_group command is used to remove a LUN group from a mapping view. |
| remove mapping_view port_group | The remove mapping_view port_group command is used to remove a port group from a mapping view. |
| remove mapping_view host_group | The remove mapping_view host_group command is used to remove a host group from a mapping view. |
| add mapping_view host_group | The add mapping_view host_group command is used to add a host group to a mapping view. |
| create mapping_view | The create mapping_view command is used to create a mapping view. |
| change mapping_view | The change mapping_view command is used to modify the settings of a mapping view including the view name and the function switch for in-band commands. Also, it can be used to change the host LUN IDs of the LUNs in mapping_view. |
| add mapping_view lun_group | The add mapping_view lun_group command is used to add a LUN group to a mapping view. |
| add smartqos_policy hierarchical | The add smartqos_policy hierarchical command is used to add normal SmartQoS policies to a specified hierarchical SmartQoS policy. |
| add smartqos_policy lun | The add smartqos_policy lun command is used to add logical unit numbers (LUNs) to a SmartQoS policy. |
| add smartqos_policy lun_group | The add smartqos_policy lun_group command is used to add LUN groups to a SmartQoS policy. |
| remove smartqos_policy hierarchical | The remove smartqos_policy hierarchical command is used to remove normal SmartQoS policies from a specified hierarchical SmartQoS policy. |
| remove smartqos_policy host | The remove smartqos_policy host command is used to remove hosts from a specific SmartQoS policy. |
| remove smartqos_policy lun | The remove smartqos_policy lun command is used to remove LUNs from a specific SmartQoS policy. |
| remove smartqos_policy lun_group | The remove smartqos_policy lun_group command is used to remove LUN groups from a specific SmartQoS policy. |
| change smartqos_policy enabled | The change smartqos_policy enabled command is used to enable or disable a specified SmartQoS policy. |
| change smartqos_policy general | The change smartqos_policy general command is used to modify SmartQoS policies. |
| delete smartqos_policy | The delete smartqos_policy command is used to delete one or more specified SmartQoS policies. |
| add smartqos_policy file_system | The add smartqos_policy file_system command is used to add file systems to a SmartQoS policy. |
| show remote_replication available_file_system | The show remote_replication available_file_system command is used to query the information on available file system tasks. |
| change initiator | The change initiator command is used to modify the attributes associated with an initiator including the Challenge Handshake Authentication Protocol (CHAP) status, initiator alias, and multipathing mode. Also, it can be used to replace initiators. |
| add host nvme_over_roce_initiator | The add host nvme_over_roce_initiator command is used to add an NVMe over RoCE initiator to a host. |
| change nvme_over_roce_initiator general | The change nvme_over_roce_initiator general command is used to modify the attributes of an initiator, including its alias and NVMe qualified name (NQN), as well as replace an initiator. |
| remove host nvme_over_roce_initiator | The remove host nvme_over_roce_initiator command is used to remove an NVMe over RoCE initiator from a host. |
| delete nvme_over_roce_initiator general | The delete nvme_over_roce_initiator general command is used to delete an NVMe over RoCE initiator. After the deletion, the host can no longer access the storage system resources through the initiator. |
| change iscsi initiator_name | The change iscsi initiator_name command is used to change the name of an iSCSI initiator configured for the storage system. |
| change iscsi initiator_name_v2 | The change iscsi initiator_name_v2 command is used to change the name of an iSCSI initiator configured for the storage system. |
| change lun_migration | The change lun_migration command is used to change the LUN migration properties. |
| create lun_migration | The create lun_migration command is used to create LUN migration. |
| delete lun_migration | The delete lun_migration command is used to delete LUN migration tasks. |
| change lun_migration_split consistency | The change lun_migration_split consistency command is used to split LUN migration tasks. |
| delete vstore general | The delete vstore general command is used to delete a vStore. |
| change smartqos_policy min_goal_reserved | The change smartqos_policy min_goal_reserved command is used to modify the minimum performance of LUNs that have not been added to a lower limit guarantee policy. |
| delete quota general | The delete quota general command is used to delete a quota of a file system, or a quota of a specified dtree. |
| remove hyper_cdp_schedule fs | The remove hyper_cdp_schedule fs command is used to remove file systems from a HyperCDP schedule. |
| change file_system enabled | The change file_system enabled command is used to enable file system related functions, such as to enable checksum, to perform periodic snapshots, and to modify the Atime. |
| change file_system general | The change file_system general command is used to modify file system parameters such as the name, capacity, block size, and owning controller. |
| create file_system general | The create file_system general command is used to create a file system. |
| delete file_system general | The delete file_system general command is used to delete file systems. |
| change service cifs_config | The change service cifs_config command is used to change the CIFS common configuration. |
| clear cifs connection | The clear cifs connection command is used to close the network connection of the specified client or server. |
| change service cifs | The change service cifs command is used to modify the settings of the CIFS share service. |
| delete windows_user | The delete windows_user command is used to delete a Windows user. |
| delete windows_group | The delete windows_group command is used to delete a Windows user group. |
| delete unix_user | The delete unix_user command is used to delete a UNIX user. |
| delete unix_group | The delete unix_group command is used to delete a UNIX group. |
| delete share nfs | The delete share nfs command is used to delete an NFS share. |
| delete share cifs | The delete share cifs command is used to delete a CIFS share. |
| create share_homedir_rule cifs | The create share_homedir_rule cifs command is used to create a mapping rule for a Homedir share. |
| change share_homedir_rule cifs | The change share_homedir_rule cifs command is used to modify the mapping rule of a Homedir share. |
| create share nfs | The create share nfs command is used to create an NFS share. |
| change share nfs | The change share nfs command is used to modify the configurations of an NFS share. |
| change share_permission nfs | The change share_permission nfs command is used to modify NFS share permission settings. |
| delete smart_cache_partition | The delete smart_cache_partition command is used to delete a SmartCache partition. |
| change smart_cache_pool switch | The change smart_cache_pool switch command is used to enable or disable a SmartCache pool. |
| delete smart_cache_pool | The delete smart_cache_pool command is used to delete a SmartCache pool. |
| remove smart_cache_partition lun | The remove smart_cache_partition lun command is used to remove LUNs from a SmartCache partition. |
| remove smart_cache_partition file_system | The remove smart_cache_partition file_system command is used to remove file systems from a SmartCache partition. |
| delete dtree general | The delete dtree general command is used to delete a dtree. |
| delete mapping general | The delete mapping general command is used to delete a mapping. |
| change mapping general | The change mapping general command is used to modify mapping information. |
| change mapping host_lun_id | The change mapping host_lun_id command is used to modify IDs of mapped host LUNs. |
| create mapping general | The create mapping general command is used to create a mapping. |
| change container_service general | The change container_service general command is used to change the status of a container service. |
| change container_service active | The change container_service active command is used to activate the container service for the first time. |
| change container_application general | The change container_application general command is used to update an application. |
| delete container_application general | The delete container_application general command is used to delete an application. |
| delete vstore_pair general | The delete vstore_pair general command is used to delete a vStore pair. |
| create vstore_pair general | The create vstore_pair general command is used to create a vStore pair. |
| add fs_hyper_metro_domain quorum_server | The add fs_hyper_metro_domain quorum_server command is used to add a quorum server to a HyperMetro domain. |
| remove fs_hyper_metro_domain quorum_server | The remove fs_hyper_metro_domain quorum_server command is used to remove a quorum server from a HyperMetro domain. |
| change fs_hyper_metro_domain split | The change fs_hyper_metro_domain split command is used to split a file system-based HyperMetro domain. |
| swap fs_hyper_metro_domain | The swap fs_hyper_metro_domain command is used to perform a primary/secondary switchover for a HyperMetro domain cluster. |
| change fs_hyper_metro_domain second_fs_access | The change fs_hyper_metro_domain second_fs_access command is used to modify the access permission of the secondary end of a HyperMetro domain cluster. |
| change fs_hyper_metro_domain recover | The change fs_hyper_metro_domain recover command is used to recover a file system HyperMetro domain. |
| change fs_hyper_metro_domain local_logical_port_work_status | The change fs_hyper_metro_domain local_logical_port_work_status command is used to change the working status of all local logical ports in a HyperMetro domain cluster. |
| change hyper_copy restore | The change hyper_copy restore command is used to start, stop, pause, and resume full or differential reverse synchronization of the HyperCopy pair. |
| delete hyper_copy | The delete hyper_copy command is used to delete a HyperCopy pair. |
| remove hyper_copy_consistency_group hyper_copy | The remove hyper_copy_consistency_group hyper_copy command is used to remove HyperCopy pairs from a specified HyperCopy consistency group. Use this command if consistency management is not required for HyperCopy pairs. |
| change hyper_copy_consistency_group restore | The change hyper_copy_consistency_group restore command is used to set reverse synchronization parameters of a HyperCopy consistency group. |
| change hyper_copy_consistency_group synchronize | The change hyper_copy_consistency_group synchronize command is used to start, pause, continue, and stop member synchronization of a HyperCopy consistency group. |
| create hyper_copy_consistency_group | The create hyper_copy_consistency_group command is used to create a HyperCopy consistency group. |
| change hyper_copy general | The change hyper_copy general command is used to modify HyperCopy pair settings. |
| change hyper_copy_consistency_group general | The change hyper_copy_consistency_group general command is used to modify HyperCopy consistency group settings. |
| create clone relation | The create clone relation command is used to create a clone pair. |
| delete clone | The delete clone command is used to delete a clone pair. |
| change clone restore | The change clone restore command is used to start, stop, pause, and resume full or differential reverse synchronization of the clone pair. |
| remove clone_consistency_group clone | The remove clone_consistency_group clone command is used to remove clone pairs from a specified clone consistency group. Use this command if consistency management is not required for clone pairs. |
| create hyper_copy local | The create hyper_copy local command is used to create a HyperCopy pair. |
| delete clone_consistency_group | The delete clone_consistency_group command is used to delete a clone consistency group. |
| change clone_consistency_group synchronize | The change clone_consistency_group synchronize command is used to start, pause, continue, and stop member synchronization of a clone consistency group. |
| change clone_consistency_group restore | The change clone_consistency_group restore command is used to set reverse synchronization parameters of a clone consistency group. |
| remove snapshot_consistency_group snapshot | The remove snapshot_consistency_group snapshot command is used to remove snapshots from a specified snapshot consistency group. |
| test system trust | This test system trust command is used to test whether the system can be trusted and show the test result to users. |
| delete dr_star general | The delete dr_star general command is used to delete DR Star. |
| change dr_star disable | The change dr_star disable command is used to deactivate DR Star. |
| change dr_star third_resource_access | The change dr_star third_resource_access command is used to change the read and write permissions of secondary LUNs in remote replication at the DR Star third site. |
| change rest msg_return_type | The change rest msg_return_type command is used to change the command output returning mode of REST interfaces to synchronous or asynchronous. |
| change devicemanager ciphersuite | The change devicemanager ciphersuite command is used to configure the OpenSSL cipher suite used by the DeviceManager service. |
| change hyper_cdp_consistency_group restore | The change hyper_cdp_consistency_group restore command is used to restore data using HyperCDP consistency groups. You can use the HyperCDP consistency groups to restore the source protection group data by running this command. |
| change hyper_cdp_consistency_group general | The change hyper_cdp_consistency_group general command is used to modify the name and restoration speed of a HyperCDP consistency group. |
| change hyper_cdp_consistency_group cancel_restore | change hyper_cdp_consistency_group cancel_restore command is used to cancel the restoration of a HyperCDP consistency group. |
| delete hyper_cdp | The delete hyper_cdp command is used to delete HyperCDP objects. |
| change hyper_cdp general | The change hyper_cdp general command is used to modify the name and restoration speed of a HyperCDP object. |
| remove hyper_cdp_schedule lun | The remove hyper_cdp_schedule lun command is used to remove LUNs from a HyperCDP schedule. |
| change snapshot cancel_restore | The change snapshot cancel_restore command is used to cancel the rollback of a snapshot. |
| change snapshot capacity | The change snapshot capacity command is used to modify the capacity of a snapshot. |
| change snapshot deactivate | The change snapshot deactivate command is used to deactivate a snapshot. |
| change snapshot io_priority | The change snapshot io_priority command is used to change the I/O priority of the snapshot. |
| change snapshot restore | The change snapshot restore command is used to roll back snapshots. You can use the snapshots to restore the destination LUN data by running this command. |
| change snapshot description | The change snapshot description command is used to modify the description of snapshots. |
| change snapshot name | The change snapshot name command is used to rename snapshots. |
| change snapshot speed | The change snapshot speed command is used to change the rollback speed of the snapshot. |
| delete hyper_cdp_consistency_group | The delete hyper_cdp_consistency_group command is used to delete HyperCDP consistency groups. |
| remove hyper_cdp_schedule lun_consistency_group | The remove hyper_cdp_schedule lun_consistency_group command is used to remove LUN consistency groups from a HyperCDP schedule. |
| remove hyper_cdp_schedule protect_group | The remove hyper_cdp_schedule protect_group command is used to remove protection groups from a HyperCDP schedule. |
| delete snapshot | The delete snapshot command is used to delete snapshots. |
| change snapshot reactivate | The change snapshot reactivate command is used to reactivate snapshots. Use this command if you want to set the point in time of a snapshot to the latest point in time of the source LUN or HyperCDP object. |
| create snapshot duplicate | The create snapshot duplicate command is used to create a duplicate for a snapshot or a HyperCDP object. You can back up a snapshot or a HyperCDP object by running this command. |
| create snapshot_consistency_group general | The create snapshot_consistency_group general command is used to create a snapshot consistency group for a specified LUN consistency group. |
| create snapshot_consistency_group universal | The create snapshot_consistency_group universal command is used to create a snapshot consistency group for a specified LUN protection group. |
| change hyper_cdp_schedule enabled | The change hyper_cdp_schedule enabled command is used to enable or disable a HyperCDP schedule. |
| change snapshot_consistency_group reactivate | The change snapshot_consistency_group reactivate command is used to reactivate a snapshot consistency group. |
| change snapshot_consistency_group activate | The change snapshot_consistency_group activate command is used to activate a snapshot consistency group. |
| change snapshot_consistency_group deactivate | The change snapshot_consistency_group deactivate command is used to deactivate a snapshot consistency group. |
| create snapshot_consistency_group duplicate | The create snapshot_consistency_group duplicate command is used to create a duplicate for a specified snapshot consistency group or HyperCDP consistency group. |
| change snapshot_consistency_group restore | The change snapshot_consistency_group restore command is used to start restoration from a snapshot consistency group. |
| change snapshot_consistency_group cancel_restore | The change snapshot_consistency_group cancel_restore command is used to cancel restoration from a snapshot consistency group. |
| delete snapshot_consistency_group | The delete snapshot_consistency_group command is used to delete a snapshot consistency group. |
| change snapshot_consistency_group general | The change snapshot_consistency_group general command is used to modify the properties of a snapshot consistency group. |
| delete hyper_cdp_schedule | The delete hyper_cdp_schedule command is used to delete HyperCDP schedules. |
| change snapshot activate | The change snapshot activate command is used to activate snapshots. |
| create snapshot general | The create snapshot general command is used to create snapshots. You can create an identical and usable point-in-time duplicate for a data object by running this command. |
| change remote_replication second_fs_access | The change remote_replication second_fs_access command is used to set the read and write attributes of a secondary file system. |
| delete remote_replication | The delete remote_replication command is used to delete a specific remote replication. |
| change remote_replication general | The change remote_replication general command is used to modify a specified remote replication pair. |
| swap remote_replication | The swap remote_replication command is used to implement primary/secondary resource switchover of a remote replication. Use this command when you need to copy the data at the secondary resource to the primary resource using remote replication. |
| change remote_replication synchronize | The change remote_replication synchronize command is used to synchronize a specific remote replication. Use this command when you need to synchronize the data at the primary resource to a secondary resource to ensure data consistency. |
| change remote_replication split | The change remote_replication split command is used to split a remote replication task. During the split of a remote replication task, then data synchronization stops between both resources. |
| create remote_replication unified | The create remote_replication unified command is used to create a remote replication pair. |
| create remote_replication general | The create remote_replication general command is used to create a LUN-based remote replication pair. |
| remove consistency_group remote_replication | The remove consistency_group remote_replication command is used to delete remote replication pairs from a consistency group. |
| add consistency_group remote_replication_delay | The add consistency_group remote_replication_delay command is used to add the remote replication into the consistency group after the initial synchronization of the remote replication is complete. |
| swap consistency_group | The swap consistency_group command is used to implement primary/secondary switchover for existing remote replication tasks in a consistency group. |
| delete consistency_group | The delete consistency_group command is used to delete consistency groups. |
| change consistency_group split | The change consistency_group split command is used to split consistency groups. |
| change consistency_group synchronize | The change consistency_group synchronize command is used to synchronize appointed consistency groups. |
| create consistency_group synchronization | The create consistency_group synchronization command is used to create a synchronous consistency group. You can centrally manage multiple synchronous remote replication pairs by running this command. |
| create consistency_group asynchronization | The create consistency_group asynchronization command is used to create asynchronous consistency groups. |
| change consistency_group general | The change consistency_group general command is used to modify information about a consistency group. |
| delete remote_device | The delete remote_device command is used to delete a specific remote device. When the forcible deletion flag is set to "TRUE", this command can be used to forcibly delete a remote device. |
| create remote_device general | The create remote_device general command is used to create remote devices. You must create a remote device by running this command before you can effortlessly perform remote replication tasks between the storage system and remote device. |
| change remote_device general | The change remote_device general command is used to modify the name and link of remote devices. |
| change fs_snapshot restore | The change fs_snapshot restore command is used to roll back a file system to a specified snapshot. |
| change fs_hyper_cdp restore | The change fs_hyper_cdp restore command is used to roll back a file system to a specified HyperCDP object. |
| delete fs_hyper_cdp general | The delete fs_hyper_cdp general command is used to delete a file system HyperCDP object. |
| delete fs_snapshot general | The delete fs_snapshot general command is used to delete a file system snapshot. |
| change hyper_metro_pair synchronize | The change hyper_metro_pair synchronize command is used to start synchronizing a HyperMetro pair. |
| change hyper_metro_pair general | The change hyper_metro_pair general command is used to change HyperMetro pair attributes. |
| delete hyper_metro_pair general | The delete hyper_metro_pair general command is used to delete a HyperMetro pair. |
| change hyper_metro_pair general | The change hyper_metro_pair general command is used to change HyperMetro pair attributes. |
| create hyper_metro_pair unified | The create hyper_metro_pair unified command is used to create a HyperMetro pair. |
| add hyper_metro_domain quorum_server | The add hyper_metro_domain command is used to add a quorum server to HyperMetro domains. |
| remove hyper_metro_domain quorum_server | The remove hyper_metro_domain quorum_server command is used to remove a quorum server from HyperMetro domains. |
| create hyper_metro_domain general | The create hyper_metro_domain general command is used to create a HyperMetro domain. |
| delete hyper_metro_domain general | The delete hyper_metro_domain general command is used to delete a HyperMetro domain. |
| delete hyper_metro_consistency_group | The delete hyper_metro_consistency_group command is used to delete a HyperMetro consistency group. |
| change hyper_metro_consistency_group start | The change hyper_metro_consistency_group start command is used to forcibly start a HyperMetro consistency group. |
| remove hyper_metro_consistency_group pair | The remove hyper_metro_consistency_group pair command is used to delete a pair from a HyperMetro consistency group. |
| change hyper_metro_consistency_group general | The change hyper_metro_consistency_group general command is used to change the information about a HyperMetro consistency group. |
| create hyper_metro_consistency_group general | The create hyper_metro_consistency_group general command is used to create a HyperMetro consistency group. |
| change quorum_server general | The change quorum_server general command is used to change the information about a third-place quorum server. |
| remove quorum_server_link general | The remove quorum_server_link general command is used to remove a specified link between a storage array and a quorum server. |
| delete quorum_server general | The delete quorum_server general command is used to delete a third-place quorum server. |
| change key_service general | The change key_service general command is used to modify the key service configuration. |
| delete kmc general | The delete kmc general command is used to delete the configuration of an external key management server. |
| delete performance file | The delete performance file command is used to delete historical performance statistical files. |
| change ca_server | The change ca_server command is used to modify the CA server configuration. |
| change domain nis_config | The change domain nis_config command is used to modify NIS domain authentication configurations. |
| delete domain nis | The delete domain nis command is used to initialize the configuration of an NIS domain. |
| change domain ad_config | The change domain ad_config command is used to change the name, site, and machine account of the domain controller, determine whether to overwrite the existing machine account when the storage array joins the AD domain, as well as determine whether to join or exit the domain. |
| add security_rule | The add security_rule command is used to add a security rule to control the maintenance terminals that attempt to access the storage system. |
| delete security_rule | The delete security_rule command is used to delete security rules. |
| change security_rule enabled | The change security_rule enabled command is used to enable or disable security rules. |
| delete crl general | The delete crl general command is used to delete the certificate revocation list. |
| change certificate auto_update | The change certificate auto_update command is used to modify the automatic certificate update configuration. |
| import crl file | The import crl file command is used to import a new certificate revocation list. |
| delete certificate general | The delete certificate general command is used to delete CA certificate information from an array. |
| import certificate | The import certificate command is used to import a new private key, certificate, and CA certificate. |
| delete ldap configuration | The delete ldap configuration command is used to delete the configuration information on Lightweight Directory Application Protocol (LDAP) servers. |
| remove smtp_server general | The remove smtp_server general command is used to delete an email sending server. |
| change alarm_mask | The change alarm_mask command is used to mask specified alarms. |
| delete notification trap | The delete notification trap command is used to delete a trap server. |
| change alarm_object_mask | The change alarm_mask command is used to mask alarms of specified objects. |
| remove notification receiver | The remove notification receiver command is used to remove email addresses or phone numbers used to receive alarm or event notifications. |
| change alarm_level | The change alarm_level command is used to change the severity of a specified alarm. |
| change alarm clear | The change alarm clear command is used to clear alarms from the storage system. |
| export event | The export event command is used to export logs, key logs, Call Home data, event information, diagnostic files, disk enclosure logs, FTDS statistics, or disk data destruction reports of a storage system. |
| show file export_path | The show file export_path command is used to export system data to a directory in the storage system and show the directory to users. |
| change operation_log | The change operation_log command is used to modify the retention policy of operation logs. |
| change call_home general | The change call_home general command is used to set the Call Home service. |
| remove remote_support user_contact | The remove remote_support user_contact command is used to delete the contacts of eSerivce. |
| change remote_support agreement | The change remote_support agreement command is used to sign the letter of authorization. |
| change remote_support general | The change remote_support general command is used to configure basic information about eService. |
| change audit_log_strategy | The change audit_log_strategy command is used to modify the audit log strategy. |
| change iscsi target_name | The change iscsi target_name command is used to change the name of the iSCSI target configured for the storage system. |
| change snmp usm | The change snmp usm command is used to modify the configuration of a USM user. |
| change snmp safe_strategy | The change snmp safe_strategy command is used to change the security policy of the SNMP service. |
| change snmp port | The change snmp port command is used to set the port number of the SNMP service. |
| change snmp version | The change snmp version command is used to set the status of the SNMPv1 and SNMPv2c protocols and the switch status of the SNMP unique controller enclosure ID function. |
| add snmp usm | The add snmp usm command is used to add a USM user. |
| remove ntp_server general | The remove ntp_server general command is used to delete an NTP server used for time synchronization. |
| change system dns_load_balance | The change system dns_load_balance command is used to enable or disable the DNS load balancing function and configure the load balancing policy. |
| change system server_port | The change system server_port command is used to modify port information of the system. |
| change nas_service active | The change nas_service active command is used to activate the NAS feature service for the first time. |
| add ntp_server general | The add ntp_server general command is used to add an NTP server for time synchronization. |
| reboot system | The reboot system command is used to restart the storage system. Running this command causes service interruption. |
| poweroff system | The poweroff system command is used to power off the storage system. Running this command causes service interruption. |
| change system time | The change system time command is used to change the storage system's time. If the storage system's time is incorrect, you can run this command to change it. |
| change system timezone | The change system timezone command is used to change the time zone where the storage system resides in. If the displayed time zone is different from the actual local time zone, you can run this command to change the time zone. |
| change system ntp | The change system ntp command is used to configure the NTP. Run this command if you want the storage system to synchronize its time with that of an NTP server. |
| change ntp_server config | The change ntp_server config command is used to configure the time synchronization function. Run this command if you want the storage system to synchronize its time with that of an NTP server. |
| delete dns_zone general | The delete dns_zone general command is used to delete a specified zone. |
| change dns_zone general | The change dns_zone general command is used to modify the name a DNS zone. |
| change controller service_session | The change controller service_session command is used to change the service duration of a controller. |
| change controller starting_point_date | The change controller starting_point_date command is used to change the service start time of a controller. |
| change interface_module | The "change interface_module" command is used to configure an interface module mode. |
| poweroff interface_module | The poweroff interface_module command is used to power off a specific interface module. |
| delete bond_port | The delete bond_port command is used to delete an Ethernet bond port. |
| change bond_port general | The change bond_port general command is used to change the MTU of a bond port. |
| clear port bit_error | The clear port bit_error command is used to clear the bit_error of the port. |
| remove port ipv4_address | The remove port ipv4_address command is used to remove the IPv4 address of a specified port. NOTE: After the IP address of an Ethernet host port is removed, the application sever that connects to the Ethernet host port cannot access the storage system. |
| remove port ipv6_address | The remove port ipv6_address command is used to remove the IPv6 address of a specified port. NOTE: After the IP address of an Ethernet host port is removed, the application sever that connects to the Ethernet host port cannot access the storage system. |
| add port ipv4_route | The add port ipv4_route command is used to add an IPv4 route for a specific Ethernet port. If the IPv4 address of the storage system and that of an application server reside on different network segments, you can run this command to add a route to connect the storage system to application server. |
| add port ipv6_route | The add port ipv6_route command is used to add an IPv6 route for a specific Ethernet port. If the IPv6 address of the storage system and that of a host reside on different network segments, you can run this command to add a route to connect the storage system to the host. |
| remove port ipv4_route | The remove port ipv4_route command is used to remove an IPv4 route configured for a port. |
| remove port ipv6_route | The remove port ipv6_route command is used to remove an IPv6 route configured for a port. |
| remove system management_ip | The remove system management_ip command is used to delete an IP address of a management network port. |
| create bond_port | The create bond_port command is used to create an Ethernet bond port. By binding multiple Ethernet ports, you can increase the data transmission bandwidth in parallel mode. The "create bond_port iscsi_port_id_list" command is replaced with the "create bond_port port_id_list" command. |
| change system management_ip | The change system management_ip command is used to configure the IP address of a management port on new hardware. Both an IPv4 and IPv6 address can be configured, which is used by terminals to access the disk array. |
| change port roce | The change port roce command is used to configure the properties for RoCE ports. |
| change port eth | The change port eth command is used to configure the properties for Ethernet ports (including host ports and management network ports). |
| change port fc | The change port fc command is used to modify the properties of a specific Fibre Channel port. |
| change port eth_snsd_switch | The change port eth_snsd_switch command is used to enable or disable the SNSD function of an Ethernet port. |
| change port ipv6_address | The change port ipv6_address command is used to change the IPv6 address of a specific port. |
| change port ipv4_address | The change port ipv4_address command is used to change the IPv4 address of a specific port. |
| remove net_plane ipv4_address | The remove net_plane ipv4_address command is used to delete the IPv4 address of a network plane. |
| remove net_plane ipv4_gateway | The remove net_plane ipv4_gateway command is used to delete the IPv4 gateway of a network plane. |
| remove net_plane ipv6_gateway | The remove net_plane ipv6_gateway command is used to delete the IPv6 gateway of a network plane. |
| change enclosure id | The change enclosure id command is used to modify the ID of a disk enclosure. |
| change enclosure location | The change enclosure location command is used to change the location of an enclosure in a cabinet. |
| export running_data | The export running_data command is used to export storage system configuration information to a .txt file. Such a .txt file can be read by users but cannot be used during configuration information import. If you need to know storage system configuration information, run this command. |
| export configuration_data | The export configuration_data command is used to export the configuration file that resides in the storage system's memory. Such a configuration file stores important configuration information on the storage system's components and services. Export configuration data regularly and save it securely so that you can restore the configuration when the storage system fails. |
| change user_ssh_auth_info general | The change user_ssh_auth_info general command is used to change the SSH authentication mode of a user. |
| change user_mode current_mode | The change user_mode current_mode command is used to switch a user view. This command is used when you want to switch from the user view to the developer or engineer view. |
| reboot storage service | The reboot storage service command is used to restart storage system services. |
| change ftds switch | The change ftds switch command is used to enable or disable the Fault Tracing Diagnosing System (FTDS) tracing function. This command can be used to set the main switch (excluding the workload switch), tracing switch, phase switch, latency switch, counting switch, workload collection switch, and workload feature extraction switch. |
| change dsm copy_num | The change dsm copy_num command is used to modify the number of DSM copies. |
| change logical_port failover_group | The change logical_port failover_group command is used to configure failover groups for one or more logical ports. |
| remove logical_port ipv4_route | The remove logical_port ipv4_route command is used to remove the IPv4 route from a logical port. |
| remove logical_port ipv6_route | The remove logical_port ipv6_route command is used to remove the IPv6 route from a logical port. |
| delete logical_port general | The delete logical_port general command is used to delete the specific logical port. |
| change logical_port general | The change logical_port general command is used to configure a logical port. |
| change logical_port failback | The change logical_port failback command is used to fail back a logical port. |
| change vlan general | The change vlan general command is used to change the VLAN maximum transmission unit. |
| delete vlan general | The delete vlan general command is used to delete a VLAN port. |
| remove failover_group eth_port | The remove failover_group eth_port command is used to remove Ethernet ports from a customized failover group. |
| remove failover_group bond_port | The remove failover_group bond_port command is used to remove specified bond ports from a customized failover group. |
| remove failover_group vlan_port | The remove failover_group vlan_port command is used to remove specified VLAN ports from a customized failover group. |
| delete failover_group general | The delete failover_group general command is used to delete a specified customized failover group. |
