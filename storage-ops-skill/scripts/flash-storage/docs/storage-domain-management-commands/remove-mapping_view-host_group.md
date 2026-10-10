# remove mapping_view host_group


##### Function

The **remove mapping_view host_group** command is used to remove a host group from a mapping view.

##### Format

**remove mapping_view host_group** mapping_view_id=? host_group_id=?

**remove mapping_view host_group** mapping_view_name=? host_group_name=?

##### Parameters

| Parameter           | Description        | Value                                                    |
|---------------------|--------------------|----------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.   | To obtain the value, run "show mapping_view general".    |
| mapping_view_name=? | Mapping view name. | To obtain the value, run "show mapping_view general".    |
| host_group_id=?     | Host group ID.     | To obtain the value, run "show mapping_view host_group". |
| host_group_name=?   | Host group name.   | To obtain the value, run "show mapping_view host_group". |

##### Usage Guidelines

None

##### Example

Remove the host group whose ID is "0" from the mapping view whose ID is "1".

```text
admin:/>remove mapping_view host_group mapping_view_id=1 host_group_id=0
WARNING: You are about to modify mappings among LUN groups, host groups, and port groups in the mapping view.This operation will make the original mappings become invalid.
Suggestion:
1. Before performing this operation, ensure that the selected mapping view, LUN groups, host groups, and port groups are correct, and stop host services related to the mapping view.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove host group 0 successfully.
```

Remove the host group whose name is "hg01" from the mapping view whose name is "map01".

```text
admin:/>remove mapping_view host_group mapping_view_name=map01 host_group_name=hg01
WARNING: You are about to modify mappings among LUN groups, host groups, and port groups in the mapping view.This operation will make the original mappings become invalid.
Suggestion:
1. Before performing this operation, ensure that the selected mapping view, LUN groups, host groups, and port groups are correct, and stop host services related to the mapping view.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove host group 0 successfully.
```

##### System Response

None
