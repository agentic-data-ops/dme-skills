# change bond_port ipv6_address


##### Function

The **change bond_port ipv6_address** command is used to change the IPv6 address of the bond port.

##### Format

**change bond_port ipv6_address** bond_port_name=? ip=? prefix_length=?

##### Parameters

| Parameter        | Description                                                   | Value                                                  |
|------------------|---------------------------------------------------------------|--------------------------------------------------------|
| bond_port_name=? | Bond port name.                                               | To obtain the value, run the "show bond_port" command. |
| ip=?             | Bond port IPv6 address after the change.                      | The value can be, for example, "2900::111".            |
| prefix_length=?  | Prefix length of the bond port IPv6 address after the change. | The value must be an integer ranging from 1 to 128.    |

##### Usage Guidelines

-   This operation disconnects the storage system and application server.
-   Before performing this operation, check whether a redundant connection exists. If it does not exist, first stop all the services on the application server.
-   Before performing this operation, ensure that the entered IP address is reachable.
-   The IP address of a host bond port cannot be at the same network segment as that of the management network port.

##### Example

Set the IPv6 address and prefix length of the bond port whose name is "bond_1\_1" to "2900::111" and "64". The bond port ID and command output vary depending on products. The name and output here are just examples.

```text
admin:/>change bond_port ipv6_address bond_port_name=bond_1_1 ip=2900::111 prefix_length=64
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
