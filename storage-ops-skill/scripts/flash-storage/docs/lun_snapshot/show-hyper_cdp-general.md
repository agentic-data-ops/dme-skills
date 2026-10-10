# show hyper_cdp general


##### Function

The **show hyper_cdp general** command is used to query HyperCDP object information.

##### Format

**show hyper_cdp general** \[ cdp_id=? \] \[ cdp_name=? \] \[ source_lun_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_id=? | ID of a HyperCDP object. | The value is an integer ranging from 0 to 1999999. |
| cdp_name=? | Name of a HyperCDP object. | The value contains 1 to 31 characters including letters, digits, hyphens (-), underscores (_), and periods (.). |
| source_lun_id=? | Source LUN ID. | The value is an integer ranging from 0 to 65535.<br>To obtain the value, run the "show lun general" command. |

##### Usage Guidelines

-   Run "**show hyper_cdp general**" to query information about all HyperCDP objects.
-   Run "**show hyper_cdp general** source_lun_id=?" to query information about all HyperCDP objects of a specified source LUN.
-   Run "**show hyper_cdp general** cdp_id=?" or "**show hyper_cdp general** cdp_name=?" to query information about a specified HyperCDP object.

##### Example

Query information about all HyperCDP objects.

```text
admin:/>show hyper_cdp general
ID  Name              Source LUN ID  Source LUN Name  Running Status  Time Stamp
--  ----------------  -------------  ---------------  --------------  -----------------------------
0   cdp_10_0_1584946  10             lun0010          Activated       2018-09-14/12:40:19 UTC+08:00
1   cdp_10_1_1584951  10             lun0010          Activated       2018-09-14/12:40:19 UTC+08:00
2   cdp_0_0_7048381   0              lun0000          Activated       2018-09-14/09:38:04 UTC+08:00
```

Query information about all HyperCDP objects of source LUN "5".

```text
admin:/>show hyper_cdp general source_lun_id=5
ID Name Source LUN ID Source LUN Name Running Status Time Stamp
-- ---- ------------- --------------- -------------- -----------------------------
0  cdp1 5             lun5            Activated      2018-06-14/12:06:15 UTC+08:00
1  cdp2 5             lun5            Activated      2018-06-15/20:14:33 UTC+08:00
```

Query detailed information about HyperCDP object "1".

```text
admin:/>show hyper_cdp general cdp_id=1
ID                            : 1
Name                          : cdp1
Source LUN ID                 : 1
Source LUN Name               : LUN0001
Running Status                : Activated
Time Stamp                    : 2018-08-30/09:48:27 UTC+08:00
Restore Start Time            : --
Restore End Time              : --
Restore Speed                 : Middle
Restore Progress(%)           : --
Is Scheduled HyperCDP object  : No
HyperCDP consistency group ID : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                     | Meaning                                     |
|-------------------------------|---------------------------------------------|
| ID                            | ID of the HyperCDP object.                  |
| Name                          | Name of the HyperCDP object.                |
| Source LUN ID                 | Source LUN ID of the HyperCDP object.       |
| Source LUN Name               | Source LUN name of the HyperCDP object.     |
| Running Status                | Running status of the HyperCDP object.      |
| Time Stamp                    | Activation time of the HyperCDP object.     |
| Restore Start Time            | Rollback start time of the HyperCDP object. |
| Restore End Time              | Rollback end time of the HyperCDP object.   |
| Restore Speed                 | Rollback speed of the HyperCDP object.      |
| Restore Progress(%)           | Rollback progress (%).                      |
| Is Scheduled HyperCDP object  | Whether it is a timing HyperCDP object.     |
| HyperCDP consistency group ID | HyperCDP consistency group ID.              |
