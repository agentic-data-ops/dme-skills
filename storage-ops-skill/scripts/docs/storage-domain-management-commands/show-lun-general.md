# show lun general


##### Function

The **show lun general** command is used to query information about LUNs in the storage system.

##### Format

**show lun general** \[ lun_id=? \| mapping_view_id=? \| pool_id=? \| lun_name=? \| usage_type=? \| lun_id_list=? \| lun_name_list=? \| mapping_view_name=? \| pool_name=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_id=? | ID of the LUN whose information you want to query. | To obtain the value, run "show lun general" without parameters. |
| lun_name=? | Name of the LUN whose information you want to query. | To obtain the value, run "show lun general" without parameters. |
| pool_id=? | ID of a storage pool. Specifying this parameter queries information about LUNs in the specified storage pool. | To obtain the value, run "show storage_pool general". |
| mapping_view_id=? | ID of a mapping view. Specifying this parameter queries information about LUNs in the specified mapping view. | To obtain the value, run "show mapping_view general". |
| usage_type=? | LUN usage type. Specifying this parameter queries information about LUNs with the specified usage type. | The value can be "Internal", "External", "VVOL_LUN", "PE_LUN", "GLOBAL_REPO_LUN", "LOCAL_IMAGE_LUN", or "CONTAINER_CONF_LUN", where: <br>"Internal": The usage type of the LUNs is "Internal".<br>"External": The usage type of the LUNs is "External".<br>"VVOL_LUN": The usage type of the LUNs is "VVOL_LUN".<br>"PE_LUN": The usage type of the LUNs is "PE_LUN".<br>"GLOBAL_REPO_LUN": global image repository LUN.<br>"LOCAL_IMAGE_LUN": local image repository LUN.<br>"CONTAINER_CONF_LUN": container configuration LUN. |
| lun_id_list | List of LUN IDs. | Multiple IDs are separated by commas (,), or an ID range is represented using a hyphen(-). |
| lun_name_list | List of LUN names. | LUN names are separated by commas (,) or name range is represented using a hyphen(-). The length of the LUN name between a hyphen (-) must be the same as that after a hyphen, and no hyphen (-) is allowed in a LUN name. |
| pool_name=? | Name of a storage pool. Using this parameter queries information about LUNs in a specified storage pool. | - |
| mapping_view_name=? | Name of a mapping view. Using this parameter queries information about LUNs in a specified mapping view. | - |

##### Usage Guidelines

-   Run the "**show lun general**" command to query information about all LUNs in the system.
-   Run the "**show lun general** lun_id=?" command to query information about the specified LUN based on the LUN ID.
-   Run the "**show lun general** lun_name=?" command to query information about the specified LUN based on the LUN name.
-   Run the "**show lun general** pool_id=?" command to query information about all LUNs in the specified storage pool.
-   Run the "**show lun general** mapping_view_id=?" command to query information about all LUNs in the specified mapping view.
-   Run the "**show lun general** usage_type=?" command to query LUNs of the specified usage type.
-   Run the "**show lun general** {order_by=? \| maximum=? \| sort=? }" command to query deduplication and compression information about LUNs. You can specify whether the results are sorted in ascending or descending order.
-   Run the "**show lun general** mapping_view_name=?" command to query information about all LUNs in the specified mapping view.
-   Run the "**show lun general** pool_name=?" command to query information about all LUNs in the specified storage pool.

##### Example

Query information about all LUNs in the storage system.

```text
admin:/>show lun general

ID  Name                       Pool ID  Capacity  Health Status  Running Status  Type  WWN                               Is Add To Lun Group  Smart Cache Partition ID  DIF Switch  Is Clone  Subscribed Capacity  Function Type
--  -------------------------  -------  --------  -------------  --------------  ----  --------------------------------  -------------------  ------------------------  ----------  --------  -------------------  -------------
0   lun0000                    3         1.000GB  Normal         Online          Thin  688cf98100dac53000ae65c200000000  No                   --                        No          No                     0.000B  Lun
1   lun0001                    3         1.000GB  Normal         Online          Thin  688cf98100dac53000ae65f900000001  No                   --                        No          No                     0.000B  Lun
2   lun0002                    3         1.000GB  Normal         Online          Thin  688cf98100dac53000ae662c00000002  No                   --                        No          No                     0.000B  Lun
3   lun0003                    3         1.000GB  Normal         Online          Thin  688cf98100dac53000ae666300000003  No                   --                        No          No                     0.000B  Lun
4   lun0004                    3         1.000GB  Normal         Online          Thin  688cf98100dac53000ae669600000004  No                   --                        No          No                     0.000B  Lun
```

Query information about the LUN whose name is "LUN001_001".

```text
admin:/>show lun general lun_name=LUN001_001

ID                              : 0
Name                            : LUN001_001
Pool ID                         : 3
Capacity                        : 1.000GB
Subscribed Capacity             : 0.000B
Protection Capacity             : 0.000B
Sector Size                     : 512.000B
Health Status                   : Normal
Running Status                  : Online
Type                            : Thin
IO Priority                     : Low
WWN                             : 688cf98100dac53000ae65c200000000
Exposed To Initiator            : No
Data Distributing               : --
Write Policy                    : Write Back
Running Write Policy            : Write Back
Prefetch Policy                 : None
Read Cache Policy               : --
Write Cache Policy              : --
Cache Partition ID              : --
Prefetch Value                  : --
Owner Controller                : --
Work Controller                 : --
Snapshot ID(s)                  : 16
LUN Copy ID(s)                  : --
Remote Replication ID(s)        : --
Split Clone ID(s)               : --
Relocation Policy               : --
Initial Distribute Policy       : --
SmartQoS Policy ID              : --
Protection Duration(days)       : --
Has Protected For(h)            : --
Estimated Data To Move To Tier0 : --
Estimated Data To Move To Tier1 : --
Estimated Data To Move To Tier2 : --
Is Add To Lun Group             : No
Smart Cache Partition ID        : --
DIF Switch                      : No
Remote LUN WWN                  : --
Disk Location                   : Internal
LUN Migration                   : --
Progress(%)                     : --
Smart Cache Cached Size         : --
Smart Cache Hit Rage(%)         : --
Mirror Type                     : --
Thresholds Percent(%)           : 90
Thresholds Switch               : Off
Usage Type                      : Internal
HyperMetro ID(s)                : --
Dedup Enabled                   : --
Compression Enabled             : --
Workload Type Name              : --
Is Clone                        : No
LUN Clone ID(s)                 : 5
Snapshot Schedule ID            : --
Description                     :
HyperCopy ID(s)                 : 5
HyperCDP Schedule ID            : --
LUN consistency group ID        : 1
Clone ID(s)                     : 5
LUN protection group ID(s)      : 1
Function Type                   : Lun
NGUID                           : 7100dac53000ae6588cf98c200000000
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| ID | LUN ID. |
| Name | LUN name. |
| Pool ID | Storage pool ID. |
| Capacity | Total capacity. |
| Subscribed Capacity | Actual used capacity quota. |
| Protection Capacity | Data protection capacity quota. |
| Sector Size | Sector size. |
| Health Status | Health status. |
| Running Status | Running status. |
| Type | LUN type. |
| IO Priority | I/O priority of the LUN. |
| WWN | World wide name (WWN). |
| Exposed To Initiator | Whether the LUN is mapped to an initiator. |
| Data Distributing | Percentage of data in different storage tiers. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Write Policy | Cache write policy. |
| Running Write Policy | Current cache write policy. |
| Prefetch Policy | Cache prefetch policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Read Cache Policy | Cache read policy of the LUN. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Write Cache Policy | Cache write policy of the LUN. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Cache Partition ID | ID of the cache partition. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Prefetch Value | Cache prefetch value. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Owner Controller | Owning controller of the LUN. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Work Controller | Working controller of the LUN. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Snapshot ID(s) | Snapshot ID list. |
| LUN Copy ID(s) | List of LUN copy task IDs. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Remote Replication ID(s) | List of remote replication task IDs. |
| Split Clone ID(s) | IDs of LUN clone tasks. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Relocation Policy | SmartTier policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Initial Distribute Policy | Initial capacity allocation policy. NOTE: This field is not supported by the current version. The returned value is invalid. |
| SmartQoS Policy ID | SmartQoS policy ID. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Protection Duration(days) | Protection duration. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Has Protected For(h) | Period during which data has been protected. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Is Add To Lun Group | Whether to add the LUN to a LUN group. |
| Smart Cache Partition ID | ID of the current SmartCache partition. |
| DIF Switch | Whether the DIF function is enabled. |
| Remote LUN WWN | WWN of the remote LUN. |
| Estimated Data To Move To Tier0 | Amount of data that can be migrated to storage tier 0. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Estimated Data To Move To Tier1 | Amount of data that can be migrated to storage tier 1. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Estimated Data To Move To Tier2 | Amount of data that can be migrated to storage tier 2. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Disk Location | Whether the LUN is an internal one or external one. |
| LUN Migration | Whether the LUN serves as the source LUN or target LUN in LUN migration. |
| Progress(%) | Progress of data destruction. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Smart Cache Cached Size | Cached size of the current SmartCache partition. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Smart Cache Hit Rage(%) | Hit ratio of the current SmartCache partition. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Mirror Type | Image type. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Thresholds Percent(%) | Threshold for triggering an alarm in a thin LUN. If the LUN is not a thin LUN, "--" is displayed. |
| Compression Enabled | Whether compression is enabled. |
| Thresholds Switch | Switch of the alarm function when the threshold of a thin LUN is reached. If the LUN is not a thin LUN, "--" is displayed. |
| Usage Type | LUN usage type. |
| HyperMetro ID(s) | List of HyperMetro task IDs. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Dedup Enabled | Whether deduplication is enabled or disabled. |
| Workload Type Name | Application type name. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Is Clone | Clone flag. |
| LUN Clone ID(s) | ID list of LUN clones. |
| Snapshot Schedule ID | Snapshot schedule ID. |
| Description | Description. |
| HyperCopy ID(s) | ID list of HyperCopy tasks. |
| HyperCDP Schedule ID | HyperCDP schedule ID. |
| LUN consistency group ID | LUN consistency group ID. |
| Clone ID(s) | List of clone IDs. |
| LUN protection group ID(s) | List of LUN-based protection group IDs. |
| Function Type | Function type. |
| NGUID | Globally unique identifier of a namespace. |
