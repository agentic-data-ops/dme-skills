# show logical_port route


##### Function

The **show logical_port route** command is used to check the logical port route.

##### Format

**show logical_port route** \[ logical_port_name=? \]

##### Parameters

| Parameter           | Description        | Value                                                             |
|---------------------|--------------------|-------------------------------------------------------------------|
| logical_port_name=? | Logical port name. | To obtain the value, run the "show logical_port general" command. |

##### Usage Guidelines

If the "logical_port_name" parameter is specified, the logical port name you input must exist.

##### Example

Check the logical port route.

```text
admin:/>show logical_port route
Logical Port Name Destination Mask Gateway Table Type
--------------- ----------- ----------- --------- --------
rty 10.181.0.0 255.255.0.0 44.33.0.1 all
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                       |
|-------------------|-------------------------------|
| Logical Port Name | Logical port name.            |
| Destination       | Destination route IP address. |
| Mask              | Mask.                         |
| Gateway           | Gateway.                      |
| Table Type        | Type of the routing table.    |
