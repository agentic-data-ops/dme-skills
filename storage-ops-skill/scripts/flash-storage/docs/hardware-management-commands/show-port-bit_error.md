# show port bit_error


##### Function

The **show port bit_error** command is used to query port bit errors.

##### Format

**show port bit_error** \[ physical_type=? \] \[ port_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| port_id=? | ID of a port. | To obtain the value, run "show port general" without parameters. |
| physical_type=? | Physical port type. | The value can be "FC", "ETH", "SAS", or "PCIE", where: <br>"FC": Fibre Channel ports.<br>"ETH": Ethernet ports (including iSCSI host ports and management network ports).<br>"SAS": SAS ports.<br>"PCIE": PCIe ports.<br>"RDMA": RDMA ports.<br>"RoCE": RoCE ports. |

##### Usage Guidelines

-   Run "**show port bit_error**" to query bit errors of all ports.
-   Run "**show port bit_error** physical_type=? port_id=?" to query bit errors of a specified port.

##### Example

Query port bit errors.

```text

admin:/>show port bit_error
ETH port:

ID                  Error Packets  Lost Packets  Over Flowed Packets  Start Time                     CRC Errors  Frame Errors  Frame Length Errors
------------------  -------------  ------------  -------------------  -----------------------------  ----------  ------------  -------------------
CTE0.A.P2           0              0             0                    2020-07-17/11:33:57 UTC+08:00  0           0             0
CTE0.A.P3           0              0             0                    2020-07-17/11:33:57 UTC+08:00  0           0             0
CTE0.A.P4           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.A.P5           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.A.P6           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.A.P7           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.A.P8           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.A.P9           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.B.P2           0              0             0                    2020-07-17/11:33:57 UTC+08:00  0           0             0
CTE0.B.P3           0              0             0                    2020-07-17/11:33:57 UTC+08:00  0           0             0
CTE0.B.P4           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.B.P5           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.B.P6           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.B.P7           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.B.P8           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.B.P9           0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.A.MGMT         0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.B.MGMT         0              0             0                    2020-07-17/11:33:53 UTC+08:00  0           0             0
CTE0.A.MAINTENANCE  0              0             0                    2020-07-17/11:33:55 UTC+08:00  0           0             0
CTE0.B.MAINTENANCE  0              0             0                    2020-07-17/11:33:55 UTC+08:00  0           0             0
FC port:
SAS port:
ID         Invalid Dword  Consist Errors  Loss Of DWORD  PHY Reset Errors  Start Time
---------  -------------  --------------  -------------  ----------------  -----------------------------
CTE0.A.P0  0              0               0              0                 2020-07-17/11:33:53 UTC+08:00
CTE0.A.P1  0              0               0              0                 2020-07-17/11:33:53 UTC+08:00
CTE0.B.P0  0              0               0              0                 2020-07-17/11:33:53 UTC+08:00
CTE0.B.P1  0              0               0              0                 2020-07-17/11:33:53 UTC+08:00
FCoE port:
PCIE port:
RDMA port:
RoCE port:

```

Query bit errors of the port whose ID is "CTE0.A.P0". The ID varies depending on a specific product.

```text

admin:/>show port bit_error physical_type=SAS port_id=CTE0.A.P0

ID               : CTE0.A.P0
Invalid Dword    : 0
Consist Errors   : 0
Loss Of DWORD    : 0
PHY Reset Errors : 0
Start Time       : 2020-07-17/11:33:53 UTC+08:00

```

Query bit errors of the ETH port whose ID is "CTE0.A.P2". The ID varies depending on a specific product.

```text

admin:/>show port bit_error physical_type=ETH port_id=CTE0.A.P2

ID                  : CTE0.A.P2
Error Packets       : 0
Lost Packets        : 0
Over Flowed Packets : 0
Start Time          : 2020-07-17/11:33:57 UTC+08:00
CRC Errors          : 0
Frame Errors        : 0
Frame Length Errors : 0

```

##### System Response

The following table describes the parameter meanings.

| Parameter             | Meaning                                 |
|-----------------------|-----------------------------------------|
| ID                    | Port ID.                                |
| Error Packets         | Error packets number.                   |
| Over Flowed Packets   | Over flowed packets number.             |
| Lost Packets          | Lost packets number.                    |
| Start Time            | Start Time.                             |
| CRC Errors            | Cyclic redundancy check errors.         |
| Frame Errors          | Frame errors.                           |
| Frame Length Errors   | Frame length errors.                    |
| Frame End Sign Errors | Frame end sign errors.                  |
| Lost Signals          | Lost signals.                           |
| Lost Synchronizations | Lost synchronizations.                  |
| Replay Timer Timeout  | Times that replay timer timeout occurs. |
| Rollover              | Replay timer rollover times.            |
