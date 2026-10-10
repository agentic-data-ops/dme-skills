# add mapping_view lun_group


##### Function

The **add mapping_view lun_group** command is used to add a LUN group to a mapping view.

##### Format

**add mapping_view lun_group** mapping_view_id=? lun_group_id=? \[ host_lun_id_list=? \| host_lun_id_start=? \] \[ force=? \]

**add mapping_view lun_group** mapping_view_name=? lun_group_name=? \[ host_lun_id_list=? \| host_lun_id_start=? \] \[ force=? \]

##### Parameters

| Parameter           | Description                                                                                                                                                                                 | Value                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.                                                                                                                                                                            | To obtain the value, run the "show mapping_view general" command.                                                                                                                                                                                                                                                                                                                                |
| lun_group_id=?      | LUN group ID.                                                                                                                                                                               | To obtain the value, run the "show lun_group general" command.                                                                                                                                                                                                                                                                                                                                   |
| host_lun_id_list=?  | Start host LUN ID that is assigned to a LUN in the LUN group when the LUN group is being added to a mapping view.                                                                           | The value is mappings between LUN IDs and Host LUN IDs. The format is "LUN ID:Host LUN ID". If there are more than one mappings, separate them with commas (,). Run the "show host lun" and "show host snapshot" commands to query the host LUN IDs that have been assigned. A LUN ID ranges from 0 to 65535, and a host LUN ID ranges from 0 to 4095. A maximum of 1024 mappings are supported. |
| mapping_view_name=? | Mapping view name.                                                                                                                                                                          | To obtain the value, run "show mapping_view general".                                                                                                                                                                                                                                                                                                                                            |
| host_lun_id_start=? | Start host LUN ID that is assigned to a LUN in the LUN group when the LUN group is being added to a mapping view.                                                                           | Run the "show host lun" and "show host snapshot" commands to query the host LUN IDs that have been assigned.                                                                                                                                                                                                                                                                                     |
| lun_group_name=?    | LUN group name.                                                                                                                                                                             | To obtain the value, run "show lun_group general".                                                                                                                                                                                                                                                                                                                                               |
| force=?             | Whether to perform a consistency check for HyperMetro host LUN IDs. This parameter is not specified by default. In this case, a consistency check for HyperMetro host LUN IDs is performed. | The value is "true", indicating not to perform a consistency check for HyperMetro host LUN IDs.                                                                                                                                                                                                                                                                                                  |

##### Usage Guidelines

None

##### Example

Add the LUN group whose ID is "1" to the mapping view whose ID is "1".

```text
admin:/>add mapping_view lun_group mapping_view_id=1 lun_group_id=1
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group.
If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Add LUN group 1 successfully.
```

Add the LUN group whose name is "lg01" to the mapping view whose name is "map01".

```text
admin:/>add mapping_view lun_group mapping_view_name=map01 lun_group_name=lg01
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group.
If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Add LUN group 1 successfully.
```

Assign host LUN IDs "6" and "7" for LUNs whose IDs are "1" and "2" in the mapping view whose ID is "1".

```text
admin:/>add mapping_view lun_group mapping_view_id=1 lun_group_id=1 host_lun_id_list=1:6,2:7
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group.
If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
You are about to set the host LUN ID of the LUN in lun_group.
This operation causes the LUN unable to be detected by the host if the host LUN ID set is beyond the host LUN ID range supported by the host.
Before you perform this operation:
1. Ensure that mutual access exclusion has been correctly configured on service hosts.
2. Ensure that the host LUN ID set is within the host LUN ID range supported by the host.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Add LUN group 1 successfully.
```

Assign host LUN ID "6" to the LUN whose name is "lg01", and assign host LUN ID "7" to the LUN whose ID is "2" in the mapping view whose name is "map01".

```text
admin:/>add mapping_view lun_group mapping_view_name=map01 lun_group_name=lg01 host_lun_id_list=1:6,2:7
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group.
If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
You are about to set the host LUN ID of the LUN in lun_group.
This operation causes the LUN unable to be detected by the host if the host LUN ID set is beyond the host LUN ID range supported by the host.
Before you perform this operation:
1. Ensure that mutual access exclusion has been correctly configured on service hosts.
2. Ensure that the host LUN ID set is within the host LUN ID range supported by the host.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Add LUN group 1 successfully.
```

##### System Response

None
