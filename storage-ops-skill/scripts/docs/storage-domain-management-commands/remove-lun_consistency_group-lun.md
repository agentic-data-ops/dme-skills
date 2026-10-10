# remove lun_consistency_group lun


##### Function

The **remove lun_consistency_group lun** command is used to remove a member LUN from a specified LUN consistency group. Use this command when consistency protection is not required for a specified LUN.

##### Format

**remove lun_consistency_group lun** lun_consistency_group_id=? lun_id_list=? \[ remove_snapshot=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_consistency_group_id=? | ID of the LUN consistency group from which a LUN is to be removed. | To obtain the value, run "show lun_consistency_group general". |
| lun_id_list=? | ID list of LUNs to be removed from a LUN consistency group. | To obtain the LUN ID list, run "show lun_consistency_group lun". If you want to concurrently remove multiple LUNs from a LUN consistency group: <br>Separate multiple LUN IDs by commas (,). For example, "lun_id_list=1,2,3,4,5".<br>Specify a LUN ID range using a hyphen (-). For example, "lun_id_list=1-5,7,9-11". |
| remove_snapshot | Whether to remove the snapshot of the LUN from the snapshot consistency group. | - |

##### Usage Guidelines

-   If a LUN consistency group has an ongoing HyperCDP schedule, its member LUNs cannot be removed.
-   When removing a LUN, you can determine whether to remove the LUN's snapshot from the snapshot consistency group.

##### Example

Remove LUN "2" from LUN consistency group "2".

```text
admin:/>remove lun_consistency_group lun lun_consistency_group_id=2 lun_id_list=2
WARNING: You are about to remove the LUN  from the LUN consistency group. After the removal, the LUN has no consistency protection. This operation will cause the snapshot consistency group created for this LUN consistency group to fail to be rolled back.
Suggestion: Before performing this operation, ensure that the LUN does not need consistency protection.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove LUN 0 from LUN consistency group successfully.
```

##### System Response

None
