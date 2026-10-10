# change fs_hyper_cdp restore


##### Function

The **change fs_hyper_cdp restore** command is used to roll back a file system to a specified HyperCDP object.

##### Format

**change fs_hyper_cdp restore** \[ file_system_id=? \| file_system_name=? \| cdp_id=? \] \[ cdp_name=? \] \[ speed=? \]

**change fs_hyper_cdp restore** \[ file_system_id=? \| file_system_name=? \| cdp_id=? \] \[ cdp_name=? \] \[ speed=? \] \[ vstore_id=? \]

##### Parameters

| Parameter          | Description           | Value                                                  |
|--------------------|-----------------------|--------------------------------------------------------|
| file_system_id=?   | File system ID.       | To obtain the value, run "show file_system general".   |
| file_system_name=? | File system name.     | To obtain the value, run "show file_system general".   |
| cdp_id=?           | HyperCDP object ID.   | To obtain the value, run "show fs_hyper_cdp general".  |
| cdp_name=?         | HyperCDP object name. | To obtain the value, run "show fs_hyper_cdp general".  |
| speed=?            | Rollback speed.       | The value can be "Low", Middle", "High", or "Highest". |
| vstore_id=?        | vStore ID.            | vStore ID. The default value is "0".                   |

##### Usage Guidelines

Before running this command, check whether the HyperCDP object to which the file system is rolled back exists.

##### Example

Roll back the file system to the HyperCDP object whose ID is "1@snap1".

```text
admin:/>change fs_hyper_cdp restore cdp_id=1@snap1
DANGER: You are about to roll back data of the file system using a read-only snapshot. This operation will use data at the target time point to overwrite data of the file system.
Before performing this operation, ensure that the file system is not being read or written by the host, and that no data of the file system is stored in the host cache.
This operation will trigger a background copy task. The read/write performance of the host may decrease due to heavy service load.
Before the background copy task is complete, snapshots cannot be created and replication synchronization cannot be started for the file system.
Suggestions:
1. Before performing this operation, create a snapshot to back up data.
2. Before performing this operation, ensure that the correct snapshot is selected.
3. Ensure that the capacity of the file system and storage pool is sufficient.
4. Perform this operation during off-peak hours.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Roll back the file system whose name is "fs1" to the HyperCDP object whose name is "snap1", and the rollback speed is "Low".

```text
admin:/>change fs_hyper_cdp restore file_system_name=fs1 cdp_name=snap1 speed=Low
DANGER: You are about to roll back data of the file system using a read-only snapshot. This operation will use data at the target time point to overwrite data of the file system.
Before performing this operation, ensure that the file system is not being read or written by the host, and that no data of the file system is stored in the host cache.
This operation will trigger a background copy task. The read/write performance of the host may decrease due to heavy service load.
Before the background copy task is complete, snapshots cannot be created and replication synchronization cannot be started for the file system.
Suggestions:
1. Before performing this operation, create a snapshot to back up data.
2. Before performing this operation, ensure that the correct snapshot is selected.
3. Ensure that the capacity of the file system and storage pool is sufficient.
4. Perform this operation during off-peak hours.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the rollback speed of the file system whose ID is "1" to "Middle".

```text
admin:/>change fs_hyper_cdp restore file_system_id=1 speed=Middle
Command executed successfully.
```

##### System Response

None
