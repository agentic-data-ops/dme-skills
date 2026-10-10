# Data Protect Management Commands

Data protection management commands functionally covers complete data protection functions provided by the storage system. Those functions can improve data redundancy and reduce data loss risks.

## consistency_group

- add consistency_group remote_replication: add a remote replication pair to a consistency group.
- add consistency_group remote_replication_delay: add the remote replication into the consistency group after the initial synchronization of the remote replication is complete.
- change consistency_group general: modify information about a consistency group.
- change consistency_group mode: change the replication mode of the remote replication consistency group.
- change consistency_group split: split consistency groups.
- change consistency_group synchronize: synchronize appointed consistency groups.
- create consistency_group asynchronization: create asynchronous consistency groups.
- create consistency_group protect_group: create a remote replication consistency group for a protection group.
- create consistency_group synchronization: create a synchronous consistency group. You can centrally manage multiple synchronous remote replication pairs by running this command.
- create consistency_group verification_session: verify consistency groups.
- delete consistency_group: delete consistency groups.
- remove consistency_group remote_replication: delete remote replication pairs from a consistency group.
- show consistency_group available_remote_replication: query for the remote replication tasks that can be added to a consistency group.
- show consistency_group general: query details of consistency groups.
- show consistency_group member: query details on members of a consistency group task.
- swap consistency_group: implement primary/secondary switchover for existing remote replication tasks in a consistency group.

## device_manager

- change devicemanager ciphersuite: configure the OpenSSL cipher suite used by the DeviceManager service.
- change devicemanager web_config: configure the web_config SameSite field used by the DeviceManager service.
- change rest msg_return_type: change the command output returning mode of REST interfaces to synchronous or asynchronous.
- show devicemanager ciphersuite: query the OpenSSL cipher suite used by DeviceManager service in the storage system.

## dr_star

- change dr_star disable: deactivate DR Star.
- change dr_star enable: activate DR Star.
- change dr_star general: modify the attributes of a DR Star trio.
- change dr_star third_resource_access: change the read and write permissions of secondary LUNs in remote replication at the DR Star third site.
- create dr_star general: create DR Star.
- delete dr_star general: delete DR Star.
- show dr_star general: query information about DR Star trios.
- show dr_star member: query information about members of DR Star.
- swap dr_star: switch DR Star.

## fs_hyper_metro_domain

- add fs_hyper_metro_domain quorum_server: add a quorum server to a HyperMetro domain.
- change fs_hyper_metro_domain general: modify HyperMetro domain information.
- change fs_hyper_metro_domain local_logical_port_work_status: change the working status of all local logical ports in a HyperMetro domain cluster.
- change fs_hyper_metro_domain priority: change the preferred site of a HyperMetro domain cluster.
- change fs_hyper_metro_domain recover: recover a file system HyperMetro domain.
- change fs_hyper_metro_domain recover_policy: modify the recovery policy of a HyperMetro domain cluster.
- change fs_hyper_metro_domain second_fs_access: modify the access permission of the secondary end of a HyperMetro domain cluster.
- change fs_hyper_metro_domain split: split a file system-based HyperMetro domain.
- change fs_hyper_metro_domain start: forcibly start a HyperMetro domain.
- create fs_hyper_metro_domain general: create a file system-based HyperMetro domain.
- delete fs_hyper_metro_domain general: delete a HyperMetro domain.
- remove fs_hyper_metro_domain quorum_server: remove a quorum server from a HyperMetro domain.
- show fs_hyper_metro_domain general: query a file system-based HyperMetro domain.
- swap fs_hyper_metro_domain: perform a primary/secondary switchover for a HyperMetro domain cluster.

## fs_snapshot

- change fs_hyper_cdp general: modify basic attributes of a file system HyperCDP object, including the name and description.
- change fs_hyper_cdp restore: roll back a file system to a specified HyperCDP object.
- change fs_snapshot general: modify basic attributes of a file system snapshot, including the name and description.
- change fs_snapshot restore: roll back a file system to a specified snapshot.
- create fs_hyper_cdp general: create a file system HyperCDP object.
- create fs_snapshot general: create a file system snapshot.
- delete fs_hyper_cdp general: delete a file system HyperCDP object.
- delete fs_snapshot general: delete a file system snapshot.
- show fs_hyper_cdp general: query a HyperCDP object in a file system, including the name, HyperCDP object ID, file system ID, file system name, health status of the HyperCDP object, HyperCDP object creation time, and capacity consumed by the HyperCDP object.
- show fs_hyper_cdp restore: query information about a HyperCDP object that is being rolled back to.
- show fs_snapshot general: query a snapshot in a file system, including the name, snapshot ID, file system ID, file system name, health status of the snapshot, snapshot creation time, and capacity consumed by the snapshot.
- show fs_snapshot restore: query information about a snapshot that is being rolled back to.

