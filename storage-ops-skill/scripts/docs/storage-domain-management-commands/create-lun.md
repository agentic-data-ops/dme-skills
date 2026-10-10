# create lun


##### Function

The **create lun** command is used to create LUNs. After creating a storage pool, you must divide its storage space into one or multiple LUNs so that resources can be more appropriately allocated to application servers.

##### Format

**create lun** name=? \[ number=? \[ suffix_start_index=? \] \| lun_id=? \| lun_id_list=? \[ suffix_start_index=? \] \] { pool_id=? \| pool_name=? } capacity=? \[ \[ thresholds_switch=? \| thresholds_percent=? \] \| write_policy=? \| prefetch_policy=? \[ prefetch_multiple=? \] \[ prefetch_value=? \] \| owner_controller=? \| io_priority=? \| dif_switch=? \| lun_type=? \[ compression_enabled=? \| dedup_enabled=? \] \| workload_type_id=? \] \[ description=? \]

**create lun** name=? \[ number=? \[ suffix_start_index=? \] \| lun_id_list=? \[ suffix_start_index=? \] \] copy_lun_id=? \[ override_capacity=? \| override_pool_id=? \] \* \[ description=? \]

**create lun** name=? remote_lun_wwn_list=? { storage_pool_id=? \| storage_pool_name=? } \[ write_policy=? \] \[ prefetch_policy=? \] \[ prefetch_multiple=? \] \[ prefetch_value=? \] \[ io_priority=? \] \[ owner_controller=? \] \[ lun_id=? \] \[ dif_switch=? \] \[ description=? \]

**create lun** name=? vvol_type=? \[ number=? \[ suffix_start_index=? \] \] { storage_pool_id=? \| storage_pool_name=? } \[ owner_controller=? \] \[ lun_id=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a LUN that you want to create. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.).<br>When LUNs are created in a batch by assigning the "number=?" parameter, the created LUNs will be auto-named by appending four digits starting from 0000 to each name. For example, if you specify the LUN name as "LUN", the created LUNs will be auto-named "LUN0000", "LUN0001", and so on.<br> NOTE: When LUNs are created in a batch, the length of "name=?" cannot exceed 251 characters. |
| number=? | Number of LUNs that are created in a batch. This parameter cannot be used along with the "lun_id=?" and "lun_id_list=?" parameters. | The value ranges from 2 to 500. The default value is "1". |
| copy_lun_id=? | ID of a source LUN whose attributes that you want to copy. Using this parameter synchronizes the attributes of a source LUN, excluding the LUN ID and capacity, with the newly created LUN. | To obtain the value, run "show lun general". |
| pool_id=? | ID of a storage pool to which a created LUN belongs. | To obtain the value, run "show storage_pool general". |
| pool_name=? | Name of the storage pool to which a LUN belongs. | To obtain the value, run "show storage_pool general". |
| remote_lun_wwn_list=? | WWN of a remote LUN. | To obtain the value, run the "show remote_lun general" command. |
| override_capacity=? | Capacity of a new LUN which will be created using the attributes of a source LUN. | The value is in the format of "capacity+unit", where the unit is case-insensitive and can be KB, MB, GB, or TB.<br>The value ranges from 512 KB to 256 TB.<br> The capacity of a new LUN equals that of a source LUN if this parameter will not be used. |
| override_pool_id=? | ID of the storage pool to which a new LUN belongs. The LUN will be created using the attributes of a source LUN. | To obtain the value, run "show storage_pool general". A new LUN and a source LUN belong to the same storage pool if this parameter will not be used. |
| capacity=? | Capacity of a newly created LUN. | The value is in the format of capacity+unit, where the unit can be KB, MB, GB, TB or Blocks.<br>The value ranges from 512 KB to 256 TB.<br>One block equals 512 bytes.<br>When the unit is GB or TB, a decimal number can be used.<br>"remain" indicates that all the remaining space in a pool is used to create a LUN. |
| lun_type=? | Type of a LUN. | The value can be "thin". When a LUN is being created, the capacity of a LUN is automatically allocated by the system. The capacity cannot exceed the maximum value (specified by the "capacity" parameter). |
| vvol_type=? | VVol type. | The value must be "PE_LUN". "PE_LUN" indicates that the LUN is a PE LUN. |
| storage_pool_id=? | ID of the storage pool to which a LUN belongs. | To obtain the value, run the "show storage_pool general" command. |
| storage_pool_name=? | Name of the storage pool to which a LUN belongs. | To obtain the value, run the "show storage_pool general" command. |
| write_policy=? | Cache write policy. | The value can be "write_through" or "write_back", where: <br>"write_through": indicates write through. The system considers that a data write is successful only after data is written to disks. Disks are accessed in each data write.<br>"write_back": indicates write back. After data is written to the cache of the local controller, the system considers that a data write is successful. In addition, the data will be written to the cache of the peer controller as a mirror. When certain conditions are met, the caches write data to disks.<br> The default value is "write_back". |
| prefetch_policy=? | Cache prefetch policy. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "none", "constant", "variable", or "intelligent", where: <br>"none": non-prefetch.<br>"constant": constant prefetch.<br>"variable": variable prefetch.<br>"intelligent": intelligent prefetch.<br> The default value is "intelligent". |
| prefetch_multiple=? | Cache prefetch multiple. This parameter is required when "prefetch_policy=?" is set to "variable". NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value ranges from 0 to 1024. |
| prefetch_value=? | Cache prefetch value. When the value of "prefetch_policy=?" is "constant", this parameter is mandatory. When the value is "intelligent", this parameter is optional. NOTE: This parameter is not supported by the current version. The execution result is invalid. | When the value of "prefetch_policy=?" is "constant", this parameter ranges from 0 to 1024 and is expressed in KB. When the value is "intelligent", this parameter ranges from 1024 to 8192 and is expressed in KB. |
| io_priority=? | I/O priority of a LUN. | The value can be "Low", "Middle", or "High", where: <br>"Low": indicates the low priority.<br>"Middle": indicates the medium priority.<br>"High": indicates the high priority.<br> The default value is "Low". |
| owner_controller=? | Owning controller of a LUN. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0. |
| lun_id=? | ID of a LUN that you want to create. This parameter cannot be used along with the "number=?" parameter. | The value is an integer ranging from 0 to 65535. The storage system automatically allocates an ID for a newly created LUN if this parameter will not be used. |
| dif_switch=? | Whether or not to enable the DIF function. | The value can be: <br>"yes": Enable the DIF function.<br>"no": Disable the DIF function. |
| thresholds_switch=? | Switch of the function that triggers an alarm when the threshold of a thin LUN is reached. | The value can be "off" or "on", where: <br>"off": disables the alarm function.<br>"on": enables the alarm function.<br> The default value is "off". |
| thresholds_percent=? | Threshold that will trigger an alarm in a thin LUN. | The value ranges from 50 to 99, expressed in %. The default value is 90. |
| compression_enabled=? | Whether to enable the data compression function. | The value can be "yes" or "no", where: <br>"yes": The compression function will be enabled.<br>"no": The compression function will not be enabled.<br> The default value is "yes". |
| dedup_enabled=? | Whether to enable data deduplication. | The value can be "yes" or "no", where: <br>"yes": The deduplication function will be enabled.<br>"no": The deduplication function will not be enabled.<br> The default value is "yes". |
| lun_id_list=? | LUN ID list. This parameter cannot be used along with the "lun_id=?" or "number=?" parameter. | The value is an integer ranging from 0 to 65535. LUN IDs are separated by commas (,) and LUN ID ranges are represented by hyphens (-), such as "0,5-8". |
| suffix_start_index=? | Suffix start index of "name". | The value is an integer between 0 and 9998. |
| workload_type_id=? | ID of the workload type. | The value is an integer ranging from 0 to 2048. |
| description=? | Description. | - |

