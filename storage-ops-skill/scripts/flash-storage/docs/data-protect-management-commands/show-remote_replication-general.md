# show remote_replication general


##### Function

The **show remote_replication general** command is used to query information about LUN-based remote replication pairs.

##### Format

**show remote_replication general** \[ remote_replication_id=? \]

##### Parameters

| Parameter               | Description                      | Value                                                                                                                                                                                                                         |
|-------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| remote_replication_id=? | ID of a remote replication pair. | To obtain the value, run "**show remote_replication general**" without parameters. |

##### Usage Guidelines

-   Run the "**show remote_replication general**" command to query basic information about all remote replication pairs.
-   Run the "**show remote_replication general** remote_replication_id=?" command to query details of a specified remote replication pair.

##### Example

Query basic information about all remote replication pairs.

```text

admin:/>show remote_replication general

ID                                Health Status  Running Status  Is Primary  Replication Mode  Compress Enable  Compress Valid  Time Difference  DR Star ID  Local LUN Name  Remote LUN Name
--------------------------------  -------------  --------------  ----------  ----------------  ---------------  --------------  ---------------  ----------  --------------  ------------------------
2100ef02030405060000000200000000  Normal         Normal          Yes         Asynchronous      No               No                     02:53:41  --          LUN0010000      Huaage_LUN0010000_547289
2100ef02030405060000000200000001  Normal         Normal          Yes         Asynchronous      No               No                     02:53:41  --          LUN0010001      Huaage_LUN0010001_255782

```

Query details of the remote replication pair whose ID is "2100f102030405060000000200000000".

```text
admin:/>show remote_replication general remote_replication_id=2100ef02030405060000000200000000
ID                                 : 2100ef02030405060000000200000000
Health Status                      : Normal
Running Status                     : Normal
Is Primary                         : Yes
Local LUN ID                       : 6
Local LUN Name                     : LUN0030004
Remote Device ID                   : 0
Remote Device SN                   : ST000000000000000212
Remote Device Name                 : Huawei.Storage
Remote LUN ID                      : 5
Remote LUN Name                    : LUN0030003
Primary LUN Capacity               : 1.000GB
Synchronization Type               : Specified Time
Recovery Policy                    : Automatic
Replication Mode                   : Asynchronous
Progress(%)                        : 100
Start Time                         : 2020-05-21/11:58:16 UTC+08:00
End Time                           : 2020-05-21/11:58:16 UTC+08:00
Rate                               : Middle
Timing Length                      : --
Primary LUN Data Status            : Consistent
Second LUN Data Status             : Consistent
Second LUN Access                  : Read Only
Is Restore                         : No
Is In Consistency Group            : No
Consistency Group ID               : --
Consistency Group Name             : --
Is Data Sync                       : --
Compress Enable                    : No
Compress Valid                     : No
Remote I/O Timeout Period(s)       : --
Time Difference                    : 00:00:22
Time Remaining for Synchronization : --
DR Star ID                         : --
Replication Type                   : --
Bandwidth(MB/s)                    : --
Synchronize Schedule               : {"WEEK":{"WEEKDAY":"[1,3]","TIME":"11:00"}}
Time Policy                        : Execute at 11:00 on day Mon,Wed every week
Current Transfer Size(KB)          : --
Next Transfer Size(KB)             : 40
The Latency Of Async To sync(ms)   : 44
The Bandwidth of Sync to Async(KB/s): 10240
The Bandwidth of Async to Sync(KB/s): 5120
The Latency of Sync to Async(ms)   : 100
The Transfer Cycle(minute)         : 100
The Automatic Switch to Async      : close
The Automatic Switch to sync       : close
User Snapshot Sync Policy          : Not Sync Snapshot
User Snapshot Retention Num        : --
Copy Snapshot Retention Policy     : No Retention
Copy Snapshot Retention Num        : --
Resource Subtype                   : Common LUN
```

##### System Response

The following table describes the parameter meanings.

