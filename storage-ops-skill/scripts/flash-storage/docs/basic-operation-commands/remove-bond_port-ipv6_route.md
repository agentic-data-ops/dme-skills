# remove bond_port ipv6_route


##### Function

The **remove bond_port ipv6_route** command is used to delete the IPv6 route of a host bond port.

##### Format

**remove bond_port ipv6_route** bond_port_name=? target_ip=?

##### Parameters

| Parameter        | Description                                                             | Value                                                  |
|------------------|-------------------------------------------------------------------------|--------------------------------------------------------|
| bond_port_name=? | Bond port name.                                                         | To obtain the value, run the "show bond_port" command. |
| target_ip=?      | IPv6 address of the network segment at which the application server is. | The value can be, for example, "1118::0".              |

##### Usage Guidelines

Before performing this operation, ensure that the bond port already has an IPv6 route.

##### Example

Delete the IPv6 route of the host bond port whose name is "bond_1\_1" and the target network address is "1118::0". The bond port name and command output vary depending on products. The name and output here are just examples.

```text
admin:/>remove bond_port ipv6_route bond_port_name=bond_1_1 target_ip=1118::0
DANGER: You are about to remove the route of host port. This operation will interrupt the connection between the storage system and host.
Suggestion: Before you perform this operation, ensure that you have stopped the business on the route.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
