# remove mapping_view lun_group


##### Function

The **remove mapping_view lun_group** command is used to remove a LUN group from a mapping view.

##### Format

**remove mapping_view lun_group** mapping_view_id=? lun_group_id=?

**remove mapping_view lun_group** mapping_view_name=? lun_group_name=?

##### Parameters

| Parameter           | Description        | Value                                                   |
|---------------------|--------------------|---------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.   | To obtain the value, run "show mapping_view general".   |
| lun_group_id=?      | LUN group ID.      | To obtain the value, run "show mapping_view lun_group". |
| mapping_view_name=? | Mapping view name. | To obtain the value, run "show mapping_view general".   |
| lun_group_name=?    | LUN group name.    | To obtain the value, run "show mapping_view lun_group". |

##### Usage Guidelines

None.

##### Example

Remove the LUN group whose ID is "1" from the mapping view whose ID is "1".

```text
admin:/>remove mapping_view lun_group mapping_view_id=1 lun_group_id=1
WARNING: You are about to modify mappings among LUN groups, host groups, and port groups in the mapping view.This operation will make the original mappings become invalid.
Suggestion:
1. Before performing this operation, ensure that the selected mapping view, LUN groups, host groups, and port groups are correct, and stop host services related to the mapping view.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)
Remove LUN group 1 successfully.
```

Remove the LUN group whose name is "lg01" from the mapping view whose name is "map01".

```text
admin:/>remove mapping_view lun_group mapping_view_name=map01 lun_group_name=lg01
WARNING: You are about to modify mappings among LUN groups, host groups, and port groups in the mapping view.This operation will make the original mappings become invalid.
Suggestion:
1. Before performing this operation, ensure that the selected mapping view, LUN groups, host groups, and port groups are correct, and stop host services related to the mapping view.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)
Remove LUN group 1 successfully.
```

##### System Response

None
