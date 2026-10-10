# show hyper_cdp_schedule fs


##### Function

The **show hyper_cdp_schedule fs** command is used to query information about file systems in a HyperCDP schedule.

##### Format

**show hyper_cdp_schedule fs** schedule_id=?

##### Parameters

| Parameter   | Description           | Value                                                       |
|-------------|-----------------------|-------------------------------------------------------------|
| schedule_id | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". |

##### Usage Guidelines

None

##### Example

Query file systems added to the HyperCDP schedule whose ID is "1".

```text
admin:/>show hyper_cdp_schedule fs schedule_id=1
ID  Name  Storage Pool ID  Capacity  Health Status  Running Status
--  ----  ---------------  --------  -------------  --------------
1   fs1   0                32.000TB  Normal         Online
30  fs2   0                32.000TB  Normal         Online
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning               |
|-------------|-----------------------|
| schedule_id | HyperCDP schedule ID. |
