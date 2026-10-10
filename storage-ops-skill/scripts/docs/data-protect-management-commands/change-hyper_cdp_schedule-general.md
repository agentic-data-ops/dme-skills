# change hyper_cdp_schedule general


##### Function

The **change hyper_cdp_schedule general** command is used to modify information about a HyperCDP schedule, including the name, schedule policy type, and time.

##### Format

**change hyper_cdp_schedule general** { schedule_id=? } { name=? period=? } \* \[ day_of_week=? \] \[ week_start_time=? \] \[ week_reserved_num=? \] \[ frequency_time_unit=? \] \[ frequency_time=? \] \[ frequency_reserved_num=? \] \[ hour_of_day=? \] \[ minute_of_hour=? \] \[ day_reserved_num=? \] \[ day_of_month=? \] \[ month_start_time=? \] \[ month_reserved_num=? \] \[ description=? \]

**change hyper_cdp_schedule general** { schedule_name=? } { name=? period=? } \* \[ vstore_id=? \] \[ day_of_week=? \] \[ week_start_time=? \] \[ week_reserved_num=? \] \[ frequency_time_unit=? \] \[ frequency_time=? \] \[ frequency_reserved_num=? \] \[ hour_of_day=? \] \[ minute_of_hour=? \] \[ day_reserved_num=? \] \[ day_of_month=? \] \[ month_start_time=? \] \[ month_reserved_num=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id=? | HyperCDP schedule ID. | The value is an integer from 1 to 512. |
| schedule_name=? | Name of a HyperCDP schedule. | The value is a string of 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| name=? | New name of the HyperCDP schedule. | The value contains 1 to 255 ASCII characters, including letters, digits, periods (.), underscores (_), and hyphens (-). |
| period=? | Policy type of a HyperCDP schedule. | The value can be "weekly", "frequency", "daily", or "monthly", where: <br>"weekly": creates HyperCDP objects weekly.<br>"frequency": creates HyperCDP objects at fixed intervals.<br>"daily": creates HyperCDP objects daily.<br>"monthly": creates HyperCDP objects monthly.<br> You can specify multiple types of schedules separated by commas (,), such as: "period=frequency,weekly". |
| vstore_id=? | Specified vStore ID. | The value is an integer ranging from 0 to 1023. The default value is 0. |
| day_of_week=? | Day in a week when HyperCDP objects are created. | The value can be "mon", "tue", "wed", "thu", "fri", "sat", or "sun". For example, "day_of_week=mon".<br>You can specify multiple days separated by commas (,), such as: "day_of_week=mon,tue". |
| week_start_time=? | Time in a week when HyperCDP objects are created. | The value is in the format of "HH:MM". It is a point in time from 00:00 to 23:59. |
| week_reserved_num=? | Reserved number of HyperCDP objects created weekly. | The value is an integer from 1 to 256. |
| frequency_time_unit=? | Unit of the fixed interval. | The value can be: <br>"hour": indicates hours.<br>"minute": indicates minutes.<br>"second": indicates seconds. |
| frequency_time=? | Fixed interval. | When frequency_time_unit is set to hour, the value of frequency_time ranges from 1 to 24.<br>When frequency_time_unit is set to minute, the value of frequency_time ranges from 1 to 1440.<br>When frequency_time_unit is set to second and the object type in the HyperCDP schedule is file, the value ranges from 15 to 59. If the object type in the HyperCDP schedule is block, the value ranges from 3 to 59. |
| frequency_reserved_num=? | Reserved number of HyperCDP objects created at fixed intervals. | When the object type is file, the value is an integer ranging from 1 to 4096. When the object type is block, the value is an integer ranging from 1 to 60000. |
| hour_of_day=? | Hour of a day when HyperCDP objects are created. | The value is an integer from 0 to 23 (unit: hour). If multiple values are selected, separate them with commas (,). For example, "hour_of_day=1,2,3". |
| minute_of_hour=? | Minute in a day when HyperCDP objects are created. | The value is an integer from 0 to 59. |
| day_reserved_num=? | Reserved number of HyperCDP objects created daily. | The value is an integer from 1 to 256. |
| day_of_month=? | Day in a month when HyperCDP objects are created. | The value is an integer from 1 to 31 or "lastday". If multiple values are selected, separate them with commas (,). For example, "day_of_month=1,21,lastday". NOTE: The value "lastday" indicates the last day of a month. |
| month_start_time=? | Time in a month when HyperCDP objects are created. | The value is in the format of "HH:MM". It is a point in time from 00:00 to 23:59. |
| month_reserved_num=? | Reserved number of HyperCDP objects created monthly. | The value is an integer from 1 to 256. |
| description=? | Description. | - |

##### Usage Guidelines

-   Before performing this operation, confirm that the schedule ID is correct.
-   Before performing the operation, confirm that the name of the schedule to be modified is correct and exits.
-   If "period" is set to "weekly", parameters "day_of_week", "week_start_time", and "week_reserved_num" are optional.
-   If "period" is set to "frequency", parameters "frequency_time" and "frequency_reserved_num" are optional.
-   If "period" is set to "daily", parameters "hour_of_day" and "minute_of_hour" are optional.
-   If "period" is set to "monthly", parameters "day_of_month" and "month_start_time" are optional.
-   The built-in schedule of the file system cannot be operated by name.

##### Example

Modify the properties of the HyperCDP schedule whose ID is "1".

```text
admin:/> change hyper_cdp_schedule general schedule_id=1 name=auto1 period=weekly,frequency day_of_week=mon week_start_time=12:45 week_reserved_num=2 frequency_time_unit=minute frequency_time=2 frequency_reserved_num=3
Command executed successfully.
```

##### System Response

None
