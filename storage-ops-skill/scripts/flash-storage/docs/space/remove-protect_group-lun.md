# remove protect_group lun


##### Function

The **remove protect_group lun** command is used to remove a member LUN from a specified protected group.

##### Format

**remove protect_group lun** protect_group_id=? lun_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| protect_group_id=? | Protected group ID. | To obtain the value, run the "show protect_group general" command. |
| lun_id_list=? | ID list of LUNs to be removed from a protected group. | You can run the "show protect_group lun" command to obtain the ID list of member LUNs. To remove multiple LUNs at a time: <br>IDs of multiple LUNs can be separated by commas (,). For example, lun_id_list=1,2,3,4,5.<br>You can specify LUN ID ranges separated by hyphens (-). For example, lun_id_list=1-5,7,9-11.<br>A maximum of 100 LUN IDs can be specified at a time. |

##### Usage Guidelines

None

##### Example

Remove LUN "2" from protected group "2".

```text
admin:/>remove protect_group lun protect_group_id=2 lun_id_list=2
WARNING: You are about to remove the LUN from a protection group. After the removal, the LUN has no protection.
Suggestion: Before performing this operation, ensure that the LUN does not need protection.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Removing LUNs from PG or LUN group (pg) in background.
Run the "show task general task_id=3" command to query the execution result.
```

##### System Response

None
