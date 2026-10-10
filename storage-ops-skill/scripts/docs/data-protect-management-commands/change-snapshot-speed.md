# change snapshot speed


##### Function

The **change snapshot speed** command is used to change the rollback speed of the snapshot.

##### Format

**change snapshot speed** { snapshot_id=? restore_speed=? \| snapshot_name=? restore_speed=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id=? | ID of a snapshot. | To obtain the value, run "show snapshot general". |
| snapshot_name=? | Snapshot name. | To obtain the value, run "show snapshot general". |
| restore_speed=? | Rollback speed. | The value can be "Low", "Middle", "High", or "Highest", where: <br>"Low": indicates the low speed.<br>"Middle": indicates the medium speed.<br>"High": indicates the high speed.<br>"Highest": indicates the highest speed. |

##### Usage Guidelines

You can only change the rollback speed of a snapshot being used for rollback.

##### Example

Change the rollback speed for snapshot "7" to "low".

```text
admin:/>change snapshot speed snapshot_id=7 restore_speed=low
Command executed successfully.
```

##### System Response

None
