# delete hyper_cdp_consistency_group


##### Function

The **delete hyper_cdp_consistency_group** command is used to delete HyperCDP consistency groups.

##### Format

**delete hyper_cdp_consistency_group** cdp_consistency_group_id_list=? \[ protect_group_id=? \] \[ lun_consistency_group_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_consistency_group_id_list=? | ID of a HyperCDP consistency group. | The value is an integer ranging from 0 to 99999.<br>To obtain the value, run "show hyper_cdp_consistency_group universal".<br>Multiple HyperCDP consistency groups are separated by commas(,), or the ID range is separated by hyphens (-), such as: 0,5-8. |
| lun_consistency_group_id=? | ID of a source LUN consistency group. | The value is an integer ranging from 0 to 16383.<br>You can run the "show lun_consistency_group general" command to obtain the value. |
| protect_group_id=? | Protection group ID. | The value is an integer ranging from 0 to 16383.<br>You can run the "show protect_group general" command to obtain the value. |

##### Usage Guidelines

-   Multiple HyperCDP consistency groups can be deleted at the same time.
-   Before running this command, ensure that the selected HyperCDP consistency group is exactly the one you want to delete and is no longer needed.

##### Example

Delete HyperCDP consistency group "1".

```text
admin:/>delete hyper_cdp_consistency_group cdp_consistency_group_id_list=1
WARNING: You are about to delete the HyperCDP consistency group, which is an irreversible operation. If you delete a HyperCDP consistency group, all HyperCDP objects and their data in the HyperCDP consistency group will be deleted.
Suggestion: Before performing this operation, ensure that the selected HyperCDP consistency group is correct and you do not need the data of the HyperCDP object.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
delete HyperCDP consistency group 1 successfully.
```

##### System Response

None
