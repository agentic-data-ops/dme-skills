# remove bond_port ipv4_route


##### Function

The **remove bond_port ipv4_route** command is used to delete the IPv4 route of a host bond port.

##### Format

**remove bond_port ipv4_route** bond_port_name=? target_ip=? mask=? gateway=?

##### Parameters

| Parameter        | Description                                                             | Value                                                  |
|------------------|-------------------------------------------------------------------------|--------------------------------------------------------|
| bond_port_name=? | Bond port name.                                                         | To obtain the value, run the "show bond_port" command. |
| target_ip=?      | IPv4 address of the network segment at which the application server is. | The value can be, for example, "192.168.2.0".          |
| mask=?           | Subnet mask of the IPv4 address of the application server.              | \-                                                     |
| gateway=?        | IPv4 address of the gateway of the host bond port.                      | \-                                                     |

##### Usage Guidelines

Before performing this operation, ensure that the bond port already has an IPv4 route.

##### Example

Delete the route of the host bond port whose name is "bond_1\_1" and the target IP address is "192.168.3.0". The bond port ID and command output vary depending on products. The name and output here are just examples.

```text
admin:/>remove bond_port ipv4_route bond_port_name=bond_1_1 target_ip=192.168.3.0 mask=255.255.255.0 gateway=192.168.0.1
DANGER: You are about to remove the route of host port. This operation will interrupt the connection between the storage system and host.
Suggestion: Before you perform this operation, ensure that you have stopped the business on the route.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
