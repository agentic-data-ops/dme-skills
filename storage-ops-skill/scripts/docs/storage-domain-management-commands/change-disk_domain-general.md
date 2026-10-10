# change disk_domain general


##### Function

The **change disk_domain general** command is used to modify the properties of a disk domain, including the disk domain name, hot spare strategy, switch status of the LUN mapping table repair function, and similarity-based deduplication execution level.

##### Format

**change disk_domain general** disk_domain_id=? { name=? \| hotspare_strategy=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disk_domain_id=? | ID of a disk domain whose properties you want to modify. | To obtain the value, run "show disk_domain general". |
| name=? | Name of a disk domain. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| hotspare_strategy=? | Hot spare policy of a disk domain. | The value can be "low", "high", "none", or 0 to 8, where: <br>"low": The hot spare strategy is low and the number of hot spare disks is 1.<br>"high": The hot spare strategy is high and the number of hot spare disks is 2.<br>"none": The hot spare strategy is none and the number of hot spare disks is 0.<br>0 to 8: You can enter 0 to 8 hot spare disks. |

##### Usage Guidelines

None

##### Example

Change the name of disk domain "0" to "domain_0".

```text
admin:/>change disk_domain general disk_domain_id=0 name=domain_0
Command executed successfully.
```

Change the hot spare strategy in disk domain "0" to "none".

```text
admin:/>change disk_domain general disk_domain_id=0 hotspare_strategy=none
DANGER: You are about to reduce the hot spare space of the disk domain.
This operation may decrease the data security of the disk domain and make faulty or failing disks unable to be handled in a timely manner. What is worse, ongoing reconstruction or pre-copy tasks will fail, and services may be interrupted in some scenarios.
Suggestion: Before performing this operation, ensure that the remaining capacity is sufficient and the selected disk domain and policy are correct.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
