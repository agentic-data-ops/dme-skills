# show hyper_cdp_schedule lun


##### Function

The **show hyper_cdp_schedule lun** command is used to query information about LUNs in a HyperCDP schedule.

##### Format

**show hyper_cdp_schedule lun** { schedule_id=? \| schedule_name=? }

##### Parameters

| Parameter       | Description                  | Value                                                                                              |
|-----------------|------------------------------|----------------------------------------------------------------------------------------------------|
| schedule_id=?   | HyperCDP schedule ID.        | To obtain the value, run "show hyper_cdp_schedule general". The value is an integer from 1 to 512. |
| schedule_name=? | Name of a HyperCDP schedule. | You can run the show hyper_cdp_schedule general command to obtain the value.                       |

##### Usage Guidelines

Before performing the operation, confirm that the schedule ID is correct and exits.

##### Example

Query information about LUNs in HyperCDP schedule "1".

```text
admin:/>show hyper_cdp_schedule lun schedule_id=1

ID  Name         Pool ID  Capacity    Health Status   Running Status  Type   WWN
--  -----------  -------  ----------  -------------   --------------  -----  --------------------------------
0   testlun0000  0        2.000GB     Normal          Online          Thin   6010203100040506000b780900000000
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning          |
|----------------|------------------|
| ID             | LUN ID.          |
| Name           | LUN name.        |
| Pool ID        | Storage pool ID. |
| Capacity       | Total capacity.  |
| Health Status  | Health status.   |
| Running Status | Running status.  |
| Type           | LUN type.        |
| WWN            | World Wide Name. |
