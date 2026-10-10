# show hyper_cdp_consistency_group cdp


##### Function

The **show hyper_cdp_consistency_group cdp** command is used to query information about HyperCDP objects in a HyperCDP consistency group.

##### Format

**show hyper_cdp_consistency_group cdp** cdp_consistency_group_id=?

##### Parameters

| Parameter                  | Description                         | Value                                            |
|----------------------------|-------------------------------------|--------------------------------------------------|
| cdp_consistency_group_id=? | ID of a HyperCDP consistency group. | The value is an integer ranging from 0 to 99999. |

##### Usage Guidelines

None

##### Example

Query information about HyperCDP objects in HyperCDP consistency group "1".

```text
admin:/>show hyper_cdp_consistency_group cdp cdp_consistency_group_id=1
ID   Name                          Source LUN ID  Source LUN Name  Running Status  Time Stamp
---  ----------------------------  -------------  ---------------  --------------  -----------------------------
100  lun00001_1808210306260000100  1              lun00001         Activated       2018-08-21/11:06:26 UTC+08:00
101  lun00002_1808210306260000101  2              lun00002         Activated       2018-08-21/11:06:26 UTC+08:00
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                               |
|-----------------|---------------------------------------|
| ID              | ID of a HyperCDP object.              |
| Name            | Name of a HyperCDP object.            |
| Source LUN ID   | Source LUN ID of a HyperCDP object.   |
| Source LUN Name | Source LUN name of a HyperCDP object. |
| Running Status  | Running status of a HyperCDP object.  |
| Time Stamp      | Activation time of a HyperCDP object. |
