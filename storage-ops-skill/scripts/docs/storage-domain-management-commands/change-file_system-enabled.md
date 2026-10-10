# change file_system enabled


##### Function

The **change file_system enabled** command is used to enable file system related functions, such as to enable checksum, to perform periodic snapshots, and to modify the Atime.

##### Format

**change file_system enabled** \[ file_system_id=? \| file_system_name=? \] { checksum_enabled=? \| atime_enabled=? \| atime_update_mode=? \| show_enabled=? \| auto_delete_snapshot_enabled=? \| timing_snapshot_enabled=? \| isolate_enabled=? \| alternate_data_streams_enabled=? \| vstore_id=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_system_id=? | File system ID. | The value is an integer between 0 and 65535. If the value is not specified, the system automatically allocates an ID to the newly created file system. |
| file_system_name=? | File system name. | The value consists of 1 to 255 ASCII characters including numbers, letters, and underscores (_). |
| checksum_enabled=? | Whether to enable the checksum function. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the checksum function.<br>"no": disables the checksum function. |
| atime_enabled=? | Whether to enable the Atime function. | The value can be "yes" or "no", where: <br>"yes": enables the Atime function.<br>"no": disables the Atime function. |
| atime_update_mode=? | Atime update mode. | The value can be "off", "hourly", or "daily", where: <br>"off": disables the update.<br>"hourly": updates data every hour.<br>"daily": updates data every day.<br> The default value is "off". |
| compression_enabled=? | Whether to enable the compression function. | The value can be yes or no. The options are as follows: <br>yes: The compression function is enabled.<br>no: The compression function is disabled. |
| dedup_enabled=? | Whether to enable the deduplication function. | The value can be yes or no. The options are as follows: <br>yes: The deduplication function is enabled.<br>no: deduplication is disabled. |
| show_enabled=? | Whether to show the snapshot directory. | The value can be "yes" or "no", where: <br>"yes": shows the snapshot directory.<br>"no": does not show the snapshot directory. |
| auto_delete_snapshot_enabled=? | Whether to enable the function of automatically deleting snapshots. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the function of automatically deleting snapshots.<br>"no": disables the function of automatically deleting snapshots. |
| timing_snapshot_enabled=? | Whether to enable the timing snapshot function. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the timing snapshot function.<br>"no": disables the timing snapshot function. |
| isolate_enabled=? | Whether to enable the object-based isolation function. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the isolation flag setting function.<br>"no": disables the isolation flag setting function. |
| alternate_data_streams_enabled=? | Whether to enable the alternate data streams function. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the alternate data streams function.<br>"no": disables the alternate data streams function. |
| vstore_id | vStore ID. | The value ranges from 0 to 1023. |

##### Usage Guidelines

-   Before running this command, check that you have selected the correct file system.
-   You must enter the file system ID.

##### Example

Check the configuration of the file system before the modification.

```text
admin:/>show file_system general file_system_id=0
ID : 0
Name : fs003
Pool ID : 0
Cache Partition ID :
Health Status : Normal
Running Status : Online
Capacity : 10.000GB
Description :
Type : Thin
Snapshot Reserve(%) : 20
Owner Controller : 0B
Work Controller : 0B
IO Priority : Middle
Block Size : 64.000KB
Checksum Enabled : Yes
Atime Enabled : No
Atime Update Mode : off
Show Snapshot Directory Enabled : Yes
Available Capacity : 7.874GB
Capacity Threshold(%) : 50
Auto Delete Snapshot Enabled : No
Snapshot Used Capacity : 0.000B
Timing Snapshot Max Number : 20
Snapshot Reserve Capacity : --
Timing Snapshot Enabled : No
Timing Snapshot Schedule ID :
Snapshot Background Freeing Capacity : --
Used Capacity Ratio(%) : 1
Initial Distribute Policy : Automatic
Alternate Data Streams Enabled : No
```

Enable all features for the file system.

```text
admin:/>change file_system enabled file_system_id=0 atime_enabled=yes atime_update_mode=daily  auto_delete_snapshot_enabled=yes checksum_enabled=yes show_enabled=yes timing_snapshot_enabled=yes alternate_data_streams_enabled=yes
WARNING: You are about to run a command to set the auto delete snapshot switch used by the system to delete the snapshot in this filesystem when the filesystem has insufficient capacity.
If the switch is set to yes, there may be risks.
Suggestion: Before running this command, ensure that you have selected the correct filesystem.
Have you read warning message carefully?<y/n>y
Are you sure you really want to perform the operation?<y/n>y
Command executed successfully.
```

Check the modification result.

```text
admin:/>show file_system general file_system_id=0
ID : 0
Name : fs003
Pool ID : 0
Cache Partition ID :
Health Status : Normal
Running Status : Online
Capacity : 10.000GB
Description :
Type : Thin
Snapshot Reserve(%) : 20
Owner Controller : 0B
Work Controller : 0B
IO Priority : Middle
Block Size : 64.000KB
Checksum Enabled : Yes
Atime Enabled : Yes
Atime Update Mode : daily
Show Snapshot Directory Enabled : Yes
Available Capacity : 7.874GB
Capacity Threshold(%) : 50
Auto Delete Snapshot Enabled : Yes
Snapshot Used Capacity : 0.000B
Timing Snapshot Max Number : 20
Snapshot Reserve Capacity : --
Timing Snapshot Enabled : Yes
Timing Snapshot Schedule ID :
Snapshot Background Freeing Capacity : --
Used Capacity Ratio(%) : 1
Initial Distribute Policy : Automatic
Alternate Data Streams Enabled : Yes
```

Check file system configuration.

```text
admin:/>show file_system general file_system_id=0
ID : 0
Name : fs003
Pool ID : 0
Cache Partition ID :
Health Status : Normal
Running Status : Online
Capacity : 10.000GB
Description :
Type : Thin
Snapshot Reserve(%) : 20
Owner Controller : 0B
Work Controller : 0B
IO Priority : Middle
Block Size : 64.000KB
Checksum Enabled : Yes
Atime Enabled : No
Atime Update Mode : off
Show Snapshot Directory Enabled : Yes
Available Capacity : 7.874GB
Capacity Threshold(%) : 50
Auto Delete Snapshot Enabled : No
Snapshot Used Capacity : 0.000B
Timing Snapshot Max Number : 20
Snapshot Reserve Capacity : --
Timing Snapshot Enabled : No
Timing Snapshot Schedule ID :
Snapshot Background Freeing Capacity : --
Used Capacity Ratio(%) : 1
Initial Distribute Policy : Automatic
Isolate Enable : Yes
Alternate Data Streams Enabled : Yes
```

##### System Response

None
