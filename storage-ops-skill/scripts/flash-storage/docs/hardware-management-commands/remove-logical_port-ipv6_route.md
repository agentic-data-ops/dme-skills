# remove logical_port ipv6_route


##### Function

The **remove logical_port ipv6_route** command is used to remove the IPv6 route from a logical port.

##### Format

**remove logical_port ipv6_route** logical_port_name=? ipv6_address=?

##### Parameters

| Parameter           | Description                       | Value                                                           |
|---------------------|-----------------------------------|-----------------------------------------------------------------|
| logical_port_name=? | Logical port name.                | To obtain the value, run the "show logical_port route" command. |
| ipv6_address=?      | IPv6 address of the logical port. | To obtain the value, run the "show logical_port route" command. |

##### Usage Guidelines

Before running this command, check that there is an IPv6 route on this logical port.

##### Example

Remove the IPv6 route from a logical port.

```text
admin:/>remove logical_port ipv6_route logical_port_name=lif1 ipv6_address=2011::
DANGER: You are about to remove the route of logical port. This operation will interrupt the connection between the storage system and host.
Suggestion: Before you perform this operation, ensure that you have stopped the business on the route.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
