# show snapshot available_snapshot


##### Function

The **show snapshot available_snapshot** command is used to query snapshots for which the snapshots can be created.

##### Format

**show snapshot available_snapshot**

##### Parameters

| Parameter  | Description    | Value                        |
|------------|----------------|------------------------------|
| usage_type | Snapshot type. | The value can be "LUN_SNAP". |

##### Usage Guidelines

None

##### Example

Query snapshots for which snapshots can be created.

```text
admin:/>show snapshot available_snapshot
ID  Name  Source LUN ID  Source LUN Name  Health Status  Running Status  WWN                               Time Stamp                     Parent ID  Parent Name  Cascaded Level
--  ----  -------------  ---------------  -------------  --------------  --------------------------------  -----------------------------  ---------  -----------  --------------
1   snap0   0              lun              Normal         Activated       658605f10000da0300049d3a00000001  2017-05-09/15:57:41 UTC+08:00  0          lun          0
2   snap1   0              lun              Normal         Activated       658605f10000da030004a09b00000002  2017-05-09/15:57:44 UTC+08:00  0          lun          0
3   snap2   0              lun              Normal         Activated       658605f10000da03000689a400000003  2017-05-09/16:06:03 UTC+08:00  0          lun          0
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
| Running Status  | Running status of the snapshot.        |
| WWN             | World Wide Name (WWN) of the snapshot. |
| Time Stamp      | Activation time of the snapshot.       |
| Parent ID       | Parent ID of the snapshot.             |
| Parent Name     | Parent name of the snapshot.           |
| Cascaded Level  | Cascaded level of the snapshot.        |
