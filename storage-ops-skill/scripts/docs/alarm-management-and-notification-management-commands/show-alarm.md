# show alarm


##### Function

The **show alarm** command is used to query system alarms.

##### Format

**show alarm** { from_time=? \| to_time=? \| level=? \| number=? \| sequence=? \| object_type=? \| alarm_state=? \| root_cause_sequence=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| from_time=? | Start time to query alarms. All alarms generated later than this point in time will be displayed. NOTE: Enter local time for "from_time". | The value is in the format of "year-month-day/hour:minute:second", where: <br>"year": The year ranges from 2000 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |
| to_time=? | End time to query alarms. All alarms generated earlier than this point in time will be displayed. NOTE: Enter local time for "to_time". | The value is in the format of "year-month-day/hour:minute:second", where: <br>"year": The year ranges from 2000 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |
| level=? | Alarm severity. | The value can be "warning", "major", "critical", where: <br>"warning": The log message is for warning.<br>"major": The log message is major.<br>"critical": The log message is critical. |
| number=? | Number of alarms that you want to query. When you specify this parameter, you can query a specific number of latest alarms. | The value is an integer ranging from 1 to 10000. |
| sequence=? | Alarm sequence number. To obtain the value, run "show alarm" without parameters. | The value is an integer between 1 and 4294967295. |
| object_type=? | Alarm object type. | The value is an integer ranging from 0 to 65535. |

##### Usage Guidelines

-   The allowed query period ranges from 2000-01-01/00:00:01 to 2035-12-31/23:59:59 in UTC.
-   If too many alarms are displayed, press "q" to stop and exit the display.
-   "sequence" and other parameters are mutually exclusive and cannot be used at the same time. Except that in the developer view, "sequence" can be used together with "alarm_state".
-   The "alarm_state" and "root_cause_sequence" can be used in the developer view only.
-   When alarms are queried in the developer view, parameter "Alarm State" will be displayed.
-   When the "sequence" parameter is used in the developer view and the child alarms are queried, the "Root Cause Sequence" will be displayed.

##### Example

Query all the system alarms.

```text
admin:/>show alarm
Sequence      Level          Occurred On                    Name                              ID           Alarm Object Type
------------  -------------  -----------------------------  --------------------------------  -----------  -----------------
102632        Critical       2015-07-31/18:59:36 UTC+08:00  Failed To Monitor The Controller  0xF00CF0014  207
101941        Major          2015-07-31/15:51:28 UTC+08:00  License Has Expired               0xF0C90002   244
100055        Major          2015-07-31/12:14:37 UTC+08:00  Power Module Has No Input         0xF00170014  23
```

Query all the alarms in the developer view.

```text
developer:/>show alarm alarm_state=all

Sequence      Level          Occurred On                    Name                              ID           Alarm Object Type  Alarm State
------------  -------------  -----------------------------  --------------------------------  -----------  -----------------  ---------
102632        Critical       2015-07-31/18:59:36 UTC+08:00  Failed To Monitor The Controller  0xF00CF0014  207                Reported
101941        Major          2015-07-31/15:51:28 UTC+08:00  License Has Expired               0xF0C90002   244                Waiting Root
100055        Major          2015-07-31/12:14:37 UTC+08:00  Power Module Has No Input         0xF00170014  23                 Blocking
100054        Major          2015-07-31/12:14:37 UTC+08:00  Power Module Has No Input         0xF00170014  23                 Waiting Recovery
100053        Major          2015-07-31/12:14:37 UTC+08:00  Power Module Has No Input         0xF00170014  23                 Suspending
```

Query child alarms based on the parent alarm in the developer view.

```text
developer:/>show alarm root_cause_sequence=5970
Sequence      Level          Occurred On                    Name                                           ID           Alarm Object Type  Root Cause Sequence
------------  -------------  -----------------------------  ---------------------------------------------  -----------  -----------------  -------------------
5969          Major          2016-01-04/22:25:50 UTC+08:00  External LUN Has Links To Only One Controller  0xF000B0063  11                 5970
```

Query alarms by specifying the SN in the developer view.

```text
developer:/>show alarm sequence=5969 alarm_state=all
Sequence            : 5969
Level               : Major
Occurred On         : 2016-01-04/22:25:50 UTC+08:00
ID                  : 0xF000B0063
Name                : External LUN Has Links To Only One Controller
Detail              : External LUN(heterogeneous array ID 10, vendor 30, product model --, external LUN WWN 20) has links to only one controller.
Repair Suggestion   : Step1 Check whether only one controller has a link to the external LUN.
1.1 If yes, connect the link based on the standard network in the related product manual.
1.2 If no=>[Step2].
Step2 Check whether the initiator of a link is removed.
2.1 If yes, add the initiator back.
2.2 If no=>[Step3].
Step3 Check whether the mapping of the corresponding external LUN has been deleted.
3.1 If yes, add the mapping.
3.2 If no=>[Step4].
Step4 Collect related event information and contact technical support.
Root Cause Sequence : 5970
Alarm State         : Blocking
```

Query alarms generated later than 15:51:28 on July 31, 2015.

```text
admin:/>show alarm from_time=2015-07-31/15:51:28
Sequence      Level          Occurred On                    Name                              ID           Alarm Object Type
------------  -------------  -----------------------------  --------------------------------  -----------  -----------------
102782        Critical       2015-07-31/19:14:42 UTC+08:00  Failed To Monitor The Controller  0xF00CF0014  207
101941        Major          2015-07-31/15:51:28 UTC+08:00  License Has Expired               0xF0C90002   244
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning                              |
|---------------------|--------------------------------------|
| Sequence            | Alarm sequence number.               |
| Level               | Alarm severity.                      |
| Occurred On         | Alarm occurrence time.               |
| ID                  | Alarm ID.                            |
| Name                | Alarm name.                          |
| Detail              | Alarm details.                       |
| Repair Suggestion   | Alarm handling suggestion.           |
| Alarm Object Type   | Alarm object type.                   |
| Root Cause Sequence | Sequence number of the parent alarm. |
| Alarm State         | Alarm inner state.                   |
