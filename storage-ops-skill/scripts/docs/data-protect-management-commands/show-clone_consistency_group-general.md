# show clone_consistency_group general


##### Function

The **show clone_consistency_group general** command is used to query the basic information about a clone consistency group.

##### Format

**show clone_consistency_group general** \[ clone_consistency_group_id=? \| clone_consistency_group_name=? \]

##### Parameters

| Parameter                      | Description                   | Value                                                                                                                                                                                                                         |
|--------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| clone_consistency_group_id=?   | Clone consistency group ID.   | You can run the **show clone_consistency_group general** command to obtain the value. |
| clone_consistency_group_name=? | Clone consistency group name. | You can run the **show clone_consistency_group general** command to obtain the value. |

##### Usage Guidelines

None

##### Example

Query information about all clone consistency groups in the storage system.

```text
admin:/>show clone_consistency_group general
ID  Name   Health Status  Running Status  Copy Speed  Sync Start Time  Sync End Time
--  -----  -------------  --------------  ----------  ---------------  -------------
2   a0000  Normal         Unsynchronized    Middle      --               --
```

Query information about clone consistency group "2".

```text
admin:/>show clone_consistency_group general clone_consistency_group_id=2
ID                 : 2
Name               : a0000
Health Status      : Normal
Running Status     : Unsynchronized
Copy Speed         : Middle
Sync Start Time    : --
Sync End Time      : --
Restore Start Time : --
Restore End Time   : --
Description        : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                                   |
|--------------------|-------------------------------------------|
| ID                 | Clone consistency group ID.               |
| Name               | Name of a clone consistency group.        |
| Health Status      | Health status of a clone pair.            |
| Running Status     | Running status of a clone pair.           |
| Copy Speed         | Copy speed.                               |
| Sync Start Time    | Synchronization start time.               |
| Sync End Time      | Synchronization end time.                 |
| Restore Start Time | Start time of reverse synchronization.    |
| Restore End Time   | End time of reverse synchronization.      |
| Description        | Description of a clone consistency group. |
