# create hyper_cdp_consistency_group general


##### Function

The **create hyper_cdp_consistency_group general** command is used to create a HyperCDP consistency group for a specified LUN consistency group.

##### Format

**create hyper_cdp_consistency_group general** lun_consistency_group_id_list=? name=? \[ cdp_consistency_group_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_consistency_group_id_list=? | ID of a source LUN consistency group. | The value is an integer ranging from 0 to 16383.<br>You can run the "show lun_consistency_group general" command to obtain the value.<br>Multiple source LUN consistency groups can be added. Multiple LUN consistency group IDs are separated by ",", or ranges are separated by "-", for example, 0,5-8. |
| name=? | Name of a HyperCDP consistency group. | The value contains 1 to 31 characters including letters, digits, hyphens (-), underscores (_), and periods (.). NOTE: When you create HyperCDP consistency groups in a batch, the length of "name=?" cannot exceed 27 characters. |
| cdp_consistency_group_id=? | ID of a HyperCDP consistency group. | The value is an integer ranging from 0 to 99999. |

##### Usage Guidelines

You can create multiple HyperCDP consistency groups for different LUN consistency groups at the same time.

##### Example

Create HyperCDP consistency group "new" for LUN consistency group "1".

```text
admin:/>create hyper_cdp_consistency_group general lun_consistency_group_id_list=1 name=new
create HyperCDP consistency group new successfully.
```

Create three HyperCDP consistency groups, each for LUN consistency groups "1", "3", and "4".

```text
admin:/>create hyper_cdp_consistency_group general lun_consistency_group_id_list=1,3,4 name=cdp_cg
create HyperCDP consistency group cdp_cg0000 successfully.
create HyperCDP consistency group cdp_cg0001 successfully.
create HyperCDP consistency group cdp_cg0002 successfully.
```

##### System Response

None
