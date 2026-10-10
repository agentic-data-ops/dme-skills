# remove bond_port ipv6_address


##### Function

The **remove bond_port ipv6_address** command is used to delete the IPv6 address of a bond port.

##### Format

**remove bond_port ipv6_address** bond_port_name=?

##### Parameters

| Parameter        | Description     | Value                                                  |
|------------------|-----------------|--------------------------------------------------------|
| bond_port_name=? | Bond port name. | To obtain the value, run the "show bond_port" command. |

##### Usage Guidelines

Deleting the IP address of a host bond port causes the storage system to be inaccessible to the application server connected to the port.

##### Example

Delete the IPv6 address of the host bond port whose name is "bond_1\_1". The bond port name and command output vary depending on products. The name and output here are just examples.

```text
admin:/>remove bond_port ipv6_address bond_port_name=bond_1_1
DANGER: You are about to clear IP addresses on port. This operation will disconnect the storage system from hosts.
Suggestion: Check whether there are redundant connections to hosts. If there are no redundant connections, stop host services.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
