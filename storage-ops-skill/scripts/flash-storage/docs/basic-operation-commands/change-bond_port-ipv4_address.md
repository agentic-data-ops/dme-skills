# change bond_port ipv4_address


##### Function

The **change bond_port ipv4_address** command is used to change the IPv4 address of the bond port.

##### Format

**change bond_port ipv4_address** bond_port_name=? ip=? mask=?

##### Parameters

| Parameter        | Description                                         | Value                                                               |
|------------------|-----------------------------------------------------|---------------------------------------------------------------------|
| bond_port_name=? | Bond port name.                                     | To obtain the value, run the "show bond_port" command.              |
| ip=?             | Bond port IPv4 address after the change.            | The IPv4 address cannot start with 0 or an integer from 224 to 255. |
| mask=?           | IPv4 subnet mask of the bond port after the change. | \-                                                                  |

##### Usage Guidelines

-   This operation disconnects the storage system and application server.
-   Before performing this operation, check whether a redundant connection exists. If it does not exist, first stop all the services on the application server.
-   Before performing this operation, ensure that the entered IP address is reachable.
-   The IP address of a host bond port cannot be at the same network segment as that of the management network port.

##### Example

Set the IP address and subnet mask of the bond port whose name is "bond_1\_1" to "192.168.3.2" and "255.255.0.0". The bond port name and command output vary depending on products. The name and output here are just examples.

```text
admin:/>change bond_port ipv4_address bond_port_name=bond_1_1 ip=192.168.3.2 mask=255.255.0.0
DANGER: You are about to change the IP address of port. This operation will disconnect the storage system from hosts. This operation will also clear the configured routes on the IP address that is modified on this port.
Suggestion:
1. Check whether there are redundant connections to hosts. If there are no redundant connections, stop host services.
2. Ensure that the entered IP address is available.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
