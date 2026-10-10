# change snapshot_consistency_group general


##### Function

The **change snapshot_consistency_group general** command is used to modify the properties of a snapshot consistency group.

##### Format

**change snapshot_consistency_group general** { snapshot_consistency_group_id=? \| snapshot_consistency_group_name=? } \[ name=? \] \[ restore_speed=? \] \[ description=? \]

##### Parameters

| Parameter                         | Description                                                          | Value                                                                                                                    |
|-----------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| snapshot_consistency_group_id=?   | ID of a snapshot consistency group.                                  | To obtain the value, run the "show snapshot_consistency_group general" command.                                          |
| snapshot_consistency_group_name=? | Name of a snapshot consistency group.                                | You can run the show snapshot_consistency_group general command to obtain the value.                                     |
| name=?                            | Name of the snapshot consistency group after modification.           | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |
| restore_speed=?                   | Rollback speed of the snapshot consistency group after modification. | \-                                                                                                                       |
| description=?                     | Description of the snapshot consistency group after modification.    | \-                                                                                                                       |

##### Usage Guidelines

Only the name, rollback speed, and description of the snapshot consistency group can be modified.

##### Example

Change the name of a snapshot consistency group.

```text
admin:/>change snapshot_consistency_group general snapshot_consistency_group_id=1 name=snapshotCg1
Command executed successfully.
```

Change the rollback speed of a snapshot consistency group.

```text
admin:/>change snapshot_consistency_group general snapshot_consistency_group_id=24 restore_speed=High
WARNING: You are about to change the rollback rate of the snapshot consistency group . This operation may cause heavy service load and decrease the read/write performance of the host.
Suggestion: Select the medium speed. If you select the high or highest speed, perform this operation during off-peak hours.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
