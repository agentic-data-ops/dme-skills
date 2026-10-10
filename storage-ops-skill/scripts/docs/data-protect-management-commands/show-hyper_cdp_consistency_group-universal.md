# show hyper_cdp_consistency_group universal


##### Function

The **show hyper_cdp_consistency_group universal** command is used to query information about a HyperCDP consistency group.

##### Format

**show hyper_cdp_consistency_group universal** \[ cdp_consistency_group_id=? \] \[ cdp_consistency_group_name=? \] \[ protect_group_id=? \]

##### Parameters

| Parameter                    | Description                           | Value                                                                                                            |
|------------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------|
| cdp_consistency_group_id=?   | ID of a HyperCDP consistency group.   | The value is an integer ranging from 0 to 99999.                                                                 |
| cdp_consistency_group_name=? | Name of a HyperCDP consistency group. | The value contains 1 to 31 characters including letters, digits, hyphens (-), underscores (\_), and periods (.). |
| protect_group_id=?           | Protection group ID.                  | The value ranges from 0 to 16383.                                                                                |

##### Usage Guidelines

-   Run "**show hyper_cdp_consistency_group universal**" to query information about all HyperCDP consistency groups.
-   Run "**show hyper_cdp_consistency_group universal** protect_group_id=?" to query information about all HyperCDP consistency groups of a specified source protection group.
-   Run "**show hyper_cdp_consistency_group universal** cdp_consistency_group_id=?" or "**show hyper_cdp_consistency_group universal** cdp_consistency_group_name=?" to query information about a specified HyperCDP consistency group.

##### Example

Query information about all HyperCDP consistency groups.

```text
admin:/>show hyper_cdp_consistency_group universal

ID  Name   Source Group ID  Source Group Name  Source Group Type  Running Status  Time Stamp
--  -----  ---------------  -----------------  -----------------  --------------  -----------------------------
1   cdpcg  1                pg                 --                 Activated       2020-07-05/16:01:28 UTC+08:00
```

Query detailed information about the HyperCDP consistency group whose ID is "1".

```text
admin:/>show hyper_cdp_consistency_group universal cdp_consistency_group_id=1
ID                                      : 1
Name                                    : cdp_group_1
Source Group ID                         : 1
Source Group Name                       : lun_group
Source Group Type                       : Protect group
Running Status                          : Activated
Time Stamp                              : 2018-01-24/12:06:15 UTC+08:00
Restore Speed                           : High
Is Scheduled HyperCDP Consistency Group : Yes
```

Query information about the HyperCDP consistency group of a protection group.

```text
admin:/>show hyper_cdp_consistency_group universal protect_group_id=1

ID  Name   Source Group ID  Source Group Name  Source Group Type  Running Status  Time Stamp
--  -----  ---------------  -----------------  -----------------  --------------  -----------------------------
1   cdpcg  1                pg                 --                 Activated       2020-07-05/16:01:28 UTC+08:00
```

##### System Response

The following table describes the parameter meanings.

| Parameter                               | Meaning                                                    |
|-----------------------------------------|------------------------------------------------------------|
| ID                                      | ID of the HyperCDP consistency group.                      |
| Name                                    | Name of the HyperCDP consistency group.                    |
| Source Group ID                         | Source group ID of the HyperCDP consistency group.         |
| Source Group Name                       | Source group name of the HyperCDP consistency group.       |
| Source Group Type                       | Source group type of the HyperCDP consistency group.       |
| Running Status                          | Running status of the HyperCDP consistency group.          |
| Time Stamp                              | Activation time of the HyperCDP consistency group.         |
| Restore Speed                           | Rollback speed of the HyperCDP consistency group.          |
| Is Scheduled HyperCDP Consistency Group | Whether the HyperCDP consistency group is a scheduled one. |
