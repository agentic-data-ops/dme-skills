# show lun_takeover general


##### Function

The **show lun_takeover general** command is used to query information about takeover LUNs of the storage system.

##### Format

**show lun_takeover general** \[ lun_id=? \] \[ lun_id_list=? \]

##### Parameters

| Parameter   | Description                                                  | Value                                                                                                                                                                                              |
|-------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lun_id=?    | ID of the takeover LUN whose information you want to query.  | To obtain the value, run "**show lun_takeover general**" without parameters. |
| lun_id_list | ID list of takeover LUNs whose information is to be queried. | To obtain the value, run "**show lun_takeover general**" without parameters. |

##### Usage Guidelines

-   Run the "**show lun_takeover general**" command to query information about all takeover LUNs of the storage system.
-   Run the "**show lun_takeover general** lun_id=?" command to query information about the specified takeover LUN of the storage system.

##### Example

Query information about the takeover LUN whose ID is "0".

```text
admin:/>show lun_takeover general lun_id=0
ID : 0
Name : lun200GB1
Pool ID : 0
Capacity : 200.000GB
Subscribed Capacity : 200.000GB
Protection Capacity : 0.000B
Sector Size : 512.000B
Health Status : Normal
Running Status : Online
Type : Thick
IO Priority : Low
WWN : 60022a11000f85170003e36b00000000
Exposed To Initiator : Yes
Data Distributing : --
Write Policy : Write Back
Running Write Policy : Write Back
Prefetch Policy : --
Read Cache Policy : --
Write Cache Policy : --
Cache Partition ID : --
Prefetch Value : --
Owner Controller : --
Work Controller : --
Snapshot ID(s) : --
LUN Copy ID(s) : --
Remote Replication ID(s) : --
Split Clone ID(s) : --
Relocation Policy : --
Initial Distribute Policy : --
SmartQoS Policy ID : --
Protection Duration(days) : --
Has Protected For(h) : --
Estimated Data To Move To Tier0 : --
Estimated Data To Move To Tier1 : --
Estimated Data To Move To Tier2 : --
Is Add To Lun Group : Yes
DIF Switch : No
Remote LUN WWN : --
Disk Location : Internal
LUN Migration : --
Progress(%) : --
Smart Cache Cached Size : --
Smart Cache Hit Rage(%) : --
Mirror Type : --
Thresholds Percent(%) : 0
Thresholds Switch : 0ff
Takeover LUN Type : Basic
HyperMetro ID(s) : --
Takeover LUN WWN : 60032a11000f85170003e36b0000001a
```

Query information about all takeover LUNs of the storage system.

```text
admin:/>show lun_takeover general

ID  Name            Pool ID  Capacity  Health Status  Running Status  Type   WWN                               Is Add To Lun Group  DIF Switch  Takeover LUN Type  Takeover LUN WWN
--  --------------  -------  --------  -------------  --------------  -----  --------------------------------  -------------------  ----------  -----------------  --------------------------------
0   eDevLUN001_002  0        30.000GB  Normal         Online          Thick  680d4a51008ea53a00a60d1800000000  No                   No          THIRD-PARTY        6006016028f03600e4b6a94e6295e811
1   eDevLUN002_001  0         5.000GB  Normal         Online          Thick  680d4a51008ea53a00a78edb00000001  No                   No          BASIC              6e0979610056725a0158678a00000008
2   eDevLUN002_002  0         5.000GB  Normal         Online          Thick  680d4a51008ea53a00a78f3900000002  No                   No          BASIC              6e0979610056725a0158672c00000007
3   eDevLUN004_001  0        21.000GB  Normal         Online          Thick  680d4a51008ea53a00a7971700000003  No                   No          THIRD-PARTY        50002ac10ec71c9f0000000000000000
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| ID | LUN ID. |
| Name | LUN name. |
| Pool ID | Storage pool ID. |
| Capacity | Total capacity. |
| Subscribed Capacity | Actual used capacity. |
| Protection Capacity | Data protection capacity quota. |
| Sector Size | Sector size. |
| Health Status | Health status. |
| Running Status | Running status. |
| Type | LUN type. |
| IO Priority | I/O priority. |
| WWN | World Wide Name. |
| Exposed To Initiator | Whether to be mapped to an initiator. |
| Data Distributing | Percentage of data in different storage tiers. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Write Policy | Cache write policy. |
| Running Write Policy | Current cache write policy. |
| Supported Multipathing | Type of multipathing software supported by masquerading LUNs. |
| Prefetch Policy | Cache prefetch policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Read Cache Policy | Cache read policy of a LUN. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Write Cache Policy | Cache write policy of a LUN. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Cache Partition ID | ID of the cache partition. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Prefetch Value | Cache prefetch value. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Owner Controller | Owning controller of a LUN. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Work Controller | Working controller of a LUN. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Snapshot ID(s) | Snapshot IDs. |
| LUN Copy ID(s) | IDs of LUN copy tasks. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Remote Replication ID(s) | IDs of remote replication tasks. |
| Split Clone ID(s) | IDs of LUN clone tasks. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Relocation Policy | SmartTier policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Initial Distribute Policy | Initial capacity allocation policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| SmartQoS Policy ID | ID of the SmartQoS policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Protection Duration(days) | Protection duration. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Has Protected For(h) | Protection execution duration. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Estimated Data To Move To Tier0 | Amount of data that can be migrated to storage tier 0. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Estimated Data To Move To Tier1 | Amount of data that can be migrated to storage tier 1. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Estimated Data To Move To Tier2 | Amount of data that can be migrated to storage tier 2. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Is Add To Lun Group | Whether a LUN is added to a LUN group. |
| DIF Switch | Whether the DIF function is enabled. |
| Remote LUN WWN | WWN of an external LUN. |
| Disk Location | Whether the LUN is an internal one or an external one. |
| LUN Migration | Whether the LUN serves as the source LUN or the target LUN in LUN migration. |
| Progress(%) | Progress of data destruction. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Smart Cache Cached Size | SmartCache cached size. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Smart Cache Hit Rage(%) | SmartCache hit ratio. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Mirror Type | Mirror type. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Thresholds Percent(%) | Threshold for triggering an alarm in a thin LUN (If the LUN is not a thin LUN, "--" is displayed). |
| Thresholds Switch | Switch of the alarm function when the threshold of a thin LUN is reached (If the LUN is not a thin LUN, "--" is displayed). |
| Takeover LUN Type | Type of the takeover LUNs. |
| HyperMetro ID(s) | IDs of HyperMetro tasks. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Takeover LUN WWN | WWN of the takeover LUNs. |
