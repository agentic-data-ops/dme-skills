# show lun_consistency_group snapshot_consistency_group


##### Function

The **show lun_consistency_group snapshot_consistency_group** command is used to query information about snapshot consistency groups related to LUN consistency groups.

##### Format

**show lun_consistency_group snapshot_consistency_group** lun_consistency_group_id=?

##### Parameters

| Parameter                  | Description                                    | Value                                                                                         |
|----------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------|
| lun_consistency_group_id=? | ID of the LUN consistency group to be queried. | To obtain the value, run the "show lun_consistency_group general" command without parameters. |

##### Usage Guidelines

Run the "**show lun_consistency_group snapshot_consistency_group** lun_consistency_group_id=?" command to query information about snapshot consistency groups related to LUN consistency groups.

##### Example

Query information about the snapshot consistency group related to a specified LUN consistency group.

```text
admin:/>show lun_consistency_group snapshot_consistency_group lun_consistency_group_id=1
ID  Name  Running Status  Time Stamp
--  ----  --------------  -----------------------------
1   scg2  Activated       2018-06-29/18:23:29 UTC+08:00
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                               |
|----------------|---------------------------------------|
| ID             | ID of a snapshot consistency group.   |
| Name           | Name of a snapshot consistency group. |
| Running Status | Running status.                       |
| Time Stamp     | Creation time.                        |
