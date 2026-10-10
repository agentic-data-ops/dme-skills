# change snapshot deactivate


##### Function

The **change snapshot deactivate** command is used to deactivate a snapshot.

##### Format

**change snapshot deactivate** { snapshot_id=? \| snapshot_id_list=? \| snapshot_name=? \| snapshot_name_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id=? | ID of a snapshot. | To obtain the value, run "show snapshot general". |
| snapshot_id_list=? | Snapshot ID list. | To obtain the value, run "show snapshot general". You can specify multiple snapshot IDs separated by commas (,), or an ID range separated by hyphens (-), such as: "0,5-8". |
| snapshot_name=? | Snapshot name. | To obtain the value, run "show snapshot general". |
| snapshot_name_list=? | Snapshot name. | To obtain the value, run "show snapshot general". Multiple snapshots can be activated at the same time. Separate multiple snapshot names with commas (,). |

##### Usage Guidelines

-   Only a snapshot in the state of activated can be deactivated.
-   Running this command erases the data of the selected snapshot.
-   Before running this command, ensure that the selected snapshot is exactly the one you want to deactivate.

##### Example

Deactivate snapshot "10".

```text
admin:/>change snapshot deactivate snapshot_id=10
DANGER: You are about to deactivate the snapshot. This operation will delete the snapshot data.
Suggestion: Before performing this operation, ensure that the selected snapshot is correct and considered to have no useful data.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Deactivate snapshots "11", "12", and "13".

```text
admin:/>change snapshot deactivate snapshot_id_list=11,12,13
DANGER: You are about to deactivate the snapshot. This operation will delete the snapshot data.
Suggestion: Before performing this operation, ensure that the selected snapshot is correct and considered to have no useful data.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Deactivate snapshot 11 from activated snapshots successfully.
Deactivate snapshot 12 from activated snapshots successfully.
Deactivate snapshot 13 from activated snapshots successfully.
```

##### System Response

None