## hyper_copy

- add clone_consistency_group clone: add clone pairs to a specified clone consistency group. Use this command if consistency management is required for clone pairs.
- add hyper_copy_consistency_group hyper_copy: add HyperCopy pairs to a specified HyperCopy consistency group. Use this command if consistency management is required for HyperCopy pairs.
- change clone general: modify clone pair settings.
- change clone restore: start, stop, pause, and resume full or differential reverse synchronization of the clone pair.
- change clone synchronize: start, stop, pause, and continue clone pair synchronization.
- change clone_consistency_group general: modify clone consistency group settings.
- change clone_consistency_group restore: set reverse synchronization parameters of a clone consistency group.
- change clone_consistency_group synchronize: start, pause, continue, and stop member synchronization of a clone consistency group.
- change hyper_copy general: modify HyperCopy pair settings.
- change hyper_copy restore: start, stop, pause, and resume full or differential reverse synchronization of the HyperCopy pair.
- change hyper_copy synchronize: start, stop, pause, and continue HyperCopy pair synchronization.
- change hyper_copy_consistency_group general: modify HyperCopy consistency group settings.
- change hyper_copy_consistency_group restore: set reverse synchronization parameters of a HyperCopy consistency group.
- change hyper_copy_consistency_group synchronize: start, pause, continue, and stop member synchronization of a HyperCopy consistency group.
- create clone general: create a clone pair.
- create clone relation: create a clone pair.
- create clone_consistency_group: create a clone consistency group.
- create hyper_copy local: create a HyperCopy pair.
- create hyper_copy_consistency_group: create a HyperCopy consistency group.
- delete clone: delete a clone pair.
- delete clone_consistency_group: delete a clone consistency group.
- delete hyper_copy: delete a HyperCopy pair.
- delete hyper_copy_consistency_group: delete a HyperCopy consistency group.
- remove clone_consistency_group clone: remove clone pairs from a specified clone consistency group. Use this command if consistency management is not required for clone pairs.
- remove hyper_copy_consistency_group hyper_copy: remove HyperCopy pairs from a specified HyperCopy consistency group. Use this command if consistency management is not required for HyperCopy pairs.
- show clone general: query clone pair information.
- show clone_consistency_group clone: query information about members in a clone consistency group.
- show clone_consistency_group general: query the basic information about a clone consistency group.
- show hyper_copy general: query HyperCopy pair information.
- show hyper_copy_consistency_group general: query the basic information about a HyperCopy consistency group.
- show hyper_copy_consistency_group hyper_copy: query information about members in a HyperCopy consistency group.

## hyper_metro_consistency_group

- add hyper_metro_consistency_group pair: add a HyperMetro pair to a HyperMetro consistency group.
- change hyper_metro_consistency_group general: change the information about a HyperMetro consistency group.
- change hyper_metro_consistency_group pause: pause a HyperMetro consistency group.
- change hyper_metro_consistency_group priority: change the priority of the primary and secondary devices of a HyperMetro consistency group.
- change hyper_metro_consistency_group start: forcibly start a HyperMetro consistency group.
- change hyper_metro_consistency_group synchronize: start the synchronization of a HyperMetro consistency group.
- create hyper_metro_consistency_group general: create a HyperMetro consistency group.
- create hyper_metro_consistency_group protect_group: create a HyperMetro consistency group for a protection group.
- create hyper_metro_consistency_group verification_session: verify the configuration consistency of the primary and secondary devices of a HyperMetro consistency group.
- delete hyper_metro_consistency_group: delete a HyperMetro consistency group.
- remove hyper_metro_consistency_group pair: delete a pair from a HyperMetro consistency group.
- show hyper_metro_consistency_group general: query a HyperMetro consistency group.
- show hyper_metro_consistency_group pair: query the pairs in a HyperMetro consistency group.

## hyper_metro_domain

- add hyper_metro_domain quorum_server: add a quorum server to HyperMetro domains.
- change hyper_metro_domain general: change the information about HyperMetro.
- create hyper_metro_domain general: create a HyperMetro domain.
- delete hyper_metro_domain general: delete a HyperMetro domain.
- remove hyper_metro_domain quorum_server: remove a quorum server from HyperMetro domains.
- show hyper_metro_domain general: query HyperMetro domains.

## hyper_metro_pair

