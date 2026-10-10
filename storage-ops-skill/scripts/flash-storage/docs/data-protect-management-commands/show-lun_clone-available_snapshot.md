# show lun_clone available_snapshot


##### Function

The **show lun_clone available_snapshot** command is used to query the snapshot for which the clone can be created.

##### Format

**show lun_clone available_snapshot**

##### Parameters

| Parameter  | Description    | Value                        |
|------------|----------------|------------------------------|
| usage_type | Snapshot type. | The value can be "LUN_SNAP". |

##### Usage Guidelines

Run "**show lun_clone available_snapshot**" to query the snapshot for which the clone can be created.

##### Example

Query snapshots for which clones can be created.

```text
admin:/>show lun_clone available_snapshot
ID  Name  Source LUN ID  Source LUN Name  Health Status  Running Status  WWN                               Time Stamp                     Parent ID  Parent Name  Cascaded Level
--  ----  -------------  ---------------  -------------  --------------  --------------------------------  -----------------------------  ---------  -----------  --------------
3   snap  2              lun              Normal         Activated       688cf98100dac530001314bc00000003  2017-08-02/12:53:50 UTC+08:00  2          lun          0
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                |
|-----------------|----------------------------------------|
| ID              | ID of the snapshot.                    |
| Name            | Name of the snapshot.                  |
| Source LUN ID   | Source LUN ID of the snapshot.         |
| Source LUN Name | Source LUN name of the snapshot.       |
| Health Status   | Health status of the snapshot.         |
| Running Status  | Running status of the clone.           |
| WWN             | World Wide Name (WWN) of the snapshot. |
| Time Stamp      | Activation time of the snapshot.       |
| Parent ID       | Parent object ID of the snapshot.      |
| Parent Name     | Parent object name of the snapshot.    |
| Cascaded Level  | Cascaded level of the snapshot.        |
