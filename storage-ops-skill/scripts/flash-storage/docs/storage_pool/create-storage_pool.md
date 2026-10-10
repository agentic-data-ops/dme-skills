# create storage_pool


##### Function

The **create storage_pool** command is used to create a storage pool.

##### Format

**create storage_pool** name=? disk_list=? \[ raid_level=? \| full_threshold=? \| used_up_threshold=? \| pool_id=? \| usage_type=? \| block_size=? \| description=? \| provisioning_limit_switch=? \[ provisioning_limit=? \] \| protection_low_threshold=? \| protection_high_threshold=? \| automatic_deletion_switch=? \| controller_enclosure_list=? \| hotspare_strategy=? \| disk_encryption_switch=? \| max_raid_member_number=? \| redundancy_strategy=? \] \*

**create storage_pool** name=? capacity=? \[ raid_level=? \| full_threshold=? \| used_up_threshold=? \| disk_domain_id=? \| pool_id=? \| usage_type=? \| block_size=? \| description=? \| provisioning_limit_switch=? \[ provisioning_limit=? \] \| protection_low_threshold=? \| protection_high_threshold=? \| automatic_deletion_switch=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a storage pool. | The value contains 1 to 255 characters including digits, letters, underscores (_), hyphens (-), and periods (.). |
| capacity=? | Capacity of a storage pool. | The value is an integer, expressed in GB or TB. The value ranges from 1 GB to 12864 TB. The value "remain" indicates that all the remaining space in a disk domain is used to create a storage pool. The default value is "remain". |
| disk_list=? | Disk ID list. | The value can be "all", a disk ID range, or a disk ID list, where: <br>"all": All free disks in the normal state in the specified controller enclosure are added to a disk domain. If no controller enclosure parameter is specified, all free disks in the normal state in controller enclosure 0 are added to the disk domain by default.<br>Disk ID range: The value is in the format of start disk ID-end disk ID, for example, DAE000.1-5.<br>Disk ID list: Multiple disk IDs are separated by commas (,), for example, DAE000.1,DAE000.2,DAE000.3.<br> You can run the "show disk general" command to obtain the current system disk list. |
| controller_enclosure_list=? | Controller enclosure ID list. | The value is in the CTEX format, where X is an integer starting from 0, for example, CTE0 or CTE1. |
| disk_domain_id=? | ID of a disk domain where a storage pool resides. | To obtain the value, run "show disk_domain general". |
| raid_level=? | RAID level. NOTE: Disks added to a disk domain are divided into fixed-sized logical blocks, and are grouped in accordance with the selected RAID level. By purpose, those logical blocks are categorized as data blocks and parity blocks. | The value can be "RAID5", "RAID6", "RAID-TP", or "RAID10", where: <br>"RAID5": contains one parity block.<br>"RAID6": contains two parity blocks.<br>"RAID-TP": contains three parity blocks.<br>"RAID10": The number of logical blocks is automatically specified by the system.<br> The default value for disk-level redundancy is "RAID6", and that for enclosure-level redundancy is "RAID-TP". |
| full_threshold=? | Capacity alarm threshold. | The value ranges from 1 to 95, expressed in percentage (%). The default value is "80". |
| used_up_threshold=? | Capacity exhaustion threshold. | The value ranges from (full_threshold+1) to 99, expressed in percentage. The default value is "90". |
| pool_id=? | ID of a storage pool. | The value ranges from 0 to 63. If this parameter is not specified, the storage system automatically allocates an ID to a newly created storage pool. |
| usage_type=? | Storage pool usage. NOTE: This parameter is not supported by the current version. The execution result is invalid. | - |
| block_size=? | Block size in the storage pool. NOTE: If deduplication or compression is enabled, the value is the size of the deduplication or compression block. | The value can be "4KB" or "8KB". The default value is "8KB". The value cannot be changed after being configured. |
| description=? | Description. | - |
| provisioning_limit_switch=? | Switch of setting the thin LUN provisioning limit. | The value can be "off" (default value) or "on", where: <br>"off": turns off the switch.<br>"on": turns on the switch. |
| provisioning_limit=? | Thin LUN provisioning limit. | The value ranges from 0 to 65535. |
| protection_low_threshold=? | Low threshold of the storage pool protection capacity. | The value ranges from 1 to 95, expressed in percentage (%). The default value is 20. |
| protection_high_threshold=? | High threshold of the storage pool protection capacity. | The value ranges from (protection_low_threshold+1) to 99, expressed in percentage (%). The default value is 30. |
| automatic_deletion_switch=? | Automatic deletion switch of a storage pool. | The value can be: <br>"off": disables the function of automatically reclaiming the protected space (scheduled HyperCDP object and scheduled HyperCDP consistency group) in the storage pool.<br>"on": enables the function of automatically reclaiming the protected space (scheduled HyperCDP object and scheduled HyperCDP consistency group) in the storage pool. |
| disk_encryption_switch=? | Whether to enable disk encryption. | The value can be "off" or "on", where: <br>"off": disables disk encryption.<br>"on": enables disk encryption. |
| hotspare_strategy=? | Hot spare strategy. | The value can be "low", "high", "none", or 0 to 8, where: <br>"low": The hot spare level is low with 1 hot spare disk.<br>"high": The hot spare level is high with 2 hot spare disks.<br>"none": The hot spare level is none with no hot spare disk.<br>0 to 8: You can specify a hot spare disk quantity from 0 to 8. |
| max_raid_member_number=? | Maximum number of RAID member disks. This parameter is supported in OceanStor Dorado 3000 V6 storage systems. | The value can be "15" or "25". NOTE: In admin mode, this parameter can be set only when raid_level is set to RAID5. |
| max_raid_member_number=? | Maximum number of RAID member disks. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value can be "12" or "25". NOTE: In admin mode, this parameter can be set only when raid_level is set to RAID5. |
| redundancy_strategy | Redundancy policy for the storage pool. | The value can be "disk" or "enclosure", where: <br>"disk": disk-level redundancy policy.<br>"enclosure": enclosure-level redundancy policy. |

##### Usage Guidelines

-   The storage system provides storage space for application servers in storage pool mode. A storage pool combines multiple independent disks based on different RAID policies to provide larger storage space and improve disk read performance and data security.
-   You are advised to create a storage pool by specifying the controller enclosure and disk list.

##### Example

Create storage pool "poolTest" with all disks of controller enclosure "CTE0" and keep the default values of the other parameters.

```text
admin:/>create storage_pool name=poolTest disk_list=all controller_enclosure_list=CTE0
Command executed successfully.
```

Create storage pool "poolTest" in which the hot spare strategy is set to "none".

```text
admin:/>create storage_pool name=poolTest disk_list=all hotspare_strategy=none
DANGER: You are about to create the hot spare strategy of a storage pool to None. After this operation, faulty or failing disks may fail to be handled, ongoing reconstruction and pre-copy tasks will fail, or even services may get interrupted.
Suggestion: Set the hot spare strategy to High or Low or ensure that there is sufficient free capacity.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Creating storage pool (poolTest) in background.
Run the "show task general task_id=0" command to query the execution result.
```

Create a storage pool named "poolTest". Set the RAID level of the storage pool to "RAID5" and the maximum number of RAID member disks to 25.

```text
admin:/>create storage_pool name=poolTest disk_list=all raid_level=RAID5 max_raid_member_number=25
Create Storage Pool (poolTest) in background.
Run the "show task general task_id=2" command to query the execution result.
```

##### System Response

None
