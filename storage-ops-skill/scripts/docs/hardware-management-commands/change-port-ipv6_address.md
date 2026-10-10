# change port ipv6_address


##### Function

The **change port ipv6_address** command is used to change the IPv6 address of a specific port.

##### Format

**change port ipv6_address** eth_port_id=? ip=? prefix_length=?

##### Parameters

| Parameter       | Description                                          | Value                                         |
|-----------------|------------------------------------------------------|-----------------------------------------------|
| eth_port_id=?   | ID of a port.                                        | To obtain the value, run "show port general". |
| ip=?            | Changed IPv6 address of a port.                      | \-                                            |
| prefix_length=? | Changed prefix length of the IPv6 address of a port. | \-                                            |

##### Usage Guidelines

-   Running this command interrupts the connection between the storage system and the application server.
-   Before running this command, check whether there are redundant links. If there is no redundant link, stop services running on the application server.
-   Before running this command, check that the specified IP address is available.
-   The IP address of a host port cannot reside on the same network segment as that of the management network port.

##### Example

Change the IPv6 address to "2900::111" and prefix length to "64" for the Ethernet port whose ID is "ENG0.A3.P0". The ID and output vary depending on a specific product.

```text
admin:/>change port ipv6_address eth_port_id=ENG0.A3.P0 ip=2900::111 prefix_length=64
DANGER: You are about to change the IP address of Ethernet port.This operation will disconnect the storage system from hosts. This operation will also clear the configured routes on the IP address that is modified on this port.
Suggestion:
1. Check whether there are redundant connections to hosts. If there are no redundant connections, stop host services.
2. Ensure that the entered IP address is available.Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
