# change snapshot_consistency_group activate


##### Function

The **change snapshot_consistency_group activate** command is used to activate a snapshot consistency group.

##### Format

**change snapshot_consistency_group activate** snapshot_consistency_group_id=? \[ cdp_consistency_group_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_consistency_group_id | ID of the snapshot consistency group to be activated. | The value is an integer from 0 to 16383.<br>To obtain the value, run "show snapshot_consistency_group general". |
| cdp_consistency_group_id | ID of the HyperCDP consistency group. | The value is an integer from 0 to 99999.<br>To obtain the value, run "show hyper_cdp_consistency_group general". |

##### Usage Guidelines

None

##### Example

Activate snapshot consistency group "1" for HyperCDP consistency group "0".

```text
admin:/>change snapshot_consistency_group activate snapshot_consistency_group_id=1 cdp_consistency_group_id=0
DANGER: You are about to activate snapshot consistency group.
Suggestion: Before performing this operation, ensure that the storage pool capacity is sufficient.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Activate snapshot consistency group "1".

```text
admin:/>change snapshot_consistency_group activate snapshot_consistency_group_id=1
DANGER: You are about to activate snapshot consistency group.
Suggestion: Before performing this operation, ensure that the storage pool capacity is sufficient.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
