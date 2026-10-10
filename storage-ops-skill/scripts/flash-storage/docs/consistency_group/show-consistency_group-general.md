# show consistency_group general


##### Function

The **show consistency_group general** command is used to query details of consistency groups.

##### Format

**show consistency_group general** \[ consistency_group_id=? \]

##### Parameters

| Parameter              | Description                | Value                                                                                                                                                                                                                      |
|------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| consistency_group_id=? | ID of a consistency group. | To obtain the value, run "**show consistency_group general**" without parameters. |

##### Usage Guidelines

-   To query details of all the consistency groups, run "**show consistency_group general**".
-   To query details of a specific consistency group, run "**show consistency_group general** consistency_group_id=?".

##### Example

Query basic information about all consistency groups.

```text
admin:/>show consistency_group general

ID                                Name                             Health Status  Running Status  Recovery Policy  Replication Mode  Role     Compress Enable  Compress Valid  Time Difference  DR Star ID  Local Protect Group ID  Remote Protect Group ID
--------------------------------  -------------------------------  -------------  --------------  ---------------  ----------------  -------  ---------------  --------------  ---------------  ----------  ----------------------  -----------------------
21001702030405060000000300000000  cg_rep_Huawei.Storage_PG0001199  Normal         Normal          Automatic        Asynchronous      Primary  No               No                           --  --          0                       0
```

Query details of the consistency group whose ID is "21008038bc1e70e90000000300000000".

```text
admin:/>show consistency_group general consistency_group_id=2100ef02030405060000000300000003
ID                                   : 2100ef02030405060000000300000003
Name                                 : cg2
Health Status                        : Normal
Running Status                       : Normal
Recovery Policy                      : Automatic
Replication Mode                     : Asynchronous
Rate                                 : Middle
Synchronization Type                 : Specified Time
Role                                 : Primary
Timing Length                        : --
Compress Enable                      : No
Compress Valid                       : No
Remote I/O Timeout Period(s)         : --
Time Difference                      : --
Start Time                           : --
End Time                             : --
DR Star ID                           : --
Replication Type                     : --
Local Protect Group ID               : --
Local Protect Group Name             : --
Remote Protect Group ID              : --
Remote Protect Group Name            : --
Bandwidth(MB/s)                      : --
Synchronize Schedule                 : {"HOUR":"09"}
Time Policy                          : Execute at minute 09 every hour
The Latency Of Async To sync(ms)     : 44
The Bandwidth of Sync to Async(KB/s) : 10240
The Bandwidth of Async to Sync(KB/s) : 5120
The Latency of Sync to Async(ms)     : 100
The Transfer Cycle(minute)           : 100
The Automatic Switch to Async        : close
The Automatic Switch to sync         : close
User Snapshot Sync Policy            : Not Sync Snapshot
User Snapshot Retention Num          : --
Copy Snapshot Retention Policy       : No Retention
Copy Snapshot Retention Num          : --
Resource Subtype                     : Common LUN
Description                          :
```

##### System Response

The following table describes the parameter meanings.

| Parameter                            | Meaning                                                                                                                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DR Star ID                           | DR Star trio ID.                                                                                                                                                              |
| ID                                   | Consistency group ID.                                                                                                                                                         |
| Name                                 | Consistency group name.                                                                                                                                                       |
| Health Status                        | Health status.                                                                                                                                                                |
| Running Status                       | Running status.                                                                                                                                                               |
| Recovery Policy                      | Recovery policy.                                                                                                                                                              |
| Replication Mode                     | Synchronization mode.                                                                                                                                                         |
| Rate                                 | Synchronization rate.                                                                                                                                                         |
| Synchronization Type                 | Synchronization type.                                                                                                                                                         |
| Role                                 | Role.                                                                                                                                                                         |
| Timing Length                        | Timing period (data synchronization period).                                                                                                                                  |
| Compress Enable                      | Whether compression is enabled.                                                                                                                                               |
| Compress Valid                       | Whether compression is valid.                                                                                                                                                 |
| Remote I/O Timeout Period(s)         | Remote I/O timeout period.                                                                                                                                                    |
| Time Difference                      | Time difference between the data synchronization points in time of the primary and secondary resources in a synchronization period of a remote replication consistency group. |
| Start Time                           | Start time of the synchronization of a remote replication consistency group.                                                                                                  |
| End Time                             | End time of the synchronization of a remote replication consistency group.                                                                                                    |
| Replication Type                     | Type of the consistency group.                                                                                                                                                |
| Local Protect Group Id               | Local protection group ID.                                                                                                                                                    |
| Local Protect Group Name             | Local protection group name.                                                                                                                                                  |
| Remote Protect Group Id              | Remote protection group ID.                                                                                                                                                   |
| Remote Protect Group Name            | Remote protection group name.                                                                                                                                                 |
| bandwidth                            | Data synchronization rate between arrays.                                                                                                                                     |
| Synchronize Schedule                 | Schedule for starting the synchronization of a consistency group.                                                                                                             |
| Time Policy                          | Timing policy.                                                                                                                                                                |
| The Latency Of Async To sync(ms)     | Host latency when asynchronous replication switches to synchronous replication.                                                                                               |
| The Latency of Sync to Async(ms)     | Host latency when synchronous replication switches to asynchronous replication.                                                                                               |
| The Bandwidth of Async to Sync(KB/s) | Host bandwidth when asynchronous replication switches to synchronous replication.                                                                                             |
| The Bandwidth of Sync to Async(KB/s) | Host bandwidth when synchronous replication switches to asynchronous replication.                                                                                             |
| The Transfer Cycle(minute)           | Duration during which the automatic switchover condition is met when asynchronous replication switches to synchronous replication.                                            |
| The Automatic Switch to sync         | Whether asynchronous replication automatically switches to synchronous replication.                                                                                           |
| The Automatic Switch to Async        | Whether synchronous replication automatically switches to asynchronous replication.                                                                                           |
| User Snapshot Sync Policy            | User snapshot synchronization policy.                                                                                                                                         |
| User Snapshot Retention Num          | Number of user snapshots retained on the secondary storage system.                                                                                                            |
| Copy Snapshot Retention Policy       | Retention policy of snapshot copies on the secondary storage system.                                                                                                          |
| Copy Snapshot Retention Num          | Number of snapshot copies retained on the secondary storage system.                                                                                                           |
| Resource Subtype                     | Resource sub-type.                                                                                                                                                            |
| Description                          | Description.                                                                                                                                                                  |
