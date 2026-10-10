# remove snapshot_consistency_group snapshot


##### Function

The **remove snapshot_consistency_group snapshot** command is used to remove snapshots from a specified snapshot consistency group.

##### Format

**remove snapshot_consistency_group snapshot** snapshot_consistency_group_id=? snapshot_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_consistency_group_id | ID of the snapshot consistency group. | To obtain the value, run "show snapshot_consistency_group general". |
| snapshot_id_list | ID list of the snapshots to be removed. | To obtain the value, run "show snapshot general". If you want to concurrently remove multiple snapshots from a snapshot consistency group: <br>Separate multiple snapshot IDs by commas (,). For example, "snapshot_id_list=1,2,3,4,5".<br>Specify a snapshot ID range using a hyphen (-). For example, "snapshot_id_list=1-5,7,9-11". |

##### Usage Guidelines

None

##### Example

Remove the snapshots whose IDs are "2" and "3" from the snapshot consistency group whose ID is "1".

```text
admin:/>remove snapshot_consistency_group snapshot snapshot_consistency_group_id=1 snapshot_id_list=2,3
WARNING: You are about to remove snapshot  from snapshot consistency group. After the removal, the snapshot is not protected by the snapshot consistency group.
Suggestion: Before performing this operation, ensure that the snapshot does not need snapshot consistency group protection.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove Snapshot 2 from Snapshot consistency group successfully.
Remove Snapshot 3 from Snapshot consistency group successfully.
```

##### System Response

None
