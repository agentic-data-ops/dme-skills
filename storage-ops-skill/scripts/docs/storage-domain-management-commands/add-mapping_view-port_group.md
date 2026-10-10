# add mapping_view port_group


##### Function

The **add mapping_view port_group** command is used to add a port group to a mapping view.

##### Format

**add mapping_view port_group** mapping_view_id=? port_group_id=?

**add mapping_view port_group** mapping_view_name=? port_group_name=?

##### Parameters

| Parameter           | Description        | Value                                                 |
|---------------------|--------------------|-------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.   | To obtain the value, run "show mapping_view general". |
| port_group_id=?     | Port group ID.     | To obtain the value, run "show port_group general".   |
| mapping_view_name=? | Mapping view name. | To obtain the value, run "show mapping_view general". |
| port_group_name=?   | Port group name.   | To obtain the value, run "show port_group general".   |

##### Usage Guidelines

None.

##### Example

Add the port group whose ID is "0" to the mapping view whose ID is "1".

```text
admin:/>add mapping_view port_group mapping_view_id=1 port_group_id=0
WARNING: You are about to modify mappings among LUN groups, host groups, and port groups in the mapping view.This operation will make the original mappings become invalid.
Suggestion:
1. Before performing this operation, ensure that the selected mapping view, LUN groups, host groups, and port groups are correct, and stop host services related to the mapping view.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Add port group 0 successfully.
```

Add the port group whose name is "port01" to the mapping view whose name is "map01".

```text
admin:/>add mapping_view port_group mapping_view_name=map01 port_group_name=port01
WARNING: You are about to modify mappings among LUN groups, host groups, and port groups in the mapping view.This operation will make the original mappings become invalid.
Suggestion:
1. Before performing this operation, ensure that the selected mapping view, LUN groups, host groups, and port groups are correct, and stop host services related to the mapping view.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Add port group 0 successfully.
```

##### System Response

None
