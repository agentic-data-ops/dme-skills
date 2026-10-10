# show file_system general


##### Function

The **show file_system general** command is used to query details about file systems.

##### Format

**show file_system general** \[ file_system_id=? \| file_system_name=? \| file_system_id_list=? \| file_system_name_list=? \] \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_system_id=? | File system ID. | To obtain the value, run the "show file_system general" command without parameters. |
| file_system_name=? | File system name. | To obtain the value, run the "show file_system general" command without parameters. |
| filter_name=? | Filters file system names. NOTE: This parameter is not supported by the current version. The execution result is invalid. | To obtain the value, run the "show file_system general" command without parameters. |
| filter_storage_pool_id=? | Filters file system storage pool IDs. NOTE: This parameter is not supported by the current version. The execution result is invalid. | To obtain the value, run the "show file_system general" command without parameters. |
| filter_health_status=? | Filters file system health status. NOTE: This parameter is not supported by the current version. The execution result is invalid. | To obtain the value, run the "show file_system general" command without parameters. |
| filter_running_status=? | Filters file system running status. NOTE: This parameter is not supported by the current version. The execution result is invalid. | To obtain the value, run the "show file_system general" command without parameters. |
| offset=? | Start serial number of the query. The returned data does not include the specified object and starts from the next data record of the specified object. | To obtain the value, run the "show file_system general" command without parameters. |
| limit=? | Number of entries to be queried at a time. | To obtain the value, run the "show file_system general" command without parameters. |
| sort_by=? | Sorting field. The value can be "Name", "healthStatus", "runningStatus", or "capacity". | To obtain the value, run the "show file_system general" command without parameters. |
| sort_mode=? | Sorting order. The value can be "Ascending" or "Descending". | To obtain the value, run the "show file_system general" command without parameters. |
| file_system_id_list=? | List of file system IDs. | Multiple IDs are separated by commas (,), or ID ranges represented using hyphens(-). |
| file_system_name_list=? | List of file system names. | Separate multiple file system names using commas (,), or use a hyphen (-) to separate two file system names to represent a file system range. For a file system range, the two names before and after the hyphen (-) must be of the same format and length. |
| vstore_id=? | vStore ID. | The default value is 0. |

##### Usage Guidelines

Before running this command, check that you have selected the correct file system.

##### Example

Query brief information about all the file systems.

```text
admin:/>show file_system general
ID  Name       Pool ID  Smart Cache Partition ID  Cache Partition ID  Health Status  Running Status  Capacity  Type  Available Capacity  Snapshot Used Capacity  Sub Type  Vstore ID  Application Scenario  Clone  Audit Log FS
--  ---------  -------  ------------------------  ------------------  -------------  --------------  --------  ----  ------------------  ----------------------  --------  ---------  --------------------  -----  -------------
0   fs         0        --                        --                  Normal         Online          16.000PB  Thin             1.981TB                36.000KB  Normal    --         User Defined          No     No
1   fs_clone   0        --                        --                  Normal         Online          16.000PB  Thin             1.980TB                  0.000B  Normal    --         User Defined          No     No
3   fs_clone2  0        --                        --                  Normal         Online          16.000PB  Thin             1.980TB                  0.000B  Normal    --         User Defined          Yes    No
```

Query details about a specific file system.

```text
admin:/>show file_system general file_system_id=1
ID : 1
Name : FileSystem1438915680Pool390000
Pool ID : 39
Smart Cache Partition ID : --
Cache Partition ID : --
Initial Distribute Policy : Automatic
Health Status : Normal
Running Status : Online
Capacity : 11.000GB
Description :
Type : Thin
Snapshot Reserve(%) : 20
Owner Controller : 0A
Work Controller : 0A
IO Priority : Low
Block Size : 8.000KB
Checksum Enabled : Yes
Atime Enabled : No
Show Snapshot Directory Enabled : Yes
Available Capacity : 8.432GB
Capacity Threshold(%) : 90
Auto Delete Snapshot Enabled : No
Snapshot Used Capacity : 0.000B
Timing Snapshot Max Number : 16
Snapshot Reserve Capacity : 2.199GB
Timing Snapshot Enabled : No
Timing Snapshot Schedule ID : --
Snapshot Background Freeing Capacity : --
Used Capacity Ratio(%) : 0
Dedup Enabled : Yes
Byte_by_byte Comparison Enabled : No
Compression Enabled : Yes
Compression Method : Fast
Dedup Saved Capacity : 0.000B
Dedup Saved Ratio(%) : 0
Compression Saved Capacity : 0.000B
Compression Saved Ratio(%) : 0
Total Saved Capacity : 0.000B
Total Saved Ratio(%) : 0
Smart Cache Cached Size : 0.000B
Smart Cache Hit Rage(%) : 0
Sub Type : Normal
Remote Replication ID(s) : --
Intelligent Dedup Enabled : Yes
Dedup Running Status : Yes
Traverse Dir Adapter : Yes
Dedup MetaData Sample Ratio : 1
Isolate Enable : Yes
Vstore ID : 1
Application Scenario : Database
Hyper Metro Pair ID(s) : --
Hyper Vault Pair ID(s): --
Clone          : No
Clone Parent      : --
Clone Children Number : 1
Clone Split Speed   : --
Clone Split Status   : --
Clone Split Progress(%): --
Dedup Checksum Enabled : Yes
Space Self Adjustment Mode: Grow
Auto Size Enable: Yes
Auto Shrink Threshold Percent(%): 50
Auto Grow Threshold Percent(%): 85
Minimum Auto Size: 20GB
Maximum Auto Size: 100GB
Auto Size Increment: 10GB
Space Recycle Mode: Autosize First
Allocated Capacity: 3GB
Alternate Data Streams Enabled: Yes
Support File System Tier: Yes
SSD Capacity Upper Limit Of User Data: 5.000GB
Used SSD Capacity By User Data: 1.000GB
Prefetch Policy: Constant
Prefetch Value:  64KB
Read Write Status: Read Only
Long Filename Enabled: Yes
Security Style: Mixed
Background Dedup Enabled: No
Background Compression Enabled: No
Atime Update Mode : off
Workload Type Name : NAS_Default
Support 32bit Inode : No
Schedule ID   : --
Unix Permissions : 755
Fs Layer Distribution Algorithm : Performance Mode
Schedule Name : --
Audit Log FS : No
```

