# show snapshot_consistency_group universal


##### Function

The **show snapshot_consistency_group universal** command is used to query basic universal about snapshot consistency groups.

##### Format

**show snapshot_consistency_group universal** \[ protect_group_id=? \| protect_group_name=? \| snapshot_consistency_group_id=? \| snapshot_consistency_group_name=? \]

##### Parameters

| Parameter                         | Description                                            | Value                                                                           |
|-----------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------|
| protect_group_id=?                | ID of the source LUN protection group to be queried.   | To obtain the value, run the "show protect_group general" command.              |
| protect_group_name=?              | Name of the source LUN protection group to be queried. | You can run the show protect_group general command to obtain the value.         |
| snapshot_consistency_group_id=?   | ID of the snapshot consistency group to be queried.    | To obtain the value, run the "show snapshot_consistency_group general" command. |
| snapshot_consistency_group_name=? | Name of the snapshot consistency group to be queried.  | To obtain the value, run the "show snapshot_consistency_group general" command. |

##### Usage Guidelines

None

##### Example

Query all snapshot consistency groups of a specified source LUN protection group.

```text
admin:/>show snapshot_consistency_group universal protect_group_id=0
ID  Name  Source Group ID  Source Group Name  Source Group Type  Running Status  Time Stamp                     Restore Speed
--  ----  ---------------  -----------------  -----------------  --------------  -----------------------------  -------------
0   s0    0                p0                 Protect group      Activated       2019-06-06/09:51:55 UTC+08:00  Middle
admin:/>
```

Query snapshot consistency group "2".

```text
admin:/>show snapshot_consistency_group universal snapshot_consistency_group_id=2

ID                                   : 2
Name                                 : snapConsistencyGroup1
Source Group ID                      : 1249
Source Group Name                    : lunConsistencyGroup1
Source Group Type                    : Protect group
Running Status                       : Activated
Time Stamp                           : 2018-04-26/08:39:43 UTC+08:00
Restore Speed                        : --
Description                          : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                                                                 |
|-------------------|-------------------------------------------------------------------------|
| ID                | ID of a snapshot consistency group.                                     |
| Name              | Name of a snapshot consistency group.                                   |
| Source Group ID   | ID of the source group corresponding to a snapshot consistency group.   |
| Source Group Name | Name of the source group corresponding to a snapshot consistency group. |
| Source Group Type | Type of the source group corresponding to a snapshot consistency group. |
| Running Status    | Running status of a snapshot consistency group.                         |
| Time Stamp        | Time when a snapshot consistency group is activated.                    |
| Restore Speed     | Rollback rate of a snapshot consistency group.                          |
| Description       | Description of a snapshot consistency group.                            |
