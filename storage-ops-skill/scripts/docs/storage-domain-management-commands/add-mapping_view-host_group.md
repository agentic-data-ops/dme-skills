# add mapping_view host_group


##### Function

The **add mapping_view host_group** command is used to add a host group to a mapping view.

##### Format

**add mapping_view host_group** mapping_view_id=? host_group_id=? \[ force=? \]

**add mapping_view host_group** mapping_view_name=? host_group_name=? \[ force=? \]

##### Parameters

| Parameter           | Description                                                                                                                                                                                 | Value                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.                                                                                                                                                                            | To obtain the value, run "show mapping_view general".                                           |
| host_group_id=?     | Host group ID.                                                                                                                                                                              | To obtain the value, run "show host_group general".                                             |
| host_group_name=?   | Host group name.                                                                                                                                                                            | To obtain the value, run "show host_group general".                                             |
| mapping_view_name=? | Mapping view name.                                                                                                                                                                          | To obtain the value, run "show mapping_view general".                                           |
| force=?             | Whether to perform a consistency check for HyperMetro host LUN IDs. This parameter is not specified by default. In this case, a consistency check for HyperMetro host LUN IDs is performed. | The value is "true", indicating not to perform a consistency check for HyperMetro host LUN IDs. |

##### Usage Guidelines

None.

##### Example

Add the host group whose ID is "0" to the mapping view whose ID is "0".

```text
admin:/>add mapping_view host_group mapping_view_id=0 host_group_id=0
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Add host group 0 successfully.

```

Add the host group whose name is "host01" to the mapping view whose name is "map01".

```text
admin:/>add mapping_view host_group host_group_name=host01 mapping_view_name=map01 force=true
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Add host group hg1 successfully.

```

##### System Response

None
