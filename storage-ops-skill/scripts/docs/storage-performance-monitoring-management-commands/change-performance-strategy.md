# change performance strategy


##### Function

The **change performance strategy** command is used to configure the policies of collecting system performance statistics.

##### Format

**change performance strategy** \[ interval=? \] \[ archive_enabled=? \] \[ archive_time=? \] \[ auto_stop_enabled=? \] \[ duration=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| interval=? | Interval between system performance statistics collections. | The value can be "5s", "10s", "30s", or "60s". |
| archive_enabled=? | Whether to enable the automatic archiving function. | The value can be: <br>"yes": to enable the automatic archiving function.<br>"no": not to enable the automatic archiving function. |
| archive_time=? | Archiving cycle. | The value can be "5s", "60s", "120s", "300s", "600s", "1800s", or "3600s". |
| auto_stop_enabled=? | Whether to enable the function of automatically stopping performance statistics collection. | The value can be: <br>"yes": to enable the function of automatically stopping performance statistics collection.<br>"no": not to enable the function of automatically stopping performance statistics collection. |
| duration=? | Maximum number of days to collect performance statistics. NOTE: When the "auto_stop_enabled=?" is set to "yes", this parameter is valid and must be specified. | The value is an integer between 1 and 31. |

##### Usage Guidelines

-   This command is used to set the system performance statistics policy.

 

Before running this command, ensure that the performance statistics function has been disabled or the "change performance statistic_enabled enabled=no" command has been executed.

-   After the system performance statistics policy is configured, you must run the "change performance statistic_enabled enabled=yes" command before using the new performance statistics policy to collect performance data.

##### Example

Set the interval of collecting system performance statistics to "60s", enable the automatic archiving function, and set the maximum number of days to collect performance statistics to "1".

```text
admin:/>change performance strategy interval=60s archive_enabled=yes archive_time=60s auto_stop_enabled=yes duration=1
Command executed successfully.
```

##### System Response

None
