# delete lun_consistency_group


##### Function

The **delete lun_consistency_group** command is used to delete a LUN consistency group.

##### Format

**delete lun_consistency_group** lun_consistency_group_id_list=?

##### Parameters

| Parameter                       | Description                                          | Value                                                          |
|---------------------------------|------------------------------------------------------|----------------------------------------------------------------|
| lun_consistency_group_id_list=? | ID list of the LUN consistency groups to be deleted. | To obtain the value, run "show lun_consistency_group general". |

##### Usage Guidelines

-   This operation will delete the LUN consistency group information from a system and the information cannot be restored.
-   Before performing this operation, check whether the ID of the selected LUN consistency group is correct.
-   If a LUN consistency group contains member LUNs, the LUN consistency group cannot be deleted. Remove all member LUNs first.

##### Example

Delete LUN consistency group "1".

```text
admin:/>delete lun_consistency_group lun_consistency_group_id_list=1
Delete LUN consistency group 1 successfully.
```

##### System Response

None
