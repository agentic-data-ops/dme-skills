# remote_replication

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