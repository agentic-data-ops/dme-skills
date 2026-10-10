# remove lun_group lun


##### Function

The **remove lun_group lun** command is used to remove LUNs from a specified LUN group.

##### Format

**remove lun_group lun** { lun_group_id=? \| lun_group_name=? } { lun_id_list=? \| lun_name_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_group_id=? | LUN group ID. | To obtain the value, run "show lun_group general". |
| lun_group_name=? | LUN group name. | To obtain the value, run "show lun_group general". |
| lun_id_list=? | ID list of LUNs or snapshots. | To obtain the value, run "show lun_group lun" or "show lun_group snapshot". If multiple LUNs or snapshots need to be removed from a LUN group: <br>Separate the LUN or snapshot IDs with commas (,). For example, "lun_id_list=1,2,3,4,5".<br>Specify LUN or snapshot ID ranges and separate the ranges with hyphens (-). For example, "lun_id_list=1-5,7,9-11". |
| lun_name_list=? | Name list of LUNs or snapshots. | To obtain the value, run "show lun general" or "show snapshot general". If multiple LUNs or snapshots need to be added to a LUN group, separate the LUN or snapshot names with commas (,). For example, "lun_name_list=lun1,lun2,lun3,lun4,lun5". |

##### Usage Guidelines

None.

##### Example

Remove LUN "2" from LUN group "2".

```text
admin:/>remove lun_group lun lun_group_id=2 lun_id_list=2
WARNING: You are about to remove the selected LUNs from its LUN group. This operation will prevent the hosts associated with the LUN group from accessing the removed LUNs.
Suggestion: Before performing this operation, ensure that the selected LUNs and LUN group are correct, and stop host services running on the LUNs to be removed.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove LUN 2 from LUN group successfully.
```

Remove LUN "Lun1" from LUN group "LunGroup1".

```text
admin:/>remove lun_group lun lun_group_name=LunGroup1 lun_name_list=Lun1
WARNING: You are about to remove the selected LUNs from its LUN group. This operation will prevent the hosts associated with the LUN group from accessing the removed LUNs.
Suggestion: Before performing this operation, ensure that the selected LUNs and LUN group are correct, and stop host services running on the LUNs to be removed.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove LUN Lun1 from LUN group successfully.
```

Remove LUN "5" from LUN group "3" that belongs to a protection group.

```text
admin:/>remove lun_group lun lun_group_id=3 lun_id_list=5
WARNING: You are about to remove the selected LUNs from its LUN group. This operation will prevent the hosts associated with the LUN group from accessing the removed LUNs.
Suggestion: Before performing this operation, ensure that the selected LUNs and LUN group are correct, and stop host services running on the LUNs to be removed.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Removing LUNs from PG or LUN group (lg03) in background.
Run the "show task general task_id=11" command to query the execution result.

admin:/>show task general task_id=11
Task ID    : 11
Task Name  : removeLunFromGroup
Duration   : 0 day(s),0 hour(s),0 minute(s),2 second(s)
Start Time : 2019-09-20/10:31:18 UTC+08:00
End Time   : 2019-09-20/10:31:20 UTC+08:00
Process    : 100%
Status     : success
Object     : lg03
```

##### System Response

None
