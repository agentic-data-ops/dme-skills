# show remote_replication unified


##### Function

The **show remote_replication unified** command is used to query information about remote replication pairs.

##### Format

**show remote_replication unified** \[ list_type=? \] \[ remote_replication_id=? \]

##### Parameters

| Parameter               | Description                 | Value                                                                                                                                                                                                      |
|-------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| list_type=?             | Object type.                | The value can be "lun" or "file_system".                                                                                                                                                                   |
| remote_replication_id=? | Remote replication pair ID. | To obtain the value, run "**show remote_replication unified**". |

##### Usage Guidelines

None

##### Example

Batch query information about remote replication pairs.

```text

admin:/>show remote_replication unified

ID                                Type         Health Status  Running Status  Is Primary  Remote Device SN      Replication Mode  User Type  Compress Enable  Compress Valid  Time Difference  Dr Star ID  Local Resource Name  Remote Resource Name
--------------------------------  -----------  -------------  --------------  ----------  ----------------  ---------  ---------------  --------------  ---------------  ----------  -------------------  ------------------------
2100ef02030405060000000200000000  LUN          Normal         Normal          Yes         ST000000000000000212  Asynchronous      --         No               No                     02:37:30  --          LUN0010000           Huaage_LUN0010000_547289
2100ef02030405060000000200000001  LUN          Normal         Normal          Yes         ST000000000000000212  Asynchronous      --         No               No                     02:37:30  --          LUN0010001           Huaage_LUN0010001_255782
2100ef02030405060000000200000002  File System  Normal         Normal          Yes         ST000000000000000212  Asynchronous      --         No               No                     02:37:18  --          1                    Huaage_1_538921
2100ef02030405060000000200000003  File System  Normal         Normal          Yes         ST000000000000000212  Asynchronous      --         No               No                     02:37:14  --          2                    Huaage_2_606952
2100e102030405060000000200000004  File System  Normal         Normal          No          ST000000000000000212  Asynchronous      --         No               No                    106:27:56  --          Huaage_4_983925      4

2100e102030405060000000200000005  File System  Normal         Normal          No          ST000000000000000212  Asynchronous      --         No               No                    106:27:56  --          Huaage_5_983496      5

```

Batch query information about file system-based remote replication pairs.

```text

admin:/>show remote_replication unified

ID                                Type         Health Status  Running Status  Is Primary  Remote Device SN      Replication Mode  User Type  Compress Enable  Compress Valid  Time Difference  Dr Star ID  Local Resource Name  Remote Resource Name
--------------------------------  -----------  -------------  --------------  ----------  ----------------  ---------  ---------------  --------------  ---------------  ----------  -------------------  ------------------------
2100ef02030405060000000200000002  File System  Normal         Normal          Yes         ST000000000000000212  Asynchronous      --         No               No                     02:37:18  --          1                    Huaage_1_538921
2100ef02030405060000000200000003  File System  Normal         Normal          Yes         ST000000000000000212  Asynchronous      --         No               No                     02:37:14  --          2                    Huaage_2_606952
2100e102030405060000000200000004  File System  Normal         Normal          No          ST000000000000000212  Asynchronous      --         No               No                    106:27:56  --          Huaage_4_983925      4

2100e102030405060000000200000005  File System  Normal         Normal          No          ST000000000000000212  Asynchronous      --         No               No                    106:27:56  --          Huaage_5_983496      5

```

Query details of the remote replication pair whose ID is "2100f102030405060000000200000000".

