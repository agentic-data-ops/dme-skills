# add logical_port ipv4_route


##### Function

The **add logical_port ipv4_route** command is used to add an IPv4 route for the logical port.

##### Format

**add logical_port ipv4_route** logical_port_name=? type=? ipv4_address=? ipv4_mask=? ipv4_gateway=? \[ table_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| logical_port_name=? | Logical port name. | To obtain the value, run "show logical_port general". |
| type=? | Route type of the logical port. | The value can be "net", "host", or "default", where: <br>"net": indicates a route to the target network segment.<br>"host": indicates a route to the target host.<br>"default": indicates a default route. If there is no route to the target network segment or the target host, the target host accesses the storage system through the default route. |
| ipv4_address=? | IPv4 address of the logical port. | The IPv4 address cannot start with 0. |
| ipv4_mask=? | IPv4 mask of the logical port. | - |
| ipv4_gateway=? | IPv4 gateway of the logical port. | - |
| table_type | Type of the routing table. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "all", "policy_table", or "default_table", where: <br>"all": indicates a policy routing table and default routing table.<br>"policy_table": indicates a policy routing table.<br>"default_table": indicates a default routing table. |

##### Usage Guidelines

-   When the value of "type" is "net", parameters "ipv4_address", "ipv4_mask", and "ipv4_gateway" are expected.
-   When the value of "type" is "host", parameters "ipv4_address" and "ipv4_mask" are expected.
-   When the value of "type" is "default", parameter "ipv4_gateway" is expected.

##### Example

Add an IPv4 route for the logical port.

```text
admin:/>add logical_port ipv4_route logical_port_name=lif1 type=net ipv4_address=192.168.0.0 ipv4_mask=255.255.0.0 ipv4_gateway=192.168.0.1
Command executed successfully.
```

##### System Response

None
