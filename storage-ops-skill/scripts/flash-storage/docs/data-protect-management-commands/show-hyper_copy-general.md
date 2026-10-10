# show hyper_copy general


##### Function

The **show hyper_copy general** command is used to query HyperCopy pair information.

##### Format

**show hyper_copy general** \[ hyper_copy_id=? \] \[ name=? \] \[ source_lun_id=? \]

##### Parameters

| Parameter     | Description                          | Value                                                                                                             |
|---------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| hyper_copy_id | HyperCopy pair ID.                   | The value is an integer ranging from 0 to 65535.                                                                  |
| name          | HyperCopy pair name.                 | The value contains 1 to 255 characters including letters, digits, hyphens (-), underscores (\_), and periods (.). |
| source_lun_id | Source LUN ID or source snapshot ID. | The value is an integer ranging from 0 to 65535.                                                                  |

##### Usage Guidelines

-   Run "**show hyper_copy general**" to query information about all HyperCopy pairs.
-   Run "**show hyper_copy general** hyper_copy_id=?" to query information about a HyperCopy pair whose ID is specified.
-   Run "**show hyper_copy general** name=?" to query information about a HyperCopy pair whose name is specified.
-   Run "**show hyper_copy general** source_lun_id=?" to query information about a HyperCopy pair whose source LUN ID is specified.

##### Example

Query information about HyperCopy pair "3".

```text
admin:/>show hyper_copy general hyper_copy_id=3

ID                      : 3
Name                    : www
Source ID               : 2
Source Type             : LUN
Target ID               : 3
Health Status           : Normal
Running Status          : Normal
Copy Speed              : High
HyperCopy Cg ID        : --
Sync Start Time         : 2018-08-14/16:12:44 UTC+08:00
Sync End Time           : 2018-08-14/16:12:44 UTC+08:00
Restore Start Time      : 2018-08-14/15:27:19 UTC+08:00
Restore End Time        : 2018-08-14/15:27:19 UTC+08:00
Progress(%)             : --
Estimated Copy End Time : --
Description             :
```

Query information of all HyperCopy pairs.

```text
admin:/>show hyper_copy general
ID   Name  Source ID  Source Type   Target ID   Health Status  Running Status  Copy Speed  HyperCopy Cg ID  Sync Start Time  Sync End Time
---  ----  ---------  -----------  ----------  -------------  --------------   ----------  ---------------  ---------------  -------------
2    cl       0          LUN           2            Normal    Unsynchronized        Middle        --              --               --
```

##### System Response

The following table describes the parameter meanings.

| Parameter               | Meaning                                                              |
|-------------------------|----------------------------------------------------------------------|
| ID                      | HyperCopy pair ID.                                                   |
| Name                    | HyperCopy pair name.                                                 |
| Source ID               | ID of a HyperCopy pair source object, including a LUN or a snapshot. |
| Source Type             | Source object type.                                                  |
| Target ID               | ID of a HyperCopy pair target object (only LUN supported).           |
| Running Status          | Running status of a HyperCopy pair.                                  |
| Health Status           | Health status of a HyperCopy pair.                                   |
| Copy Speed              | Copy speed.                                                          |
| HyperCopy Cg ID         | HyperCopy consistency group ID.                                      |
| Sync Start Time         | Synchronization start time.                                          |
| Sync End Time           | Synchronization end time.                                            |
| Restore Start Time      | Start time of reverse synchronization.                               |
| Restore End Time        | End time of reverse synchronization.                                 |
| Progress(%)             | Copy progress.                                                       |
| Estimated Copy End Time | Estimated copy end time.                                             |
| Description             | HyperCopy description.                                               |
