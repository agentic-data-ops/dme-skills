# change consistency_group general


##### Function

The **change consistency_group general** command is used to modify information about a consistency group.

##### Format

**change consistency_group general** consistency_group_id=? { bandwidth=? \| compress_enable=? \| name=? \| recovery_policy=? \| synchronization_rate=? \| synchronization_type=? \[ timing_length=? timing_unit=? synchronize_schedule=? \] \| second_res_access=? \| sync_to_async_latency=? \| async_to_sync_latency=? \| sync_to_async_bandwidth=? \| async_to_sync_bandwidth=? \| transfer_cycle=? \| remote_io_timeout_period=? \| switch_to_async=? \| switch_to_sync=? \| user_snap_sync_policy=? \| user_snap_retention_num=? \| copy_snap_retention_policy=? \| copy_snap_retention_num=? \| description=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| consistency_group_id=? | ID of a consistency group. | To obtain the value, run "show consistency_group general". |
| name=? | Updated name of a consistency group. | The value contains 1 to 255 ASCII characters, including digits, letters, hyphens (-), underscores (_), and periods (.), and must start with a digit or a letter. |
| recovery_policy=? | Recovery policy when remote replication links of a consistency group are recovered from an unexpected disconnection. | The value can be: <br>"automatic": When links are recovered, the remote replication services in the consistency group are resumed automatically.<br>"manual": When links are recovered, the remote replication services in the consistency group are resumed manually. The consistency group retains the state preserved at the time when links are interrupted, and does not resume the interrupted remote replication services automatically.<br> The default value is "automatic". |
| synchronization_rate=? | Updated synchronization rate. | The value can be: <br>"Low": indicates the low rate.<br>"Middle": indicates the medium rate.<br>"High": indicates the high rate.<br>"Highest": indicates the highest rate.<br> The default value is "Middle". |
| synchronization_type=? | Updated synchronization type. This parameter is valid only when the consistency group type is asynchronous. | The value can be: <br>"manual": Data is synchronized manually.<br>"timed_wait_when_synchronization_begins": When a data synchronization job is started, the storage system waits for a period before implementing the next synchronization job.<br>"timed_wait_when_synchronization_ends": When a data synchronization job is completed, the storage system waits for a period before implementing the next synchronization job.<br>"specified_time": specifies a time policy.<br> The default value is "manual". |
| timing_length=? | Synchronization period. This parameter is valid only when "synchronization_type=?" is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The value ranges from 1 to 1440, expressed in minutes.<br>The value ranges from 10 to 59, expressed in seconds. |
| timing_unit=? | Unit of the synchronization period. | The value can be: <br>"minute": minutes.<br>"second": seconds. |
| second_res_access=? | Read and write attributes of the secondary LUN. | The value can be: <br>"read_only": The secondary LUN can only be read.<br>"read_write": The secondary LUN can be read and written. |
| compress_enable=? | Whether to enable compression. | The value can be "yes" or "no", where: <br>"yes": enables compression.<br>"no": disables compression. |
| bandwidth | Data synchronization rate between arrays. | The value ranges from 1 to 1024, expressed in MB/s. |
| synchronize_schedule=? | Schedule for starting the synchronization of remote replication consistency group. This parameter is available only when "synchronization_type" is set to "specified_time". | Delivery by week: "{"WEEK":{"WEEKDAY":"[1,3]","TIME":"11:00"}}". "WEEKDAY" indicates the day in a week on which synchronization is enabled and the value ranges from 0 to 6. Multiple days are separated by commas (,). "TIME" indicates the time when synchronization starts on a day and the value ranges from 00:00 to 23:59.<br>Delivery by day: "{"DAY":"01:00"}". "DAY" indicates the time when synchronization starts every day and the value ranges from 00:00 to 23:59.<br>Delivery by hour: "{"HOUR":"9"}". "HOUR" indicates the time in each hour when synchronization starts and the value ranges from 0 to 59. |
| transfer_cycle | Duration during which the automatic switchover condition is met when asynchronous replication switches to synchronous replication. | - |
| async_to_sync_bandwidth=? | Host bandwidth when asynchronous replication switches to synchronous replication. | - |
| sync_to_async_latency=? | Host latency when synchronous replication switches to asynchronous replication. | The value ranges from 1 to 5000. |
| sync_to_async_bandwidth=? | Host bandwidth when synchronous replication switches to asynchronous replication. | - |
| async_to_sync_latency=? | Host latency when asynchronous replication switches to synchronous replication. | The value ranges from 1 to 5000. |
| remote_io_timeout_period=? | Timeout period of I/Os written to the secondary storage array during dual-write of synchronous remote replication. | The value ranges from 10 to 30, expressed in seconds. |
| switch_to_sync | Whether asynchronous replication automatically switches to synchronous replication. | - |
| switch_to_async | Whether synchronous replication automatically switches to asynchronous replication. | - |
| user_snap_sync_policy=? | User snapshot synchronization policy. | The value can be: <br>"not_sync_snap": does not synchronize user snapshots.<br>"same_as_source": synchronizes snapshots from the primary storage system to the secondary storage system.<br>"user_snap_retention_num": retains a specified number of user snapshots on the secondary storage system. |
| user_snap_retention_num=? | Number of user snapshots retained on the secondary storage system. This parameter is valid only when "user_snap_sync_policy=?" is set to "user_snap_retention_num". | The value ranges from 1 to 512. |
| description=? | Description. | A string of 1 to 255 ASCII characters. |
| copy_snap_retention_policy | Copy snapshot retention policy at the secondary end. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The options are as follows: <br>no_retention: The secondary end does not retain copy snapshots.<br>copy_snap_retention_num: The secondary end retains a specified number of copy snapshots. |
| copy_snap_retention_num | Number of retained copy snapshots at the secondary end. NOTE: This parameter is not supported in this version, and the execution result is invalid. This parameter is valid only when copy_snap_retention_policy=? is set to "copy_snap_retention_num". | The value ranges from 1 to 512. |

##### Usage Guidelines

-   If the recovery policy changes from "automatic" to "manual" by running this command, synchronization tasks for the selected consistency group will not be automatically resumed after links are recovered.
-   Before running this command, ensure that the selected consistency group is exactly the one you want to modify.

##### Example

Modify the properties of consistency group "200bc79b99520000". Set the name to "newname", recovery policy to manual, and description to "xx".

```text
admin:/>change consistency_group general consistency_group_id=200bc79b99520000 name=newname recovery_policy=manual description=xx
Command executed successfully.
```

Modify the properties of consistency group "200bc79b99520000". Set the name to "newname", synchronization speed to highest, recovery policy to manual, and description to xx.

```text
admin:/>change consistency_group general consistency_group_id=200bc79b99520000 name=newname synchronization_rate=Highest recovery_policy=manual description=xx
WARNING:
You are about to select the "Highest" speed for synchronization. After the operation,remote replication pairs in the consistency group will be synchronized at the highest speed, which may cause overloaded services and disconnection of remote replication pairs.
Suggestion: Select the "High" speed. If you select the "Highest" speed, check the performance of the data receiving end and whether the link bandwidth between local and remote arrays is sufficient to prevent the disconnection of  remote replication pairs during synchronization.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
