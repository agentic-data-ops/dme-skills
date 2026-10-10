# create remote_replication general


##### Function

The **create remote_replication general** command is used to create a LUN-based remote replication pair.

##### Format

**create remote_replication general** replication_model=? lun_id=? remote_device_id=? secondary_lun_id=? \[ is_data_sync=? \] \[ is_standby=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \] \[ remote_io_timeout_period=? \] \[ user_snap_sync_policy=? \] \[ user_snap_retention_num=? \] \[ copy_snap_retention_policy=? \] \[ copy_snap_retention_num=? \] \[ initial_sync_type=? \]

**create remote_replication general** replication_model=? lun_id=? remote_device_id=? \[ remote_name_rule=? \] \[ name_prefix=? \] \[ name_suffix=? \] \[ remote_storage_pool_id=? \] \[ is_data_sync=? \] \[ is_standby=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \] \[ remote_io_timeout_period=? \] \[ user_snap_sync_policy=? \] \[ user_snap_retention_num=? \] \[ copy_snap_retention_policy=? \] \[ copy_snap_retention_num=? \] \[ initial_sync_type=? \]

**create remote_replication general** replication_model=? lun_id=? remote_device_id=? \[ remote_name_rule=? \] \[ name_prefix=? \] \[ name_suffix=? \] \[ remote_storage_pool_id=? \] \[ is_data_sync=? \] \[ is_standby=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \] \[ remote_io_timeout_period=? \] \[ user_snap_sync_policy=? \] \[ user_snap_retention_num=? \] \[ copy_snap_retention_policy=? \] \[ copy_snap_retention_num=? \] \[ initial_sync_type=? \]

