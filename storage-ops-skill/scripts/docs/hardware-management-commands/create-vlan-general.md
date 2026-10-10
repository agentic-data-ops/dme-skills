# create vlan general


##### Function

The **create vlan general** command is used to create a VLAN.

##### Format

**create vlan general** vlan_id=? port_type=? \[ eth_port_id=? \] \[ bond_port_id=? \] \[ roce_port_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| vlan_id=? | VLAN ID (tag value). | The value is an integer between 1 and 4094. |
| port_type=? | VLAN type. | The value can be "eth", "roce", or "bond", where: <br>"eth": ETH port<br>"bond": Bond port.<br>"roce": RoCE port. |
| eth_port_id=? | ID of a physical port. | To obtain the value, run the "show port general" command. |
| bond_port_id=? | ID of a bond port. | To obtain the value, run the "show bond_port" command. |
| roce_port_id=? | ID of a RoCE port. | To obtain the value, run the "show port general" command. |

##### Usage Guidelines

-   When "port_type" is set to "eth", "eth_port_id" must be specified.
-   When "port_type" is set to "bond", "bond_port_id" must be specified.
-   When "port_type" is set to "roce", "roce_port_id" must be specified.

##### Example

Create a VLAN whose ID is "1", port type is "eth", and port ID is "ENG0.A2P1".

```text
admin:/>create vlan general vlan_id=1 port_type=eth eth_port_id=ENG0.A2.P1
Command executed successfully.
```

Check the VLAN you have created.

```text
admin:/>show vlan general
Name Running Status VLAN ID MTU Port Type Port ID
---------- ----------- ------- ---- ---------- ----------
ENG0.A2.P0.2 Link Down 2 1500 ETH ENG0.A2.P0
ENG0.A2.P1.1 Link Down 1 1500 ETH ENG0.A2.P1
```

##### System Response

None
