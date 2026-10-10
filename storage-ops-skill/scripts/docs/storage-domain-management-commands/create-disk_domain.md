# create disk_domain


##### Function

The **create disk_domain** command is used to create a disk domain.

##### Format

**create disk_domain** name=? disk_list=? \[ disk_domain_id=? \| hotspare_strategy=? \| controller_enclosure_list=? \| controller_list=? \| disk_encryption_switch=? \| max_raid_member_number=? \| redundancy_strategy=? \| raid_level=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Disk domain name. | The value contains 1 to 255 digits, letters, underscores (_), hyphens (-), and periods (.). |
| disk_domain_id=? | Disk domain ID. | The value ranges from 0 to 63.<br>When this parameter is not specified, the system automatically allocates an ID for a new disk domain. |
| disk_list=? | Disk ID list. | The value can be "all", a disk ID range, or a disk ID list, where: <br>"all": All free disks in the normal state in the specified controller enclosure are added to a disk domain. If no controller enclosure parameter is specified, all free disks in the normal state in controller enclosure 0 are added to the disk domain by default.<br>Disk ID range: The value is in the format of start disk ID-end disk ID, for example, DAE000.1-5.<br>Disk ID list: Multiple disk IDs are separated by commas (,), for example, "DAE000.1,DAE000.2,DAE000.3".<br> You can run the "show disk general" command to obtain the current system disk list. |
| hotspare_strategy=? | Hot spare strategy for the disk domain. | The value can be "low", "high", "none", or 0 to 8, where: <br>"low": The hot spare level is low with 1 hot spare disk.<br>"high": The hot spare level is high with 2 hot spare disks.<br>"none": The hot spare level is none with no hot spare disk.<br>0 to 8: You can specify a hot spare disk quantity from 0 to 8. |
| controller_enclosure_list=? | Controller enclosure ID list. | The value is in the CTEX format, where X is an integer starting from 0, for example, CTE0 or CTE1. |
| disk_encryption_switch=? | Disk encryption switch. | The value can be "off" or "on", where: <br>"off": enables the encryption switch.<br>"on": disables the encryption switch. |
| controller_list=? | Controller ID list. | Controller IDs are separated by commas (,). The value format is XA, XB, XC, or XD, where X is an integer starting from 0, for example, 0A,0B, 0C,0D, or 0A,0B,0C,0D. |
| redundancy_strategy | Redundancy policy for the disk domain. | The value can be "disk" or "enclosure", where: <br>"disk": disk-level redundancy policy.<br>"enclosure": enclosure-level redundancy policy. |
| raid_level | RAID level. NOTE: Disks added to a disk domain are divided into fixed-sized logical blocks, and are grouped in accordance with the selected RAID level. By purpose, those logical blocks are categorized as data blocks and parity blocks. | The value can be "RAID5", "RAID6", "RAID-TP", or "RAID10", where: <br>"RAID5": contains one parity block.<br>"RAID6": contains two parity blocks.<br>"RAID-TP": contains three parity blocks.<br>"RAID10": The number of logical blocks is automatically specified by the system.<br> The default value for disk-level redundancy is "RAID6", and that for enclosure-level redundancy is "RAID-TP". |
| max_raid_member_number=? | Maximum number of RAID member disks. This parameter is supported in OceanStor Dorado 3000 V6 storage systems. | The value can be "15" or "25". NOTE: In admin mode, this parameter can be set only when raid_level is set to raid5. |
| max_raid_member_number=? | Maximum number of RAID member disks. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value can be "12" or "25". NOTE: In admin mode, this parameter can be set only when raid_level is set to raid5. |

##### Usage Guidelines

None

##### Example

Create disk domain "test" with the hot spare strategy set to "none".

```text
admin:/>create disk_domain name=test disk_list=all hotspare_strategy=none
DANGER: You are about to create the hot spare strategy of a disk domain to None. After this operation, faulty or failing disks may fail to be handled, ongoing reconstruction and pre-copy tasks will fail, or even services may get interrupted.
Suggestion: Set the hot spare strategy to High or Low or ensure that there is sufficient free capacity.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a disk domain named "test". Set the disk ID to "DAE000.0-7", owning controller enclosure to "CTE0", and owning controller ID to "0A,0B".

```text
admin:/>create disk_domain name=test disk_list=DAE000.0-7 controller_enclosure_list=CTE0 controller_list=0A,0B
Command executed successfully.
```

Create a disk domain named "test". Set the disk ID to "all", owning controller enclosure to "CTE0", and owning controller ID to "0A,0B,0C,0D".

```text
admin:/>create disk_domain name=test disk_list=all controller_enclosure_list=CTE0 controller_list=0A,0B,0C,0D
Command executed successfully.
```

Create a disk domain named "test", and set the disk ID to "all", RAID level to "RAID5", and maximum number of RAID columns to 25.

```text
admin:/>create disk_domain name=test disk_list=all raid_level=RAID5 max_raid_member_number=25
Command executed successfully.
```

##### System Response

None
