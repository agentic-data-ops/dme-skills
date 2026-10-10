# show remote_device link


##### Function

The **show remote_device link** command is used to query information about existing links to a storage system.

##### Format

**show remote_device link** \[ link_type=? \[ link_id=? \] \| remote_device_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| link_type=? | Type of a link. | The value can be "FC", "IP", or "iSCSI", where: <br>"FC": Remote and local devices are connected through FC links.<br>"IP": Remote and local devices are connected through IP links.<br>"iSCSI": Remote and local devices are connected through iSCSI links. |
| link_id=? | ID of a link. | To obtain the value, run "show remote_device link" without parameters. |
| remote_device_id=? | ID of a remote device. | To obtain the value, run "show remote_device general". |

##### Usage Guidelines

-   Run "**show remote_device link**" to query information about all links to the storage system.
-   Run "**show remote_device link** link_type=? link_id=?" to query information about a specified link.
-   Run "**show remote_device link** remote_device_id=?" to query information about links to a specified remote device.

##### Example

Query information about the links, where the link type is "FC" and the remote device ID is "0".

```text
admin:/>show remote_device link link_type=FC remote_device_id=0
ID     Health Status  Running Status  Local Controller  Remote Device Type  In Remote Device  Remote Device ID  Remote Device WWN  Remote Controller   Local Port ID      Remote Port ID     Remote Device Name
-----  -------------  --------------  ----------------  ------------------  ----------------  ----------------  -----------------  ------------------  -----------------  -----------------  ------------------
0      Normal         Link Up         0A                Replication         No                --                21001233234e556d   0A                  CTE0.A.H0          CTE0.A1.P0         Huawei Storage
```

Query information about the link, where the link type is "FC" and the link ID is "0".

```text
admin:/>show remote_device link link_type=FC link_id=0
ID : 0
Health Status : Normal
Running Status : Link Up
Local Controller : 0A
Remote Device Type : Replication
In Remote Device : No
Remote Device ID : --
Local Port ID : CTE0.A.H0
Local Port WWPN : 20803400a3e2690f
Remote Device Name : Huawei Storage
Remote Device WWN : 210030d17eb33e32
Remote Controller : 0A
Remote Port ID : CTE0.A1.P0
Remote Port WWPN : 200830d17eb33e32
Fast Write Enable : No
```

Query information about the link, where the link type is "IP" and the link ID is "0".

```text
admin:/>show remote_device link link_type=IP link_id=0
ID : 0
Health Status : Normal
Running Status : Link Up
Local Controller : 0A
Remote Device Type : Replication
In Remote Device : No
Remote Device ID : --
Local ETH Logical Port : A2P0
Local IP : 200.47.61.8
Remote Device Name : Huawei Storage
Remote Device WWN : 210030d17eb33e32
Remote Controller : 0A
Remote ETH Logical Port: B2P1
Remote IP : 200.47.61.12
Fast Write Enable : Yes
```

Query information about the links, where the link type is "IP" and the remote device ID is "0".

```text
admin:/>show remote_device link link_type=IP remote_device_id=0
ID     Health Status  Running Status  Local Controller  Remote Device Type  In Remote Device  Remote Device ID  Local IP           Remote Device Name  Remote Device WWN  Remote Controller  Remote IP
-----  -------------  --------------  ----------------  ------------------  ----------------  ----------------  -----------------  ------------------  -----------------  -----------------  ------------------
65536  Normal         Link Up         0B                Replication         Yes               0                 8.47.41.75         Huawei.Storage      210004bd70e378ff   0B                 8.47.41.143
```

Query information about the link, where the link type is "iSCSI" and the link ID is "0".

```text
admin:/>show remote_device link link_type=iSCSI link_id=0
ID : 0
Health Status : Normal
Running Status : Link Up
Local Controller : 0A
Remote Device Type : Replication
In Remote Device : No
Remote Device ID : --
Local ETH Logical Port : A2P0
Local IP : 200.47.61.8
Remote Device Name : Huawei Storage
Remote Device WWN : 210030d17eb33e32
Remote Controller : 0A
Remote ETH Logical Port: B2P1
Remote IP : 200.47.61.12
Fast Write Enable : Yes
```

Query information about the links, where the link type is "iSCSI" and the remote device ID is "0".

```text
admin:/>show remote_device link link_type=iSCSI remote_device_id=0
ID     Health Status  Running Status  Local Controller  Remote Device Type  In Remote Device  Remote Device ID  Local IP           Remote Device Name  Remote Device WWN  Remote Controller  Remote IP
-----  -------------  --------------  ----------------  ------------------  ----------------  ----------------  -----------------  ------------------  -----------------  -----------------  ------------------
65537  Normal         Link Up         0B                Replication         Yes               0                 129.46.9.87        Huawei.Storage      21007cc3855e802c   0B                 129.46.9.85
```

Query information about all links.

```text
admin:/>show remote_device link
FC Link:

ID     Health Status  Running Status  Local Controller  Remote Device Type  In Remote Device  Remote Device ID  Remote Device WWN  Remote Controller   Local Port ID      Remote Port ID     Remote Device Name
-----  -------------  --------------  ----------------  ------------------  ----------------  ----------------  -----------------  ------------------  -----------------  -----------------  ------------------
0      Normal         Link Up         0A                Replication         No                --                21001233234e556d   0A                  CTE0.A.H0          CTE0.A1.P0         Huawei Storage
IP Link

ID     Health Status  Running Status  Local Controller  Remote Device Type  In Remote Device  Remote Device ID  Local IP           Remote Device Name  Remote Device WWN  Remote Controller  Remote IP
-----  -------------  --------------  ----------------  ------------------  ----------------  ----------------  -----------------  ------------------  -----------------  -----------------  ------------------
65536  Normal         Link Up         0B                Replication         Yes               0                 8.47.41.75         Huawei.Storage      210004bd70e378ff   0B                 8.47.41.143
iSCSI Link:

ID     Health Status  Running Status  Local Controller  Remote Device Type  In Remote Device  Remote Device ID  Local IP           Remote Device Name  Remote Device WWN  Remote Controller  Remote IP
-----  -------------  --------------  ----------------  ------------------  ----------------  ----------------  -----------------  ------------------  -----------------  -----------------  ------------------
65537  Normal         Link Up         0B                Replication         Yes               0                 129.46.9.87        Huawei.Storage      21007cc3855e802c   0B                 129.46.9.85

```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                                         |
|--------------------|-------------------------------------------------|
| ID                 | ID of a link.                                   |
| Health Status      | Health status of a link.                        |
| Running Status     | Running status of a link.                       |
| Local Controller   | Local controller where a link resides.          |
| Remote Device Type | Remote device type.                             |
| In Remote Device   | Whether a link is added to a remote device.     |
| Remote Device ID   | Remote device ID.                               |
| Local Port ID      | Local port ID.                                  |
| Local Port WWPN    | Local port WWPN.                                |
| Remote Device Name | Remote device name.                             |
| Remote Device WWN  | Remote device WWN.                              |
| Remote Controller  | Remote controller.                              |
| Remote Port ID     | Remote port ID.                                 |
| Remote Port WWPN   | Remote port WWPN.                               |
| Remote IP          | Remote IP address.                              |
| Local IP           | Local IP address.                               |
| Fast Write Enable  | Whether FastWrite is supported (Fibre Channel). |
| Chap Enabled       | Whether CHAP is enabled.                        |
| Chap User          | CHAP user name.                                 |