Query details about a specific file system.

```text
admin:/>show file_system general file_system_name=FileSystem1438915680Pool390000
ID : 1
Name : FileSystem1438915680Pool390000
Pool ID : 39
Smart Cache Partition ID : --
Cache Partition ID : --
Initial Distribute Policy : Automatic
Health Status : Normal
Running Status : Online
Capacity : 11.000GB
Description :
Type : Thin
Snapshot Reserve(%) : 20
Owner Controller : 0A
Work Controller : 0A
IO Priority : Low
Block Size : 8.000KB
Checksum Enabled : Yes
Atime Enabled : No
Show Snapshot Directory Enabled : Yes
Available Capacity : 8.432GB
Capacity Threshold(%) : 90
Auto Delete Snapshot Enabled : No
Snapshot Used Capacity : 0.000B
Timing Snapshot Max Number : 16
Snapshot Reserve Capacity : 2.199GB
Timing Snapshot Enabled : No
Timing Snapshot Schedule ID : --
Snapshot Background Freeing Capacity : --
Used Capacity Ratio(%) : 0
Dedup Enabled : Yes
Byte_by_byte Comparison Enabled : No
Compression Enabled : Yes
Compression Method : Fast
Dedup Saved Capacity : 0.000B
Dedup Saved Ratio(%) : 0
Compression Saved Capacity : 0.000B
Compression Saved Ratio(%) : 0
Total Saved Capacity : 0.000B
Total Saved Ratio(%) : 0
Smart Cache Cached Size : 0.000B
Smart Cache Hit Rage(%) : 0
Sub Type : Normal
Remote Replication ID(s) : --
Intelligent Dedup Enabled : Yes
Dedup Running Status : Yes
Traverse Dir Adapter : Yes
Dedup MetaData Sample Ratio : 1
Isolate Enable : Yes
Vstore ID : 1
Application Scenario : Database
Hyper Metro Pair ID(s) : --
Hyper Vault Pair ID(s): --
Clone          : No
Clone Parent      : --
Clone Children Number : 1
Clone Split Speed   : --
Clone Split Status   : --
Clone Split Progress(%): --
Dedup Checksum Enabled : Yes
Space Self Adjustment Mode: Grow
Auto Size Enable: Yes
Auto Shrink Threshold Percent(%): 50
Auto Grow Threshold Percent(%): 85
Minimum Auto Size: 20GB
Maximum Auto Size: 100GB
Auto Size Increment: 10GB
Space Recycle Mode: Autosize First
Allocated Capacity: 3GB
Alternate Data Streams Enabled: Yes
Support File System Tier: Yes
SSD Capacity Upper Limit Of User Data: 5.000GB
Used SSD Capacity By User Data: 1.000GB
Prefetch Policy: Constant
Prefetch Value:  64KB
Read Write Status: Read Only
Long Filename Enabled: Yes
Security Style: Mixed
Background Dedup Enabled: No
Background Compression Enabled: No
Atime Update Mode : off
Workload Type Name : NAS_Default
Support 32bit Inode : No
Schedule ID  : --
Unix Permissions : 755
Fs Layer Distribution Algorithm : Performance Mode
Schedule Name : --
Audit Log FS : No
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| ID | File system ID. |
| Name | File system name. |
| Pool ID | Storage pool ID. |
| Smart Cache Partition ID | SmartCache partition ID. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Schedule ID | ID of the HyperCDP schedule to which the file system is added. |
| Cache Partition ID | Cache partition ID. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Initial Distribute Policy | Initial distribution policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Health Status | Health status. |
| Running Status | Running status. |
| Capacity | Total capacity of the file system. |
| Description | Description of the file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Type | Type of the file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Snapshot Reserve(%) | Proportion of space reserved for snapshots. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Owner Controller | Owning controller. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Work Controller | Working controller. NOTE: This field is not supported by the current version. The returned value is invalid. |
| IO Priority | I/O priority. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Block Size | Block size. |
| Checksum Enabled | Whether the consistency verification function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Atime Enabled | Whether the Atime function is enabled. |
| Atime Update Mode | Atime update mode. |
| Show Snapshot Directory Enabled | Whether to show the snapshot directory. |
| Available Capacity | Available capacity. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Capacity Threshold(%) | Capacity alarm threshold. |
| Auto Delete Snapshot Enabled | Whether the function of deleting timing snapshots is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Snapshot Used Capacity | Capacity occupied by snapshots. |
| Timing Snapshot Max Number | Maximum number of timing snapshots. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Snapshot Reserve Capacity | Reserved capacity for snapshots. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Timing Snapshot Enabled | Whether the timing snapshot function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Timing Snapshot Schedule ID | ID of the timing snapshot policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Snapshot Background Freeing Capacity | File system capacity that is being reclaimed in the background. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Used Capacity Ratio(%) | Proportion of consumed capacity in the file system. |
| Dedup Enabled | Whether the deduplication function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Byte_by_byte Comparison Enabled | Whether the byte-by-byte comparison function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Compression Enabled | Whether the compression function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Compression Method | Compression algorithm. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Dedup Saved Capacity | Capacity saved by deduplication. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Dedup Saved Ratio(%) | Proportion of the capacity saved by deduplication out of the capacity consumed by the system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Compression Saved Capacity | Capacity saved by compression. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Compression Saved Ratio(%) | Proportion of the capacity saved by compression out of the capacity consumed by the system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Total Saved Capacity | Total capacity saved by deduplication and compression. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Total Saved Ratio(%) | Proportion of the capacity saved by deduplication and compression out of the capacity consumed by the system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Smart Cache Cached Size | Cached capacity of the file system in SmartCache. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Smart Cache Hit Rage(%) | Read hit ratio of the file system in SmartCache. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Sub Type | Sub-type of the file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Remote Replication ID(s) | Specifies the remote replication ID. |
| Intelligent Dedup Enabled | Whether the intelligent deduplication function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Dedup Running Status | Running status of the deduplication function. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Traverse Dir Adapter | Traverses directory with 32 bits. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Dedup MetaData Sample Ratio | Deduplication metadata sample ratio. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Isolate Enable | Whether the file system isolation function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Vstore ID | vStore ID. |
| Application Scenario | Application scenario of the file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Hyper Metro Pair ID(s) | HyperMetro pair ID. |
| Hyper Vault Pair ID(s) | HyperVault ID. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Clone | Whether the file system is a clone file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Clone Parent | Name of the parent file system of a clone file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Clone Children Number | Number of clone file systems. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Clone Split Speed | Split speed of a clone file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Clone Split Status | Split status of a clone file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Clone Split Progress(%) | Split progress of a clone file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Dedup Checksum Enabled | Whether the deduplication verification function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Auto Size Enable | Switch of automatic capacity adjustment. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Auto Shrink Threshold Percent(%) | Percentage threshold that triggers automatic capacity reduction. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Space Self Adjustment Mode | Automatic capacity adjustment mode. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Auto Grow Threshold Percent(%) | Percentage threshold that triggers automatic capacity expansion. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Minimum Auto Size | Lower limit of automatic capacity reduction. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Maximum Auto Size | Upper limit of automatic capacity expansion. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Auto Size Increment | Capacity change of a single expansion/reduction. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Space Recycle Mode | Capacity reclamation mode. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Allocated Capacity | Capacity that a file system has applied for. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Support File System Tier | Whether the tiering feature is supported. NOTE: This field is not supported by the current version. The returned value is invalid. |
| SSD Capacity Upper Limit Of User Data | SSD capacity upper limit of user data. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Alternate Data Streams Enabled | Whether the alternate data streams function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Used SSD Capacity By User Data | Used SSD capacity by user data. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Prefetch Policy | Cache prefetch policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Prefetch Value | Cache prefetch value. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Read Write Status | File system read and write status. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Long Filename Enabled | Whether the long file name function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Security Style | Security style supported by the file system. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Background Dedup Enabled | Whether the background deduplication function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Background Compression Enabled | Whether the background compression function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Workload Type Name | Name of the application type. |
| Support 32bit Inode | Whether 32-bit inodes are supported. |
| Unix Permissions | UNIX permissions of the file system root directory. |
| Fs Layer Distribution Algorithm | Data distribution algorithm of the file system. <br>"Performance Mode": performance mode. Directories and files are allocated to the access controller preferentially, to improve access performance of directories and files.<br>"Capacity Balance Mode": capacity balancing mode. Directories and files are evenly allocated to each controller by capacity.<br>"Directory Balance Mode": directory balancing mode. Directories are evenly allocated to each controller by quantity.<br>"Directory Shuffle Mode": directory polling mode. Directories are allocated to each controller based on the creation sequence. |
| Audit Log FS | Whether it is an audit log file system. |
| Schedule Name | Name of the schedule to which the file system has been added. |
