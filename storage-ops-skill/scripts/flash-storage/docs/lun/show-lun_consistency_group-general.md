# show lun_consistency_group general


##### Function

The **show lun_consistency_group general** command is used to query information about LUN consistency groups in the storage system.

##### Format

**show lun_consistency_group general** \[ lun_consistency_group_id=? \| lun_consistency_group_name=? \]

##### Parameters

| Parameter                    | Description                                      | Value                                                                                                                                                                                                                            |
|------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lun_consistency_group_id=?   | ID of the LUN consistency group to be queried.   | To obtain the value, run the "**show lun_consistency_group general**" command without parameters. |
| lun_consistency_group_name=? | Name of the LUN consistency group to be queried. | To obtain the value, run the "**show lun_consistency_group general**" command without parameters. |

##### Usage Guidelines

-   Run the "**show lun_consistency_group general**" command to query information about all LUN consistency groups in the storage system.
-   Run the "**show lun_consistency_group general** lun_consistency_group_id=?" command to query information about a specified LUN consistency group.

##### Example

Query information about all LUN consistency groups in the storage system.

```text
admin:/>show lun_consistency_group general
ID  Name  Running Status  ScheduleId
--  ----  --------------  ----------
1   cg1   Normal          --
```

Query information about the LUN consistency group whose ID is "1".

```text
developer:/>show lun_consistency_group general lun_consistency_group_id=1
ID              : 1
Name            : cg1
Running Status  : Normal
ScheduleId      : --
Description     :
Disable Schedule Policy : None
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                                  |
|----------------|----------------------------------------------------------|
| ID             | ID of a LUN consistency group.                           |
| Name           | Name of a LUN consistency group.                         |
| Running Status | Running status.                                          |
| ScheduleId     | ID of a HyperCDP schedule for the LUN consistency group. |
| Description    | Description.                                             |