- change hyper_metro_pair general: change HyperMetro pair attributes.
- change hyper_metro_pair general: change HyperMetro pair attributes.
- change hyper_metro_pair pause: pause a HyperMetro pair.
- change hyper_metro_pair priority: change the priority of the primary and secondary LUNs of a SAN HyperMetro pair.
- change hyper_metro_pair start: forcibly start a HyperMetro pair.
- change hyper_metro_pair synchronize: start synchronizing a HyperMetro pair.
- create hyper_metro_pair unified: create a HyperMetro pair.
- create hyper_metro_pair verification_session: verify the configuration consistency of the primary and secondary devices of a HyperMetro pair.
- delete hyper_metro_pair general: delete a HyperMetro pair.
- show fs_hyper_metro_domain fs_pair: query file system-based HyperMetro pairs in a HyperMetro domain.
- show hyper_metro_pair general: query HyperMetro pairs.
- show vstore_pair hyper_metro_pair: query HyperMetro pairs in a vStore pair.

## kmc

- add kmc general: add the configuration of an external key management server.
- add kmc test: test the connectivity of an external key management server.
- change key_service general: modify the key service configuration.
- change kms key_backup: modify the key file backup server configurations of the internal key management service.
- delete kmc general: delete the configuration of an external key management server.
- export kms key: export the key file of the internal key management service.
- show key_service general: query the key service configuration.
- show kmc general: query the configurations of the external key management server.
- show kms key_backup: query the key file backup server configurations of the internal key management service.
- test kms key_backup: test the key file backup server configurations of the internal key management service.

## kmm

- test system trust: This **test system trust** command is used to test whether the system can be trusted and show the test result to users.

## lun_snapshot

- add hyper_cdp_schedule lun: add LUNs to a HyperCDP schedule.
- add hyper_cdp_schedule lun_consistency_group: add LUN consistency groups to a HyperCDP schedule.
- add hyper_cdp_schedule protect_group: add protection groups to a HyperCDP schedule.
- change hyper_cdp cancel_restore: cancel the rollback of a HyperCDP object.
- change hyper_cdp general: modify the name and restoration speed of a HyperCDP object.
- change hyper_cdp restore: restore data using HyperCDP objects. You can use the HyperCDP objects to restore the source LUN data by running this command.
- change hyper_cdp_consistency_group cancel_restore: **change hyper_cdp_consistency_group cancel_restore** command is used to cancel the restoration of a HyperCDP consistency group.
- change hyper_cdp_consistency_group general: modify the name and restoration speed of a HyperCDP consistency group.
- change hyper_cdp_consistency_group restore: restore data using HyperCDP consistency groups. You can use the HyperCDP consistency groups to restore the source protection group data by running this command.
- change hyper_cdp_schedule enabled: enable or disable a HyperCDP schedule.
- change hyper_cdp_schedule general: modify information about a HyperCDP schedule, including the name, schedule policy type, and time.
- change snapshot activate: activate snapshots.
- change snapshot cancel_restore: cancel the rollback of a snapshot.
- change snapshot capacity: modify the capacity of a snapshot.
- change snapshot deactivate: deactivate a snapshot.
- change snapshot description: modify the description of snapshots.
- change snapshot io_priority: change the I/O priority of the snapshot.
- change snapshot name: rename snapshots.
- change snapshot reactivate: reactivate snapshots. Use this command if you want to set the point in time of a snapshot to the latest point in time of the source LUN or HyperCDP object.
- change snapshot restore: roll back snapshots. You can use the snapshots to restore the destination LUN data by running this command.
- change snapshot speed: change the rollback speed of the snapshot.
- change snapshot_consistency_group activate: activate a snapshot consistency group.
- change snapshot_consistency_group cancel_restore: cancel restoration from a snapshot consistency group.
- change snapshot_consistency_group deactivate: deactivate a snapshot consistency group.
- change snapshot_consistency_group general: modify the properties of a snapshot consistency group.
- change snapshot_consistency_group reactivate: reactivate a snapshot consistency group.
- change snapshot_consistency_group restore: start restoration from a snapshot consistency group.
- create hyper_cdp general: create a HyperCDP object. You can create a point-in-time backup for a LUN by running this command.
- create hyper_cdp_consistency_group general: create a HyperCDP consistency group for a specified LUN consistency group.
- create hyper_cdp_consistency_group universal: create a HyperCDP consistency group for a specified protection group.
- create hyper_cdp_schedule general: create a HyperCDP schedule.
- create snapshot duplicate: create a duplicate for a snapshot or a HyperCDP object. You can back up a snapshot or a HyperCDP object by running this command.
- create snapshot general: create snapshots. You can create an identical and usable point-in-time duplicate for a data object by running this command.
- create snapshot_consistency_group duplicate: create a duplicate for a specified snapshot consistency group or HyperCDP consistency group.
- create snapshot_consistency_group general: create a snapshot consistency group for a specified LUN consistency group.
- create snapshot_consistency_group universal: create a snapshot consistency group for a specified LUN protection group.
- delete hyper_cdp: delete HyperCDP objects.
- delete hyper_cdp_consistency_group: delete HyperCDP consistency groups.
- delete hyper_cdp_schedule: delete HyperCDP schedules.
- delete snapshot: **delete snapshot**s.
- delete snapshot_consistency_group: delete a snapshot consistency group.
- remove hyper_cdp_schedule lun: remove LUNs from a HyperCDP schedule.
- remove hyper_cdp_schedule lun_consistency_group: remove LUN consistency groups from a HyperCDP schedule.
- remove hyper_cdp_schedule protect_group: remove protection groups from a HyperCDP schedule.
- show hyper_cdp general: query HyperCDP object information.
- show hyper_cdp_consistency_group cdp: query information about HyperCDP objects in a HyperCDP consistency group.
- show hyper_cdp_consistency_group general: query information about a HyperCDP consistency group.
- show hyper_cdp_consistency_group universal: query information about a HyperCDP consistency group.
- show hyper_cdp_schedule general: query information about a HyperCDP schedule.
- show hyper_cdp_schedule protect_group: query information about protection groups in a HyperCDP schedule.
- show lun_clone available_snapshot: query the snapshot for which the clone can be created.
- show snapshot available_lun: query the information on the logical unit numbers (LUNs) that can serve as snapshot source LUNs.
- show snapshot available_snapshot: query snapshots for which the snapshots can be created.
- show snapshot general: query snapshot information.
- show snapshot lun_group: query information about the LUN group that is associated with a snapshot.
- show snapshot_consistency_group general: query basic information about snapshot consistency groups.
- show snapshot_consistency_group snapshot: query information about member snapshots in a specified snapshot consistency group.
- show snapshot_consistency_group universal: query basic universal about snapshot consistency groups.

