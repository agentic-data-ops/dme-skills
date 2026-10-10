# show storage_pool general


##### Function

The **show storage_pool general** command is used to query information about storage pools.

##### Format

**show storage_pool general** { pool_id=? \| pool_name=? }

##### Parameters

| Parameter   | Description             | Value                                                                                                                                                                                                       |
|-------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pool_id=?   | ID of a storage pool.   | To obtain the value, run "**show storage_pool general**" without parameters. |
| pool_name=? | Name of a storage pool. | To obtain the value, run "**show storage_pool general**" without parameters. |

##### Usage Guidelines

-   Run "**show storage_pool general**" to query basic information about all storage pools.
-   Run "**show storage_pool general** pool_id=?" to query detailed information about a specified storage pool.

##### Example

Query basic information about all storage pools.

```text
admin:/>show storage_pool general
ID  Name      Disk Domain ID  Health Status  Running Status  Total Capacity  Free Capacity  Usage Type
--  --------  --------------  -------------  --------------  --------------  -------------  ----------
0   poolTest  0               Normal         Online                 8.000GB        8.000GB  --
```

Query details of the storage pool whose ID is "0".

```text
admin:/>show storage_pool general pool_id=0
ID                                 : 0
Name                               : poolTest
Disk Domain ID                     : 0
Health Status                      : Normal
Running Status                     : Online
Total Capacity                     : 8.000GB
Subscribed Capacity                : 0.000B
Free Capacity                      : 8.000GB
Protection Capacity                : 0.000B
Tier0 Capacity                     : --
Tier1 Capacity                     : --
Tier2 Capacity                     : --
Full Threshold(%)                  : 80
Used Up Threshold(%)               : 90
Raid Level                         : RAID6
LUN Total Capacity                 : 0.000B
LUN Subscribed Capacity            : 0.000B
Deduplication Ratio                : --
Compression Ratio                  : --
Data Reduction Ratio               : --
Thin Provision Saving(%)           : 0.0
Overall Efficiency                 : 1.0:1
Usage Type                         : --
Extent Size                        : --
SmartTier Feature Status           : --
Relocation Status                  : --
Relocation Trigger Mode            : --
Relocation Paused                  : --
Estimated Move-up Data             : --
Estimated Move-down Data           : --
Estimated Data Relocation Duration : --
Full Protect Threshold(%)          : --
File System Total Capacity         : --
Block Size                         : 8KB
Used Capacity Percent(%)           : 0
Description                        :
Provisioning Limit Switch          : on
Provisioning Limit                 : 100
Protection Low Threshold(%)        : 20
Protection High Threshold(%)       : 30
Allocated Protection Capacity      : 0.000B
Automatic Deletion Switch          : off
Used Subscribed Capacity           : 0.000B
Used Capacity                      : 0.000B
LUN Used Subscribed Capacity       : 0.000B
FS Used Subscribed Capacity        : 0.000B
FS Subscribed Capacity             : 0.000B
LUN Mapped Capacity                : 0.000B
FS Shared Capacity                 : 0.000B
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| ID | Storage pool ID. |
| Name | Name of the storage pool. |
| Disk Domain ID | Disk domain ID. |
| Health Status | Health status. |
| Running Status | Running status. |
| Total Capacity | Total capacity of the storage pool. |
| Subscribed Capacity | Total subscribed capacity of the storage pool. |
| Free Capacity | Free capacity of the storage pool. |
| Protection Capacity | Data protection capacity quota. |
| Tier0 Capacity | Capacity of tier 0. |
| Tier1 Capacity | Capacity of tier 1. |
| Tier2 Capacity | Capacity of tier 2. |
| Full Threshold(%) | Capacity alarm threshold. |
| Used Up Threshold(%) | Capacity exhaustion threshold. |
| Raid Level | RAID level. |
| LUN Total Capacity | Total capacity of LUNs that are configured in the storage pool. |
| LUN Subscribed Capacity | Total subscribed capacity of LUNs in the storage pool. |
| Deduplication Ratio | Deduplication ratio. |
| Compression Ratio | Compression ratio. |
| Data Reduction Ratio | Data reduction ratio. |
| Thin Provision Saving(%) | Space saving ratio of thin LUNs. |
| Overall Efficiency | Overall space saving ratio. |
| Usage Type | Storage pool use. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Extent Size | Data relocation granularity. |
| SmartTier Feature Status | SmartTier status. |
| Relocation Status | Data relocation status. |
| Relocation Trigger Mode | Relocation triggering mode. |
| Relocation Paused | Whether SmartTier is suspended. |
| Estimated Move-up Data | Amount of data that can be moved up. |
| Estimated Move-down Data | Amount of data that can be moved down. |
| Estimated Data Relocation Duration | Estimated data migration duration. |
| Full Protect Threshold(%) | Protection capacity alarm threshold. |
| File System Total Capacity | Sum of file system capacities specified during file system creation in the storage pool. |
| Block Size | Block size in the storage pool. |
| Used Capacity Percent(%) | Percentage of the used capacity to the total capacity. |
| Description | Description. |
| Provisioning Limit Switch | Switch of setting the thin LUN provisioning limit. |
| Provisioning Limit | Thin LUN provisioning limit. |
| Protection Low Threshold(%) | Low threshold of the storage pool protection capacity. |
| Protection High Threshold(%) | High threshold of the storage pool protection capacity. |
| Allocated Protection Capacity | Protection capacity of a storage pool after deduplication and compression. |
| Automatic Deletion Switch | Automatic deletion switch of a storage pool. |
| Used Subscribed Capacity | Used subscribed capacity of the storage pool. |
| Used Capacity | Used physical capacity of the storage pool. |
| LUN Used Subscribed Capacity | Total subscribed capacity used by LUNs configured in the storage pool. |
| FS Used Subscribed Capacity | Total subscribed capacity used by file systems in the storage pool. |
| FS Subscribed Capacity | Total subscribed capacity of file systems in the storage pool. |
| LUN Mapped Capacity | Total subscribed capacity of mapped LUNs in the storage pool. |
| FS Shared Capacity | Total subscribed capacity of shared file systems in the storage pool. |
