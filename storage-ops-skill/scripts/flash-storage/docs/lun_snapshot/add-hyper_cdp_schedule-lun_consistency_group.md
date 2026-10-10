# add hyper_cdp_schedule lun_consistency_group


##### Function

The **add hyper_cdp_schedule lun_consistency_group** command is used to add LUN consistency groups to a HyperCDP schedule.

##### Format

**add hyper_cdp_schedule lun_consistency_group** schedule_id=? lun_consistency_group_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id=? | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". |
| lun_consistency_group_id_list=? | ID list of the LUN consistency groups to be added. | To obtain the value, run "show lun_consistency_group general".<br>You can specify multiple LUN consistency group IDs separated by commas (,) or an ID range using hyphens (-), such as: 1,5-8. |

##### Usage Guidelines

After you add LUN consistency groups to a HyperCDP schedule, the schedule will be effective for the added LUN consistency groups.

##### Example

Add LUN consistency groups "1", "5", and "6" to HyperCDP schedule "1".

```text
admin:/> add hyper_cdp_schedule lun_consistency_group schedule_id=1 lun_consistency_group_id_list=1,5-6
Add HyperCDP schedule lun_consistency_group  1 successfully.
Add HyperCDP schedule lun_consistency_group  5 successfully.
Add HyperCDP schedule lun_consistency_group  6 successfully.
```

##### System Response

None
