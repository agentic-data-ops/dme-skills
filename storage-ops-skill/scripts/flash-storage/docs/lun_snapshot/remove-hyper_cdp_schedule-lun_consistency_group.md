# remove hyper_cdp_schedule lun_consistency_group


##### Function

The **remove hyper_cdp_schedule lun_consistency_group** command is used to remove LUN consistency groups from a HyperCDP schedule.

##### Format

**remove hyper_cdp_schedule lun_consistency_group** schedule_id=? lun_consistency_group_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id=? | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". |
| lun_consistency_group_id_list=? | ID list of the LUN consistency groups to be removed. | To obtain the value, run "show lun_consistency_group general".<br>You can specify multiple LUN consistency group IDs separated by commas (,) or an ID range separated by hyphens (-), such as: 1,5-8. |

##### Usage Guidelines

-   Before performing the operation, confirm that the schedule ID is correct and exists.
-   Before performing the operation, confirm that the LUN consistency group is correct and exists.

##### Example

Remove LUN consistency group "2" from HyperCDP schedule "2".

```text
admin:/>remove hyper_cdp_schedule lun_consistency_group schedule_id=2 lun_consistency_group_id_list=2
WARNING: You are about to remove LUN/LUN consistency group from HyperCDP schedule. Removal is irreversible. This operation will delete the relationship between the LUN/LUN consistency group and the HyperCDP schedule.
Suggestion: Before performing this operation, ensure that you have selected the LUN/LUN consistency group to be removed.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove HyperCDP schedule lun_consistency_group 2 successfully.
```

##### System Response

None
