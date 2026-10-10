# change snapshot io_priority


##### Function

The **change snapshot io_priority** command is used to change the I/O priority of the snapshot.

##### Format

**change snapshot io_priority** { snapshot_id=? \| snapshot_name=? } io_priority=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id=? | ID of a snapshot. | To obtain the value, run "show snapshot general". |
| snapshot_name=? | Snapshot name. | To obtain the value, run "show snapshot general". |
| io_priority=? | I/O priority of a snapshot. | The value can be "Low", "Middle", or "High", where: <br>"Low": indicates the low priority.<br>"Middle": indicates the medium priority.<br>"High": indicates the high priority. |

##### Usage Guidelines

Run **change snapshot io_priority** snapshot_id=? io_priority=? to set the I/O priority of a specified snapshot.

##### Example

Change the I/O priority of snapshot "1" to "High".

```text
admin:/>change snapshot io_priority snapshot_id=1 io_priority=High
WARNING: You are about to change the priority of snapshot. This operation may affect snapshot performance. When a timing snapshot is used, it is converted to a common snapshot.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the correct snapshot is selected.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
