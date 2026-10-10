# add port ipv4_route


##### Function

The **add port ipv4_route** command is used to add an IPv4 route for a specific Ethernet port. If the IPv4 address of the storage system and that of an application server reside on different network segments, you can run this command to add a route to connect the storage system to application server.

##### Format

**add port ipv4_route** eth_port_id=? type=? \[ target_ip=? \] \[ mask=? \] gateway=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| eth_port_id=? | ID of a port. | To obtain the value, run "show port general". The value contains 1 to 31 characters, including letters, digits, and periods (.). The value cannot start with a digit or a period (.), or end with a period (.). |
| type=? | Route type. | The value can be "net", "host", or "default", where: <br>"net": indicates a route to the target network segment.<br>"host": indicates a route to the target application server.<br>"default": indicates a default route. If there is no route to the target network segment or the target application server, the target application server accesses the storage system through the default route. |
| target_ip=? | Address of the IPv4 network segment where an application server resides. This parameter is valid only when type=? is set to "net" and "host". | Example: 192.168.2.0. The IPv4 address cannot start with 0 or an integer from 224 to 255. |
| mask=? | IPv4 subnet mask of a host. This parameter is valid only when type=? is set to "net". | - |
| gateway=? | IPv4 gateway address of a port. | The IPv4 gateway cannot start with 0 or an integer from 224 to 255. |

##### Usage Guidelines

-   Before running "**add port ipv4_route**", ensure that an IP address has been assigned to the Ethernet port. To query the IP addresses of ports, run "show port general".
-   To add a route to the target network segment, run "**add port ipv4_route** eth_port_id=? net target_ip=? mask=? gateway=?".
-   To add a route to the target application server, run "**add port ipv4_route** eth_port_id=? host gateway=?".
-   To add a default route, run "**add port ipv4_route** eth_port_id=? default gateway=?".
-   This command does not support to add the route of maintenance port.

##### Example

Add an IPv4 route for the port whose ID is "ENG0.A3.P0", where the target network segment address is "192.168.3.0", the subnet mask is "255.255.255.0", and the gateway address is "192.168.1.1". The ID and output vary depending on a specific product.

```text
admin:/>add port ipv4_route eth_port_id=ENG0.A3.P0 type=net target_ip=192.168.3.0 mask=255.255.255.0 gateway=192.168.1.1
DANGER: You are about to add the route of port. If the route is unavailable, this operation will disconnect the storage system from hosts.
Suggestion: Before performing this operation, ensure that the entered route is available.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
