# remove mapping_view port_group


##### Function

The **remove mapping_view port_group** command is used to remove a port group from a mapping view.

##### Format

**remove mapping_view port_group** mapping_view_id=? port_group_id=?

**remove mapping_view port_group** mapping_view_name=? port_group_name=?

##### Parameters

| Parameter           | Description        | Value                                                    |
|---------------------|--------------------|----------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.   | To obtain the value, run "show mapping_view general".    |
| port_group_id=?     | Port group ID.     | To obtain the value, run "show mapping_view port_group". |
| mapping_view_name=? | Mapping view name. | To obtain the value, run "show mapping_view general".    |
| port_group_name=?   | Port group name.   | To obtain the value, run "show mapping_view port_group". |

##### Usage Guidelines

None.

##### Example

Remove the port group whose ID is "0" from the mapping view whose ID is "1".

```text
admin:/>remove mapping_view port_group mapping_view_id=1 port_group_id=0
CAUTION: You are about to modify mappings among LUN groups, host groups, and port groups in the mapping view.
This operation will make the original mappings become invalid.
Suggestion: Before performing this operation, ensure that the selected mapping view, LUN groups, host groups, and port groups are correct, and stop host services related to the mapping view.
Do you wish to continue?(y/n)y
Remove port group 0 successfully.
```

Remove the port group whose name is "pg01" from the mapping view whose name is "map01".

```text
admin:/>remove mapping_view port_group mapping_view_name=map01 port_group_name=pg01
CAUTION: You are about to modify mappings among LUN groups, host groups, and port groups in the mapping view.
This operation will make the original mappings become invalid.
Suggestion: Before performing this operation, ensure that the selected mapping view, LUN groups, host groups, and port groups are correct, and stop host services related to the mapping view.
Do you wish to continue?(y/n)y
Remove port group 0 successfully.
```

##### System Response

None
