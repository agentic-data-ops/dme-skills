# show hyper_cdp_consistency_group general


##### Function

The **show hyper_cdp_consistency_group general** command is used to query information about a HyperCDP consistency group.

##### Format

**show hyper_cdp_consistency_group general** \[ cdp_consistency_group_id=? \] \[ cdp_consistency_group_name=? \] \[ source_lun_consistency_group_id=? \]

##### Parameters

| Parameter                         | Description                           | Value                                                                                                            |
|-----------------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------|
| cdp_consistency_group_id=?        | ID of a HyperCDP consistency group.   | The value is an integer ranging from 0 to 99999.                                                                 |
| cdp_consistency_group_name=?      | Name of a HyperCDP consistency group. | The value contains 1 to 31 characters including letters, digits, hyphens (-), underscores (\_), and periods (.). |
| source_lun_consistency_group_id=? | Source LUN consistency group ID.      | The value ranges from 0 to 16383.                                                                                |

##### Usage Guidelines

-   Run "**show hyper_cdp_consistency_group general**" to query information about all HyperCDP consistency groups.
-   Run "**show hyper_cdp_consistency_group general** source_lun_consistency_group_id=?" to query information about all HyperCDP consistency groups of a specified source LUN consistency group.
-   Run "**show hyper_cdp_consistency_group general** cdp_consistency_group_id=?" or "**show hyper_cdp_consistency_group general** cdp_consistency_group_name=?" to query information about a specified HyperCDP consistency group.

##### Example

Query information about all HyperCDP consistency groups.

```text
admin:/>show hyper_cdp_consistency_group general

ID  Name   Source LUN consistency group ID  Source LUN consistency group Name  Running Status  Time Stamp
--  -----  -------------------------------  ---------------------------------  --------------  -----------------------------
1   cdpcg  1                                pg                                 Activated       2020-07-05/16:01:28 UTC+08:00
```

Query detailed information about the HyperCDP consistency group whose ID is "1".

```text
admin:/>show hyper_cdp_consistency_group general cdp_consistency_group_id=1
ID                                      : 1
Name                                    : cdp_group_1
Source LUN consistency group ID         : 1
Source LUN consistency group name       : lun_group
Running Status                          : Activated
Time Stamp                              : 2018-01-24/12:06:15 UTC+08:00
Restore Speed                           : High
Is Scheduled HyperCDP consistency group : Yes
```

Query information about the HyperCDP consistency group of a LUN consistency group.

```text
admin:/>show hyper_cdp_consistency_group general source_lun_consistency_group_id=1

ID  Name   Source LUN consistency group ID  Source LUN consistency group Name  Running Status  Time Stamp
--  -----  -------------------------------  ---------------------------------  --------------  -----------------------------
1   cdpcg  1                                pg                                 Activated       2020-07-05/16:01:28 UTC+08:00
```

##### System Response

The following table describes the parameter meanings.

| Parameter                               | Meaning                                                              |
|-----------------------------------------|----------------------------------------------------------------------|
| ID                                      | ID of the HyperCDP consistency group.                                |
| Name                                    | Name of the HyperCDP consistency group.                              |
| Source LUN consistency group ID         | Source LUN consistency group ID of the HyperCDP consistency group.   |
| Source LUN consistency group Name       | Source LUN consistency group name of the HyperCDP consistency group. |
| Running Status                          | Running status of the HyperCDP consistency group.                    |
| Time Stamp                              | Activation time of the HyperCDP consistency group.                   |
| Restore Speed                           | Rollback speed of the HyperCDP consistency group.                    |
| Is Scheduled HyperCDP consistency group | Whether the HyperCDP consistency group is a scheduled one.           |
