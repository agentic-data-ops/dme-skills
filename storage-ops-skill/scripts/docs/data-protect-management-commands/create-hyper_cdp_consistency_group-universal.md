# create hyper_cdp_consistency_group universal


##### Function

The **create hyper_cdp_consistency_group universal** command is used to create a HyperCDP consistency group for a specified protection group.

##### Format

**create hyper_cdp_consistency_group universal** protect_group_id_list=? name=? \[ cdp_consistency_group_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| protect_group_id_list=? | ID of a source protection group. | The value is an integer ranging from 0 to 16383.<br>You can run the "show protect_group general" command to obtain the value.<br>Multiple source protection groups can be added. Protection group IDs are separated by "," or by "-", for example, 0,5-8. |
| name=? | Name of a HyperCDP consistency group. | The value contains 1 to 31 characters including letters, digits, hyphens (-), underscores (_), and periods (.). NOTE: When you create HyperCDP consistency groups in a batch, the length of "name=?" cannot exceed 27 characters. |
| cdp_consistency_group_id=? | ID of a HyperCDP consistency group. | The value is an integer ranging from 0 to 99999. |

##### Usage Guidelines

You can create multiple HyperCDP consistency groups for different protection groups at the same time.

##### Example

Create HyperCDP consistency group "new" for protection group "1".

```text
admin:/>create hyper_cdp_consistency_group universal protect_group_id_list=1 name=new
create HyperCDP consistency group new successfully.
```

Create three HyperCDP consistency groups, each for protection groups "1", "3", and "4".

```text
admin:/>create hyper_cdp_consistency_group universal protect_group_id_list=1,3,4 name=cdp_cg
create HyperCDP consistency group cdp_cg0000 successfully.
create HyperCDP consistency group cdp_cg0001 successfully.
create HyperCDP consistency group cdp_cg0002 successfully.
```

##### System Response

None
