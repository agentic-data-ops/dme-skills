# create snapshot_consistency_group general


##### Function

The **create snapshot_consistency_group general** command is used to create a snapshot consistency group for a specified LUN consistency group.

##### Format

**create snapshot_consistency_group general** name=? { source_lun_consistency_group_id_list=? \| source_lun_consistency_group_name_list=? } \[ snapshot_consistency_group_id=? \] \[ description=? \] \[ dst_lun_group_id_list=? \| dst_lun_group_name_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a snapshot consistency group. | - |
| source_lun_consistency_group_id_list=? | ID of the LUN consistency group for which a snapshot consistency group needs to be created. | You can run the show lun_consistency_group general command to obtain the LUN consistency group ID list. To create snapshot consistency groups for multiple LUN consistency groups: <br>Use commas (,) to separate multiple LUN consistency group IDs. For example, source_lun_consistency_group_id_list=1,2,3,4,5.<br>You can specify the range of LUN consistency group IDs. Use hyphens (-) to separate the ranges. For example, source_lun_consistency_group_id_list=1-5,7,9-11. |
| source_lun_consistency_group_name_list | Name of the LUN consistency group for which a snapshot consistency group is to be created. | You can run the show lun_consistency_group general command to obtain the LUN consistency group name list. To create snapshot consistency groups for multiple LUN consistency groups: Multiple LUN consistency group names can be separated by commas (,). For example, source_lun_consistency_group_name_list=lcg1,lcg2. |
| snapshot_consistency_group_id | ID of a snapshot consistency group. | The value is an integer ranging from 0 to 16383. If this parameter is not specified, the system automatically allocates an ID to the newly created snapshot consistency group. |
| description=? | Description of a snapshot consistency group. | - |
| dst_lun_group_id_list | ID of the target LUN group. The number of dst_lun_group_id_list IDs must be the same as that of source_lun_consistency_group_id_list. | You can run the show lun_group general command to obtain the list of destination LUN group IDs. When multiple LUN groups need to be specified: <br>Use commas (,) to separate multiple LUN group IDs. For example, dst_lun_group_id_list=1,2,3,4,5.<br>You can specify LUN group ID ranges and use hyphens (-) to separate them. For example, dst_lun_group_id_list=1-5,7,9-11. |
| dst_lun_group_name_list=? | Name of the target LUN group. The number of dst_lun_group_name_list name lists must be the same as that of source_lun_consistency_group_name_list. | You can run the show lun_group general command to obtain the list of destination LUN group names. When multiple LUN groups need to be specified: Multiple LUN group names can be separated by commas (,). For example, dst_lun_group_name_list=lg1,lg2. |

##### Usage Guidelines

In the current version, you are advised to run the "create snapshot_consistency_group universal" command rather than the "**create snapshot_consistency_group general**" command to create a snapshot consistency group for a specified LUN consistency group.

##### Example

Create a snapshot consistency group.

```text
admin:/>create snapshot_consistency_group general name=snapcg1 source_lun_consistency_group_id_list=1
Create snapshot consistency group 1 successfully.
```

Use target LUN group "0" to create a snapshot consistency group.

```text
admin:/>create snapshot_consistency_group general name=cg2 source_lun_consistency_group_id_list=0 dst_lun_group_id_list=0
WARNING: You are about to create a snapshot consistency group. This operation will reclaim data of the member LUNs in the target LUN group. Before this operation, ensure that the host is not reading or writing the member LUNs in the target LUN group, and no data of these LUN is stored in the host cache.
Suggestion: If you want to retain data of these LUN, back up the data in advance.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Create snapshot consistency group 0 successfully.
```

##### System Response

None
