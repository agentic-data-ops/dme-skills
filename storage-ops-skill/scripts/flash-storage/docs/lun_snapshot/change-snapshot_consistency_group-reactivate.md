# change snapshot_consistency_group reactivate


##### Function

The **change snapshot_consistency_group reactivate** command is used to reactivate a snapshot consistency group.

##### Format

**change snapshot_consistency_group reactivate** { snapshot_consistency_group_id=? \| snapshot_consistency_group_name=? } cdp_consistency_group_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_consistency_group_id | ID of the snapshot consistency group to be reactivated. | The value is an integer ranging from 0 to 16383.<br>You can run the show snapshot_consistency_group general command to view the value. |
| snapshot_consistency_group_name | Name of a snapshot consistency group. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.).<br>You can run the show snapshot_consistency_group general command to view the value. |
| cdp_consistency_group_id | ID of the HyperCDP consistency group. | The value is an integer from 0 to 99999.<br>To obtain the value, run "show hyper_cdp_consistency_group general". |

##### Usage Guidelines

None

##### Example

Reactivate snapshot consistency group "1" for HyperCDP consistency group "0".

```text
admin:/>change snapshot_consistency_group reactivate snapshot_consistency_group_id=1 cdp_consistency_group_id=0
DANGER: You are about to reactivate the snapshot consistency group, which is an irreversible operation. This operation will overwrite the data protected by the snapshot in the snapshot consistency group.
Suggestion: Before performing this operation, ensure that the selected snapshot consistency group is correct and you do not need the data protected by snapshots in the snapshot consistency group.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Reactivate snapshot consistency group "1".

```text
admin:/>change snapshot_consistency_group reactivate snapshot_consistency_group_id=1
DANGER: You are about to reactivate the snapshot consistency group, which is an irreversible operation. This operation will overwrite the data protected by the snapshot in the snapshot consistency group.
Suggestion: Before performing this operation, ensure that the selected snapshot consistency group is correct and you do not need the data protected by snapshots in the snapshot consistency group.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
