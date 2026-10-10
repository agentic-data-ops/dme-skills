# delete snapshot


##### Function

The **delete snapshot** command is used to **delete snapshot**s.

##### Format

**delete snapshot** snapshot_id_list=? \[ is_delete_dst_lun=? \]

**delete snapshot** snapshot_name_list=? \[ is_delete_dst_lun=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id_list=? | ID of a snapshot. | To obtain the value, run "show snapshot general". Multiple snapshots are separated by commas(,), or an ID range is separated by hyphens(-), such as: "0, 5-8". |
| snapshot_name_list=? | Snapshot name. | To obtain the value, run "show snapshot general". Multiple snapshots can be activated at the same time. Separate multiple snapshot names with commas (,). |
| is_delete_dst_lun | Whether to delete the target LUN. If this parameter is not specified, the target LUN is deleted by default. | The value can be "yes" or "no", where: <br>"yes": Delete the target LUN.<br>"no": Do not delete the target LUN. |

##### Usage Guidelines

-   Multiple snapshots can be deleted in the mean time.
-   Before running this command, ensure that the selected snapshots are exactly the ones you want to delete and that the snapshots are no longer needed.

##### Example

Delete the snapshot whose ID is "1".

```text
admin:/>delete snapshot snapshot_id_list=1
WARNING: You are about to delete snapshot. This operation cannot be undone. This operation will delete the information about the snapshot from the system.
Suggestion: Before performing this operation, ensure that the selected snapshot is no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Delete snapshot 1 successfully.
```

Delete the snapshot whose ID is "2".

```text
admin:/>delete snapshot snapshot_id_list=2 is_delete_dst_lun=no
WARNING: You are about to delete a snapshot. This operation cannot be undone. After this operation, the relationship between the snapshot and source LUN will be interrupted, and snapshot data will be reclaimed.
Suggestion: Before performing this operation, ensure that the correct snapshot is selected and that data protected by the snapshot is no longer needed.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete snapshot 2 successfully.
```

##### System Response

None
