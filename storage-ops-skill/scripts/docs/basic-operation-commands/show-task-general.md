# show task general


##### Function

The **show task general** command is used to query configuration tasks.

##### Format

**show task general** { task_id=? \| task_name=? \| status=? \| start_from_time=? \| end_from_time=? \| sort1=? \| sort2=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| task_id=? | ID of the configuration task. | The value is an integer from 0 to 1023. |
| task_name=? | Name of the configuration task. | The value can contain letters and digits. |
| status=? | Status of the configuration task. | The value can be "executing", "wait", "success", "fail", "rollback", "rollback_fail", or "rollback_success", where: <br>"executing": being executed.<br>"wait": waiting.<br>"success": execution succeeded.<br>"fail": execution failed.<br>"rollback": rolling back.<br>"rollback_fail": rollback failed.<br>"rollback_success": rollback succeeded. |
| start_from_time=? | Query start time after which configuration tasks start to be executed. | The value is in the format of "year-month-day/hour:minute:second", where: <br>"year": The year ranges from 1970 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |
| sort2=? | Sort in ascending or descending order. | The value can be "desc" or "asc", where: <br>"desc": descending order.<br>"asc": ascending order. |
| sort1=? | Sort by start time or end time. | The value can be "startTime" or "EndTime", where: <br>"startTime": time when a task starts.<br>"endTime": time when a task ends. |
| end_from_time=? | Query end time after which configuration tasks are executed. | The value is in the format of "year-month-day/hour:minute:second", where: <br>"year": The year ranges from 1970 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |

##### Usage Guidelines

If too many tasks are displayed, press "q" to stop and exit the display.

##### Example

Query configuration tasks in batches.

```text

admin:/>show task general

Task ID  Task Name                     Duration       Start Time                     End Time                       Process  Status   Object
-------  -----------------------       -------------  -----------------------------  -----------------------------  -------  -------  ------------------------
0        Create Storage Pool           0d_0h_0m_14s   2019-08-21/03:19:10 UTC+02:00  2019-08-21/03:19:24 UTC+02:00  100%     success  StoragePool001
1        Start Synchronizing Clone CG  0d_0h_0m_6s    2019-08-21/03:48:28 UTC+02:00  2019-08-21/03:48:34 UTC+02:00  75%      fail     SyncCloneGroup1_52278
2        Start Synchronizing Clone CG  0d_0h_0m_9s    2019-08-21/03:53:55 UTC+02:00  2019-08-21/03:54:04 UTC+02:00  100%     success  SyncCloneGroup1_52605

```

Query details about configuration task "1".

```text
admin:/>show task general task_id=1
Task ID    : 1
Task Name  : Create Storage Pool
Duration   : 0d_0h_0m_11s
Start Time : 2019-08-08/15:38:47 UTC+08:00
End Time   : 2019-08-08/15:38:58 UTC+08:00
Process    : 100%
Status     : success
Object     : omtaskTest1_2-3
```

Query details about configuration tasks whose names are "Create_Storage_Pool".

```text

admin:/>show task general task_name=Create_Storage_Pool

Task ID  Task Name             Duration       Start Time                     End Time                       Process  Status   Object
-------  --------------------  -------------  -----------------------------  -----------------------------  -------  -------  ------------------------
0        Create Storage Pool   0d_0h_0m_14s   2019-08-08/22:42:50 UTC+02:00  2019-08-08/22:43:04 UTC+02:00  100%     success  pool
2        Create Storage Pool   0d_0h_0m_14s   2019-08-08/22:45:17 UTC+02:00  2019-08-08/22:45:31 UTC+02:00  100%     success  pool

```

Query details about configuration tasks whose status is "success".

```text

admin:/>show task general status=success

Task ID  Task Name            Duration       Start Time                     End Time                       Process  Status   Object

-------  -------------------  -------------  -----------------------------  -----------------------------  -------  -------  ------------------------
0        Create Storage Pool   0d_0h_0m_14s  2019-08-08/22:42:50 UTC+02:00  2019-08-08/22:43:04 UTC+02:00  100%     success  pool
1        Delete Storage Pool   0d_0h_0m_11s  2019-08-08/22:43:46 UTC+02:00  2019-08-08/22:43:57 UTC+02:00  100%     success  pool
2        Create Storage Pool   0d_0h_0m_14s  2019-08-08/22:45:17 UTC+02:00  2019-08-08/22:45:31 UTC+02:00  100%     success  pool

```

Query details about configuration tasks which start to be executed after 2019-08-09/09:11:49.

```text

admin:/>show task general start_from_time=2019-08-09/09:11:49

Task ID  Task Name                 Duration       Start Time                     End Time                       Process  Status   Object
-------  ------------------------- -------------  -----------------------------  -----------------------------  -------  -------  ------------------------
0        Create Storage Pool       0d_0h_0m_14s   2019-08-09/09:12:36 UTC+02:00  2019-08-09/09:12:50 UTC+02:00  100%     success   StoragePool001
1        Create and Map LUN Group  0d_0h_0m_5s    2019-08-09/09:13:28 UTC+02:00  2019-08-09/09:13:33 UTC+02:00  100%     success   LUNGroup001

```

Query details about the configuration task which is executed after 2019-08-09/11:22:46.

```text

admin:/>show task general end_from_time=2019-08-09/11:22:46

Task ID  Task Name             Duration        Start Time                     End Time                       Process  Status   Object
-------  --------------------  -------------  -----------------------------  -----------------------------  -------  -------  ------------------------
0        Delete Storage Pool   0d_0h_0m_12s   2019-08-09/11:22:34 UTC+08:00  2019-08-09/11:22:46 UTC+08:00  100%     success  cfg_upgrade_test_pool

```

Query configuration tasks based on the start time. The output is displayed in descending order.

```text

admin:/>show task general sort1=startTime sort2=desc

Task ID  Task Name                 Duration        Start Time                     End Time                       Process  Status   Object
-------  ------------------------  -------------  -----------------------------  -----------------------------  -------  -------  ------------------------
26       Create and Map LUN Group  0d_0h_1m_23s   2019-08-09/12:35:04 UTC+08:00  2019-08-09/12:36:27 UTC+08:00  100%     success  LunGroup_0140_25481
25       Create and Map LUN Group  0d_3h_55m_18s  2019-08-09/12:28:35 UTC+08:00  2019-08-09/16:23:53 UTC+08:00  100%     success  LunGroup_0130_25092

```

##### System Response

The following table describes the parameter meanings.

| Parameter  | Meaning                  |
|------------|--------------------------|
| Task ID    | Task ID.                 |
| Task Name  | Task name.               |
| End Time   | Time when a task ends.   |
| Process    | Task execution progress. |
| Status     | Task status.             |
| Object     | Task execution object.   |
| Start Time | Time when a task starts. |
