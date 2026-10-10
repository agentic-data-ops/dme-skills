# add hyper_cdp_schedule protect_group


##### Function

The **add hyper_cdp_schedule protect_group** command is used to add protection groups to a HyperCDP schedule.

##### Format

**add hyper_cdp_schedule protect_group** { schedule_id=? \| schedule_name=? } { protect_group_id_list=? \| protect_group_name_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id=? | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". |
| schedule_name=? | Name of a HyperCDP schedule. | To obtain the value, run "show hyper_cdp_schedule general". |
| protect_group_id_list=? | ID list of the protection groups to be added. | To obtain the value, run "show protect_group general".<br>You can specify multiple protection group IDs separated by commas (,) or an ID range using hyphens (-), such as: 1,5-8. |
| protect_group_name_list=? | Name list of the protection groups to be added. | To obtain the value, run "show protect_group general". |

##### Usage Guidelines

After you add protection groups to a HyperCDP schedule, the schedule will be effective for the added protection groups.

##### Example

Add protection groups "1", "5", and "6" to HyperCDP schedule "3".

```text
admin:/>add hyper_cdp_schedule protect_group schedule_id=3 protect_group_id_list=1,5-6
Add PG to HyperCDP Schedule (sch1) in background.
Run the "show task general task_id=36" command to query the execution result.
Add PG to HyperCDP Schedule (sch1) in background.
Run the "show task general task_id=37" command to query the execution result.
Add PG to HyperCDP Schedule (sch1) in background.
Run the "show task general task_id=38" command to query the execution result.

```

##### System Response

None
