# change remote_replication general


##### Function

The **change remote_replication general** command is used to modify a specified remote replication pair.

##### Format

**change remote_replication general** remote_replication_id=? { compress_enable=? \| recovery_policy=? \| synchronization_rate=? \| synchronization_type=? \[ timing_length=? timing_unit=? \| synchronize_schedule=? \] \| second_res_access=? \| remote_io_timeout_period=? \| bandwidth=? \| sync_to_async_latency=? \| async_to_sync_latency=? \| sync_to_async_bandwidth=? \| async_to_sync_bandwidth=? \| transfer_cycle=? \| switch_to_async=? \| switch_to_sync=? \| user_snap_sync_policy=? \| user_snap_retention_num=? \| copy_snap_retention_policy=? \| copy_snap_retention_num=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_replication_id=? | ID of a remote replication pair. | To obtain the value, run "show remote_replication unified". |
| recovery_policy=? | Recovery policy. | The value can be "automatic" or "manual", where: <br>"automatic": When interrupted links are recovered, a remote replication pair is automatically resumed. Data is automatically synchronized from the primary LUN to the secondary LUN.<br>"manual": When interrupted links are recovered, a remote replication pair needs to be resumed manually. The secondary LUN retains the state preserved at the time when links are interrupted. Data is not automatically synchronized from the primary LUN to the secondary LUN. |
| bandwidth | Data synchronization rate between arrays. | The value ranges from 1 to 1024, expressed in MB/s. |
| synchronization_type=? | Synchronization type. This parameter is available only for asynchronous remote replication. | The value can be: <br>"manual": Data needs to be synchronized manually.<br>"timed_wait_when_synchronization_begins": The system starts timing as soon as data synchronization starts.<br>"timed_wait_when_synchronization_ends": The system starts timing as soon as data synchronization ends.<br>"specified_time": specifies a time policy. |
| synchronization_rate=? | Synchronization speed. | The value can be "Low", "Middle", "High", or "Highest", where: <br>"Low": low.<br>"Middle": medium.<br>"High": high.<br>"Highest": highest. |
| timing_length=? | Timing period (data synchronization period). This parameter is available only when "synchronization_type" is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The value ranges from 1 to 1440, expressed in minutes.<br>For LUN-based remote replication pairs, the value ranges from 3 to 59, expressed in seconds. For file system-based remote replication pairs, the value ranges from 15 to 59, expressed in seconds. |
| timing_unit=? | Unit of the synchronization period. | The value can be: <br>"minute": minutes.<br>"second": seconds. |
| second_res_access=? | Read and write attributes of the secondary resource. | The value can be: <br>"read_only": The secondary resource can only be read.<br>"read_write": The secondary resource can be read and written. |
| remote_io_timeout_period=? | Timeout period of I/Os written to the secondary storage array during dual-write of synchronous remote replication. | The value ranges from 10 to 30, expressed in seconds. |
| compress_enable=? | Whether to enable compression. | The value can be: <br>"yes": enables compression.<br>"no": disables compression. |
| synchronize_schedule=? | Schedule for starting the synchronization of remote replication. This parameter is available only when "synchronization_type" is set to "specified_time". | Delivery by week: "{"WEEK":{"WEEKDAY":"[1,3]","TIME":"11:00"}}". "WEEKDAY" indicates the day in a week on which synchronization is enabled and the value ranges from 0 to 6. Multiple days are separated by commas (,). "TIME" indicates the time when synchronization starts on a day and the value ranges from 00:00 to 23:59.<br>Delivery by day: "{"DAY":"01:00"}". "DAY" indicates the time when synchronization starts every day and the value ranges from 00:00 to 23:59.<br>Delivery by hour: "{"HOUR":"9"}". "HOUR" indicates the time in each hour when synchronization starts and the value ranges from 0 to 59. |
| async_to_sync_latency=? | Host latency when asynchronous replication switches to synchronous replication. | The value ranges from 1 to 5000. |
| sync_to_async_bandwidth | Host bandwidth when synchronous replication switches to asynchronous replication. | - |
| sync_to_async_latency=? | Host latency when synchronous replication switches to asynchronous replication. | The value ranges from 1 to 5000. |
| async_to_sync_bandwidth=? | Host bandwidth when asynchronous replication switches to synchronous replication. | - |
| transfer_cycle | Duration during which the automatic switchover condition is met when asynchronous replication switches to synchronous replication. | - |
| switch_to_async | Whether synchronous replication automatically switches to asynchronous replication. | - |
| switch_to_sync | Whether asynchronous replication automatically switches to synchronous replication. | - |
| user_snap_sync_policy=? | User snapshot synchronization policy. | The value can be: <br>"not_sync_snap": does not synchronize user snapshots.<br>"same_as_source": synchronizes snapshots from the primary storage system to the secondary storage system.<br>"user_snap_retention_num": retains a specified number of user snapshots on the secondary storage system. |
| user_snap_retention_num=? | Number of user snapshots retained on the secondary storage system. This parameter is valid only when "user_snap_sync_policy" is set to "user_snap_retention_num". | The value ranges from 1 to 1024. |
| copy_snap_retention_policy=? | Snapshot retention policy of the secondary LUN copy. NOTE: LUN remote replication does not support this parameter. | The value can be: <br>"no_retention": does not retain copy snapshots on the secondary storage system.<br>"copy_snap_retention_num": retains a specified number of copy snapshots on the secondary storage system. |
| copy_snap_retention_num=? | Number of retained snapshots of the secondary end. NOTE: LUN remote replication does not support this parameter. This parameter is valid only when copy_snap_retention_policy=? is set to "copy_snap_retention_num". | The value ranges from 1 to 512. |

##### Usage Guidelines

-   If the recovery policy changes from "automatic" to "manual" by running this command, synchronization tasks for the selected remote replication pair will not be automatically resumed after links are recovered.
-   Before running this command, ensure that the selected remote replication pair is exactly the one you want to modify.
-   After the links disconnect, you can run the command that modifies the write protection status of the secondary LUN on the secondary storage array.
-   If you want to modify the timeout period, note the following restrictions:
-   This command is only used to modify the timeout period of the synchronous remote replication.
-   This command can be implemented only when the links between the primary and secondary storage arrays of synchronous remote replication are normal.
-   This command can be implemented only when modification of the timeout period is supported by the primary and secondary storage arrays of synchronous remote replication.

##### Example

Change the recovery policy of remote replication pair "2100ef02030405060000000200000000" to "automatic".

```text
admin:/>change remote_replication general remote_replication_id=2100ef02030405060000000200000000 recovery_policy=automatic
Command executed successfully.
```

Change the speed of remote replication pair "2100ef02030405060000000200000000" to "Highest".

```text
admin:/>change remote_replication general remote_replication_id=2100ef02030405060000000200000000 synchronization_rate=Highest
WARNING: You are about to select the "Highest" speed for synchronization.
After the operation, the remote replication pair will be synchronized at the highest speed, which may cause overloaded services and disconnection of remote replication pairs.
Suggestion: Select the "High" speed. If you select the "Highest" speed, check the performance of the local and remote devices and whether the replication link bandwidth is sufficient to prevent the disconnection of remote replication pairs during synchronization.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
