# delete snapshot_consistency_group


##### Function

The **delete snapshot_consistency_group** command is used to delete a snapshot consistency group.

##### Format

**delete snapshot_consistency_group** { snapshot_consistency_group_id_list=? \| snapshot_consistency_group_name_list=? } \[ is_delete_dst_lun=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_consistency_group_id_list=? | ID of the snapshot consistency group to be deleted. | To obtain the value, run "show snapshot_consistency_group general". |
| snapshot_consistency_group_name_list=? | Name of the snapshot consistency group to be deleted. | To obtain the value, run the "show snapshot_consistency_group general" command. |
| is_delete_dst_lun=? | Whether to delete the target LUN. If the target LUN is not delivered, the target LUN is deleted by default. | The value can be "yes" or "no", where: <br>"yes": The target LUN is deleted.<br>"no": The target LUN is not deleted. |

##### Usage Guidelines

After a snapshot consistency group is deleted, its member snapshots are also deleted. Data once protected at this point in time will no longer be protected.

##### Example

Delete snapshot consistency group "2".

```text
admin:/>delete snapshot_consistency_group snapshot_consistency_group_id_list=2
WARNING: You are about to delete the snapshot consistency group , which is an irreversible operation. If you delete a consistency group, all snapshots and data in the consistency group will be deleted.
Suggestion: Before performing this operation, ensure that the selected snapshot consistency group is correct and you do not need data in the snapshot.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete snapshot consistency group 2 successfully.
```

Delete snapshot consistency group "1".

```text
admin:/>delete snapshot_consistency_group snapshot_consistency_group_id_list=1 is_delete_dst_lun=no
WARNING: You are about to delete a snapshot consistency group. This operation cannot be undone. After this operation, the relationship between the snapshot and source LUN will be interrupted, and snapshot data will be reclaimed.
Suggestion: Before performing this operation, ensure that the correct snapshot consistency group is selected and that data protected by the snapshot is no longer needed.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete snapshot consistency group 1 successfully.
```

##### System Response

None
