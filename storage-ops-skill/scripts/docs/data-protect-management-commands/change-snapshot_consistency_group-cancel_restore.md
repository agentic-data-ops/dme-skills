# change snapshot_consistency_group cancel_restore


##### Function

The **change snapshot_consistency_group cancel_restore** command is used to cancel restoration from a snapshot consistency group.

##### Format

**change snapshot_consistency_group cancel_restore** { snapshot_consistency_group_id=? \| snapshot_consistency_group_name=? }

##### Parameters

| Parameter                       | Description                           | Value                                                                                                                          |
|---------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| snapshot_consistency_group_id   | ID of a snapshot consistency group.   | The value is an integer ranging from 0 to 16383.                                                                               |
| snapshot_consistency_group_name | Name of a snapshot consistency group. | The value is a string of 1 to 255 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

None

##### Example

Cancel restoration from snapshot consistency group "1".

```text
change snapshot_consistency_group cancel_restore snapshot_consistency_group_id=1
DANGER: You are about to stop rolling back snapshot data in snapshot consistency group to LUNs in protection group. This operation will cause data on LUNs in the protection group to be unavailable.
Suggestion: Before performing this operation, ensure that data on LUNs in the protection group is no longer needed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
