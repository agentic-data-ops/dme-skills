# add hyper_cdp_schedule lun


##### Function

The **add hyper_cdp_schedule lun** command is used to add LUNs to a HyperCDP schedule.

##### Format

**add hyper_cdp_schedule lun** { schedule_id=? \| schedule_name=? } { lun_id_list=? \| lun_name_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id=? | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". |
| schedule_name=? | Name of a HyperCDP schedule. | You can run the show hyper_cdp_schedule general command to obtain the value. |
| lun_id_list=? | ID list of the LUNs to be added. | To obtain the value, run "show lun general".<br>You can specify multiple LUN IDs separated by commas (,) or an ID range using hyphens (-), such as: 0,5-8. |
| lun_name_list=? | Name list of the LUNs to be added. | You can run the show lun general command to obtain the value. |

##### Usage Guidelines

After you add LUNs to a HyperCDP schedule, the schedule will be effective for the added LUNs.

##### Example

Add LUNs "0", "5", and "6" to HyperCDP schedule "1".

```text
admin:/> add hyper_cdp_schedule lun schedule_id=1 lun_id_list=0,5-6
Add HyperCDP schedule lun  0 successfully.
Add HyperCDP schedule lun  5 successfully.
Add HyperCDP schedule lun  6 successfully.
```

##### System Response

None
