# create consistency_group protect_group


##### Function

The **create consistency_group protect_group** command is used to create a remote replication consistency group for a protection group.

##### Format

**create consistency_group protect_group** replication_model=? protect_group_id=? remote_device_id=? remote_storage_pool_id=? \[ compress_enable=? \| recovery_policy=? \| synchronization_rate=? \| user_snap_sync_policy=? \| user_snap_retention_num=? \| copy_snap_retention_policy=? \| copy_snap_retention_num=? \| synchronization_type=? \[ timing_length=? timing_unit=? \] \[ replication_type=? \] \] \*

**create consistency_group protect_group** replication_model=? protect_group_id=? remote_device_id=? remote_storage_pool_id=? \[ remote_name_rule=? \| name_prefix=? \| name_suffix=? \| compress_enable=? \| recovery_policy=? \| synchronization_rate=? \| user_snap_sync_policy=? \| user_snap_retention_num=? \| copy_snap_retention_policy=? \| copy_snap_retention_num=? \| synchronization_type=? \[ timing_length=? timing_unit=? \] \[ replication_type=? \] \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| replication_model=? | Replication mode. | The value can be: <br>"asynchronization": indicates asynchronous replication.<br>"synchronization": indicates synchronous replication. |
| protect_group_id=? | Protection group ID. | The value ranges from 0 to 16383. |
| remote_device_id=? | Remote device ID. | The value ranges from 0 to 63. |
| remote_storage_pool_id=? | Storage pool ID of the remote device. | The value ranges from 0 to 63. |
| compress_enable=? | Whether to enable compression. | The value can be "yes" or "no", where: <br>"yes": enables compression.<br>"no": disables compression. |
| recovery_policy=? | Recovery policy when remote replication links of a consistency group are recovered from an unexpected disconnection. | The value can be: <br>"automatic": When links are recovered, the remote replication services in the consistency group are resumed automatically.<br>"manual": When links are recovered, the remote replication services in the consistency group are resumed manually. The consistency group retains the state preserved at the time when links are interrupted, and does not resume the interrupted remote replication services automatically.<br> The default value is "automatic". |
| synchronization_rate=? | Synchronization rate. | The value can be: <br>"Low": indicates the low rate.<br>"Middle": indicates the medium rate.<br>"High": indicates the high rate.<br>"Highest": indicates the highest rate.<br> The default value is "Middle". |
| synchronization_type=? | Synchronization type. | The value can be: <br>"manual": Data is synchronized manually.<br>"timed_wait_when_synchronization_begins": When a data synchronization job is started, the storage system waits for a period before implementing the next synchronization job.<br>"timed_wait_when_synchronization_ends": When a data synchronization job is completed, the storage system waits for a period before implementing the next synchronization job.<br>"specified_time": Specifies a time policy.<br> The default value is "manual". |
| synchronize_schedule | Schedule for starting the synchronization of remote replication consistency group. This parameter is available only when "synchronization_type" is set to "specified_time". | Delivery by week: "{"WEEK":{"WEEKDAY":"[1,3]","TIME":"11:00"}}". "WEEKDAY" indicates the day in a week on which synchronization is enabled and the value ranges from 0 to 6. Multiple days are separated by commas (,). "TIME" indicates the time when synchronization starts on a day and the value ranges from 00:00 to 23:59.<br>Delivery by day: "{"DAY":"01:00"}". "DAY" indicates the time when synchronization starts every day and the value ranges from 00:00 to 23:59.<br>Delivery by hour: "{"HOUR":"9"}". "HOUR" indicates the time in each hour when synchronization starts and the value ranges from 0 to 59. |
| timing_length=? | Synchronization period. This parameter is valid only when "synchronization_type=?" is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The value ranges from 1 to 1440, expressed in minutes.<br>The value ranges from 10 to 59, expressed in seconds.<br>The default value is 60 minutes.<br>For 2200 V3, the value ranges from 15 to 1440. The unit is minute. |
| timing_unit=? | Unit of the synchronization period. | The value can be: <br>"minute": indicates minutes.<br>"second": indicates seconds.<br>For 2200 V3, the unit is minute. |
| replication_type=? | Type of the consistency group. | The value can be: <br>"comm": common consistency group. |
| user_snap_sync_policy=? | User snapshot synchronization policy. This parameter is valid only when "replication_model=?" is set to "asynchronization". | The value can be: <br>"not_sync_snap": does not synchronize user snapshots.<br>"same_as_source": synchronizes snapshots from the primary storage system to the secondary storage system.<br>"user_snap_retention_num": retains a specified number of user snapshots on the secondary storage system. |
| user_snap_retention_num=? | Number of user snapshots retained on the secondary storage system. This parameter is valid only when "user_snap_sync_policy=?" is set to "user_snap_retention_num". | The value ranges from 1 to 512. |
| remote_name_rule=? | Naming rules of remote resources. | The value can be: <br>"automatically_generated": The name is automatically generated by the system.<br>"same_as_locally": The name is the same as that of the local resource.<br>"user_defined": The name is user-defined. |
| name_prefix=? | User-defined name prefix. This parameter is valid only when "remote_name_rule=?" is set to "user_defined". | The value contains 1 to 32 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.), and must start with a digit or letter. |
| name_suffix=? | User-defined name suffix. This parameter is valid only when "remote_name_rule=?" is set to "user_defined". | The value contains 1 to 16 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| copy_snap_retention_policy | Copy snapshot retention policy at the secondary end. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The options are as follows: <br>no_retention: The secondary end does not retain copy snapshots.<br>copy_snap_retention_num: The secondary end retains a specified number of copy snapshots. |
| copy_snap_retention_num | Number of retained copy snapshots at the secondary end. NOTE: This parameter is not supported in this version, and the execution result is invalid. This parameter is valid only when copy_snap_retention_policy=? is set to "copy_snap_retention_num". | The value ranges from 1 to 512. |

##### Usage Guidelines

After this command is executed, the system automatically creates LUNs (with the same properties as all member LUNs in the local protection group) in the storage pool of the specified remote device. In addition, the system creates remote replication pairs and a remote replication consistency group, and adds the pairs to the consistency group.

##### Example

Create a remote replication consistency group for local protection group "0", remote device "0", and remote storage resource pool "0" in the manual recovery policy.

```text
admin:/>create consistency_group protect_group replication_model=asynchronization protect_group_id=0 remote_device_id=0 remote_storage_pool_id=0 synchronization_type=manual
Enabling protection for PG or LUN group (aa) in background.
Run the "show task general task_id=1" command to query the execution result.
```

Create a remote replication consistency group in manual synchronization mode based on local protection group 0, remote device 0, remote storage resource pool 0, and remote protection group name suffix \_slv.

```text
admin:/>create consistency_group protect_group replication_model=asynchronization protect_group_id=0 remote_device_id=0 remote_storage_pool_id=0 remote_name_rule=user_defined name_suffix=_slv synchronization_type=manual
Enabling protection for PG or LUN group (aa) in background.
Run the "show task general task_id=1" command to query the execution result.
```

##### System Response

None
