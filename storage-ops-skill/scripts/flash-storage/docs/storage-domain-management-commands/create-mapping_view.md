# create mapping_view


##### Function

The **create mapping_view** command is used to create a mapping view.

##### Format

**create mapping_view** name=? \[ mapping_view_id=? \] \[ lun_group_id=? \] \[ host_group_id=? \] \[ port_group_id=? \] \[ force=? \]

**create mapping_view** name=? \[ mapping_view_id=? \] \[ lun_group_name=? \] \[ host_group_name=? \] \[ port_group_name=? \] \[ force=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Mapping view name. | The value contains 1 to 31 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| mapping_view_id=? | Mapping view ID. | The value ranges from 0 to n minus one. n indicates the maximum number of mapping views. If you do not specify this parameter, the storage system automatically assigns a value. |
| lun_group_id=? | LUN group ID. If you specify this parameter, the storage system adds the LUN group corresponding to the ID to a mapping view. | To obtain the value, run "show lun_group general". |
| host_group_id=? | Host group ID. If you specify this parameter, the storage system adds the host group corresponding to the ID to a mapping view. | To obtain the value, run "show host_group general". |
| port_group_id=? | Port group ID. If you specify this parameter, the system adds the port group corresponding to the ID to a mapping view. This parameter is available only when you specify parameter "host_group_id". | To obtain the value, run "show port_group general". |
| lun_group_name=? | LUN group name. If you specify this parameter, the storage system adds the LUN group corresponding to the name to a mapping view. | To obtain the value, run "show lun_group general". |
| host_group_name=? | Host group name. If you specify this parameter, the storage system adds the host group corresponding to the name to a mapping view. | To obtain the value, run "show host_group general". |
| port_group_name=? | Port group name. If you specify this parameter, the storage system adds the port group corresponding to the name to a mapping view. This parameter is valid only when "host_group_name=?" is specified. | To obtain the value, run "show port_group general". |
| force=? | Whether to perform a consistency check for HyperMetro host LUN IDs. This parameter is not specified by default. In this case, a consistency check for HyperMetro host LUN IDs is performed. | The value is "true", indicating not to perform a consistency check for HyperMetro host LUN IDs. |

##### Usage Guidelines

None.

##### Example

Create a mapping view whose name is "mapping_Test" and ID is "1" and add LUN group "1", host group "0", and port group "0" to the mapping view.

```text
admin:/>create mapping_view name=mapping_Test mapping_view_id=1 lun_group_id=1 host_group_id=0 port_group_id=0
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Create mapping view successfully.
Add host group 0 to mapping view successfully.
Add LUN group 1 to mapping view successfully.
Add port group 0 to mapping view successfully.
```

Create a mapping view whose name is "mapping_Test" and ID is "1" and add LUN group "lg01", host group "lg01", and port group "pg01" to the mapping view.

```text
admin:/>create mapping_view name=mapping_Test mapping_view_id=1 lun_group_name=lg01 host_group_name=hg01 port_group_name=pg01
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Create mapping view successfully.
Add host group 0 to mapping view successfully.
Add LUN group 1 to mapping view successfully.
Add port group 0 to mapping view successfully.
```

##### System Response

None
