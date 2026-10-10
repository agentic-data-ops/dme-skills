# change snapshot description


##### Function

The **change snapshot description** command is used to modify the description of snapshots.

##### Format

**change snapshot description** { snapshot_id=? \| snapshot_name=? } { description=? \| clear_description=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id=? | ID of a snapshot. | To obtain the value, run "show snapshot general". |
| snapshot_name=? | Snapshot name. | To obtain the value, run "show snapshot general". |
| description | Updated description of a snapshot. | - |
| clear_description | Clear the description. | The value can be: "enable": clears the description. |

##### Usage Guidelines

None

##### Example

Modify the description of snapshot "1" to "SnapshotDescription".

```text
admin:/>change snapshot description snapshot_id=1 description=SnapshotDescription
CAUTION: You are about to modify the name or description of snapshot. This operation will change the name or description of a snapshot. When a timing snapshot is used, it is converted to a common snapshot.
Suggestion: Select a correct snapshot.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
