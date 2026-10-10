# remove hyper_cdp_schedule lun


##### Function

The **remove hyper_cdp_schedule lun** command is used to remove LUNs from a HyperCDP schedule.

##### Format

**remove hyper_cdp_schedule lun** schedule_id=? lun_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id=? | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". |
| lun_id_list=? | ID list of the LUNs to be removed. | To obtain the value, run "show lun general".<br>You can specify multiple LUN IDs separated by commas (,) or an ID range separated by hyphens (-), such as: 0,5-8. |

##### Usage Guidelines

-   Before performing the operation, confirm that the schedule ID is correct and exists.
-   Before performing the operation, confirm that the LUN ID is correct and exists.

##### Example

Remove LUN "2" from HyperCDP schedule "2".

```text
admin:/>remove hyper_cdp_schedule lun schedule_id=2 lun_id_list=2
WARNING: You are about to remove LUN or protection group from HyperCDP schedule, which cannot be undone. This operation will delete the relationship between the LUN or protection group and the HyperCDP schedule.
Suggestion: Before performing this operation, ensure that you have correctly selected the LUN or protection group to be removed.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove HyperCDP schedule lun 2 successfully.
```

##### System Response

None
