# show performance file


##### Function

The **show performance file** command is used to query historical performance statistics files.

##### Format

**show performance file** \[ controller=? \| ip_enclosure=? \] \[ from_time=? \] \[ to_time=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller=? | Controller ID. | To obtain the value, run the "show controller general" command. |
| from_time=? | Start time to query performance files. All performance files updated later than this point in time will be displayed. NOTE: "from_time" is local time. | The value is in the format of "year-month-day/hour:minute:second", where: <br>"year": The year ranges from 2000 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |
| to_time=? | End time to query performance files. All performance files updated earlier than this point in time will be displayed. NOTE: "to_time" is local time. | The value is in the format of "year-month-day/hour:minute:second", where: <br>"year": The year ranges from 2000 to 2035.<br>"month": The month ranges from 01 to 12.<br>"day": The day ranges from 01 to 31.<br>"hour": The hour ranges from 00 to 23.<br>"minute": The minute ranges from 00 to 59.<br>"second": The second ranges from 00 to 59. |
| ip_enclosure=? | Node ID of an IP controller enclosure. The value is in the format of "X.A", or "X.B", where "X" is the IP controller enclosure ID, for example, "DAE000.A". | To obtain the IP controller enclosure ID, run the "show enclosure" command. |

##### Usage Guidelines

-   The system time ranges from 2000-01-01/00:00:01 to 2035-12-31/23:59:59 in UTC.

##### Example

Query historical performance statistics files. The command output varies with product models. In the following command output, the fields related to the product model are replaced by X.

```text
admin:/>show performance file
File Name                                                          Updated Time                   File Size
-----------------------------------------------------------------  -----------------------------  ----------
PerfData_XXXXX_SN_snystrw623h7d739dmc9_SP0_0_20150729194049.tgz    2015-07-29/19:42:09 UTC+08:00     2.000KB
PerfData_XXXXX_SN_snystrw623h7d739dmc9_SP0_0_20150729193655.tgz    2015-07-29/19:36:57 UTC+08:00     2.000KB
PerfData_XXXXX_SN_snystrw623h7d739dmc9_SP1_0_20150729194049.tgz    2015-07-29/19:42:09 UTC+08:00     1.000KB
PerfData_XXXXX_SN_snystrw623h7d739dmc9_SP1_0_20150729193655.tgz    2015-07-29/19:36:57 UTC+08:00     1.000KB
```

##### System Response

The following table describes the parameter meanings.

| Parameter    | Meaning                                                          |
|--------------|------------------------------------------------------------------|
| File Name    | Name of the historical performance statistics file.              |
| Updated Time | Time when the historical performance statistics file is updated. |
| File Size    | Size of the historical performance statistics file.              |
