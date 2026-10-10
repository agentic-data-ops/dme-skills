# show hyper_cdp_schedule general


##### Function

The **show hyper_cdp_schedule general** command is used to query information about a HyperCDP schedule.

##### Format

**show hyper_cdp_schedule general** \[ schedule_id=? \]

**show hyper_cdp_schedule general** \[ schedule_name=? \] \[ vstore_id=? \]

##### Parameters

| Parameter       | Description                  | Value                                                                                                                                                                                                                                       |
|-----------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| schedule_id=?   | HyperCDP schedule ID.        | To obtain the value, run "**show hyper_cdp_schedule general**". The value is an integer from 1 to 512. |
| schedule_name=? | Name of a HyperCDP schedule. | You can run the **show hyper_cdp_schedule general** command to obtain the value.                       |
| vstore_id=?     | Specified vStore ID.         | The value is an integer ranging from 0 to 1023. The default value is 0.                                                                                                                                                                     |

##### Usage Guidelines

-   Before performing the operation, confirm that the schedule ID is correct and exists.
-   Running the command with a schedule ID queries information about a schedule. Running the command without a schedule ID queries information about all schedules.
-   The built-in schedule of the file system cannot be operated by name.

##### Example

Query information about the HyperCDP schedule whose ID is "1".

```text
admin:/>show hyper_cdp_schedule general schedule_id=1
ID                     : 1
Name                   : schedule1
Health Status          : Normal
Running Status         : Disabled
Week Days              : --
Week Start Time        : --
Week Reserved Num      : --
Frequency Time         : 0 hour(s),0 minute(s),15 second(s)
Frequency Reserved Num : 1
Hours                  : --
Start Minute           : --
Day Reserved Num       : --
Month Days             : --
Month Start Time       : --
Month Reserved Num     : --
Last Execution Time    : --
Last Execution Result  : --
Description            :
type                   : File
Vstore ID              : --
Scope                  : Vstore
```

Query information about all HyperCDP schedules.

```text
admin:/>show hyper_cdp_schedule general
ID  Name     Health Status  Running Status  Last Execution Time            Last Execution Result  type   Vstore ID  Scope
--  -------  -------------  --------------  -----------------------------  ---------------------  -----  ---------  -------
1   cdp      Normal         Enabled         2020-07-11/16:04:43 UTC+08:00  Success                Block  --         Vstore
2   cdp2     Normal         Enabled         2020-07-11/16:04:42 UTC+08:00  Success                File   --         Cluster

```

##### System Response

The following table describes the parameter meanings.

| Parameter              | Meaning                                                                                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                     | HyperCDP schedule ID.                                                                                                                                              |
| Name                   | HyperCDP schedule name.                                                                                                                                            |
| Health Status          | Health status of a HyperCDP schedule.                                                                                                                              |
| Running Status         | Running status of a HyperCDP schedule.                                                                                                                             |
| Week Days              | Day in a week when HyperCDP objects are created. The value is an integer from 0 to 6 (indicating from Sunday to Saturday).                                         |
| Week Start Time        | Time when HyperCDP objects are created. The value is in the format of "HH:MM". It is a point in time between "00:00-23:59".                                        |
| Week Reserved Num      | Reserved number of HyperCDP objects created weekly. The value is an integer from 1 to 256.                                                                         |
| Frequency Time         | Indicates a fixed interval.                                                                                                                                        |
| Frequency Reserved Num | Reserved number of HyperCDP objects created at fixed intervals. The value is an integer from 1 to 256.                                                             |
| Hours                  | Hour in a day when HyperCDP objects are created. The value is an integer from 0 to 23.                                                                             |
| Start Minute           | Minute in an hour when HyperCDP objects are created. The value is an integer from 0 to 59.                                                                         |
| Day Reserved Num       | Reserved number of HyperCDP objects created daily. The value is an integer from 1 to 60000.                                                                        |
| Month Days             | Day in a month when HyperCDP objects are created. The value is an integer from 1 to 31 (indicating which day in the month) or "lastday" (the last day of a month). |
| Month Start Time       | Time when HyperCDP objects are created. The value is in the format of "HH:MM". It is a point in time between "00:00-23:59".                                        |
| Month Reserved Num     | Reserved number of HyperCDP objects created monthly. The value is an integer from 1 to 256.                                                                        |
| Last Execution Time    | Last execution time.                                                                                                                                               |
| Last Execution Result  | Last execution result.                                                                                                                                             |
| Description            | Description.                                                                                                                                                       |
| type                   | Type of objects added to the HyperCDP schedule.                                                                                                                    |
| Vstore ID              | vStore ID.                                                                                                                                                         |
| Scope                  | Scope.                                                                                                                                                             |
