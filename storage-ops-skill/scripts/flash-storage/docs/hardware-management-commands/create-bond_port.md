# create bond_port


##### Function

The **create bond_port** command is used to create an Ethernet bond port. By binding multiple Ethernet ports, you can increase the data transmission bandwidth in parallel mode. The "**create bond_port** iscsi_port_id_list" command is replaced with the "**create bond_port** port_id_list" command.

##### Format

**create bond_port** iscsi_port_id_list=? \[ name=? \]

**create bond_port** port_id_list=? \[ name=? \]

##### Parameters

| Parameter            | Description                                        | Value                                                                                                                   |
|----------------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| iscsi_port_id_list=? | List of port IDs that you want to bind.            | To obtain the value, run "show port general".                                                                           |
| name=?               | Name of the Ethernet bond port you want to create. | The value contains 1 to 31 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |
| port_id_list         | List of port IDs that you want to bind.            | To obtain the value, run "show port general".                                                                           |

##### Usage Guidelines

-   Running this command interrupts the connections of all Ethernet ports involved in the port bonding. In addition, these Ethernet ports' IP addresses and route settings will be lost, and the bond port will be used to carry services.
-   Before running this command, stop services carried by all Ethernet ports.
-   An Ethernet port can be bound only once.

##### Example

Create an Ethernet bond port, where IDs of the ports to be bound are "ENG0.B1.P0" and "ENG0.B1.P1", and the name of the bond port is "newbond". The ID and output vary depending on a specific product.

```text
admin:/>create bond_port iscsi_port_id_list=ENG0.B1.P0,ENG0.B1.P1 name=newbond
DANGER:You are about to bond Ethernet port.
This operation will disconnect all links to the Ethernet port, and the IP address and route configurations will be lost. Services are switched to the new bond port. The mode of all switch ports connected to the Ethernet port must be configured to 802.3AD LACP.
Suggestion:
1. Before performing this operation, stop all services on the Ethernet port.
2. Configure the mode of all switch ports connected to the Ethernet port to 802.3AD LACP.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

Create an Ethernet bond port, where IDs of the ports to be bound are "ENG0.B1.P0" and "ENG0.B1.P1", and the name of the bond port is "newbond". The ID and output vary depending on a specific product.

```text
admin:/>create bond_port port_id_list=ENG0.B1.P0,ENG0.B1.P1 name=newbond
DANGER:You are about to bond Ethernet port.
This operation will disconnect all links to the Ethernet port, and the IP address and route configurations will be lost. Services are switched to the new bond port. The mode of all switch ports connected to the Ethernet port must be configured to 802.3AD LACP.
Suggestion:
1. Before performing this operation, stop all services on the Ethernet port.
2. Configure the mode of all switch ports connected to the Ethernet port to 802.3AD LACP.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
