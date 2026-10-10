# create snapshot_consistency_group universal


##### Function

The **create snapshot_consistency_group universal** command is used to create a snapshot consistency group for a specified LUN protection group.

##### Format

**create snapshot_consistency_group universal** name=? protect_group_name_list=? \[ snapshot_consistency_group_id=? \] \[ description=? \] \[ dst_lun_group_name_list=? \]

**create snapshot_consistency_group universal** name=? protect_group_id_list=? \[ snapshot_consistency_group_id=? \] \[ description=? \] \[ dst_lun_group_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a snapshot consistency group. | - |
| protect_group_id_list=? | ID of the LUN protection group for which a snapshot consistency group needs to be created. | To obtain the LUN protection group ID list, run "show protect_group general". If you want to create snapshot consistency groups for multiple LUN protection groups concurrently: <br>Separate multiple LUN protection group IDs by commas (,). For example, "protect_group_id_list=1,2,3,4,5".<br>Specify a LUN protection group ID range using a hyphen (-). For example, "protect_group_id_list=1-5,7,9-11". |
| protect_group_name_list=? | Name of the LUN protection group for which a snapshot consistency group is to be created. | To obtain the value, run the "show protect_group general" command. To create snapshot consistency groups for multiple LUN protection groups: Multiple LUN protection group names can be separated by commas (,). For example, protect_group_name_list=pg1,pg2. |
| snapshot_consistency_group_id=? | ID of a snapshot consistency group. | The value is an integer ranging from 0 to 16383. If this parameter is not specified, the system automatically allocates an ID to the newly created snapshot consistency group. |
| description=? | Description of a snapshot consistency group. | - |
| dst_lun_group_id_list=? | ID of the target LUN group. The number of dst_lun_group_id_list IDs must be the same as that of protect_group_id_list. | You can run the show lun_group general command to obtain the list of target LUN group IDs. When multiple LUN groups need to be specified: <br>Use commas (,) to separate multiple LUN group IDs. For example, dst_lun_group_id_list=1,2,3,4,5.<br>You can specify LUN group ID ranges and use hyphens (-) to separate them. For example, dst_lun_group_id_list=1-5,7,9-11. |
| dst_lun_group_name_list=? | Name of the target LUN group. The number of dst_lun_group_name_list name lists must be the same as that of protect_group_name_list. | You can run the show lun_group general command to obtain the list of destination LUN group names. When multiple LUN groups need to be specified: Multiple LUN group names can be separated by commas (,). For example, dst_lun_group_name_list=lg1,lg2. |

##### Usage Guidelines

None

##### Example

Create a snapshot consistency group.

```text
admin:/>create snapshot_consistency_group universal name=scg1 protect_group_id_list=1
Create snapshot consistency group of protect group 1 successfully.
```

Use target LUN group "0" to create a snapshot consistency group.

```text
admin:/>create snapshot_consistency_group universal name=cg1 protect_group_id_list=0 dst_lun_group_id_list=0
WARNING: You are about to create a snapshot consistency group. This operation will reclaim data of the member LUNs in the target LUN group. Before this operation, ensure that the host is not reading or writing the member LUNs in the target LUN group, and no data of these LUN is stored in the host cache.
Suggestion: If you want to retain data of these LUN, back up the data in advance.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Create snapshot group of protect group 0 successfully.
```

##### System Response

None
