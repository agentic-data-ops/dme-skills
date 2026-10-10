# create remote_replication unified


##### Function

The **create remote_replication unified** command is used to create a remote replication pair.

##### Format

**create remote_replication unified** replication_model=? remote_device_id=? lun_id=? secondary_lun_id=? \[ is_standby=? \] \[ is_data_sync=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ synchronize_schedule=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \] \[ user_snap_sync_policy=? \] \[ user_snap_retention_num=? \] \[ copy_snap_retention_policy=? \] \[ copy_snap_retention_num=? \] \[ initial_sync_type=? \]

**create remote_replication unified** replication_model=? remote_device_id=? lun_id_list=? secondary_lun_id_list=? \[ is_standby=? \] \[ is_data_sync=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ synchronize_schedule=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \] \[ user_snap_sync_policy=? \] \[ user_snap_retention_num=? \] \[ copy_snap_retention_policy=? \] \[ copy_snap_retention_num=? \] \[ initial_sync_type=? \]

**create remote_replication unified** replication_model=? remote_device_id=? lun_id=? \[ remote_name_rule=? \] \[ name_prefix=? \] \[ name_suffix=? \] \[ remote_storage_pool_id=? \] \[ is_standby=? \] \[ is_data_sync=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ synchronize_schedule=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \] \[ user_snap_sync_policy=? \] \[ user_snap_retention_num=? \] \[ copy_snap_retention_policy=? \] \[ copy_snap_retention_num=? \] \[ initial_sync_type=? \]

**create remote_replication unified** replication_model=? remote_device_id=? file_system_id=? secondary_file_system_id=? \[ is_standby=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ synchronize_schedule=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \]

**create remote_replication unified** replication_model=? remote_device_id=? file_system_id_list=? secondary_file_system_id_list=? \[ is_standby=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ synchronize_schedule=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \]

**create remote_replication unified** replication_model=? remote_device_id=? file_system_id=? \[ remote_name_rule=? \] \[ name_prefix=? \] \[ name_suffix=? \] \[ remote_storage_pool_id=? \] \[ is_standby=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ synchronize_schedule=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \]