##### Usage Guidelines

You can create LUNs in either of the following ways:

-   To manually assign the parameters for a LUN to be created.**create lun** name=? \[ number=? \[**suffix_start_index=***?*\] \| lun_id=? \| lun_id_list=? \[**suffix_start_index=***?*\] \] pool_id=? capacity=? \[ lun_type=? \[ thresholds_switch=? \| thresholds_percent=? \] \| write_policy=? \| prefetch_policy=? \| owner_controller=? \| io_priority=? \| dif_switch=? \| compression_enabled=? \| dedup_enabled=? \| workload_type_id=? \] \*.
-   To create a LUN by copying the attributes of a source LUN.

**create lun** name=? \[ number=? \[**suffix_start_index=***?*\] \| lun_id_list=? \[**suffix_start_index=***?*\] \] copy_lun_id=? \[ override_capacity=? \| override_pool_id=? \] \*.

##### Example

Create a LUN and set its parameters as follows:
-   Name: newlun.
-   ID of the storage pool: 0
-   LUN capacity: 100 MB.

```text
admin:/>create lun name=newlun pool_id=0 capacity=100MB
Command executed successfully.
```

Create two LUNs and set their parameters as follows:
-   LUN name prefix: newlun-clone
-   Source LUN ID for copying attributes: 2
-   LUN capacity: 200 MB.

```text
admin:/>create lun name=newlun-clone copy_lun_id=2 override_capacity=200MB number=2
Create LUN newlun-clone0000 successfully.
Create LUN newlun-clone0001 successfully.
```

Create a thin LUN with the compression function and set its parameters as follows:
-   Name: asdf
-   ID of the storage pool: 0
-   LUN capacity: 2 GB
-   LUN type: thin
-   Compression function switch: yes.

```text
admin:/>create lun name=asdf pool_id=0 capacity=2GB lun_type=thin compression_enabled=yes
Command executed successfully.
```

Create a LUN and set its parameters as follows:
-   Name: lun.
-   Usage type: LOCAL_IMAGE_LUN
-   ID of the storage pool: 0
-   LUN capacity: 100 MB
-   Controller: 0A.

```text
developer:/>create lun name=lun usage_type=LOCAL_IMAGE_LUN pool_id=0 capacity=100MB device_controller=0A
Command executed successfully.
```

##### System Response

None
