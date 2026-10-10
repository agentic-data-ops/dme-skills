# show hyper_copy_consistency_group general


##### Function

The **show hyper_copy_consistency_group general** command is used to query the basic information about a HyperCopy consistency group.

##### Format

**show hyper_copy_consistency_group general** \[ hyper_copy_consistency_group_id=? \]

##### Parameters

| Parameter                       | Description                     | Value                                           |
|---------------------------------|---------------------------------|-------------------------------------------------|
| hyper_copy_consistency_group_id | HyperCopy consistency group ID. | The value is an integer ranging from 1 to 4096. |

##### Usage Guidelines

None

##### Example

Query information about all HyperCopy consistency groups in the storage system.

```text
admin:/>show hyper_copy_consistency_group general
ID  Name   Health Status  Running Status  Copy Speed  Sync Start Time  Sync End Time
--  -----  -------------  --------------  ----------  ---------------  -------------
2   a0000  Normal         Unsynchronized    Middle      --               --
```

Query information about HyperCopy consistency group "2".

```text
admin:/>show hyper_copy_consistency_group general hyper_copy_consistency_group_id=2
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

| Parameter          | Meaning                                       |
|--------------------|-----------------------------------------------|
| ID                 | HyperCopy consistency group ID.               |
| Name               | Name of a HyperCopy consistency group.        |
| Health Status      | Health status of a HyperCopy pair.            |
| Running Status     | Running status of a HyperCopy pair.           |
| Copy Speed         | Copy speed.                                   |
| Sync Start Time    | Synchronization start time.                   |
| Sync End Time      | Synchronization end time.                     |
| Restore Start Time | Start time of reverse synchronization.        |
| Restore End Time   | End time of reverse synchronization.          |
| Description        | Description of a HyperCopy consistency group. |
