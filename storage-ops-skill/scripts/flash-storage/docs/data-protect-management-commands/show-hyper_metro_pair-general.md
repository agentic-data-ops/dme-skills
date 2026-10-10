# show hyper_metro_pair general


##### Function

The **show hyper_metro_pair general** command is used to query HyperMetro pairs.

##### Format

**show hyper_metro_pair general** pair_id=?

##### Parameters

| Parameter | Description                | Value                                                                                                                                                                                                            |
|-----------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pair_id=? | ID of the HyperMetro pair. | To obtain the value, run the "**show hyper_metro_pair general**" command. |

##### Usage Guidelines

None

##### Example

Query all HyperMetro pairs in the device.

```text
admin:/>show hyper_metro_pair general
ID Health Status Running Status Domain Name Type Size Role Local Name Remote Name Owning vStore
---------------- ------------- -------------- ------ ----- ------------ ------------------ - -------------------- --------
200bc79b99520000 Normal Normal HCD001 LUN 100.000GB Preferred LUN001 extLun001 v1
200bc79b99520002 Normal Normal HCD002 FS 10.000GB Non-preferred FS001 extFS001 v1
```

Query details of the HyperMetro pair whose ID is "200bc79b99520000".

```text
admin:/>show hyper_metro_pair general pair_id=200bc79b99520000
ID : 200bc79b99520000
Health Status : Normal
Running Status : Normal
Link Status : Linkup
Domain ID : 1
Domain Name : HCD001
Type : LUN
Size : 100.000GB
WWN : 200bc78945612300
IP(s) : --
Role : Preferred
Local ID : 5
Local Name : LUN005
Local Data Status : Consistent
Local Access Status : Read And Write
Remote ID : 5
Remote Name : extLUN005
Remote Data Status : Consistent
Remote Access Status : Read And Write
Recovery Policy : Automatic
Sync Progress(%) : --
Sync Direction : --
Sync Rate : Middle
Start Time : 2013-12-22/17:18:32 UTC+08:00
End Time : 2013-12-22/17:18:32 UTC+08:00
Consistency Group ID : 1
Consistency Group Name : cg001
Isolation Switch        : Close
Isolation Threshold(ms) : 1000
Lock Mode  : Optimistic Mode
Time Remaining for Synchronization : --
Write Secondary Timeout(s)         : --
Bandwidth(MB/s)  : --
DR Star ID       : --
Config Status : Normal
Vstore Pair ID : 200bc79b99520001
Owning vStore : v1
```

##### System Response

The following table describes the parameter meanings.

| Parameter                          | Meaning                                                                                                                                             |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                                 | UUID of the HyperMetro pair, 64 bits.                                                                                                               |
| Health Status                      | Health status, which can be normal or faulty.                                                                                                       |
| Running Status                     | Running status: Normal, Synchronizing, To be synchronized, Paused, Forcibly started, Deleting, and Invalid.                                         |
| Link Status                        | Link status. The value can be "Linkup" or "Linkdown".                                                                                               |
| Domain ID                          | ID of the HyperMetro domain.                                                                                                                        |
| Domain Name                        | Name of the HyperMetro domain.                                                                                                                      |
| Type                               | Resource type. The value can be "LUN" or "FS".                                                                                                      |
| Size                               | Resource size.                                                                                                                                      |
| WWN                                | LUN WWN.                                                                                                                                            |
| IP(s)                              | IP address of the file system shared service.                                                                                                       |
| Role                               | Whether the site is the primary/secondary or preferred/non-preferred site. A/P indicates active/passive, and A/A indicates arbitration is required. |
| Local ID                           | ID of the local resource.                                                                                                                           |
| Local Name                         | Name of the local resource.                                                                                                                         |
| Local Data Status                  | Local data status. The value can be "Consistent" or "Inconsistent".                                                                                 |
| Local Access Status                | Local host access status. The value can be "No Access" or "Read and Write".                                                                         |
| Remote ID                          | ID of the remote resource.                                                                                                                          |
| Remote Name                        | Name of the remote resource.                                                                                                                        |
| Remote Data Status                 | Remote data status. The value can be "Consistent" or "Inconsistent".                                                                                |
| Remote Access Status               | Remote host access status. The value can be "No Access", "Read Only", or "Read and Write".                                                          |
| Recovery Policy                    | Recovery policy. The value can be "Automatic" or "Manual".                                                                                          |
| Sync Progress(%)                   | Synchronization progress (%). The value ranges from 0 to 100 (valid for LUNs only).                                                                 |
| Sync Direction                     | Synchronization direction. The value can be "Local to Remote" or "Remote to Local".                                                                 |
| Sync Rate                          | Synchronization rate. The value can be "Highest", "High", "Middle", or "Low".                                                                       |
| Start Time                         | Start time of the last synchronization.                                                                                                             |
| End Time                           | End time of the last synchronization.                                                                                                               |
| Consistency Group ID               | Owning consistency group ID.                                                                                                                        |
| Consistency Group Name             | Owning consistency group name.                                                                                                                      |
| Isolation Switch                   | Isolation switch.                                                                                                                                   |
| Isolation Threshold(ms)            | Isolation threshold.                                                                                                                                |
| Lock Mode                          | Lock mode used by the HyperMetro pair. The value can be "Optimistic Mode" or "Pessimistic Mode".                                                    |
| Time Remaining for Synchronization | Time remaining for synchronization.                                                                                                                 |
| Write Secondary Timeout(s)         | Timeout period of I/Os writing the remote storage system (unit: second).                                                                            |
| Bandwidth                          | Bandwidth.                                                                                                                                          |
| DR Star ID                         | DR Star trio ID.                                                                                                                                    |
| Keep Consistent Data               | Whether the consistency data is retained.                                                                                                           |
| Rollback State                     | Rollback status.                                                                                                                                    |
| Rollback Progress                  | Rollback progress.                                                                                                                                  |
| Config Status                      | Configuration synchronization status.                                                                                                               |
| Vstore Pair ID                     | vStore pair ID.                                                                                                                                     |
| Owning vStore                      | Name of the owning vStore.                                                                                                                          |
