# change ntp_server config


##### Function

The **change ntp_server config** command is used to configure the time synchronization function. Run this command if you want the storage system to synchronize its time with that of an NTP server.

##### Format

**change ntp_server config** { enabled=? \| ntp_interval=? ntp_unit=? \| auth_enabled=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Whether to enable the time synchronization function. | The value can be "yes" or "no", where: <br>"yes": enables NTP time synchronization.<br>"no": disables NTP time synchronization. |
| ntp_interval=? | Synchronization period. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The maximum synchronization period is 10 days and the minimum synchronization period is 60 seconds. |
| ntp_unit=? | Synchronization period. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "day", "hour", "minute" or "second", where: <br>"day": The synchronization period is expressed in days.<br>"hour": The synchronization period is expressed in hours.<br>"minute": The synchronization period is expressed in minutes.<br>"second": The synchronization period is expressed in seconds. |
| auth_enabled | Whether to enable the NTP authentication function. The NTP version needs to be NTPv4 (included) or later. | The value can be "yes" or "no", where: <br>"yes": enables NTP authentication function.<br>"no": disables NTP authentication function.<br> The default state is "no". |

##### Usage Guidelines

-   The time synchronization function can be enabled only when the value of the "enabled=?" parameter is "yes" and an NTP server is added.
-   If you configure NTP for the first time, run the "add ntp_server general" command to add an NTP server. Then run the "**change ntp_server config** enabled=? ntp_interval=? ntp_unit=?" command to enable the time synchronization function and configure an automatic synchronization period.
-   If two NTP servers are configured for a system, ensure that the times of the two NTP server are consistent.

##### Example

Enable the time synchronization and NTP authentication function.

```text
admin:/>change ntp_server config enabled=yes ntp_interval=24 ntp_unit=hour auth_enabled=yes
WARNING: You are about to change the system network time protocol (NTP) configuration.
1. This operation may affect system licenses, alarms, performance monitoring, certificates, and CallHome data backhaul.
2. Modifying the configuration will restart the NTP service. The restart process takes about 5 minutes.
Suggestion: Make sure that you want to change the system NTP configuration before performing the operation. If you need to change, set the array time to be the same as that of the NTP server before the operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
