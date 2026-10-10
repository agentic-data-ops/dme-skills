# remove port ipv6_address


##### Function

The **remove port ipv6_address** command is used to remove the IPv6 address of a specified port.

 

After the IP address of an Ethernet host port is removed, the application sever that connects to the Ethernet host port cannot access the storage system.

##### Format

**remove port ipv6_address** eth_port_id=?

##### Parameters

| Parameter     | Description   | Value                                         |
|---------------|---------------|-----------------------------------------------|
| eth_port_id=? | ID of a port. | To obtain the value, run "show port general". |

##### Usage Guidelines

None

##### Example

Remove the IPv6 address of the Ethernet host port whose ID is "ENG0.A3.P0". The ID and output vary depending on a specific product.

```text
admin:/>remove port ipv6_address eth_port_id=ENG0.A3.P0
DANGER: You are about to clear IP addresses on Ethernet port.This operation will disconnect the storage system from hosts.
Suggestion: Check whether there are redundant connections to hosts. If there are no redundant connections, stop host services.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
