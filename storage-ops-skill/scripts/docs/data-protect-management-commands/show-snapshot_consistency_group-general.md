# show snapshot_consistency_group general


##### Function

The **show snapshot_consistency_group general** command is used to query basic information about snapshot consistency groups.

##### Format

**show snapshot_consistency_group general** \[ source_lun_consistency_group_id=? \| snapshot_consistency_group_id=? \| snapshot_consistency_group_name=? \]

##### Parameters

| Parameter                         | Description                                           | Value                                                                                                                                                                                                                            |
|-----------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| source_lun_consistency_group_id=? | ID of the source LUN consistency group to be queried. | To obtain the value, run the "show lun_consistency_group general" command.                                                                                                                                                       |
| snapshot_consistency_group_id=?   | ID of the snapshot consistency group to be queried.   | To obtain the value, run the "**show snapshot_consistency_group general**" command. |
| snapshot_consistency_group_name=? | Name of the snapshot consistency group to be queried. | To obtain the value, run the "**show snapshot_consistency_group general**" command. |

##### Usage Guidelines

In the current version, you are advised to run the "show snapshot_consistency_group universal" command rather than the "**show snapshot_consistency_group general**" command to query the basic information about a snapshot consistency group.

##### Example

Query all snapshot consistency groups of a specified source LUN consistency group.

```text
admin:/>show snapshot_consistency_group general source_lun_consistency_group_id=2
ID    Name                  Source Lun Consistency Group ID  Source Lun Consistency Group Name       Running Status    Time Stamp                       Restore Speed
----  --------------------  -------------------------------  ------------------------------      -------------     --------------                   ----------------
1251  YvPlaR_445h853330000  1249                             Ky_443W543240001                    Activated           2018-04-26/08:39:43 UTC+08:00  Middle
```

Query snapshot consistency group "2".

```text
admin:/>show snapshot_consistency_group general snapshot_consistency_group_id=2

ID                                   : 2
Name                                 : snapConsistencyGroup1
Source Lun Consistency Group ID      : 1249
Source Lun Consistency Group Name    : lunConsistencyGroup1
Running Status                       : Activated
Time Stamp                           : 2018-04-26/08:39:43 UTC+08:00
Restore Speed                        : --
Description                          : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                         | Meaning                                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------------|
| ID                                | ID of a snapshot consistency group.                                                     |
| Name                              | Name of a snapshot consistency group.                                                   |
| Source Lun consistency group ID   | ID of the source LUN consistency group corresponding to a snapshot consistency group.   |
| Source Lun consistency group Name | Name of the source LUN consistency group corresponding to a snapshot consistency group. |
| Running Status                    | Running status of a snapshot consistency group.                                         |
| Time Stamp                        | Time when a snapshot consistency group is activated.                                    |
| Restore Speed                     | Rollback rate of a snapshot consistency group.                                          |
| Description                       | Description of a snapshot consistency group.                                            |
