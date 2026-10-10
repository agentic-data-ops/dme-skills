# change snapshot restore


##### Function

The **change snapshot restore** command is used to roll back snapshots. You can use the snapshots to restore the destination LUN data by running this command.

##### Format

**change snapshot restore** { snapshot_id=? \| snapshot_name=? } \[ restore_speed=? \] \[ target_object_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id=? | ID of a snapshot. | To obtain the value, run "show snapshot general". |
| snapshot_name=? | Snapshot name. | To obtain the value, run "show snapshot general". |
| restore_speed=? | Rollback speed. | The value can be: <br>"Low": indicates the low speed.<br>"Middle": indicates the medium speed.<br>"High": indicates the high speed.<br>"Highest": indicates the highest speed.<br> The default value is "Middle". |
| target_object_id=? | Destination object ID. | To obtain the value, run the "show snapshot general source_lun_id" command. |

##### Usage Guidelines

-   Running this command overwrites the data of a destination LUN using that of an existing snapshot.
-   Before running this command, ensure that the data of the selected snapshot is exactly the data you want to restore to a destination LUN and that the destination LUN has been backed up.
-   You can roll back only a public snapshot that is in the activated state. To obtain the value, run "show snapshot general". All snapshots queried by the command "show snapshot general" are public snapshots.

##### Example

Roll back the data of a source LUN to that of snapshot "7" in the medium rollback rate.

```text
admin:/>change snapshot restore snapshot_id=7 restore_speed=Middle
DANGER: You are about to use snapshot to roll back target object. This operation will overwrite data on the target object with that on the snapshot. Before performing this operation, ensure that the target object is not being read or written by hosts, no data is saved on the cache of hosts and the source object is not written by hosts.
Suggestion:
1. Before performing this operation, back up the data on the target object.
2. Ensure that the free capacity of the storage pool is larger than the capacity occupied by the target object.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Roll back the data of a source LUN to that of snapshot "7" in the high rollback rate.

```text
admin:/>change snapshot restore snapshot_id=7 restore_speed=High
DANGER: You are about to use snapshot to roll back target object. This operation will overwrite data on the target object with that on the snapshot. This operation may cause heavy service loads and decrease the read/write performance of the host. Before performing this operation, ensure that the target object is not being read or written by hosts, no data is saved on the cache of hosts and the source object is not written by hosts.
Suggestion:
1. Before performing this operation, back up the data on the target object.
2. Ensure that the free capacity of the storage pool is larger than the capacity occupied by the target object.
3. Select the "Middle" speed. If you select the "High" or "Highest" speed, perform this operation when the service is idle.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
