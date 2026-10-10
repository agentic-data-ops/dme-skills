# show port_group port


##### Function

The **show port_group port** command is used to query information about ports in a port group.

##### Format

**show port_group port** { port_group_id=? \| port_group_name=? } \[ port_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| port_group_id=? | ID of a port group that you want to query. | To obtain the value, run "show port_group general". |
| port_group_name=? | Name of a port group that you want to query. | To obtain the value, run "show port_group general" without parameters. |
| port_type=? | Type of a port that you want to query. | "FC": indicates Fibre Channel ports.<br>"ETH": indicates ETH ports.<br>"ROCE": indicates RoCE ports. |

##### Usage Guidelines

None.

##### Example

Query information about ports in port group "0". The ID and output vary depending on a specific product.

```text
admin:/>show port_group port port_group_id=0
ETH port:
FC port:

ID Health Status Running Status Type Working Rate(Mbps)
---------- ------------- -------------- --------- ------------------
ENG0.A2.P1 Normal Link Down Host Port --
ENG0.A2.P2 Normal Link Down Host Port --

WWN Role Working Mode Configured Mode
---------------- ----------- ------------ ---------------
0000000002010101 INI and TGT -- Auto-Adapt
0000000002010202 INI and TGT -- Auto-Adapt
```

Query information about ports in port group "portgroup1". The ID and output vary depending on a specific product.

```text
admin:/>show port_group port port_group_name=portgroup1
ETH port:
FC port:

ID Health Status Running Status Type Working Rate(Mbps)
---------- ------------- -------------- --------- ------------------
ENG0.A2.P1 Normal Link Down Host Port --
ENG0.A2.P2 Normal Link Down Host Port --

WWN Role Working Mode Configured Mode
---------------- ----------- ------------ ---------------
0000000002010101 INI and TGT -- Auto-Adapt
0000000002010202 INI and TGT -- Auto-Adapt
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                         |
|--------------------|---------------------------------|
| ID                 | ID of a port.                   |
| Health Status      | Health status of a port.        |
| Running Status     | Running status of a port.       |
| Type               | Port type.                      |
| IPv4 Address       | IPv4 address of an ETH port.    |
| IPv6 Address       | IPv6 address of an ETH port.    |
| MAC                | MAC address of an ETH port.     |
| Role               | Role of a port in the link.     |
| Working Rate(Mbps) | Working rate of a port.         |
| Enabled            | Whether the port is enabled.    |
| Max Speed(Mbps)    | Maximum working rate of a port. |
| WWN                | WWN of a port.                  |
| Channel Number     | Channel number of a port.       |
