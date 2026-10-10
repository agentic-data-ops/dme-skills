# create hyper_cdp_schedule general


##### Function

The **create hyper_cdp_schedule general** command is used to create a HyperCDP schedule.

##### Format

**create hyper_cdp_schedule general** name=? period=? day_of_week=? week_start_time=? week_reserved_num=? frequency_time_unit=? frequency_time=? frequency_reserved_num=? hour_of_day=? minute_of_hour=? day_reserved_num=? day_of_month=? month_start_time=? month_reserved_num=? \[ type=? \] \[ schedule_id_list=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | HyperCDP schedule name. | The value contains 1 to 255 ASCII characters, including letters, digits, periods (.), underscores (_), and hyphens (-).<br>When you batch create HyperCDP schedules (by specifying "schedule_id_list=?"), the system automatically numbers the schedule names by adding a four-digit suffix to each name. The suffix starts from 0000. For example, if you specify the name to "auto", the newly created HyperCDP schedules are automatically names as "auto0000", "auto0001", and so on.<br> NOTE: When you batch create HyperCDP schedules, the value of "name=?" cannot exceed 251 characters. |
| period=? | Policy type of a HyperCDP schedule. | The value can be "weekly", "frequency", "daily", or "monthly", where: <br>"weekly": creates HyperCDP objects weekly.<br>"frequency": creates HyperCDP objects at fixed intervals.<br>"daily": creates HyperCDP objects daily.<br>"monthly": creates HyperCDP objects monthly.<br> You can specify multiple types of schedules separated by commas (,), such as: "period=frequency,weekly". |
| day_of_week=? | Day in a week when HyperCDP objects is created. | The value can be "mon", "tue", "wed", "thu", "fri", "sat", or "sun". For example, "day_of_week=mon".<br>You can specify multiple days separated by commas (,), such as: "day_of_week=mon,tue". |
| week_start_time=? | Time in a week when HyperCDP objects are created. | The value is in the format of "HH:MM". It is a point in time from 00:00 to 23:59. |
| week_reserved_num=? | Reserved number of HyperCDP objects created weekly. | The value is an integer from 1 to 256. |
| frequency_time_unit=? | Unit of the fixed interval. | The value can be: <br>"hour": indicates hours.<br>"minute": indicates minutes.<br>"second": indicates seconds. |
| frequency_time=? | Fixed interval. | If the value of "frequency_time_unit" is set to "hour", "frequency_time" ranges from 1 to 24.<br>If the value of "frequency_time_unit" is set to "minute", "frequency_time" ranges from 1 to 1440.<br>When "frequency_time_unit" is set to "second", the value ranges from 15 to 59 if "type" is set to "1" (file), and ranges from 3 to 59 if "type" is set to "0" (block). |
| frequency_reserved_num=? | Reserved number of HyperCDP objects created at fixed intervals. | When "type" is set to "1" (file), the value is an integer ranging from 1 to 4096. When "type" is set to "0" (block), the value is an integer ranging from 1 to 60,000. |
| hour_of_day=? | Hour of a day when HyperCDP objects are created. | The value is an integer from 0 to 23 (unit: hour). If multiple values are selected, separate them with commas (,). For example, "hour_of_day=1,2,3". |
| minute_of_hour=? | Minute in a day when HyperCDP objects are created. | The value is an integer from 0 to 59. |
| day_reserved_num=? | Reserved number of HyperCDP objects created daily. | The value is an integer from 1 to 256. |
| day_of_month=? | Day in a month when HyperCDP objects are created. | The value is an integer from 1 to 31 or "lastday". If multiple values are selected, separate them with commas (,). For example, "day_of_month=1,21,lastday". NOTE: The value "lastday" indicates the last day of a month. |
| month_start_time=? | Time in a month when HyperCDP objects are created. | The value is in the format of "HH:MM". It is a point in time from 00:00 to 23:59. |
| month_reserved_num=? | Reserved number of HyperCDP objects created monthly. | The value is an integer from 1 to 256. |
| type | Type of objects added to the HyperCDP schedule. | The value can be "0" or "1", where: <br>"0": block.<br>"1": file. |
| schedule_id_list=? | ID list of HyperCDP schedules. | The value is an integer from 1 to 512.<br>You can create multiple schedule IDs separated by commas (,) or an ID range using hyphens (-), such as: "1,5-8". |
| description=? | Description. | - |

##### Usage Guidelines

-   Before performing this operation, confirm that the ID of the schedule to be set is correct.
-   Before performing this operation, confirm that the ID of the schedule to be set exists.
-   Before performing this operation, confirm that the name of the schedule to be set exists.
-   When "period" is set to "weekly", parameters "day_of_week" and "week_start_time" are mandatory.
-   When "period" is set to "frequency", parameter "frequency_time" is mandatory.
-   When "period" is set to "daily", parameters "hour_of_day" and "minute_of_hour" are mandatory.
-   When "period" is set to "monthly", parameters "day_of_month" and "month_start_time" are mandatory.

##### Example

Create HyperCDP schedule with ID "1".

```text
admin:/>create hyper_cdp_schedule general name=auto period=weekly,frequency day_of_week=sun week_start_time=00:00 week_reserved_num=10 frequency_time_unit=second frequency_time=30 frequency_reserved_num=10 schedule_id_list=1
Create HyperCDP schedule auto0000 successfully.
```

Create HyperCDP schedules with IDs "1" and "2".

```text
admin:/>create hyper_cdp_schedule general name=auto period=daily,monthly hour_of_day=12,20 minute_of_hour=40 day_reserved_num=2 day_of_month=1,2 month_start_time=12:12 month_reserved_num=3 schedule_id_list=1-2
Create HyperCDP schedule auto0000 successfully.
Create HyperCDP schedule auto0001 successfully.
```

Create a HyperCDP schedule whose type is file.

```text
admin:/>create hyper_cdp_schedule general name=cdp period=frequency frequency_time_unit=second frequency_time=3 frequency_reserved_num=122 type=file
Create HyperCDP schedule cdp successfully.
```

##### System Response

None
