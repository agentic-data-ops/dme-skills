# create snapshot_consistency_group duplicate


##### Function

The **create snapshot_consistency_group duplicate** command is used to create a duplicate for a specified snapshot consistency group or HyperCDP consistency group.

##### Format

**create snapshot_consistency_group duplicate** source_snapshot_consistency_group_name=? name=? \[ description=? \] \[ dst_lun_group_name=? \]

**create snapshot_consistency_group duplicate** source_snapshot_consistency_group_id=? name=? \[ description=? \] \[ dst_lun_group_id=? \]

**create snapshot_consistency_group duplicate** source_cdp_consistency_group_id=? name=? \[ description=? \] \[ dst_lun_group_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| source_snapshot_consistency_group_id | ID of the snapshot consistency group to duplicate. | To obtain the value, run "show snapshot_consistency_group general". |
| source_snapshot_consistency_group_name | Name of the snapshot consistency group for which a copy is to be created. | You can run the show snapshot_consistency_group general command to view the value. |
| source_cdp_consistency_group_id | ID of the HyperCDP consistency group to duplicate. | The value is an integer ranging from 0 to 99999.<br>To obtain the value, run "show hyper_cdp_consistency_group general". |
| name | Name of a duplicate. | - |
| description | Description of a duplicate. | - |
| dst_lun_group_id | ID of the target LUN group. | - |
| dst_lun_group_name | Name of the target LUN group. | - |

##### Usage Guidelines

None

##### Example

Create a duplicate for a specified snapshot consistency group.

```text
admin:/>create snapshot_consistency_group duplicate source_snapshot_consistency_group_id=1 name=d1
Command executed successfully.
```

Create a duplicate for a specified HyperCDP consistency group.

```text
admin:/>create snapshot_consistency_group duplicate source_cdp_consistency_group_id=2 name=d2
Command executed successfully.
```

Use target LUN group "0" to create a duplicate for a snapshot consistency group.

```text
admin:/>create snapshot_consistency_group duplicate source_snapshot_consistency_group_id=2 dst_lun_group_id=0 name=copy
WARNING: You are about to create a snapshot consistency group copy. This operation will reclaim data of the member LUNs in the target LUN group. Before this operation, ensure that the host is not reading or writing the member LUNs in the target LUN group, and no data of these LUN is stored in the host cache.
Suggestion: If you want to retain data of these LUN, back up the data in advance.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
