# show disk_domain available_capacity


##### Function

The **show disk_domain available_capacity** command is used to query the usable capacity of a specific RAID level in a disk domain.

##### Format

**show disk_domain available_capacity** disk_domain_id=? raid_level=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disk_domain_id=? | ID of a disk domain. | To obtain the value, run "show disk_domain general". |
| raid_level=? | RAID level. NOTE: Disks added to a disk domain are divided into fixed-sized logical blocks, and are grouped in accordance with the selected RAID level. By purpose, those logical blocks are categorized as data blocks and parity blocks. | The value can be "RAID5", "RAID6" (default value), or "RAID-TP", where: <br>"RAID5": The RAID5 contains one parity block, and the number of data blocks is automatically adjusted based on reliability and space utilization.<br>"RAID6": The RAID6 contains two parity blocks, and the number of data blocks is automatically adjusted based on reliability and space utilization.<br>"RAID-TP": The RAID-TP contains three parity blocks, and the number of data blocks is automatically adjusted based on reliability and space utilization. |

##### Usage Guidelines

None.

##### Example

Query the usable capacity of "RAID6" in the disk domain whose ID is "0".

```text
admin:/>show disk_domain available_capacity disk_domain_id=0 raid_level=RAID6

ID  Name    Available Capacity
--  ------  ------------------
0   dom_1              6.784TB
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                                   |
|--------------------|-------------------------------------------|
| ID                 | Disk domain ID.                           |
| Name               | Disk domain name.                         |
| Available Capacity | Total usable capacity of the disk domain. |
