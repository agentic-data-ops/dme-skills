# show clone general


##### Function

The **show clone general** command is used to query clone pair information.

##### Format

**show clone general** \[ clone_id=? \] \[ name=? \] \[ source_lun_id=? \] \[ source_lun_name=? \]

##### Parameters

| Parameter         | Description                            | Value                                                                                                              |
|-------------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| clone_id=?        | ID of a clone pair.                    | The value is an integer ranging from 0 to 65535.                                                                   |
| name=?            | Name of a clone pair.                  | The value contains 1 to 255 characters, including letters, digits, hyphens (-), underscores (\_), and periods (.). |
| source_lun_id=?   | Source LUN ID or source snapshot ID.   | The value is an integer ranging from 0 to 65535.                                                                   |
| source_lun_name=? | Source LUN ID or source snapshot name. | The value contains 1 to 255 characters, including letters, digits, hyphens (-), underscores (\_), and periods (.). |

##### Usage Guidelines

-   Run "**show clone general**" to query information about all clone pairs.
-   Run "**show clone general** clone_id=?" to query information about a clone pair whose ID is specified.
-   Run "**show clone general** name=?" to query information about a clone pair whose name is specified.
-   Run "**show clone general** source_lun_id=?" to query information about a clone pair whose source LUN ID is specified.

##### Example

Query information about clone pair "3".

```text
admin:/>show clone general clone_id=3

ID                      : 3
Name                    : www
Source ID               : 2
Source Type             : LUN
Target ID               : 3
Health Status           : Normal
Running Status          : Normal
Copy Speed              : High
Clone Cg ID             : --
Sync Start Time         : 2018-08-14/16:12:44 UTC+08:00
Sync End Time           : 2018-08-14/16:12:44 UTC+08:00
Restore Start Time      : 2018-08-14/15:27:19 UTC+08:00
Restore End Time        : 2018-08-14/15:27:19 UTC+08:00
Progress(%)             : --
Estimated Copy End Time : --
Description             :
```

Query information of all clone pairs.

```text
admin:/>show clone general
ID   Name  Source ID  Source Type   Target ID   Health Status  Running Status  Copy Speed    Clone Cg ID    Sync Start Time  Sync End Time
---  ----  ---------  -----------  ----------  -------------  --------------   ----------  ---------------  ---------------  -------------
2    cl       0          LUN           2            Normal    Unsynchronized        Middle        --              --               --
```

##### System Response

The following table describes the parameter meanings.

| Parameter               | Meaning                                                           |
|-------------------------|-------------------------------------------------------------------|
| ID                      | Clone pair ID.                                                    |
| Name                    | Clone pair name.                                                  |
| Source ID               | ID of a clone pair source object, including a LUN and a snapshot. |
| Source Type             | Source object type.                                               |
| Target ID               | ID of a clone pair target object (only LUN supported).            |
| Running Status          | Running status of a clone pair.                                   |
| Health Status           | Health status of a clone pair.                                    |
| Copy Speed              | Copy speed.                                                       |
| Clone Cg ID             | Clone consistency group ID.                                       |
| Sync Start Time         | Synchronization start time.                                       |
| Sync End Time           | Synchronization end time.                                         |
| Restore Start Time      | Start time of reverse synchronization.                            |
| Restore End Time        | End time of reverse synchronization.                              |
| Progress(%)             | Copy progress.                                                    |
| Estimated Copy End Time | Estimated copy end time.                                          |
| Description             | Clone pair description.                                           |
