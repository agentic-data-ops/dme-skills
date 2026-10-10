# add disk_domain disk


##### Function

The **add disk_domain disk** command is used to add disks to a disk domain.

##### Format

**add disk_domain disk** disk_domain_id=? disk_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disk_domain_id=? | ID of a disk domain to which you want to add disks. | To obtain the value, run "show disk_domain general". |
| disk_list=? | ID list of disks that you want to add to a disk domain. | The value can be "all", a disk ID range, or a disk ID list, where: <br>"all": All free disks are added to a disk domain.<br>Disk ID range: The value is in the format of start disk ID-end disk ID, for example, DAE000.1-5.<br>Disk ID list: Multiple disk IDs are separated by commas (,), for example, "DAE000.1,DAE000.2,DAE000.3".<br> You can run the "show disk general" command to obtain the current system disk list. |

##### Usage Guidelines

None

##### Example

Add SSDs to the disk domain whose ID is "0".

```text
admin:/>add disk_domain disk disk_domain_id=0 disk_list=all
WARNING: You are about to add disks to the disk domain. If too much disk space is added, the disk domain space cannot be fully utilized. Use the evaluation tool(eDesigner) to evaluate capacity expansion and then perform capacity expansion.
Suggestion: Before performing this operation, ensure that you have correctly selected the disks and disk domain.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