**create remote_replication unified** replication_model=? remote_device_id=? file_system_id=? secondary_file_system_id=? \[ recovery_policy=? \] \[ synchronization_rate=? \] \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ synchronize_schedule=? \] \[ start_synchronize_after_create=? \] \[ compress_enable=? \] \[ replication_type=? \] \[ bandwidth=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_device_id=? | Remote device ID. | To obtain the value, run "show remote_device general". |
| lun_id=? | Primary LUN ID. This parameter is used to create LUN-based remote replication pairs only. | To obtain the value, run "show lun general". |
| secondary_lun_id=? | Secondary LUN ID. This parameter is used to create LUN-based remote replication pairs only. | To obtain the value, run "show remote_lun general array_type=replication remote_device_id=?". |
| lun_id_list=? | Primary LUN ID list. | You can run the show lun general command to query the LUN ID. 2 IDs of multiple LUNs are separated by commas (,), or ID ranges are represented by hyphens (-).<br>A maximum of 100 IDs can be entered. |
| secondary_lun_id_list=? | Secondary LUN ID list. | To obtain the value, run the show remote_lun general array_type=replication remote_device_id=? command.<br>IDs of multiple LUNs are separated by commas (,), or ID ranges are represented by hyphens (-).<br>A maximum of 100 IDs can be entered. |
| file_system_id=? | Primary file system ID. This parameter is used to create file system-based remote replication pairs only. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | Local file system ID. |
| secondary_file_system_id=? | Secondary file system ID. This parameter is used to create file system-based remote replication pairs only. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | Remote file system ID. |
| file_system_id_list=? | List of primary file system IDs. | Multiple IDs are separated by commas (,), or ID ranges are represented by hyphens (-).<br>The value is an integer that ranges from 1 to 65535.<br>A maximum of 100 IDs can be entered. |
| secondary_file_system_id_list | List of secondary file system IDs. | Multiple IDs are separated by commas (,), or ID ranges are represented by hyphens (-).<br>The value is an integer that ranges from 1 to 65535.<br>A maximum of 100 IDs can be entered. |
| is_data_sync=? | Whether data on the primary and secondary resources is consistent. This parameter is used to create LUN-based remote replication pairs only. | The value can be "yes" or "no", where: <br>"yes": Data on the primary and secondary resources is consistent.<br>"no": Data on the primary and secondary resources is inconsistent. |
| recovery_policy=? | Recovery policy. | The value can be "automatic" or "manual", where: <br>"automatic": When links are recovered, a remote replication pair is automatically resumed. Data is automatically synchronized from the primary resource to the secondary resource.<br>"manual": When links are recovered, a remote replication pair needs to be resumed manually. The secondary resource retains the state preserved at the time when links are interrupted. Data is not automatically synchronized from the primary resource to the secondary resource.<br> The default value is "automatic". |
| synchronization_rate=? | Synchronization speed. | The value can be "Low", "Middle", "High", or "Highest". The default value is "Middle". |
| replication_model=? | Remote replication mode. | The value can be "synchronization" or "asynchronization", where: <br>"synchronization": synchronous remote replication.<br>"asynchronization": asynchronous remote replication. |
| synchronization_type=? | Synchronization type. This parameter is available only when "replication_model" is set to "asynchronization". | The value can be: <br>"manual": Data needs to be synchronized manually.<br>"timed_wait_when_synchronization_begins": The system starts timing as soon as data synchronization starts.<br>"timed_wait_when_synchronization_ends": The system starts timing as soon as data synchronization ends.<br>"specified_time": Specifies a time policy.<br> The default value is "manual". |
| timing_length=? | Timing period (data synchronization period). This parameter is available only when "synchronization_type" is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The value ranges from 1 to 1440, expressed in minutes.<br>For LUN-based remote replication pairs, the value ranges from 3 to 59, expressed in seconds. For file system-based remote replication pairs, the value ranges from 15 to 59, expressed in seconds. |
| timing_unit=? | Unit of the synchronization period. This parameter is available only when "synchronization_type" is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The value can be "minute" or "second". |
| synchronize_schedule=? | Schedule for starting the synchronization of remote replication. This parameter is available only when "synchronization_type" is set to "specified_time". | Delivery by week: "{"WEEK":{"WEEKDAY":"[1,3]","TIME":"11:00"}}". "WEEKDAY" indicates the day in a week on which synchronization is enabled and the value ranges from 0 to 6. Multiple days are separated by commas (,). "TIME" indicates the time when synchronization starts on a day and the value ranges from 00:00 to 23:59.<br>Delivery by day: "{"DAY":"01:00"}". where "DAY" indicates the time when synchronization starts every day and the value ranges from 00:00 to 23:59.<br>Delivery by hour: "{"HOUR":"9"}". where "HOUR" indicates the time in each hour when synchronization starts and the value ranges from 0 to 59. |
| start_synchronize_after_create=? | Whether initial synchronization will be performed after a remote replication pair is created. | The value can be "yes" or "no", where: <br>"yes": Initial synchronization will be performed.<br>"no": Initial synchronization will not be performed.<br> The default value is "yes". |
| compress_enable=? | Whether to enable compression. | The value can be "yes" or "no", where: <br>"yes": enables compression.<br>"no": disables compression. |
| is_standby=? | Whether an asynchronous remote replication pair in the standby state is created. | The value can be "no" or "yes", where: <br>"no": creates an asynchronous remote replication pair not in the standby state.<br>"yes": creates an asynchronous remote replication pair in the standby state. |
| replication_type | Remote replication type. | The value can be "comm" or "cloud", where: <br>"comm": creates a common remote replication pair.<br>"cloud": creates a cloud-based remote replication pair. |
| bandwidth | Data synchronization rate between arrays. | The value ranges from 0 to 1024, expressed in MB/s. |
| remote_io_timeout_period=? | Timeout period of I/Os written to the secondary storage array during dual-write of synchronous remote replication. This parameter is available only when "replication_model" is set to "synchronization". | The value ranges from 10 to 30, expressed in seconds. |
| user_snap_sync_policy=? | User snapshot synchronization policy. This parameter is valid only when "replication_model" is set to "asynchronization". | The value can be: <br>"not_sync_snap": does not synchronize user snapshots.<br>"same_as_source": synchronizes snapshots from the primary storage system to the secondary storage system.<br>"user_snap_retention_num": retains a specified number of user snapshots on the secondary storage system. |
| user_snap_retention_num=? | Number of user snapshots retained on the secondary storage system. This parameter is valid only when "user_snap_sync_policy" is set to "user_snap_retention_num". | The value ranges from 1 to 1024. |
| copy_snap_retention_policy=? | Retention policy of snapshot copies on the secondary storage system.This parameter is valid only when "replication_model=?" is set to "asynchronization". NOTE: This parameter is not supported by LUN-based remote replication. | The value can be: <br>"no_retention": does not retain copy snapshots on the secondary storage system.<br>"copy_snap_retention_num": retains a specified number of copy snapshots on the secondary storage system. |
| copy_snap_retention_num=? | Number of snapshot copies retained on the secondary storage system.This parameter is valid only when "copy_snap_retention_policy=?" is set to "copy_snap_retention_num". NOTE: This parameter is not supported by LUN-based remote replication. | The value ranges from 1 to 512. |
| initial_sync_type=? | Initial synchronization type of readable and writable snapshot LUNs. This parameter is valid only when "replication_model" is set to "asynchronization". | The value can be: <br>"initial_sync_full_data": synchronizes all data.<br>"initial_sync_increment_data": only synchronizes data written to a snapshot. |
| remote_name_rule=? | Naming rules of remote resources. | The value can be: <br>"automatically_generated": The name is automatically generated by the system.<br>"same_as_locally": The name is the same as that of the local resource.<br>"user_defined": The name is user-defined. |
| name_prefix=? | User-defined name prefix. This parameter is valid only when "remote_name_rule=?" is set to "user_defined". | The value contains 1 to 32 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.), and must start with a digit or letter. |
| name_suffix=? | User-defined name suffix. This parameter is valid only when "remote_name_rule=?" is set to "user_defined". | The value contains 1 to 16 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| remote_storage_pool_id=? | Storage pool ID of the remote device. | The value ranges from 0 to 63. |
| remote_vstore_id=? | ID of a remote vStore. | Value range: 0 to 1023. |

