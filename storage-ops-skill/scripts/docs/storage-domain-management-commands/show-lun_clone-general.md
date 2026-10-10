# show lun_clone general


##### Function

The **show lun_clone general** command is used to query clone information.

##### Format

**show lun_clone general** { \[ clone_id=? \] \| \[ clone_name=? \] \| \[ source_id=? \] \| \[ source_name=? \] \| \[ source_type=? \] }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_id | Clone ID. The user can use this parameters to set an ID for the new clone. If the ID is specified, it cannot be changed. If you do not set this parameter, the storage system automatically allocates an ID for the clone based on IDs of created clones. | The value is an integer ranging from 0 to 65535. |
| clone_name | Name of a clone. | The value contains 1 to 255 characters including letters, digits, hyphens (-), underscores (_), and periods (.). |
| source_id | ID of a source LUN or a source snapshot. | To obtain the value, run "show lun_clone available_lun".<br>To obtain the value, run "show lun_clone available_snapshot". |
| source_name | Name of a source LUN or a source snapshot. | To obtain the value, run "show lun_clone available_lun".<br>To obtain the value, run "show lun_clone available_snapshot". |
| source_type | LUN or snapshot. | The value is either LUN or snapshot. |

##### Usage Guidelines

-   Run "**show lun_clone general**" to query information about all clones.
-   Run "**show lun_clone general** clone_id=?" to query information a clone whose ID is specified.
-   Run "**show lun_clone general** clone_name=?" to query information about a clone whose name is specified.
-   Run "**show lun_clone general** source_id=?" to query information about specified clone source LUN.

##### Example

Query detailed information about lun_clone "1".

```text
admin:/>show lun_clone general clone_id=1
ID                  : 1
Name                : clone_lun1
Pool ID             : 0
Capacity            : 100.000GB
Subscribed Capacity : 0.000B
Source ID           : 0
Source Name         : lun_1
Source Type         : Lun
Health Status       : Normal
Running Status      : Online
Time Stamp          : 2017-11-09/09:40:32 UTC+08:00
Split Status        : Not split
Split Start Time    : --
Estimated Split End Time      : --
Split Speed         : Middle
Split Progress(%)   : --
SmartQoS Policy ID  : --
IO Priority         : Low
```

Query information about all clones.

```text
admin:/>show lun_clone general
ID  Name        Source ID  Source Name  Source Type  Health Status  Running Status  Time Stamp                     Split Status  Split Start Time  Estimated Split End Time  Split Speed
--  ----------  ---------  -----------  -----------  -------------  --------------  -----------------------------  ------------  ----------------  --------------  -----------
1   clone_lun1  0          lun_1        Lun          Normal         Online          2017-11-09/09:40:32 UTC+08:00  Not split     --                --              Middle
```

##### System Response

The following table describes the parameter meanings.

| Parameter                | Meaning                                                      |
|--------------------------|--------------------------------------------------------------|
| ID                       | ID of clone.                                                 |
| Name                     | Name of clone.                                               |
| Source ID                | Source object ID of clone, including the LUN and snapshot.   |
| Source Name              | Source object name of clone, including the LUN and snapshot. |
| Source Type              | Source object type.                                          |
| Pool ID                  | Storage pool ID.                                             |
| Running Status           | Running status of clone.                                     |
| Health Status            | Health status of clone.                                      |
| Capacity                 | Capacity.                                                    |
| Subscribed Capacity      | The actual used capacity.                                    |
| Time Stamp               | Creation time of the clone.                                  |
| Split Status             | Split status.                                                |
| Split Speed              | Split speed.                                                 |
| Split Progress(%)        | Split progress (%).                                          |
| Split Start Time         | Split start time of clone.                                   |
| Estimated Split End Time | Estimated split end time of clone.                           |
| SmartQoS Policy ID       | SmartQoS ID.                                                 |
| IO Priority              | I/O priority of clone.                                       |
