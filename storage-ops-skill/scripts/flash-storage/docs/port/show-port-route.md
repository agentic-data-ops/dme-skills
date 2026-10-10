# show port route


##### Function

The **show port route** command is used to query the route settings of ports on the storage system.

##### Format

**show port route** \[ eth_port_id=? \]

##### Parameters

| Parameter     | Description   | Value                                         |
|---------------|---------------|-----------------------------------------------|
| eth_port_id=? | ID of a port. | To obtain the value, run "show port general". |

##### Usage Guidelines

None.

##### Example

Query the route settings of all ports. The command output varies depending on a specific product.

```text
admin:/>show port route

Port ID Destination Mask Gateway
------- ----------- --------------- -----------
ENG0.A3.P0 192.168.3.0 255.255.255.0 192.168.1.1
ENG0.A3.P0 192.168.4.1 255.255.255.255 192.168.1.2
ENG0.A3.P0 0.0.0.0 0.0.0.0 192.168.1.3
ENG0.A4.P0 10.1.1.0 255.0.0.0 10.1.5.3
ENG0.A4.P0 10.3.2.0 255.255.255.0 10.3.2.56
```

Query the route settings of the port whose ID is "ENG0.A3.P0". The ID and output vary depending on a specific product.

```text
admin:/>show port route eth_port_id=ENG0.A3.P0

Port ID Destination Mask Gateway
------- ----------- --------------- -----------
ENG0.A3.P0 192.168.3.0 255.255.255.0 192.168.1.1
ENG0.A3.P0 192.168.4.1 255.255.255.255 192.168.1.2
ENG0.A3.P0 0.0.0.0 0.0.0.0 192.168.1.3
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                                |
|-------------|----------------------------------------|
| Port ID     | Port ID.                               |
| Destination | Destination address of the port route. |
| Mask        | Subnet mask of the port route.         |
| Gateway     | Gateway of the port route.             |
