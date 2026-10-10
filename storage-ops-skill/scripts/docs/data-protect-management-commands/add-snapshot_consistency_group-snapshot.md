# add snapshot_consistency_group snapshot


##### Function

The **add snapshot_consistency_group snapshot** command is used to add snapshots to a specified snapshot consistency group.

##### Format

**add snapshot_consistency_group snapshot** snapshot_consistency_group_id=? snapshot_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_consistency_group_id | ID of the snapshot consistency group to which you want to add snapshots. | To obtain the value, run "show snapshot_consistency_group general". |
| snapshot_id_list | ID list of the snapshots to be added. | To obtain the value, run "show snapshot general". If you want to concurrently add multiple snapshots to a snapshot consistency group: <br>Separate multiple snapshot IDs by commas (,). For example, "snapshot_id_list=1,2,3,4,5".<br>Specify a snapshot ID range using a hyphen (-). For example, "snapshot_id_list=1-5,7,9-11". |

##### Usage Guidelines

None

##### Example

Add the snapshot whose ID is "2" to the snapshot consistency group whose ID is "1".

```text
admin:/>add snapshot_consistency_group snapshot snapshot_consistency_group_id=1 snapshot_id_list=2
Add Snapshot 2 to Snapshot consistency group successfully.
```

##### System Response

None
