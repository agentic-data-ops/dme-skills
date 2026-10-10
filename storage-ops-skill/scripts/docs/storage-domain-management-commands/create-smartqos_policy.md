# create smartqos_policy


##### Function

The **create smartqos_policy** command is used to create SmartQoS policies. By using SmartQoS, the storage system can allocate its resources to different types of I/Os on demand.

##### Format

**create smartqos_policy** name=? schedule_policy=? \[ day_of_week=? \] schedule_start_time=? start_time=? duration=? \[ io_type=? \] \[ ctrl_type=? \] { max_bandwidth=? max_iops=? } \[ lun_id_list=? \] \[ lun_group_id_list=? \] \[ burst_iops=? \] \[ burst_bandwidth=? \] \[ burst_time=? \] \[ host_id_list=? \] \[ min_bandwidth=? \] \[ min_iops=? \] \[ latency=? \] \[ file_system_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a SmartQoS policy. | The value contains 1 to 31 characters, including digits, letters, hyphens (-), underscores (_), and periods (.). |
| schedule_policy=? | Time policy for triggering SmartQoS. | The value can be: <br>"once": The policy is executed once.<br>"daily": The policy is executed daily.<br>"weekly": The policy is executed weekly. |
| day_of_week=? | Day on which a scheduled SmartQoS policy will be cycled weekly. This parameter must be assigned and it is valid only when schedule_policy=? is set to "weekly". | You can specify multiple days in a week and separate them with commas (,). The value can be "sun", "mon", "tue", "wed", "thu", "fri", or "sat", where: <br>"sun": indicates Sunday.<br>"mon": indicates Monday.<br>"tue": indicates Tuesday.<br>"wed": indicates Wednesday.<br>"thu": indicates Thursday.<br>"fri": indicates Friday.<br>"sat": indicates Saturday. |
| schedule_start_time=? | Day from which a scheduled SmartQoS task will be started. | The value is in the format of year-month-day. The value ranges from 2000-01-01 to 2069-12-31. When "schedule_policy" is set to "once", the value cannot be earlier than the previous day of the current date. |
| start_time=? | Time from which a scheduled SmartQoS task will be started on a specific day. | The value is in the format of HH:MM. The value ranges from 00:00 to 23:59. When "schedule_policy" is set to "once" and the start date is the day before the current date, the start time cannot be earlier than the current time. |
| duration=? | Duration for performing a scheduled SmartQoS task. | The value is in the format of HH:MM or H:M. The value ranges from 00:30 to 24:00, indicating 30 minutes to 24 hours. When "schedule_policy" is set to "once", the end time of the policy cannot be earlier than the current time. |
| io_type=? | Type of I/Os to be controlled. Only I/Os of this type will be controlled by SmartQoS. | The value can be "read_write", indicating read and write I/Os. |
| ctrl_type=? | Policy control type. | The value can be: <br>"normal": normal.<br>"hierarchical": hierarchical.<br> The default value is "normal". |
| max_bandwidth=? | Maximum bandwidth. | The value is an integer ranging from 1 to 999,999,999, expressed in MB/s. |
| max_iops=? | Maximum IOPS. | The value is an integer ranging from 100 to 999,999,999. |
| lun_id_list=? | IDs of LUNs that you want to add to a SmartQoS policy. Only the added LUNs will be controlled by SmartQoS. | To obtain the value, run "show lun general".<br>You can specify multiple LUN IDs separated by commas (,), or an ID range separated by hyphens (-), such as: 0,5-8.<br>A maximum of 512 IDs are allowed. This parameter is mutually exclusive with "file_system_id_list". |
| lun_group_id_list=? | LUN groups that you want to add to a SmartQoS policy. Only the added LUN groups will be controlled by SmartQoS. | To obtain the value, run "show lun_group general". A maximum of one ID is allowed. |
| burst_bandwidth=? | Maximum burst bandwidth. This parameter can be configured only when "max_bandwidth" is configured. | The value is an integer from 1 to 999999999 (unit: MB/s). The value must be greater than that of "max_bandwidth". |
| burst_iops=? | Maximum burst IOPS. This parameter can be configured only when "max_iops" is configured. | The value is an integer from 100 to 999999999. The value must be greater than that of "max_iops". |
| burst_time=? | Burst time. This parameter can be set only when either "burst_bandwidth" or "burst_iops" is configured. | The value is an integer from 1 to 999999999 (unit: second). |
| host_id_list=? | IDs of hosts that you want to add to a SmartQoS policy. Only the added hosts will be controlled by SmartQoS. | To obtain the value, run "show host general". You can specify multiple host IDs separated by commas (,), or an ID range separated by hyphens (-), such as: 0,5-8. A maximum of 512 IDs are allowed. |
| min_bandwidth | Minimum bandwidth. | The value is an integer ranging from 1 to 999,999,999, expressed in MB/s. |
| min_iops | Minimum IOPS. | The value is an integer ranging from 100 to 999,999,999. |
| latency | I/O latency. | The value can be "0.5ms" or "1.5ms". |
| file_system_id_list=? | IDs of the file systems to be added to the SmartQoS policy. | To obtain the value, run "show file_system general".<br>Multiple file system IDs are separated by commas (,), or by hyphens (-) to represent an ID range, for example, 0,5-8.<br>A maximum of 512 IDs can be specified. This parameter is mutually exclusive with "lun_id_list". |

##### Usage Guidelines

-   After creating a SmartQoS policy, you must run "change smartqos_policy enabled" to enable the policy so that the entire command line can take effect.
-   By using SmartQoS, the storage system can intelligently dispatch the system resources occupied by different types of I/Os. This enables prioritized I/Os to be correctly processed and balances system resource allocation when the storage resources are insufficient.
-   SmartQoS is effective for the LUNs defined by the "lun_id_list=?" parameter. That is, only those LUNs are available for I/O resource dispatching. Given different LUNs normally carry different services, specifying a range of LUNs actually determines the services carried by specific types of I/Os for those LUNs. In this way, SmartQoS can dispatch system resources according to service types, helping the applications that impose demanding requirements on I/O bandwidth and latency to operate properly even when the resources are insufficient.
-   The "ctrl_type=?" parameter defines a SmartQoS policy type. For example, assigning parameter "normal" means that the SmartQoS policy can be added to a hierarchical policy and assigning parameter "hierarchical" means that the SmartQoS policy can be added to a normal policy.
-   You must specify at least one of parameters "max_bandwidth", "max_iops", "min_bandwidth", "min_iops", and "latency".
-   The "burst_bandwidth" parameter can be configured only when "max_bandwidth" is configured. The value of "burst_bandwidth" must be greater than that of "max_bandwidth".
-   The "burst_iops" parameter can be configured only when "max_iops" is configured. The value of "burst_iops" must be greater than that of "max_iops".
-   The "burst_time" parameter can be set only when either "burst_bandwidth" or "burst_iops" is configured.
-   If the "lun_group_id_list" field is set, SmartQoS takes effect on the LUNs in the specified LUN group.
-   If the "host_id_list" field is set, SmartQoS takes effect on the hosts in the specified host list.
-   The value of parameter "min_bandwidth" cannot be greater than that of parameter "max_bandwidth". The value of parameter "min_iops" cannot be greater than that of parameter "max_iops".

##### Example

Create a SmartQoS policy, where the name is "newqos", the type is "normal", the policy will be executed every Monday starting from 13:00 on December 23, 2013 with a duration of 1 hour and 30 minutes, and the maximum bandwidth is 1024 MB/s.

```text
admin:/>create smartqos_policy name=newqos schedule_policy=weekly day_of_week=mon schedule_start_time=2013-12-23 start_time=13:00 duration=1:30 max_bandwidth=1024 ctrl_type=normal
Create SmartQoS policy successfully.
```

##### System Response

None
