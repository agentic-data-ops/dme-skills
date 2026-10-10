# change hyper_copy_consistency_group general


##### Function

The **change hyper_copy_consistency_group general** command is used to modify HyperCopy consistency group settings.

##### Format

**change hyper_copy_consistency_group general** hyper_copy_consistency_group_id=? \[ copy_speed=? \] \[ name=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hyper_copy_consistency_group_id | HyperCopy consistency group ID. | To obtain the value, run "show hyper_copy_consistency_group general". |
| copy_speed | Copy speed. | The value can be "low", "middle", "high", or "highest", where: <br>"low": indicates the low speed.<br>"middle": indicates the medium speed.<br>"high": indicates the high speed.<br>"highest": indicates the highest speed. |
| name | Name of a HyperCopy consistency group. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| description | Description of a HyperCopy consistency group. | - |

##### Usage Guidelines

None

##### Example

Change the copy speed of HyperCopy consistency group "3" to "high".

```text
admin:/>change hyper_copy_consistency_group general hyper_copy_consistency_group_id=3 copy_speed=high
WARNING: You are about to change the copy rate of HyperCopy consistency group  to the high or highest speed. This operation may cause heavy service pressure and decrease the read/write performance of the host.
Suggestion: Perform this operation during off-peak hours.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
