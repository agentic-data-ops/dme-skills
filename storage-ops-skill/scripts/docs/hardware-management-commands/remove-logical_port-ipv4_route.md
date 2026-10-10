# remove logical_port ipv4_route


##### Function

The **remove logical_port ipv4_route** command is used to remove the IPv4 route from a logical port.

##### Format

**remove logical_port ipv4_route** logical_port_name=? ipv4_address=? ipv4_mask=? ipv4_gateway=?

##### Parameters

| Parameter           | Description                       | Value                                                           |
|---------------------|-----------------------------------|-----------------------------------------------------------------|
| logical_port_name=? | Logical port name.                | To obtain the value, run the "show logical_port route" command. |
| ipv4_address=?      | Target IPv4 address.              | To obtain the value, run the "show logical_port route" command. |
| ipv4_mask=?         | Target IPv4 mask.                 | To obtain the value, run the "show logical_port route" command. |
| ipv4_gateway=?      | IPv4 gateway of the logical port. | To obtain the value, run the "show logical_port route" command. |

##### Usage Guidelines

Before running this command, check that there is an IPv4 route on the logical port.

##### Example

Delete the IPv4 route from a logical port.

```text
admin:/>remove logical_port ipv4_route logical_port_name=rty ipv4_address=10.181.0.55 ipv4_mask=255.255.0.0 ipv4_gateway=10.181.0.1
DANGER: You are about to remove the route of logical port. This operation will interrupt the connection between the storage system and host.
Suggestion: Before you perform this operation, ensure that you have stopped the business on the route.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
