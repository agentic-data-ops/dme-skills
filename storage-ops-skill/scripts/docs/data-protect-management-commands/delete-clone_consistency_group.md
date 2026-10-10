# delete clone_consistency_group


##### Function

The **delete clone_consistency_group** command is used to delete a clone consistency group.

##### Format

**delete clone_consistency_group** { clone_consistency_group_id_list=? \| clone_consistency_group_name_list=? } \[ is_delete_dst_lun=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_consistency_group_id_list=? | List of clone consistency group IDs. | You can run the show clone_consistency_group general command to obtain the value. |
| clone_consistency_group_name_list=? | Clone consistency group name list. | You can run the show clone_consistency_group general command to obtain the value. |
| is_delete_dst_lun=? | Whether to delete the target LUN. | The value can be "yes" or "no", where: <br>"yes": The target LUN is deleted.<br>"no": The target LUN is not deleted. |
| is_recycle_dst_lun_data=? | Whether to reclaim data on the target LUN. | The value can be "yes" or "no", where: <br>"yes": reclaims data on the target LUN.<br>"no": does not reclaim data on the target LUN. |

##### Usage Guidelines

None

##### Example

Delete clone consistency group "7".

```text
admin:/>delete clone_consistency_group clone_consistency_group_id_list=7
WARNING: You are about to delete clone consistency group, which cannot be undone. Deleting the clone consistency group will disconnect the source LUNs from target LUNs.
Suggestion: Before performing this operation, ensure that the clone consistency group is correctly selected and confirm that you need to disconnect the source LUNs from target LUNs.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Delete clone consistency group 7 successfully.
```

Delete clone consistency group "7" and delete the target LUNs.

```text
admin:/>delete clone_consistency_group clone_consistency_group_id_list=7 is_delete_dst_lun=yes
WARNING: You are about to delete clone consistency group, which cannot be undone. Deleting the clone consistency group will disconnect the source LUNs from target LUNs and will delete the target LUNs.
Suggestion: Before performing this operation, ensure that the clone consistency group is correctly selected and confirm that you need to disconnect the source LUNs from target LUNs and delete the target LUNs.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Delete clone consistency group 7 successfully.
```

Delete clone consistency group "7" and reclaim the target LUNs' data.

```text
admin:/>delete clone_consistency_group clone_consistency_group_id_list=7 is_recycle_dst_lun_data=yes
WARNING: You are about to delete clone consistency group, which cannot be undone. Deleting the clone consistency group will disconnect the source LUNs from target LUNs and reclaim the target LUNs' data.
Suggestion: Before performing this operation, ensure that the clone consistency group is correctly selected and confirm that you need to disconnect the source LUNs from target LUNs and reclaim the target LUNs' data.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Delete clone consistency group 7 successfully.
```

##### System Response

None