##### Usage Guidelines

None

##### Example

Create a remote replication pair and set its remote replication mode to "asynchronization", primary LUN ID to "0", remote device ID to "0", and secondary LUN ID to "1".

```text
admin:/>create remote_replication unified replication_model=asynchronization remote_device_id=0 lun_id=0 secondary_lun_id=1
DANGER: You are about to create a replication mapping between primary and secondary resources. The data on the secondary resource will be overwritten by that on the primary resource after copy.
Suggestion: Before performing this operation, ensure that you select the right primary and secondary resources and the secondary resource is not being accessed by the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create multiple remote replication pairs. The remote replication mode is asynchronous, the primary LUN ID list is 0, 2, 4, and 6, the remote device ID is 0, and the secondary LUN IDs are 1, 3, 5, and 7.

```text
admin:/>create remote_replication unified replication_model=asynchronization remote_device_id=0 lun_id_list=0,2,4,6 secondary_lun_id_list=1,3,5,7
DANGER: You are about to create a replication mapping between primary and secondary resources. The data on the secondary resource will be overwritten by that on the primary resource after copy.
Suggestion: Before performing this operation, ensure that you select the right primary and secondary resources and the secondary resource is not being accessed by the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a remote replication pair. Set the remote replication mode to asynchronous remote replication, primary file system ID to "1", remote device ID to "0", and secondary file system ID to "1".

```text
admin:/>create remote_replication unified replication_model=asynchronization remote_device_id=0 file_system_id=1 secondary_file_system_id=1
DANGER: You are about to create a replication mapping between primary and secondary resources. The data on the secondary resource will be overwritten by that on the primary resource after copy.
Suggestion: Before performing this operation, ensure that you select the right primary and secondary resources and the secondary resource is not being accessed by the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create multiple remote replication pairs. The remote replication mode is asynchronous. The primary file system IDs are 2, 4, 6, and 8. The remote device ID is 0. The secondary file system IDs are 1, 3, 5, and 7.

```text
admin:/>create remote_replication unified replication_model=asynchronization remote_device_id=0 file_system_id_list=2,4,6,8 secondary_file_system_id_list=1,3,5,7
DANGER: You are about to create a replication mapping between primary and secondary resources. The data on the secondary resource will be overwritten by that on the primary resource after copy.
Suggestion: Before performing this operation, ensure that you select the right primary and secondary resources and the secondary resource is not being accessed by the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create multiple remote replication pairs. Set the remote replication mode to asynchronous. The primary LUN ID list ranges from 0 to 4, the remote device ID is 0, and the secondary LUN ID ranges from 5 to 9.

```text
admin:/>create remote_replication unified replication_model=asynchronization remote_device_id=0 lun_id_list=0-4 secondary_lun_id_list=5-9
DANGER: You are about to create a replication mapping between primary and secondary resources. The data on the secondary resource will be overwritten by that on the primary resource after copy.
Suggestion: Before performing this operation, ensure that you select the right primary and secondary resources and the secondary resource is not being accessed by the host.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create multiple remote replication pairs. Set the remote replication mode to asynchronous, the primary file system ID list to 1-5, the remote device ID list to 0, and the secondary file system ID list to 5-9.

```text
admin:/>create remote_replication unified replication_model=asynchronization remote_device_id=0 file_system_id_list=1-5 secondary_file_system_id_list=5-9
DANGER: You are about to create a replication mapping between primary and secondary resources. The data on the secondary resource will be overwritten by that on the primary resource after copy.
Suggestion: Before performing this operation, ensure that you select the right primary and secondary resources and the secondary resource is not being accessed by the host.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
