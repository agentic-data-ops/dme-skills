# show smartqos_policy general


##### Function

The **show smartqos_policy general** command is used to query details on existing SmartQoS policies of the storage system. By using SmartQoS, the storage system can allocate its resources to different types of I/Os on demand.

##### Format

**show smartqos_policy general** \[ smartqos_policy_id=? \]

##### Parameters

| Parameter            | Description              | Value                                                                                                                                                                                                          |
|----------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "**show smartqos_policy general**" without parameters. |

##### Usage Guidelines

-   To query details on existing SmartQoS policies, run **show smartqos_policy general**.
-   To query details on a specific SmartQoS policy, run **show smartqos_policy general** smartqos_policy_id=?.

##### Example

Query details on existing SmartQoS policies.

```text
admin:/>show smartqos_policy general

ID Name Health Status Running Status IO Type Enabled LUN List Filesystem List Ctrl Type     Ctrl Status
-- ------- ------------- -------------- ---------- ------- -------- -------  ------------  -----------
0 newqos Normal Inactive Read_write No -- --  Normal  Inactive
3 newqos2 Normal Inactive Read_write No 0,1,2 --  Normal  Inactive
2 newqos3 Normal Inactive Read_write No 7 --  Normal  Inactive
4 newqos4 Normal Inactive Read_write No 6 --  Hierarchical  Inactive
```

Query details on SmartQoS policy "0".

```text
admin:/>show smartqos_policy general smartqos_policy_id=0

ID : 0
Name : SmartQoS000
Health Status : Normal
Running Status : Inactive
IO Type : Read_write
Enabled : No
LUN List : 0,1,2,3
Max Bandwidth(MBps) : --
Min Bandwidth(MBps) : --
Max IOPS : 5000
Min IOPS : --
Latency(ms) : --
Schedule Policy : Weekly
Schedule Start Time : 2013-12-21
Start Time : 08:00
Duration : 24 hour(s),0 minute(s)
Schedule Days : Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday
Filesystem List: --
Ctrl Type: Normal
Parent Smartqos Policy Id:  --
Smartqos Policy List:  --
LUN Group ID List: --
Burst Bandwidth(MBps) : --
Burst IOPS : --
Burst Time : --
Host List : --
Ctrl Status : Achieved
```

##### System Response

The following table describes the parameter meanings.

| Parameter                 | Meaning                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------|
| Health Status             | Health status.                                                                                |
| Running Status            | Running status.                                                                               |
| IO Type                   | Type of the I/O that you want to control.                                                     |
| LUN List                  | ID of LUNs that you add to a SmartQoS policy.                                                 |
| Max Bandwidth(MBps)       | Maximum bandwidth.                                                                            |
| Min Bandwidth(MBps)       | Minimum bandwidth.                                                                            |
| Max IOPS                  | Maximum IOPS.                                                                                 |
| Min IOPS                  | Minimum IOPS.                                                                                 |
| Latency(ms)               | Latency for a SmartQoS policy.                                                                |
| Schedule Policy           | Time policy for triggering SmartQoS.                                                          |
| Schedule Start Time       | Day from which a scheduled SmartQoS task will be started.                                     |
| Start Time                | Time from which a scheduled SmartQoS task will be started on a specific day.                  |
| Duration                  | Duration for performing a scheduled SmartQoS task.                                            |
| Filesystem List           | ID of file systems that you add to a SmartQoS policy.                                         |
| Ctrl Type                 | Type of the SmartQoS policy that you want to control.                                         |
| Parent Smartqos Policy Id | ID of the parent hierarchical SmartQoS policy that the specified SmartQoS policy is added to. |
| Smartqos Policy List      | ID of normal SmartQoS policies that you add to a SmartQoS policy.                             |
| Enabled                   | State of a SmartQoS policy.                                                                   |
| ID                        | ID of a SmartQoS policy.                                                                      |
| Name                      | Name of a SmartQoS policy.                                                                    |
| Schedule Days             | Schedule day of a SmartQoS policy.                                                            |
| LUN Group ID List         | ID of LUN groups that you add to a SmartQoS policy.                                           |
| Burst Bandwidth(MBps)     | Maximum burst bandwidth.                                                                      |
| Burst IOPS                | Maximum burst IOPS.                                                                           |
| Burst Time                | Burst time.                                                                                   |
| Host List                 | ID list of hosts that you add to a SmartQoS policy.                                           |
| Ctrl Status               | Status of the SmartQoS policy performance achieving the control objective.                    |