```text
admin:/>show remote_replication unified remote_replication_id=2100f102030405060000000200000000
ID                           : 2100f102030405060000000200000000
Type                         : File system
Health Status                : Normal
Running Status               : Normal
Is Primary                   : Yes
Local Resource ID            : 16
Local Resource Name          : FS1
Remote Device ID             : 0
Remote Device SN             : ST000000000000000148
Remote Device Name           : Huawei.Storage
Remote Resource ID           : 16
Remote Resource Name         : Huawei.Storage_LUN0170000566
Primary Resource Capacity    : 1.000GB
Synchronization Type         : Manual
Recovery Policy              : Automatic
Replication Mode             : Asynchronous
Start Time                   : 2019-10-10/14:19:25 UTC+08:00
End Time                     : 2019-10-10/14:19:26 UTC+08:00
Rate                         : Middle
Time Policy                  : --
Timing Length                : --
Primary Resource Data Status : Consistent
Second Resource Data Status  : Consistent
Second Resource Access       : Read Only
Is Restore                   : No
User Type                    : --
Compress Enable              : No
Compress Valid               : No
Remote I/O Timeout Period(s) : --
Second Resource Capacity     : --
Time Difference              : --
Vstore Pair ID               : --
Is Local Pair                : --
Dr Star ID                   : --
Replication Type             : --
Bandwidth(MB/s)              : --
Synchronize Schedule         : --
Progress(%)                  : --
Local vStore ID              : 1
Local vStore Name            : vStore1
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
| Type                                 | Remote replication type.                                                                                                                                         |
| Health Status                        | Health status.                                                                                                                                                   |
| Running Status                       | Running status.                                                                                                                                                  |
| Is Primary                           | Whether the current end the primary end of the remote replication pair.                                                                                          |
| Local Resource ID                    | Primary resource ID.                                                                                                                                             |
| Local Resource Name                  | Primary resource name.                                                                                                                                           |
| Remote Device ID                     | Remote device ID.                                                                                                                                                |
| Remote Device SN                     | SN of the remote device.                                                                                                                                         |
| Remote Device Name                   | Remote device name.                                                                                                                                              |
| Remote Resource ID                   | Secondary resource ID.                                                                                                                                           |
| Remote Resource Name                 | Secondary resource name.                                                                                                                                         |
| Primary Resource Capacity            | Primary resource capacity.                                                                                                                                       |
| Synchronization Type                 | Synchronization type.                                                                                                                                            |
| Recovery Policy                      | Recovery policy.                                                                                                                                                 |
| Replication Mode                     | Remote replication mode.                                                                                                                                         |
| Start Time                           | Synchronization start time.                                                                                                                                      |
| End Time                             | Synchronization end time.                                                                                                                                        |
| Rate                                 | Synchronization rate.                                                                                                                                            |
| Timing Length                        | Timing period (data synchronization period).                                                                                                                     |
| Primary Resource Data Status         | Primary resource data status.                                                                                                                                    |
| Second Resource Data Status          | Secondary resource data status.                                                                                                                                  |
| Is Restore                           | Whether the secondary resource is in the rollback state.                                                                                                         |
| User Type                            | User type.                                                                                                                                                       |
| Compress Enable                      | Whether to enable compression.                                                                                                                                   |
| Compress Valid                       | Whether the compression takes effect.                                                                                                                            |
| Time Difference                      | Time difference between the data synchronization points in time of the primary and secondary resources in a synchronization period of a remote replication pair. |
| Vstore Pair ID                       | vStore pair ID.                                                                                                                                                  |
| Second Resource Access               | Read and write permissions of the host on the secondary resource.                                                                                                |
| Second Resource Capacity             | Capacity of the secondary resource.                                                                                                                              |
| Time Policy                          | Timing policy.                                                                                                                                                   |
| Remote I/O Timeout Period(s)         | Timeout period of remote I/Os.                                                                                                                                   |
| Replication Type                     | Type of remote replication (cloud-based remote replication or common remote replication).                                                                        |
| Bandwidth                            | Data synchronization rate between arrays.                                                                                                                        |
| Synchronize Schedule                 | Schedule for starting the synchronization of a remote replication pair.                                                                                          |
| Progress(%)                          | Synchronization progress.                                                                                                                                        |
| Local vStore ID                      | Local vStore ID.                                                                                                                                                 |
| Local vStore Name                    | Local vStore name.                                                                                                                                               |
| The Latency Of Async To sync(ms)     | Host latency when asynchronous replication switches to synchronous replication.                                                                                  |
| The Bandwidth of Async to Sync(KB/s) | Host latency when synchronous replication switches to asynchronous replication.                                                                                  |
| The Bandwidth of Sync to Async(KB/s) | Host bandwidth when asynchronous replication switches to synchronous replication.                                                                                |
| The Transfer Cycle(minute)           | Host bandwidth when synchronous replication switches to asynchronous replication.                                                                                |
| The Latency of Sync to Async(ms)     | Duration during which the automatic switchover condition is met when asynchronous replication switches to synchronous replication.                               |
| The Automatic Switch to sync         | Whether asynchronous replication automatically switches to synchronous replication.                                                                              |
| The Automatic Switch to Async        | Whether synchronous replication automatically switches to asynchronous replication.                                                                              |
| User Snapshot Sync Policy            | User snapshot synchronization policy.                                                                                                                            |
| User Snapshot Retention Num          | Number of user snapshots retained on the secondary storage system.                                                                                               |
| Copy Snapshot Retention Policy       | Retention policy of copy snapshots on the secondary storage system.                                                                                              |
| Copy Snapshot Retention Num          | Number of copy snapshots retained on the secondary storage system.                                                                                               |
| Resource Subtype                     | Resource sub-type.                                                                                                                                               |
