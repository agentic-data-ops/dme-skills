# change system time


##### Function

The **change system time** command is used to change the storage system's time. If the storage system's time is incorrect, you can run this command to change it.

##### Format

**change system time** time=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| time=? | Updated time of the storage system. | The value is in the format of "year-month-day/hour:minute:second", where: <br>"year": The year ranges from 2000 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |

##### Usage Guidelines

-   If the storage system's time is changed incorrectly, the scheduled tasks and the maintenance engineers' work are adversely affected.
-   Before running this command, check whether the time that you want to set is correct.
-   The system time ranges from 2000-01-01/00:00:01 to 2035-12-31/23:59:59 in UTC.
-   If the time synchronization function is enabled, you are not allowed to change the system time.

##### Example

Change the system time to "2014-04-06/11:22:05".

```text
admin:/>change system time time=2014-04-06/11:22:05
WARNING: You are about to modify the system time. This operation may affect the license, alarm, performance monitoring, log export, certificate, and CallHome data backhaul.
Suggestion: Ensure that you want to perform this operation. Do not perform this operation when upgrading the system or exporting logs.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
