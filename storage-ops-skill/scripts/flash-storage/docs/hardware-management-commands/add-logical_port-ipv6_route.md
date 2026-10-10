# add logical_port ipv6_route


##### Function

The **add logical_port ipv6_route** command is used to add an IPv6 route for a logical port.

##### Format

**add logical_port ipv6_route** logical_port_name=? type=? ipv6_address=? ipv6_mask=? ipv6_gateway=? \[ table_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| logical_port_name=? | Logical port name. | To obtain the value, run "show logical_port general". |
| type=? | Route type of the logical port. | The value can be "net", "host", or "default", where: <br>"net": indicates a route to the target network segment.<br>"host": indicates a route to the target host.<br>"default": indicates a default route. If there is no route to the target network segment or the target host, the target host accesses the storage system through the default route. |
| ipv6_address=? | IPv6 address of the logical port. | - |
| ipv6_mask=? | IPv6 mask of the logical port. | - |
| ipv6_gateway=? | IPv6 gateway of the logical port. | - |
| table_type | Type of the routing table. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "all", "policy_table", or "default_table", where: <br>"all": indicates a policy routing table and default routing table.<br>"policy_table": indicates a policy routing table.<br>"default_table": indicates a default routing table. |

##### Usage Guidelines

-   When the value of "type" is "net", parameters "ipv6_address", "ipv6_mask", and "ipv6_gateway" are expected.
-   When the value of "type" is "host", parameters "ipv6_address" and "ipv6_mask" are expected.
-   When the value of "type" is "default", parameter "ipv6_gateway" is expected.

##### Example

Add an IPv6 route for the logical port.

```text
admin:/>add logical_port ipv6_route logical_port_name=rty type=net ipv6_address=4010:: ipv6_mask=32 ipv6_gateway=2011::1
Command executed successfully.
```

##### System Response

None
