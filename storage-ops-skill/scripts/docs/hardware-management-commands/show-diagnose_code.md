# show diagnose_code


##### Function

The **show diagnose_code** command is used to query system diagnose codes.

##### Format

**show diagnose_code** \[ from_time=? \| to_time=? \| level=? \| number=? \| sequence=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| from_time=? | Start time of diagnose code query. Diagnose codes after the time will be displayed. NOTE: Set the value of parameter "from_time" to the local time. | The value is in the format of "year-month-day"/"hour:minute:second", where: <br>"year": The year ranges from 2000 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |
| sequence=? | SN of a diagnose code. To obtain the value, run the "show event" command without parameters. | The value is an integer between 1 and 4,294,967,295. |
| number=? | Maximum number of diagnose codes. | The value is an integer ranging from 1 to 10000. |
| level=? | Level of the diagnose code to be queried. | The value can be "warning", "major", "critical", or "informational", where: <br>"warning": The diagnose code is for warning.<br>"major": The diagnose code is major.<br>"critical": The diagnose code is critical.<br>"informational": The diagnose code is informational. |
| to_time=? | End time of diagnose code query. Diagnose codes before the time will be displayed. NOTE: Set the value of parameter "to_time" to the local time. | The value is in the format of "year-month-day"/"hour:minute:second", where: <br>"year": The year ranges from 2000 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |

##### Usage Guidelines

-   The system time ranges from 2000-01-01/00:00:01 to 2035-12-31/23:59:59 in UTC.
-   If too many events are displayed, press "q" to stop displaying more events.
-   The sequence parameter is mutually exclusive with all other parameters.

##### Example

Query all diagnose codes.

```text
admin:/>show diagnose_code
Sequence      Level          Occurred On                    Name                             ID
------------  -------------  -----------------------------  -------------------------------  ----------
155635        Informational  2015-11-30/14:25:59 UTC+08:00  Invoking Failed                  0xF0000904
155632        Informational  2015-11-30/14:25:43 UTC+08:00  The Software Is Abnormal         0xF0000501
155614        Informational  2015-11-30/14:23:05 UTC+08:00  Failed To Request For Resources  0xF0000601
138848        Informational  2015-11-28/17:19:59 UTC+08:00  Non-Existent Object              0xF0000901
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                                 |
|-------------|-----------------------------------------|
| Sequence    | SN of a diagnose code.                  |
| Level       | Level of a diagnose code.               |
| Occurred On | Time where a diagnose code occurred.    |
| ID          | Diagnose code ID.                       |
| Name        | Diagnose code name.                     |
| Detail      | Diagnose code details.                  |
| Suggestion  | Diagnose code rectification suggestion. |