**create remote_replication general** replication_model=? lun_id_list=? remote_device_id=? secondary_lun_id_list=? \[ is_standby=? \] \[ is_data_sync=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \] \[ remote_io_timeout_period=? \] \[ user_snap_sync_policy=? \] \[ user_snap_retention_num=? \] \[ initial_sync_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| replication_model=? | Remote replication mode. | The value can be: <br>"synchronization": indicates synchronous remote replication.<br>"asynchronization": indicates asynchronous remote replication. |
| lun_id=? | Primary LUN ID. | To obtain the value, run "show lun general". |
| remote_device_id=? | Remote device ID. | To obtain the value, run "show remote_device general". |
| secondary_lun_id=? | Secondary LUN ID. | To obtain the value, run "show remote_lun general array_type=replication remote_device_id=?". |
| is_data_sync=? | Whether data on the primary and secondary LUNs is consistent. | The value can be: <br>"yes": Data on the primary and secondary LUNs is consistent.<br>"no": Data on the primary and secondary LUNs is inconsistent.<br> The default value is "no". |
| recovery_policy=? | Recovery policy. | The value can be: <br>"automatic": When interrupted links are recovered, a remote replication pair is automatically resumed. Data is automatically synchronized from the primary LUN to the secondary LUN.<br>"manual": When interrupted links are recovered, a remote replication pair needs to be resumed manually. The secondary LUN retains the state preserved at the time when links are interrupted. Data is not automatically synchronized from the primary LUN to the secondary LUN.<br> The default value is "automatic". |
| synchronization_rate=? | Synchronization rate. | The value can be: <br>"Low": indicates the low rate.<br>"Middle": indicates the medium rate.<br>"High": indicates the high rate.<br>"Highest": indicates the highest rate.<br> The default value is "Middle". |
| synchronization_type=? | Synchronization type. This parameter is available only when replication_model=? is set to "asynchronization". | The value can be: <br>"manual": Data needs to be synchronized manually.<br>"timed_wait_when_synchronization_begins": The system starts timing as soon as data synchronization starts.<br>"timed_wait_when_synchronization_ends": The system starts timing as soon as data synchronization ends.<br>"specified_time": Specifies a time policy.<br> The default value is "manual". |
| timing_length=? | Timing period (data synchronization period). This parameter is available only when synchronization_type=? is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The value ranges from 1 to 1440, expressed in minutes.<br>The value ranges from 3 to 59, expressed in seconds.<br>The default value is 60 minutes. |
| timing_unit=? | Unit of the synchronization period. | The value can be: <br>"minute": indicates minutes.<br>"second": indicates seconds. |
| start_synchronize_after_create=? | Whether initial synchronization will be performed after a remote replication pair is created. | The value can be: <br>"yes": Initial synchronization will be performed.<br>"no": Initial synchronization will not be performed.<br> The default value is "yes". |
| compress_enable=? | Enables or disables compression. This parameter is available only when replication_model=? is set to "asynchronization". | The value can be: <br>"yes": enables compression.<br>"no": disables compression.<br> The default value is "no". |
| is_standby=? | Whether an asynchronous remote replication pair in the standby state is created. | The value can be: <br>"no": creates an asynchronous remote replication pair not in the standby state.<br>"yes": creates an asynchronous remote replication pair in the standby state. |
| replication_type | Type of the remote replication. | The value can be: <br>"comm": creates a common remote replication pair. |
| synchronize_schedule=? | Schedule for starting the synchronization of remote replication pair. This parameter is available only when "synchronization_type" is set to "specified_time". | Delivery by week: "{"WEEK":{"WEEKDAY":"[1,3]","TIME":"11:00"}}". "WEEKDAY" indicates the day in a week on which synchronization is enabled and the value ranges from 0 to 6. Multiple days are separated by commas (,). "TIME" indicates the time when synchronization starts on a day and the value ranges from 00:00 to 23:59.<br>Delivery by day: "{"DAY":"01:00"}". "DAY" indicates the time when synchronization starts every day and the value ranges from 00:00 to 23:59.<br>Delivery by hour: "{"HOUR":"9"}". "HOUR" indicates the time in each hour when synchronization starts and the value ranges from 0 to 59. |
| bandwidth=? | Data synchronization rate between arrays. | The value ranges from 1 to 1024, expressed in MB/s. |
| remote_io_timeout_period=? | Timeout period of I/Os written to the secondary storage array during dual-write of synchronous remote replication. This parameter is available only when "replication_model=?" is set to "synchronization". | The value ranges from 10 to 30, expressed in seconds. |
| user_snap_sync_policy=? | User snapshot synchronization policy. This parameter is valid only when "replication_model=?" is set to "asynchronization". | The value can be: <br>"not_sync_snap": does not synchronize user snapshots.<br>"same_as_source": synchronizes snapshots from the primary storage system to the secondary storage system.<br>"user_snap_retention_num": retains a specified number of user snapshots on the secondary storage system. |
| user_snap_retention_num=? | Number of user snapshots retained on the secondary storage system. This parameter is valid only when "user_snap_sync_policy=?" is set to "user_snap_retention_num". | The value ranges from 1 to 512. |
| copy_snap_retention_policy=? | Retention policy of snapshot copies on the secondary storage system.This parameter is valid only when "replication_model=?" is set to "asynchronization". NOTE: This parameter is not supported by LUN-based remote replication. | The value can be: <br>"no_retention": does not retain snapshot copies on the secondary storage system.<br>"copy_snap_retention_num": retains a specified number of snapshot copies on the secondary storage system. |
| copy_snap_retention_num=? | Number of snapshot copies retained on the secondary storage system.This parameter is valid only when "copy_snap_retention_policy=?" is set to "copy_snap_retention_num". NOTE: This parameter is not supported by LUN-based remote replication. | The value ranges from 1 to 512. |
| initial_sync_type=? | Initial synchronization type of readable and writable snapshot LUNs. This parameter is valid only when "replication_model=?" is set to "asynchronization". | The value can be: <br>"initial_sync_full_data": synchronizes all data.<br>"initial_sync_increment_data": only synchronizes data written to a snapshot. |
| remote_name_rule=? | Naming rules of remote resources. | The value can be: <br>"automatically_generated": The name is automatically generated by the system.<br>"same_as_locally": The name is the same as that of the local resource.<br>"user_defined": The name is user-defined. |
| name_prefix=? | User-defined name prefix. This parameter is valid only when "remote_name_rule=?" is set to "user_defined". | The value contains 1 to 32 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.), and must start with a digit or letter. |
| name_suffix=? | User-defined name suffix. This parameter is valid only when "remote_name_rule=?" is set to "user_defined". | The value contains 1 to 16 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| remote_storage_pool_id=? | Storage pool ID of the remote device. | The value ranges from 0 to 63. |
| lun_id_list | List of primary LUN IDs. | You can run the show lun general command to query the value of this parameter.<br>IDs of multiple LUNs are separated by commas (,), or ID ranges are represented by hyphens (-).<br>A maximum of 100 IDs can be entered. |
| secondary_lun_id_list | Secondary LUN ID list. | by using show remote_lun general array_type=replication remote_device_id=?.<br>IDs of multiple LUNs are separated by commas (,), or ID ranges are represented by hyphens (-).<br>A maximum of 100 IDs can be entered. |

##### Usage Guidelines

None

##### Example

Create a remote replication pair and set its mode to "asynchronization", primary LUN ID to "0", remote device ID to "0", and secondary LUN ID to "1".

```text
admin:/>create remote_replication general replication_model=asynchronization lun_id=0 remote_device_id=0 secondary_lun_id=1
DANGER: You are about to create a replication mapping between primary LUN and secondary LUN. The data on the secondary LUN will be overwritten by that on the primary LUN after copy, and the data on the secondary resources is unrecoverable.
Suggestion: Before performing this operation, ensure that all data on the secondary resources can be overwritten.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
