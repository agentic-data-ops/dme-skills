# change smartqos_policy general


##### Function

The **change smartqos_policy general** command is used to modify SmartQoS policies.

##### Format

**change smartqos_policy general** smartqos_policy_id=? \[ name=? \] \[ io_type=? \] \[ schedule_policy=? \] \[ day_of_week=? \] \[ schedule_start_time=? \] \[ start_time=? \] \[ duration=? \] \[ max_bandwidth=? max_iops=? \] \[ lun_id_list=? \] \[ burst_iops=? \] \[ burst_bandwidth=? \] \[ burst_time=? \] \[ min_bandwidth=? \] \[ min_iops=? \] \[ latency=? \] \[ file_system_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| name=? | Name of a SmartQoS policy. | The value contains 1 to 31 characters including digits, letters, hyphens (-), underscores (_), and periods (.). |
| io_type=? | Type of the I/Os that you want to control. Using this parameter specifies that SmartQoS will exclusively control a specific type of I/Os. | The value can be: <br>"read_write": indicates read and write I/Os. |
| schedule_policy=? | Time policy for triggering SmartQoS. | The value can be: <br>"once": The policy is executed once.<br>"daily": The policy is executed daily.<br>"weekly": The policy is executed weekly. |
| day_of_week=? | Day on which a scheduled SmartQoS policy will be cycled weekly. This parameter must be assigned and it is valid only when "schedule_policy=?" is set to "weekly". | You can specify multiple days in a week and separate them with commas (,). The value can be "sun", "mon", "tue", "wed", "thu", "fri", or "sat", where: <br>"sun": indicates Sunday.<br>"mon": indicates Monday.<br>"tue": indicates Tuesday.<br>"wed": indicates Wednesday.<br>"thu": indicates Thursday.<br>"fri": indicates Friday.<br>"sat": indicates Saturday. |
| schedule_start_time=? | Day from which a scheduled SmartQoS task will be started. | The value is in the format of year-month-day. The value ranges from 2000-01-01 to 2069-12-31. When "schedule_policy" is set to "once", the value cannot be earlier than the previous day of the current date. |
| start_time=? | Time from which a scheduled SmartQoS task will be started on a specific day. | The value is in the format of HH:MM. The value ranges from 00:00 to 23:59. When "schedule_policy" is set to "once" and the start date is the day before the current date, the start time cannot be earlier than the current time. |
| duration=? | Duration for performing a scheduled SmartQoS task. | The value is in the format of HH:MM or H:M. The value ranges from 00:30 to 24:00, indicating 30 minutes to 24 hours. When "schedule_policy" is set to "once", the end time of the policy cannot be earlier than the current time. |
| max_bandwidth=? | Maximum bandwidth. | The value is an integer ranging from 1 to 999,999,999, expressed in MB/s. |
| max_iops=? | Maximum IOPS. | The value is an integer ranging from 100 to 999,999,999. |
| lun_id_list=? | LUNs that you want to add to a SmartQoS policy. Only the added LUNs will be controlled by SmartQoS. | To obtain the value, run "show lun general".<br>You can specify multiple LUN IDs separated by commas (,), or an ID range separated by hyphens (-), such as: 0,5-8.<br>A maximum of 512 IDs can be specified. This parameter is mutually exclusive with "file_system_id_list". |
| burst_bandwidth=? | Maximum burst bandwidth. This parameter can be configured only when "max_bandwidth" is configured. | The value is an integer from 1 to 999999999 (unit: MB/s). The value must be greater than that of "max_bandwidth". |
| burst_iops=? | Maximum burst IOPS. This parameter can be configured only when "max_iops" is configured. | The value is an integer from 100 to 999999999. The value must be greater than that of "max_iops". |
| burst_time=? | Burst time. This parameter can be set only when either "burst_bandwidth" or "burst_iops" is configured. | The value is an integer from 1 to 999999999 (unit: second). |
| min_bandwidth | Minimum bandwidth. | The value is an integer ranging from 1 to 999,999,999, expressed in MB/s. |
| min_iops | Minimum IOPS. | The value is an integer ranging from 100 to 999,999,999. |
| latency | I/O latency. | The value can be "0.5ms" or "1.5ms". |
| file_system_id_list=? | IDs of the file systems to be added to the SmartQoS policy. | To obtain the value, run "show file_system general".<br>Multiple file system IDs are separated by commas (,), or by hyphens (-) to represent an ID range, for example, 0,5-8.<br>A maximum of 512 IDs can be specified. This parameter is mutually exclusive with "lun_id_list". |

##### Usage Guidelines

-   QoS policies can be modified online. You do not need to deactivate the QoS policies before modifying them, and new configurations take effect immediately after the modification.
-   You must specify at least one of parameters "max_bandwidth", "max_iops", "min_bandwidth", "min_iops", and "latency".
-   In a QoS policy, configure either LUNs or file systems.
-   The "burst_bandwidth" parameter can be configured only when "max_bandwidth" is configured. The value of "burst_bandwidth" must be greater than that of "max_bandwidth".
-   The "burst_iops" parameter can be configured only when "max_iops" is configured. The value of "burst_iops" must be greater than that of "max_iops".
-   The "burst_time" parameter can be set only when either "burst_bandwidth" or "burst_iops" is configured.
-   The value of parameter "min_bandwidth" cannot be greater than that of parameter "max_bandwidth". The value of parameter "min_iops" cannot be greater than that of parameter "max_iops".

##### Example

Modify SmartQoS policy "0" where the type of the I/Os to control is "read_write", and add LUNs "0" and "1" to the SmartQoS policy.

```text
admin:/>change smartqos_policy general smartqos_policy_id=0 io_type=read_write lun_id_list=0,1
CAUTION: You are about to modify storage objects in traffic control policy.
This operation may affect storage object performance.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the correct traffic control policy and storage objects are selected.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
