# create hyper_copy_consistency_group


##### Function

The **create hyper_copy_consistency_group** command is used to create a HyperCopy consistency group.

##### Format

**create hyper_copy_consistency_group** name=? \[ copy_speed=? \] \[ hyper_copy_id_list=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name | Name of a HyperCopy consistency group. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| copy_speed | Copy speed. | The value can be "low", "middle", "high", or "highest", where: <br>"low": indicates the low speed.<br>"middle": indicates the medium speed.<br>"high": indicates the high speed.<br>"highest": indicates the highest speed.<br> The default value is "middle". |
| hyper_copy_id_list | HyperCopy pair ID list. | To obtain the value, run "show hyper_copy general". If you want to concurrently add multiple HyperCopy pairs to a HyperCopy consistency group: <br>Separate multiple HyperCopy pair IDs by commas (,). For example, "hyper_copy_id_list=1,2,3,4,5".<br>Specify a HyperCopy pair ID range using a hyphen (-). For example, "hyper_copy_id_list=1-5,7,9-11". |
| description | Description of a HyperCopy consistency group. | - |

##### Usage Guidelines

None

##### Example

Create a HyperCopy consistency group named "hyper_copy_cg".

```text
admin:/>create hyper_copy_consistency_group name=hyper_copy_cg copy_speed=highest
WARNING: You are about to select the high or highest copy speed to create HyperCopy consistency group. After the operation, HyperCopy pairs in the HyperCopy consistency group will be synchronized or restored at the high or highest speed, which may cause heavy service pressure and decrease the read/write performance of the host.
Suggestion: Perform this operation during off-peak hours.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Create HyperCopy consistency group successfully.
```

##### System Response

None
