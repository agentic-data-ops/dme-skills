# show hyper_cdp_schedule protect_group


##### Function

The **show hyper_cdp_schedule protect_group** command is used to query information about protection groups in a HyperCDP schedule.

##### Format

**show hyper_cdp_schedule protect_group** { schedule_id=? \| schedule_name=? }

##### Parameters

| Parameter       | Description                  | Value                                                                                              |
|-----------------|------------------------------|----------------------------------------------------------------------------------------------------|
| schedule_id=?   | HyperCDP schedule ID.        | To obtain the value, run "show hyper_cdp_schedule general". The value is an integer from 1 to 512. |
| schedule_name=? | Name of a HyperCDP schedule. | You can run the show hyper_cdp_schedule general command to obtain the value.                       |

##### Usage Guidelines

Before performing the operation, confirm that the schedule ID is correct and exists.

##### Example

Query information about protection groups in HyperCDP schedule "1".

```text
admin:/>show hyper_cdp_schedule protect_group schedule_id=1

ID  Name    Schedule ID
--  ------  -----------
1   lunCG1  1
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                       |
|-------------|-------------------------------|
| ID          | Protection group ID.          |
| Name        | Protection group name.        |
| Schedule ID | Protection group schedule ID. |
