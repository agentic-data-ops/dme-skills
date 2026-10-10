# delete remote_replication


##### Function

The **delete remote_replication** command is used to delete a specific remote replication.

##### Format

**delete remote_replication** remote_replication_id=? \[ is_local_delete=? \] \[ is_restore_secondary_lun_when_delete=? \] \[ is_restore_secondary_fs_when_delete=? \] \[ is_force_delete=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_replication_id=? | ID of a remote replication. | To obtain the value, run "show remote_replication unified". |
| is_local_delete=? | Whether a remote replication can be locally deleted when the link is down. | The value can be: <br>"yes": The remote replication task can be locally deleted.<br>"no": The remote replication task cannot be locally deleted.<br> The default value is "no". |
| is_restore_secondary_lun_when_delete=? | Whether data on the secondary LUN needs to be rolled back to ensure data consistency when you delete a remote replication. This parameter is used to delete LUN-based remote replications only. | The value can be: <br>"yes": to ensure the consistency of the data on the secondary LUN.<br>"no": not to ensure the consistency of the data on the secondary LUN.<br> The default value is "yes", where data on the secondary LUN will be forcibly rolled back if data inconsistency occurs before the remote replication is deleted. |
| is_restore_secondary_fs_when_delete=? | Whether data on the secondary file system needs to be rolled back to ensure data consistency when you delete a remote replication. This parameter is used to delete file system-based remote replications only. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value can be: <br>"yes": to ensure the consistency of the data on the secondary file system.<br>"no": not to ensure the consistency of the data on the secondary file system.<br> The default value is "yes", where data on the secondary file system will be forcibly rolled back if data inconsistency occurs before the remote replication is deleted. |

##### Usage Guidelines

Before running this command, ensure that the selected remote replication task is exactly the one you want to delete.

##### Example

Delete remote replication "2100f102030405060000000200000000".

```text
admin:/>delete remote_replication remote_replication_id=2100f102030405060000000200000000
WARNING: You are about to delete remote replication. This operation will delete the replication relationships between the primary resource and all secondary resources in the remote replication, and this operation cannot be undone. If you want to ensure that the secondary resources can be used, use is_restore_secondary_lun_when_delete=yes or is_restore_secondary_fs_when_delete=yes.
Suggestion: Before performing this operation, confirm that you have selected the correct remote replication.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
