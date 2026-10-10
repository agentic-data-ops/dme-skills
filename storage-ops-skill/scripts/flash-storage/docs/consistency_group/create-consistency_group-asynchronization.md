# create consistency_group asynchronization


##### Function

The **create consistency_group asynchronization** command is used to create asynchronous consistency groups.

##### Format

**create consistency_group asynchronization** name=? \[ remote_device_id=? \] \[ bandwidth=? \| compress_enable=? \| recovery_policy=? \| synchronization_rate=? \| user_snap_sync_policy=? \| user_snap_retention_num=? \| copy_snap_retention_policy=? \| copy_snap_retention_num=? \| synchronization_type=? \[ timing_length=? timing_unit=? \] \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a consistency group. | The value contains 1 to 255 ASCII characters including digits, letters, hyphens (-), underscores (_), and periods (.), and must start with a digit or a letter. |
| remote_device_id=? | Remote device ID. | To obtain the value, run "show remote_device general". |
| recovery_policy=? | Link recovery policy. This parameter defines a policy for recovering the links that were unexpectedly disconnected for the remote replication tasks in a consistency group. | The value can be: <br>"automatic": When links are recovered, the remote replication services in the consistency group are resumed automatically.<br>"manual": When links are recovered, the remote replication services in the consistency group are resumed manually. The consistency group retains the state preserved at the time when links are interrupted, and does not resume the interrupted remote replication services automatically.<br> The default value is "automatic". |
| synchronization_rate=? | Synchronization rate. | The value can be: <br>"Low": indicates the low rate.<br>"Middle": indicates the medium rate.<br>"High": indicates the high rate.<br>"Highest": indicates the highest rate.<br> The default value is "Middle". |
| synchronization_type=? | Synchronization type. | The value can be: <br>"manual": Data is synchronized manually.<br>"timed_wait_when_synchronization_begins": When a data synchronization job is started, the storage system waits for a period before implementing the next synchronization job.<br>"timed_wait_when_synchronization_ends": When a data synchronization job is completed, the storage system waits for a period before implementing the next synchronization job.<br>"specified_time": specifies a time policy<br> The default value is "manual". |
| synchronize_schedule=? | Schedule for starting the synchronization of remote replication consistency group. This parameter is available only when "synchronization_type" is set to "specified_time". | Delivery by week: "{"WEEK":{"WEEKDAY":"[1,3]","TIME":"11:00"}}". "WEEKDAY" indicates the day in a week on which synchronization is enabled and the value ranges from 0 to 6. Multiple days are separated by commas (,). "TIME" indicates the time when synchronization starts on a day and the value ranges from 00:00 to 23:59.<br>Delivery by day: "{"DAY":"01:00"}". "DAY" indicates the time when synchronization starts every day and the value ranges from 00:00 to 23:59.<br>Delivery by hour: "{"HOUR":"9"}". "HOUR" indicates the time in each hour when synchronization starts and the value ranges from 0 to 59. |
| timing_length=? | Synchronization period. This parameter is valid only when "synchronization_type=?" is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The value ranges from 1 to 1440, expressed in minutes.<br>The value ranges from 10 to 59, expressed in seconds.<br>For periodic synchronization, the default value is 60 minutes. |
| timing_unit=? | Unit of the synchronization period. | The value can be: <br>"minute": minutes.<br>"second": seconds. |
| compress_enable=? | Whether to enable compression. | The value can be "yes" or "no", where: <br>"yes": enables compression.<br>"no": disables compression. |
| bandwidth=? | Data synchronization rate between arrays. | The value ranges from 1 to 1024, expressed in MB/s. |
| user_snap_sync_policy=? | User snapshot synchronization policy. | The value can be: <br>"not_sync_snap": does not synchronize user snapshots.<br>"same_as_source": synchronizes snapshots from the primary storage system to the secondary storage system.<br>"user_snap_retention_num": retains a specified number of user snapshots on the secondary storage system. |
| user_snap_retention_num=? | Number of user snapshots retained on the secondary storage system. This parameter is valid only when "user_snap_sync_policy=?" is set to "user_snap_retention_num". | The value ranges from 1 to 512. |
| copy_snap_retention_policy | Copy snapshot retention policy at the secondary end. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The options are as follows: <br>no_retention: The secondary end does not retain copy snapshots.<br>copy_snap_retention_num: The secondary end retains a specified number of copy snapshots. |
| copy_snap_retention_num | Number of retained copy snapshots at the secondary end. NOTE: This parameter is not supported in this version, and the execution result is invalid. This parameter is valid only when copy_snap_retention_policy=? is set to "copy_snap_retention_num". | The value ranges from 1 to 512. |

##### Usage Guidelines

-   An asynchronous consistency group can only contain asynchronous instead of synchronous remote replication pairs.
-   In asynchronous remote replication, a write success message is returned to the host as long as the primary LUN returns a write success message to the host. Then, a user manually triggers or the system periodically triggers data synchronization from the primary LUN to the secondary LUN. This replication mode features relatively high responsiveness to write requests but suffers from potential data inconsistency between the primary and secondary LUNs.

##### Example

Create an asynchronous consistency group, where the name of the consistency group is "efg", the synchronization rate is "middle", and the recovery policy is automatic.

```text
admin:/>create consistency_group asynchronization name=efg remote_device_id=0 synchronization_rate=middle recovery_policy=automatic
Command executed successfully.
```

Create an asynchronous consistency group, where the name of the consistency group is "efg", the synchronization rate is "Highest", and the recovery policy is automatic.

```text
admin:/>create consistency_group asynchronization name=efg remote_device_id=0 synchronization_rate=Highest
WARNING:You are about to select the "Highest" speed to create a consistency group.
After the operation, remote replication pairs in the consistency group will be synchronized at the highest speed, which may cause overloaded services and disconnection of remote replication pairs.
Suggestion: Select the "High" speed. If you select the "Highest" speed, check the performance of the local and remote devices and whether the replication link bandwidth is sufficient to prevent the disconnection of remote replication pairs during synchronization.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
