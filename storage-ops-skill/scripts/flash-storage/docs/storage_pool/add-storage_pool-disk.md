# add storage_pool disk


##### Function

The **add storage_pool disk** command is used to add disks to a storage pool.

##### Format

**add storage_pool disk** { pool_id=? \| pool_name=? } disk_list=? \[ controller_enclosure_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pool_id=? | ID of a storage pool to which you want to add disks. | To obtain the value, run "show storage_pool general". |
| pool_name=? | Name of a storage pool to which you want to add disks. | To obtain the value, run the "show storage_pool general" command. |
| disk_list=? | ID list of disks that you want to add to a storage pool. | The value can be "all", a disk ID range, or a disk ID list, where: <br>"all": All free disks in the normal state in the specified controller enclosure are added to a disk domain. If no controller enclosure parameter is specified, all free disks in the normal state in controller enclosure 0 are added to the disk domain by default.<br>Disk ID range: The value is in the format of start disk ID-end disk ID, for example, DAE000.1-5.<br>Disk ID list: Multiple disk IDs are separated by commas (,), for example, DAE000.1,DAE000.2,DAE000.3.<br> You can run the "show disk general" command to obtain the current system disk list. |
| controller_enclosure_list=? | Controller enclosure ID list. | The value is in the CTEX format, where X is an integer starting from 0, for example, CTE0 or CTE1. |

##### Usage Guidelines

None

##### Example

Add disks to storage pool "0".

```text
admin:/>add storage_pool disk pool_id=0 disk_list=all
WARNING: You are about to expand storage pool.
Suggestion: Before performing this operation, ensure that the selected storage pool and disks are correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Add disks of controller enclosure "CTE0" to storage pool "0".

```text
admin:/>add storage_pool disk pool_id=0 disk_list=all controller_enclosure_list=CTE0
WARNING: You are about to expand storage pool.
Suggestion: Before performing this operation, ensure that the selected storage pool and disks are correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
