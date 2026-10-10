# add bond_port ipv6_route


##### Function

The **add bond_port ipv6_route** command is used to add an IPv6 route to the bond port. You can run this command to add a route to connect the storage system to the application server when their IPv6 addresses are not at the same network segment.

##### Format

**add bond_port ipv6_route** bond_port_name=? type=? \[ target_ip=? \] \[ prefix_length=? \] gateway=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| bond_port_name=? | Bond port name. | To obtain the value, run the "show bond_port" command. |
| type=? | Specified route type. | The value can be "net", "host", or "default", where: <br>"net": route to the target network segment.<br>"host": route to the target application server.<br>"default": default route. If the target network segment or application server is not in any route, you can use this default route to access. |
| target_ip=? | IPv6 address of the network segment at which the application server is. This parameter is valid when "type=?" is "net" or "host". | The value can be, for example, "1118::0". |
| prefix_length=? | Prefix length of the application server's IPv6 address. This parameter is valid when "type=?" is "net". | The value can be a number ranging from 1 to 128. |
| gateway=? | IPv6 address of the gateway of the host bond port. | - |

##### Usage Guidelines

-   Before running the "**add bond_port ipv6_route**" command to add a route, you need to ensure that an IP address has been configured for the bond port.
-   Running the "**add bond_port ipv6_route** bond_port_name=? type=net target_ip=? prefix_length=? gateway=?" command adds a route to the target network segment.
-   Running the "**add bond_port ipv6_route** bond_port_name=? type=host target_ip=? gateway=?" command adds a route to the target application server.
-   Running the "**add bond_port ipv6_route** bond_port_name=? type=default gateway=?" command adds the default route.

##### Example

Add an IPv6 route for the bond port whose name is "bond_1\_1", IP address at the target network segment is "1118::0", prefix length is "32", and IP address of the gateway is "2100::1". The bond port name and command output vary depending on products. The name and output here are just examples.

```text
admin:/>add bond_port ipv6_route bond_port_name=bond_1_1 type=net target_ip=1118::0 prefix_length=32 gateway=2100::1
DANGER: You are about to add the route of port. If the route is unavailable, this operation will disconnect the storage system from hosts.
Suggestion: Before performing this operation, ensure that the entered route is available.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