| Parameter                            | Meaning                                                                                                                                                          |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DR Star ID                           | DR Star trio ID.                                                                                                                                                 |
| ID                                   | Remote replication pair ID.                                                                                                                                      |
| Health Status                        | Health status.                                                                                                                                                   |
| Running Status                       | Running status.                                                                                                                                                  |
| Is Primary                           | Whether the current end the primary end of the remote replication pair.                                                                                          |
| Local LUN ID                         | Local LUN ID.                                                                                                                                                    |
| Local LUN Name                       | Local LUN name.                                                                                                                                                  |
| Remote Device ID                     | Remote device ID.                                                                                                                                                |
| Remote Device SN                     | SN of the remote device.                                                                                                                                         |
| Remote Device Name                   | Remote device name.                                                                                                                                              |
| Remote LUN ID                        | Remote LUN ID.                                                                                                                                                   |
| Remote LUN Name                      | Remote LUN name.                                                                                                                                                 |
| Primary LUN Capacity                 | Primary LUN capacity.                                                                                                                                            |
| Synchronization Type                 | Synchronization type.                                                                                                                                            |
| Recovery Policy                      | Recovery policy.                                                                                                                                                 |
| Replication Mode                     | Remote replication mode.                                                                                                                                         |
| Progress(%)                          | Synchronization progress.                                                                                                                                        |
| Start Time                           | Synchronization start time.                                                                                                                                      |
| End Time                             | Synchronization end time.                                                                                                                                        |
| Rate                                 | Synchronization rate.                                                                                                                                            |
| Timing Length                        | Timing period (data synchronization period).                                                                                                                     |
| Primary LUN Data Status              | Primary LUN data status.                                                                                                                                         |
| Second LUN Data Status               | Secondary LUN data status.                                                                                                                                       |
| Second LUN Access                    | Secondary LUN access permission.                                                                                                                                 |
| Is Restore                           | Whether the secondary LUN is in the rollback state.                                                                                                              |
| Is In Consistency Group              | Whether the remote replication pair belongs to a consistency group.                                                                                              |
| Consistency Group ID                 | ID of the consistency group to which the remote replication pair belongs.                                                                                        |
| Consistency Group Name               | Name of the consistency group to which the remote replication pair belongs.                                                                                      |
| Is Data Sync                         | Whether data on the primary and secondary LUNs is consistent.                                                                                                    |
| Compress Enable                      | Whether compression is enabled.                                                                                                                                  |
| Compress Valid                       | Whether compression is valid.                                                                                                                                    |
| Remote I/O Timeout Period(s)         | Remote I/O timeout period.                                                                                                                                       |
| Time Difference                      | Time difference between the data synchronization points in time of the primary and secondary resources in a synchronization period of a remote replication pair. |
| Time Remaining for Synchronization   | Time remaining for synchronization.                                                                                                                              |
| Replication Type                     | Remote replication type (common remote replication).                                                                                                             |
| Bandwidth                            | Data synchronization rate between arrays.                                                                                                                        |
| Synchronize Schedule                 | Schedule for starting the synchronization of a remote replication pair.                                                                                          |
| Time Policy                          | Timing policy.                                                                                                                                                   |
| Current Transfer Size                | Amount of write data to be transferred currently.                                                                                                                |
| Next Transfer Size                   | Amount of write data to be transferred next time.                                                                                                                |
| The Latency of Async To sync(ms)     | Host latency when asynchronous replication switches to synchronous replication.                                                                                  |
| The Bandwidth of Sync to Async(KB/s) | Host bandwidth when synchronous replication switches to asynchronous replication.                                                                                |
| The Bandwidth of Async to Sync(KB/s) | Host bandwidth when asynchronous replication switches to synchronous replication.                                                                                |
| The Latency of Sync to Async(ms)     | Host latency when synchronous replication switches to asynchronous replication.                                                                                  |
| The Transfer Cycle(minute)           | Duration during which the automatic switchover condition is met when asynchronous replication switches to synchronous replication.                               |
| The Automatic Switch to Async        | Whether synchronous replication automatically switches to asynchronous replication.                                                                              |
| The Automatic Switch to sync         | Whether asynchronous replication automatically switches to synchronous replication.                                                                              |
| User Snapshot Sync Policy            | User snapshot synchronization policy.                                                                                                                            |
| User Snapshot Retention Num          | Number of user snapshots retained on the secondary storage system.                                                                                               |
| Copy Snapshot Retention Policy       | Retention policy of copy snapshots on the secondary storage system.                                                                                              |
| Copy Snapshot Retention Num          | Number of copy snapshots retained on the secondary storage system.                                                                                               |
| Resource Subtype                     | Resource sub-type.                                                                                                                                               |
