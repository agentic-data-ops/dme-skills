# change snapshot_consistency_group deactivate


##### Function

The **change snapshot_consistency_group deactivate** command is used to deactivate a snapshot consistency group.

##### Format

**change snapshot_consistency_group deactivate** snapshot_consistency_group_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_consistency_group_id | ID of the snapshot consistency group to be deactivated. | The value is an integer from 0 to 16383.<br>To obtain the value, run "show snapshot_consistency_group general". |

##### Usage Guidelines

None

##### Example

Deactivate snapshot consistency group "1".

```text
admin:/>change snapshot_consistency_group deactivate snapshot_consistency_group_id=1
DANGER: You are about to deactivate snapshot consistency group.This operation will delete the snapshot data.
Suggestion: Before performing this operation, ensure that the snapshot consistency group is correctly selected and the snapshots does not contain the data to be used.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
