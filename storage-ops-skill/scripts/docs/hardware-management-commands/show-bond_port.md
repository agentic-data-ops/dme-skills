# show bond_port


##### Function

The **show bond_port** command is used to query bond ports.

##### Format

**show bond_port** \[ bond_port_id=? \| bond_port_name=? \| failover_group_id=? \| failover_group_name=? \]

##### Parameters

| Parameter             | Description               | Value                                                                                                                                                                         |
|-----------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bond_port_id=?        | ID of the bond port.      | To obtain the value, run "**show bond_port**" without parameters. |
| bond_port_name=?      | Name of the bond port.    | To obtain the value, run "**show bond_port**" without parameters. |
| failover_group_id=?   | ID of the failover group. | The value is an integer from 0 to 8191.                                                                                                                                       |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (\_), hyphens (-), and periods (.).                                                            |

##### Usage Guidelines

-   To query all bond ports, run "**show bond_port**".
-   To query a specific bond port, run "**show bond_port** bond_port_id=?".
-   To query a specific bond port, run "**show bond_port** bond_port_name=?".
-   To query bond ports in a specified failover group, run "**show bond_port** failover_group_id=?".
-   To query bond ports in a specified failover group, run "**show bond_port** failover_group_name=?".

Parameters bond_port_id, bond_port_name, failover_group_id and failover_group_name are mutually exclusive.

##### Example

Query all bond ports.

```text
admin:/>show bond_port
ID      Name     Health Status  Running Status  MTU   Port ID List           IPv4 Address  Subnet Mask    IPv6 Address  Prefix Length  Number Of Initiators
------  -------  -------------  --------------  ----  ---------------------  ------------  -------------  ------------  -------------  --------------------
139009  newbond  Normal         Link Up         1500  CTE0.A7.P2,CTE0.A7.P3  192.168.1.1   255.255.224.0  --            --              0
```

Query the bond ports in failover group "0".

```text
admin:/>show bond_port failover_group_id=0
ID           Name    Health Status   Running Status  MTU             Port ID List
--           ------- --------------- --------------- --------------- -----------------------------
549772730113 test    Normal          Link up         3000            CTE0.IOM.H1.P0,CTE0.IOM.H1.P1
```

Query the bond ports in failover group "System-defined".

```text
admin:/>show bond_port failover_group_name=System-defined
ID                Name   Health Status  Running Status  MTU   Port ID List                   IPv4 Address  Subnet Mask  IPv6 Address  Prefix Length  Number Of Initiators
----------------  -----  -------------  --------------  ----  -----------------------------  ------------  -----------  ------------  -------------  --------------------
1970329132080897  bond1  Normal         Link Up         1500  CTE0.B.IOM1.P0,CTE0.B.IOM1.P2  --            --           --            --             0
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                               |
|----------------------|---------------------------------------|
| ID                   | ID of the bond port.                  |
| Port ID List         | Member port ID list of the bond port. |
| Name                 | Bond port name.                       |
| Health Status        | Health status of the bond port.       |
| Running Status       | Running status of the bond port.      |
| MTU                  | MTU of the bond port.                 |
| IPv4 Address         | IPv4 address.                         |
| Subnet Mask          | IPv4 subnet mask.                     |
| IPv6 Address         | IPv6 address.                         |
| Prefix Length        | IPv6 subnet mask.                     |
| Number Of Initiators | Number of initiators.                 |
