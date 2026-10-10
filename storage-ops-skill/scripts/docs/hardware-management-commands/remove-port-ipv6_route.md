# remove port ipv6_route


##### Function

The **remove port ipv6_route** command is used to remove an IPv6 route configured for a port.

##### Format

**remove port ipv6_route** eth_port_id=? target_ip=?

##### Parameters

| Parameter     | Description                                               | Value                                         |
|---------------|-----------------------------------------------------------|-----------------------------------------------|
| eth_port_id=? | ID of a port.                                             | To obtain the value, run "show port general". |
| target_ip=?   | Address of the IPv6 network segment where a host resides. | Example: "1118::0"                            |

##### Usage Guidelines

Before running this command, please guarantee that the port had the IPv6 route.

##### Example

Remove an IPv6 route configured for the port whose ID is "ENG0.A3.P0", where the target network segment address is "1118::0". The ID and output vary depending on a specific product.

```text
admin:/>remove port ipv6_route eth_port_id=ENG0.A3.P0 target_ip=1118::0
DANGER: You are about to delete the route of port.
This operation will interrupt the connection between the storage system and host.
Suggestion: Before performing this operation, ensure that you have stopped all services on the route.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
