# delete clone


##### Function

The **delete clone** command is used to delete a clone pair.

##### Format

**delete clone** { clone_id_list=? \| clone_name_list=? } \[ is_delete_dst_lun=? \] \[ is_recycle_dst_lun_data=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_id_list=? | List of clone pair IDs. | You can run the "show clone general" command to obtain the value. You can specify multiple clone IDs separated by commas (,), or specify ID ranges by hyphens (-), for example, "1,5-8". |
| clone_name_list=? | Name list of clone pairs. | You can run the show clone general command to obtain the value. You can specify multiple clone pair names separated by commas (,). |
| is_delete_dst_lun=? | Whether to delete the target LUN. | The value can be yes or no. The options are as follows: <br>yes: The target LUN is deleted.<br>no: The target LUN is not deleted. |
| is_recycle_dst_lun_data=? | Whether to reclaim data on the target LUN. | The value can be "yes" or "no", where: <br>"yes": reclaims data on the target LUN.<br>"no": does not reclaim data on the target LUN. |

##### Usage Guidelines

None

##### Example

Delete clone pairs "1", "7", and "8".

```text
admin:/>delete clone clone_id_list=1,7-8
WARNING: You are about to delete the clone pair, which cannot be undone. You must recreate a clone pair when you need it.
Suggestion: Before performing this operation, ensure that the operation and parameters are correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete clone 1 successfully.
Delete clone 7 successfully.
Delete clone 8 successfully.
```

##### System Response

None
