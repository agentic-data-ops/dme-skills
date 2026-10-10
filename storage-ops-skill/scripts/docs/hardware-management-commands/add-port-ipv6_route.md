# add port ipv6_route


##### Function

The **add port ipv6_route** command is used to add an IPv6 route for a specific Ethernet port. If the IPv6 address of the storage system and that of a host reside on different network segments, you can run this command to add a route to connect the storage system to the host.

##### Format

**add port ipv6_route** eth_port_id=? type=? \[ target_ip=? \] \[ prefix_length=? \] gateway=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| eth_port_id=? | ID of a port. | To obtain the value, run "show port general". |
| type=? | Route type. | The value can be "net", "host", or "default", where: <br>"net": indicates a route to the target network segment.<br>"host": indicates a route to the target host.<br>"default": indicates a default route. If there is no route to the target network segment or the target host, the target host accesses the storage system through the default route. |
| target_ip=? | Address of the IPv6 network segment where a host resides. This parameter is valid only when type=? is set to "net" and "host". | Example: "1118::0" |
| prefix_length=? | Prefix length of the IPv6 address of a host. This parameter is valid only when type=? is set to "net". | - |
| gateway=? | IPv6 gateway address of a port. | - |

##### Usage Guidelines

-   Before running "**add port ipv6_route**", ensure that an IP address has been assigned to the Ethernet port. To query the IP addresses of host ports, run "show port general".
-   To add a route to the target network segment, run "**add port ipv6_route** eth_port_id=? net target_ip=? prefix_length=? gateway=?".
-   To add a route to the target server, run "**add port ipv6_route** eth_port_id=? host gateway=?".
-   To add a default route, run "**add port ipv6_route** eth_port_id=? default gateway=?".
-   This command does not support to add the route of maintenance port.

##### Example

Add an IPv6 route for the port whose ID is "ENG0.A3.P0", where the target network segment address is "1118::0", the prefix length is "32", and the gateway address is "2100::1". The ID and output vary depending on a specific product.

```text
admin:/>add port ipv6_route eth_port_id=ENG0.A3.P0 type=net target_ip=1118::0 prefix_length=32 gateway=2100::1
DANGER: You are about to add the route of port. If the route is unavailable, this operation will disconnect the storage system from hosts.
Suggestion: Before performing this operation, ensure that the entered route is available.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
