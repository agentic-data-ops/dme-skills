# change snapshot_consistency_group restore


##### Function

The **change snapshot_consistency_group restore** command is used to start restoration from a snapshot consistency group.

##### Format

**change snapshot_consistency_group restore** { snapshot_consistency_group_id=? \| snapshot_consistency_group_name=? } \[ restore_speed=? \]

##### Parameters

| Parameter                       | Description                                        | Value                                                                                                                          |
|---------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| snapshot_consistency_group_id   | ID of a snapshot consistency group.                | The value is an integer ranging from 0 to 16383.                                                                               |
| snapshot_consistency_group_name | Name of a snapshot consistency group.              | The value is a string of 1 to 255 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |
| restore_speed                   | Restoration speed of a snapshot consistency group. | \-                                                                                                                             |

##### Usage Guidelines

None

##### Example

Start restoration from snapshot consistency group "1".

```text
change snapshot_consistency_group restore snapshot_consistency_group_id=1
WARNING: You are about to roll back data using the snapshot consistency group. This operation will use snapshot data in snapshot consistency group to overwrite data on LUNs in protection group. This operation may cause heavy service load and decrease the read/write performance of the host. Before performing this operation, ensure that LUNs in the protection group are not read or written by the host, no data is stored in the host cache, and snapshots in the snapshot consistency group are not written by the host.
Suggestion:
1. Before performing this operation, back up data of the protection group.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity occupied by LUNs in the protection group.
3. Select the medium speed. If you select the high or highest speed, perform this operation during off-peak hours.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
