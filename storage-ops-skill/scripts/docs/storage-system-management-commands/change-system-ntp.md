# change system ntp


##### Function

The **change system ntp** command is used to configure the NTP. Run this command if you want the storage system to synchronize its time with that of an NTP server.

##### Format

**change system ntp** enabled=? \[ server_ip=? ntp_interval=? ntp_unit=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Whether to enable the time synchronization function. | The value can be "yes" or "no", where: <br>"yes": enables NTP time synchronization.<br>"no": disables the NTP time synchronization. |
| server_ip=? | IP address of the NTP server. When "enabled=?" is set to "yes", this parameter is valid and mandatory. | - |
| ntp_interval=? | Synchronization period. When "enabled=?" is set to "yes", this parameter is valid and mandatory. | - |
| ntp_unit=? | The unit of the synchronization period. When "enabled=?" is set to "yes", this parameter is valid and mandatory. | The value can be "day", "hour", "minute" or "second", where: <br>"day": The synchronization period is expressed in days.<br>"hour": The synchronization cycle is expressed in hours.<br>"minute": The synchronization period is expressed in minutes.<br>"second": The synchronization period is expressed in seconds. |

##### Usage Guidelines

The command is used to configure only one NTP server. The "add ntp_server general", "remove ntp_server general", "change ntp_server config", and "show ntp_server general" commands are used to configure two NTP servers and a server address can be a domain name. You are advised to use the preceding four commands to configure NTP servers.

-   The time synchronization function is enabled only when "enabled=?" is set to "yes".
-   If you configure NTP for the first time, run "**change system ntp** enabled=? server_ip=? ntp_interval=? ntp_unit=?" to enable the time synchronization function and configure an IP address for the NTP server and the synchronization period.
-   Ensure that the time of NTP servers ranges from 2000-01-01/00:00:01 to 2035-12-31/23:59:59.
-   This command is invisible to adapt to the NTP authentication feature.

##### Example

Enable time synchronization. The NTP server address is 192.168.65.23 and the synchronization period is 24 hours.

```text
admin:/>change system ntp enabled=yes server_ip=192.168.65.23 ntp_interval=24 ntp_unit=hour
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
