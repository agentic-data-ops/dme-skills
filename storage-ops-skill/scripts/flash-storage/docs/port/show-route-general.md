# show route general


##### Function

The **show route general** command is used to query route configuration of storage system ports.

##### Format

**show route general** \[ port=? \]

##### Parameters

| Parameter | Description | Value                                                                                                                                                              |
|-----------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port=?    | Port.       | To obtain the value, run "**show route general**". |

##### Usage Guidelines

None.

##### Example

Query route configuration of all ports. The command output varies depending on a specific product.

```text
admin:/>show route general
Port     Destination  Mask        Gateway       Type
-------    -------    -----------    ------------    -----------
ENG0.A3.P0  192.168.3.0  255.255.255.0   192.168.1.1    ETH
ENG0.A3.P0  192.168.4.1  255.255.255.255  192.168.1.2    ETH
ENG0.A3.P0  0.0.0.0     0.0.0.0      192.168.1.3   ETH
ENG0.A4.P0  10.1.1.0    255.0.0.0     10.1.5.3    ETH
ENG0.A4.P0  10.3.2.0    255.255.255.0   10.3.2.56    ETH
ENG0.A4.P0  192.168.3.0   255.255.255.0   192.168.1.1   BOND
bond_1_1   192.168.3.0   255.255.255.0   192.168.1.1   BOND
```

Query route configuration of port ENG0.A4.P0. The command output varies depending on a specific product.

```text
admin:/>show route general port=ENG0.A4.P0
Port   Destination  Mask    Gateway   type
-------  -------   -----------  --------------- -----------
ENG0.A4.P0  10.3.2.0   255.255.255.0  10.3.2.56   ETH
ENG0.A4.P0  192.168.3.0  255.255.255.0  192.168.1.1  BOND
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                                |
|-------------|----------------------------------------|
| Port        | Port.                                  |
| Destination | Destination address of the port route. |
| Mask        | Subnet mask of the port route.         |
| Gateway     | Gateway of the port route.             |
| Type        | Port type.                             |
