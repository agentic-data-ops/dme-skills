# show hyper_cdp_schedule lun_consistency_group


##### Function

The **show hyper_cdp_schedule lun_consistency_group** command is used to query information about LUN consistency groups in a HyperCDP schedule.

##### Format

**show hyper_cdp_schedule lun_consistency_group** schedule_id=?

##### Parameters

| Parameter     | Description           | Value                                                                                              |
|---------------|-----------------------|----------------------------------------------------------------------------------------------------|
| schedule_id=? | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". The value is an integer from 1 to 512. |

##### Usage Guidelines

Before performing the operation, confirm that the schedule ID is correct and exits.

##### Example

Query information about LUN consistency groups in HyperCDP schedule "1".

```text
admin:/>show hyper_cdp_schedule lun_consistency_group schedule_id=1

ID  Name         ScheduleId
--  -----------  -------
1   lunCG1       1
```

##### System Response

The following table describes the parameter meanings.

| Parameter  | Meaning                            |
|------------|------------------------------------|
| ID         | LUN consistency group ID.          |
| Name       | LUN consistency group name.        |
| ScheduleId | LUN consistency group schedule ID. |
