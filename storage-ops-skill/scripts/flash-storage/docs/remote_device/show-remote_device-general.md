# show remote_device general


##### Function

The **show remote_device general** command is used to query information about a remote device.

##### Format

**show remote_device general** \[ scope=? \] \[ remote_device_id=? \] \[ array_type=? \] \[ show_details=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_device_id=? | Remote device ID. | To obtain the value, run "show remote device general" without parameters. |
| scope=? | Query scope. | The value can be "linked_array" or "all", where: <br>"linked_array": The remote devices that have been connected to the storage system will be queried for.<br>"all": Any created remote devices will be queried for no matter those devices have connected to the storage system or not. |
| array_type=? | Remote device type. | The value can be "replication" or "heterogeneity", where: <br>"replication": The remote device is made by Huawei.<br>"heterogeneity": The remote device is made by a third-party manufacturer. |
| show_details | Whether to display port group details. | The value can be "yes" or "no", where: <br>"yes": Port group details are displayed.<br>"no": Port group details are not displayed. |

##### Usage Guidelines

-   The following parameters or parameter sets are mutually exclusive: "scope", "remote_device_id", and "array_type".
-   Run the "**show remote_device general**" command to query information about all remote devices.
-   Run the "**show remote_device general** remote_device_id=?" command to query information about a specified remote device.
-   Run the "**show remote_device general** scope=?" command to query information about remote devices in a specified scope.
-   Run the "**show remote_device general** array_type=?" command to query information about remote devices with a specified type.

##### Example

Query information about the remote device whose ID is "0".

```text
admin:/>show remote_device general remote_device_id=0
ID                   : 0
Name                 : B
Health Status        : Normal
Running Status       : Link Up
WWN                  : 2100ff0000040506
SN                   : ST000000000000000227
Device Type          : Replication
Remote Device Type   : --
Vendor               : huawei
FC Link Number       : 0
ISCSI Link Number    : 0
Compress Algorithm   : deep
Compress Judge       : No
Compress Algvalid    : Yes
Remote Port Group ID : 0
Local Port Group ID  : 0
Remote User Name     : huawei
Bandwidth Switch     : Off
Bandwidth Value      : 0.000B
IP Link Number       : 4
Device Series        : Identical Device
```

Query detailed information about the remote device whose ID is "0".

```text
admin:/>show remote_device general remote_device_id=0 show_details=yes
ID                   : 0
Name                 : B
Health Status        : Normal
Running Status       : Link Up
WWN                  : 2100ff0000040506
SN                   : ST000000000000000227
Device Type          : Replication
Remote Device Type   : --
Vendor               : huawei
FC Link Number       : 0
ISCSI Link Number    : 0
Compress Algorithm   : deep
Compress Judge       : No
Compress Algvalid    : Yes
Remote Port Group ID : 0
Local Port Group ID  : 0
Remote User Name     : huawei
Bandwidth Switch     : Off
Bandwidth Value      : 0.000B
IP Link Number       : 4
Device Series        : Identical Device
Local FC port:

ID          Health Status  Running Status  Type       Working Rate(Mbps)  WWN               Working Mode  Configured Mode  Enabled  Max Speed(Mbps)  Number Of Initiators
----------  -------------  --------------  ---------  ------------------  ----------------  ------------  ---------------  -------  ---------------  --------------------
CTE0.A5.P1  Normal         Link Up         Host Port  16000               24091022a2b1d322  INI and TGT   Point To Point   Yes      32000            0
CTE0.B6.P1  Normal         Link Up         Host Port  16000               26111022a2b1d322  INI and TGT   Point To Point   Yes      32000            0

Local ETH port:
Logical Port Name  Running Status  IPv4 Address   IPv6 Address  Home Port Type  Home Port ID    Current Port Type  Current Port ID  Work Controller ID  vStore ID
-----------------  --------------  -------------  ------------  --------------  --------------  -----------------  ---------------  ------------------  ---------
9Pxm               Link Up         129.46.110.62  --            ETH CTE0.A3.P0  ETH CTE0.A3.P0  0A                 --
3MR9               Link Up         129.46.110.63  --            ETH CTE0.B3.P1  ETH CTE0.B3.P1  0B                 --

Remote FC port:
ID Health   Status  Running Status  Type       Working Rate(Mbps)  WWN               Working  Mode  Configured Mode  Enabled Max  Speed(Mbps)  Number Of Initiators
----------  ------  --------------  ---------  ---------           ----------------  -------------  ---------------  -----------  -----------  --------------------
CTE0.A5.P1  Normal  Link Up         Host Port  16000               24091022a2b1d322  INI and TGT    Point To Point   Yes          32000        0
CTE0.B6.P1  Normal  Link Up         Host Port  16000               26111022a2b1d322  INI and TGT    Point To Point   Yes          32000        0

Remote ETH port:
Logical Port Name  Running Status  IPv4 Address   IPv6 Address  Home Port Type  Home Port ID  Current Port Type  Current Port ID  Work Controller ID  vStore ID
-----------------  --------------  -------------  ------------  --------------  ------------  -----------------  ---------------  ------------------  ---------
9Pxm               Link Up         129.46.110.62  --            ETH             CTE0.A3.P0    ETH                CTE0.A3.P0       0A                  --
3MR9               Link Up         129.46.110.63  --            ETH             CTE0.B3.P1    ETH                CTE0.B3.P1       0B                  --
```

Query information about all remote devices.

```text
admin:/>show remote_device general
ID  Name  Health Status  Running Status  WWN               SN                    Device Type  Remote Device Type  Remote Port Group ID  Local Port Group ID  IP Link Number
--  ----  -------------  --------------  ----------------  --------------------  -----------  ------------------  --------------------  -------------------  --------------
0   B     Normal         Link Up         2100ff0000040506  ST000000000000000227  Replication  --                  0                     0                    4
1   C     Normal         Link Up         2100ad0000040506  ST000000000000000136  Replication  --                  0                     0                    4
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                                                                                                              |
|----------------------|----------------------------------------------------------------------------------------------------------------------|
| ID                   | Remote device ID.                                                                                                    |
| Name                 | Remote device name.                                                                                                  |
| Health Status        | Health state of the remote device.                                                                                   |
| Running Status       | Running state of the remote device.                                                                                  |
| Bandwidth Switch     | Whether to enable or disable bandwidth control.                                                                      |
| Bandwidth Value      | Bandwidth of the remote device (upper limit of the sending bandwidth of background I/Os on the local storage array). |
| WWN                  | World wide name (WWN) of the remote device.                                                                          |
| SN                   | Remote device SN.                                                                                                    |
| Device Type          | Remote device type.                                                                                                  |
| Remote Port Group ID | Remote port group ID.                                                                                                |
| Local Port Group ID  | Local port group ID.                                                                                                 |
| Remote Device Type   | Remote device model.                                                                                                 |
| Vendor               | Vendor of the remote device.                                                                                         |
| FC Link Number       | Number of Fibre Channel links on the remote device.                                                                  |
| ISCSI Link Number    | Number of iSCSI links on the remote device.                                                                          |
| Compress Algorithm   | Compression algorithm used between storage arrays.                                                                   |
| Compress Judge       | Whether compression for data transmission between storage arrays is enabled.                                         |
| Compress Algvalid    | Whether the compression algorithm takes effect.                                                                      |
| Remote User Name     | User name for logging in to the remote device.                                                                       |
| Device Series        | Remote device series.                                                                                                |
