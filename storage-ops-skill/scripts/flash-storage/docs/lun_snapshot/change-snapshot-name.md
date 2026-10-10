# change snapshot name


##### Function

The **change snapshot name** command is used to rename snapshots.

##### Format

**change snapshot name** { snapshot_id=? name=? \| snapshot_name=? name=? }

##### Parameters

| Parameter       | Description                 | Value                                                                                                             |
|-----------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------|
| snapshot_id=?   | ID of a snapshot.           | To obtain the value, run "show snapshot general".                                                                 |
| snapshot_name=? | Snapshot name.              | To obtain the value, run "show snapshot general".                                                                 |
| name=?          | Updated name of a snapshot. | The value contains 1 to 255 characters including letters, digits, hyphens (-), underscores (\_), and periods (.). |

##### Usage Guidelines

An updated name of a snapshot must be different from the names of all existing snapshots and LUNs.

##### Example

Rename snapshot "1" to "SnapshotName".

```text
admin:/>change snapshot name snapshot_id=1 name=SnapshotName
CAUTION: You are about to modify the name or description of snapshot. This operation will change the name or description of a snapshot. When a timing snapshot is used, it is converted to a common snapshot.
Suggestion: Select a correct snapshot.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
