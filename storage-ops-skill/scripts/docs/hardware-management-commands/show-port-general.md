# show port general


##### Function

The **show port general** command is used to query ports on the storage system.

##### Format

**show port general** \[ port_id=? \]

**show port general** \[ physical_type=? \| logic_type=? \| running_status=? \] \*

**show port general** { failover_group_id=? \| failover_group_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| port_id=? | ID of a port. If this parameter is specified, neither physical_type=? nor logic_type=? can be specified. | To obtain the value, run "show port general" without parameters. |
| logic_type=? | Logical port type. | The value can be "Host_Port", "Expansion_Port", "Management_Port", or "Maintenance_Port", where: <br>"Host_Port": indicates host ports.<br>"Expansion_Port": indicates expansion ports.<br>"Management_Port": indicates management ports.<br>"Maintenance_Port": indicates maintenance ports.<br>"Container_Front_End_Port": indicates container front end port.<br>"Container_Back_End_Port": indicates container back end port. |
| physical_type=? | Physical port type. | The value can be "FC", "ETH", "SAS", "COM", "PCIE", "RDMA" or "RoCE", where: <br>"FC": indicates Fibre Channel ports.<br>"ETH": indicates Ethernet ports (including iSCSI host ports and management network ports).<br>"SAS": indicates SAS ports.<br>"COM": indicates serial ports.<br>"PCIE": indicates PCIe ports.<br>"RDMA": indicates RDMA ports.<br>"RoCE": indicates RoCE ports. |
| running_status=? | Running status of a port. | The value can be "link_up" or "link_down", where: <br>"link_up": The port is linked.<br>"link_down": The port link is down. |
| failover_group_id=? | ID of the failover group. | The value must be an integer from 0 to 8191. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |

##### Usage Guidelines

-   To query all ports, run "**show port general**".
-   To query a specific port, run "**show port general** port_id=?".
-   To query ports of a specific type, run "**show port general** physical_type=?", "**show port general** logic_type=?", or "**show port general** physical_type=? logic_type=?".
-   To query details on ports of a specific type, run "**show port general** physical_type=?", "**show port general** logic_type=?", "**show port general** running_status=?", "**show port general** physical_type=? logic_type=?", "**show port general** physical_type=? running_status=?", "**show port general** logic_type=? running_status=?", or "**show port general** physical_type=? logic_type=? running_status=?".
-   To query Ethernet ports in a specified failover group, run "**show port general** failover_group_id=?". Fibre Channel ports in a failover group cannot be queried.

 

If you use a maintenance terminal to log in to the storage system through a serial port and find that "Running Status" of the queried serial port is "Link Down", ignore the status.

"port_id" is mutually exclusive with "logic_type" and "physical_type". "failover_group_id" is mutually exclusive with "physical_type", "logic_type", and "port_id".

##### Example

Query Fibre Channel port "CTE0.A3.P0". The ID and output vary depending on a specific product.

```text
admin:/>show port general port_id=CTE0.A3.P0
FC port:
ID                         : CTE0.A3.P0
Health Status              : Normal
Running Status             : Link Down
Type                       : Host Port
Working Rate(Mbps)         : --
Configured Speed(Mbps)     : Auto-Adapt
WWN                        : 22083400a3dc1a51
Role                       : INI and TGT
SFP Status                 : Offline
Working Mode               : --
Configured Mode            : --
Flogin Delay Times(ms)     : 0
Lost Signals               : 0
Link Errors Codes          : 0
Lost Synchronizations      : 0
Failed Connections         : 0
Start Time                 : 2015-01-04/09:20:41 UTC+08:00
Fast Write Supported       : Yes
Fast Write Enable          : Yes
Fast Write Burst Len(Byte) : 8192
Enabled                    : Yes
Max Speed(Mbps)            : --
CRC Errors                 : 0
Frame End Sign Errors      : 0
Number Of Initiators       : 0
FC MOR State               : Open
Protocol                   : FC-SCSI
```

Query port "CTE0.B.IOM0.P1". The ID and output vary depending on a specific product.

```text
admin:/>show port general port_id=CTE0.B.IOM0.P1
ETH port:
---------------  Host Port:----------------
ID                  : CTE0.B.IOM0.P1
Health Status       : Normal
Running Status      : Link Down
Type                : Host Port
IPv4 Address        : --
Subnet Mask         : --
IPv4 Gateway        : --
IPv6 Address        : --
IPv6 Prefix Length  : --
IPv6 Gateway        :
MAC                 : c4:47:3f:1b:87:2e
Role                : INI and TGT
Mode                : --
MTU                 : 1500
Working Rate(Mbps)  : --
Bond Name           :
iSCSI Port          : 0
iSCSI Name          :
Error Packets       : 0
Lost Packets        : 0
Over Flowed Packets : 0
Start Time          : 2017-11-23/16:52:17 UTC+08:00
Enabled             : Yes
Max Speed(Mbps)     : 10000
CRC Errors          : 0
Frame Errors        : 0
Frame Length Errors : 0
Total Received Packets           : 0
Total Transmitted Packets        : 0
Total Received Bytes             : 0.000B
Total Transmitted Bytes          : 0.000B
Received Packets Per Second      : 0
Transmitted Packets Per Second   : 0
Received Bytes Per Second        : 0.000B
Transmitted Bytes Per Second     : 0.000B
Number Of Initiators: 0
Work Mode           : 25GE_NOFEC
```

Query information about the port whose type is "COM". The ID and output vary depending on a specific product.

```text
admin:/>show port general physical_type=COM
ID                Health Status  Running Status  Type
----------------  -------------  --------------  ---------------
CTE0.SMM0.SERIAL  Normal         Link Up         Management Port
CTE0.SMM1.SERIAL  Normal         Link Up         Management Port
```

Query SAS port "CTE0.A0.P0". The ID and output vary depending on a specific product.

```text
admin:/>show port general port_id=CTE0.A0.P0
SAS port:
ID                 : CTE0.A0.P0
Health Status      : Normal
Running Status     : Link Up
Type               : Expansion Port
Working Rate(Mbps) : 12000
WWN                : 50022a1060708001
Role               : INI
Invalid Dword      : 2
Consist Errors     : 2
Loss Of DWORD      : 0
PHY Reset Errors   : 1
Start Time         : 2018-05-26/10:28:31 UTC+08:00
Enabled            : Yes
Max Speed(Mbps)    : 12000
Channel Number     : 4
```

Query COM port "CTE0.SMM0.SERIAL". The ID and output vary depending on a specific product.

```text
admin:/>show port general port_id=CTE0.SMM0.SERIAL
COM port:
ID             : CTE0.SMM0.SERIAL
Health Status  : Normal
Running Status : Link Up
Type           : Management Port
```

Query PCIe port "CTE0.B3.P1". The ID and output vary depending on a specific product.

```text
admin:/>show port general port_id=CTE0.B3.P1
PCIE port:
ID                   : CTE0.B3.P1
Health Status        : Normal
Running Status       : Link Down
PCIE Speed(Mbit/s)   : --
Current Peer Port Id : 4294967295
Suggest Peer Port Id : 4294967295
Lost Signals         : 0
ECRC Error           : 0
Bad Tlp              : 0
Bad Dllp             : 0
Recv Error           : 0
Chip Ecc Error       : 0
Start Time           : 2018-05-28/09:54:52 UTC+08:00
Max Speed(Mbps)      : 8000
Replay Timer Timeout : 0
Rollover             : 0
Model                : 4*5Gb PCIe Port
```

Query Ethernet ports in the failover group whose ID is 0.

```text
admin:/>show port general failover_group_id=0
ID             Health Status Running Status Type      IPv4 Address IPv6 Address MAC               Working Rate(Mbps)
-------------- ------------- -------------- --------- ------------ ------------ ----------------- ------------------
CTE0.IOM.H1.P0 Normal        Link Up        Host Port --           --           80:fb:06:df:d1:71 1000
CTE0.IOM.H1.P1 Normal        Link Down      Host Port --           --           80:fb:06:df:d1:70 --
CTE0.IOM.H1.P2 Normal        Link Down      Host Port --           --           80:fb:06:df:d1:6f --
CTE0.IOM.H1.P3 Normal        Link Down      Host Port --           --           80:fb:06:df:d1:6e --
CTE0.IOM.L1.P0 Normal        Link Down      Host Port --           --           78:1d:ba:cb:1d:cc --
CTE0.IOM.L1.P1 Normal        Link Down      Host Port --           --           78:1d:ba:cb:1d:cd --
CTE0.IOM.L1.P2 Normal        Link Down      Host Port --           --           20:0b:c7:3e:82:1a --
CTE0.IOM.L1.P3 Normal        Link Down      Host Port --           --           20:0b:c7:3e:82:19 --
```

Query Ethernet ports in the failover group whose name is System-defined.

```text
admin:/>show port general failover_group_name=System-defined
ID              Health Status  Running Status  Type       IPv4 Address  IPv6 Address  MAC                Role         Working Rate(Mbps)
--------------  -------------  --------------  ---------  ------------  ------------  -----------------  -----------  ------------------
CTE0.B.IOM1.P1  Normal         Link Up         Host Port  --            --            8c:e5:ef:ab:8b:e2  INI and TGT  1000
CTE0.B.IOM1.P3  Normal         Link Down       Host Port  --            --            8c:e5:ef:ab:8b:e4  INI and TGT  --
```

Query information about the port whose type is "ETH". The ID and output vary depending on a specific product.

```text

admin:/>show port general physical_type=ETH
------------  Management Port:-------------

ID           Health Status  Running Status  Type             IPv4 Address  IPv6 Address  MAC                Role  Working Rate(Mbps)  Enabled  Max Speed(Mbps)
-----------  -------------  --------------  ---------------  ------------  ------------  -----------------  ----  ------------------  -------  ---------------
CTE0.A.MGMT  Normal         Link Up         Management Port  8.46.17.79    --            04:bd:70:28:07:25  --    1000                Yes      1000
CTE0.B.MGMT  Normal         Link Up         Management Port  8.46.17.80    --            08:11:20:c4:a2:c8  --    1000                Yes      1000
------------  Maintenance Port:------------
ID                  Health Status  Running Status  Type              IPv4 Address    IPv6 Address  MAC                Role  Working Rate(Mbps)  Enabled  Max Speed(Mbps)
------------------  -------------  --------------  ----------------  --------------  ------------  -----------------  ----  ------------------  -------  ---------------
CTE0.A.MAINTENANCE  Normal         Link Down       Maintenance Port  --              --            04:bd:70:28:07:25  --    --                  Yes      1000
CTE0.B.MAINTENANCE  Normal         Link Down       Maintenance Port  172.31.128.102  --            08:11:20:c4:a2:c8  --    --                  Yes      1000
------------  Container Front End Port:------------
ID                  Health Status  Running Status  Type                      IPv4 Address    IPv6 Address  MAC                Role  Working Rate(Mbps)  Enabled  Max Speed(Mbps)
------------------  -------------  --------------  ------------------------  --------------  ------------  -----------------  ----  ------------------  -------  ---------------
CTE0.A.IOM0.P0      Normal         Link Down       Container Front End Port  --              --            04:bd:70:28:07:25  --    --                  Yes      1000
CTE0.A.IOM0.P1      Normal         Link Down       Container Front End Port  172.31.128.102  --            08:11:20:c4:a2:c8  --    --                  Yes      1000
CTE0.A.IOM0.P2      Normal         Link Down       Container Front End Port  --              --            04:bd:70:28:07:23  --    --                  Yes      1000
CTE0.A.IOM0.P3      Normal         Link Down       Container Front End Port  172.31.128.103  --            08:11:20:c4:a2:23  --    --                  Yes      1000

```

##### System Response

The following table describes the parameter meanings.

| Parameter                      | Meaning                                                             |
|--------------------------------|---------------------------------------------------------------------|
| Number Of Initiators           | Number of initiators.                                               |
| ID                             | ID of a port.                                                       |
| Health Status                  | Health status of a port.                                            |
| Running Status                 | Running status of a port.                                           |
| Type                           | Port usage type.                                                    |
| IPv4 Address                   | IPv4 address of an Ethernet port.                                   |
| IPv6 Address                   | IPv6 address of an Ethernet port.                                   |
| Channel Number                 | Channel number of a port.                                           |
| MAC                            | MAC address of an Ethernet port.                                    |
| Role                           | Role of a port in the link.                                         |
| Working Rate(Mbps)             | Port working rate.                                                  |
| Enabled                        | Whether the port is enabled.                                        |
| Max Speed(Mbps)                | Maximum port working rate.                                          |
| WWN                            | World wide name (WWN) of a port.                                    |
| Working Mode                   | Working mode of a port.                                             |
| Configured Mode                | Configuration mode of a port.                                       |
| PCIE Speed(Mbit/s)             | Working speed of a PCIe port.                                       |
| Current Peer Port Id           | ID of the current peer port.                                        |
| Suggest Peer Port Id           | ID of the peer port that is supposed to connect to the port.        |
| Lost Signals                   | Number of bit errors of a PCIe or FC port.                          |
| FC MOR State                   | Whether the MOR function of a Fibre Channel port is enabled.        |
| Subnet Mask                    | IPv4 mask of an Ethernet port.                                      |
| protocol                       | Protocol type of the Fibre Channel port.                            |
| IPv6 Prefix Length             | IPv6 prefix length.                                                 |
| IPv4 Gateway                   | IPv4 gateway.                                                       |
| IPv6 Gateway                   | IPv6 gateway.                                                       |
| Mode                           | Working mode.                                                       |
| MTU                            | Maximum transmission unit.                                          |
| Bond Name                      | Bond port name.                                                     |
| iSCSI Port                     | iSCSI port ID.                                                      |
| iSCSI Name                     | iSCSI port name.                                                    |
| Error Packets                  | Number of error packets.                                            |
| Over Flowed Packets            | Number of overflowed packets.                                       |
| Lost Packets                   | Number of lost packets.                                             |
| Start Time                     | Indicates the time when the statistics starts.                      |
| CRC Errors                     | CRC error.                                                          |
| Enabled                        | Whether the port is enabled.                                        |
| Frame Errors                   | Frame error.                                                        |
| Frame Length Errors            | Frame length error.                                                 |
| SFP Status                     | Optical module status.                                              |
| Lost Synchronizations          | Number of lost packets in synchronization.                          |
| Failed Connections             | Number of failed connections.                                       |
| Link Errors Codes              | Number of link errors.                                              |
| Fast Write Supported           | Whether to support FastWrite of a Fibre Channel port.               |
| Fast Write Enable              | Whether to enable FastWrite of a Fibre Channel port.                |
| Fast Write Burst Len(Byte)     | I/O size of a Fibre Channel port's FastWrite.                       |
| Invalid Dword                  | Number of invalid DWORDs.                                           |
| Consist Errors                 | Number of inconsistency errors.                                     |
| Loss Of DWORD                  | Number of lost DWORDs in synchronization.                           |
| PHY Reset Errors               | Number of failed PHY resetting.                                     |
| ECRC Error                     | Number of ECRC errors.                                              |
| Bad Tlp                        | Number of bad TLPs.                                                 |
| Bad Dllp                       | Number of bad DLLPs.                                                |
| Recv Error                     | Number of receiver errors.                                          |
| Chip Ecc Error                 | Number of ECC errors on the chip.                                   |
| Replay Timer Timeout           | Count of replay timer timeout.                                      |
| Rollover                       | Count of replay counter rollovers.                                  |
| Model                          | PCIe port model.                                                    |
| Frame End Sign Errors          | Frame end sign error.                                               |
| Work Mode                      | Work mode of an Ethernet port.                                      |
| Flogin Delay Times(ms)         | Delay time that the system waits before sending the FLOGIN command. |
| Total Received Packets         | Total number of received packets.                                   |
| Total Transmitted Packets      | Total number of sent packets.                                       |
| Total Received Bytes           | Total number of received bytes.                                     |
| Total Transmitted Bytes        | Total number of sent bytes.                                         |
| Received Packets Per Second    | Average number of packets received per second.                      |
| Transmitted Packets Per Second | Average number of packets sent per second.                          |
| Received Bytes Per Second      | Average number of bytes received per second.                        |
| Transmitted Bytes Per Second   | Number of bytes sent per second.                                    |