## quorum_server_for_server

- change quorum_server general: change the information about a third-place quorum server.
- create quorum_server general: create a third-place quorum server.
- delete quorum_server general: delete a third-place quorum server.
- remove quorum_server_link general: remove a specified link between a storage array and a quorum server.
- show quorum_server general: query third-place quorum servers.
- show quorum_server_link general: query the links between the disk array and quorum servers.

## quorum_server_link

- add quorum_server_link general: add a link between the disk array and a quorum server.

## remote_device

- change remote_device general: modify the name and link of remote devices.
- change remote_device user_password: The "**change remote_device user_password**" command is used to change the user's password that logging in to remote device.
- change remote_device white_list: modify the white list of heterogeneous disk arrays.
- create remote_device general: create remote devices. You must create a remote device by running this command before you can effortlessly perform remote replication tasks between the storage system and remote device.
- delete remote_device: delete a specific remote device. When the forcible deletion flag is set to "TRUE", this command can be used to forcibly delete a remote device.
- show remote_device elink: query information about the heterogeneous links connected to a storage system.
- show remote_device general: query information about a remote device.
- show remote_device link: query information about existing links to a storage system.
- show remote_device white_list: query the white list of heterogeneous disk arrays.

## remote_replication

- change remote_replication file_system: modify the settings of a specified file system remote replication pair.
- change remote_replication general: modify a specified remote replication pair.
- change remote_replication mode: change the replication mode of the remote replication pair.
- change remote_replication second_fs_access: set the read and write attributes of a secondary file system.
- change remote_replication split: split a remote replication task. During the split of a remote replication task, then data synchronization stops between both resources.
- change remote_replication synchronize: synchronize a specific remote replication. Use this command when you need to synchronize the data at the primary resource to a secondary resource to ensure data consistency.
- create remote_replication general: create a LUN-based remote replication pair.
- create remote_replication unified: create a remote replication pair.
- create remote_replication verification_session: verify remote replication tasks.
- delete remote_replication: delete a specific remote replication.
- show remote_replication general: query information about LUN-based remote replication pairs.
- show remote_replication unified: query information about remote replication pairs.
- swap remote_replication: implement primary/secondary resource switchover of a remote replication. Use this command when you need to copy the data at the secondary resource to the primary resource using remote replication.

## snapshot_group

- add snapshot_consistency_group snapshot: add snapshots to a specified snapshot consistency group.
- remove snapshot_consistency_group snapshot: remove snapshots from a specified snapshot consistency group.

## vstore_pair

- create vstore_pair general: create a vStore pair.
- delete vstore_pair general: delete a vStore pair.
- show fs_hyper_metro_domain vstore_pair: query vStore pairs in a file system-based HyperMetro domain.
- show vstore_pair general: query information about vStore pairs.
