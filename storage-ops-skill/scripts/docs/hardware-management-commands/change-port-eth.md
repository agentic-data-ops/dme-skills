# change port eth


##### Function

The **change port eth** command is used to configure the properties for Ethernet ports (including host ports and management network ports).

##### Format

**change port eth** eth_port_id=? { mtu=? \| work_mode=? }

##### Parameters

| Parameter     | Description                                                                               | Value                                                           |
|---------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| eth_port_id=? | Ethernet port ID.                                                                         | To obtain the value, run "show port general physical_type=ETH". |
| mtu=?         | Size of the largest data packet that can be transmitted on a certain layer of a protocol. | The value ranges from 1280 to 9000 bytes.                       |
| work_mode=?   | Work mode of an Ethernet port.                                                            | \-                                                              |

##### Usage Guidelines

None.

##### Example

Set the MTU of the Ethernet port whose ID is "ENG0.A1.P0" to "1600" bytes. The ID and output vary depending on product models.

```text
admin:/>change port eth eth_port_id=ENG0.A1.P0 mtu=1600
DANGER: You are about to modify the MTU of the Ethernet port.This operation may interrupt services or cause service exceptions.
Suggestion: Before performing this operation, determine whether the modification is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Set the work mode of the Ethernet port "CTE0.A3.P0" to "40GE_NOFEC". The ID and output vary depending on a specific product.

```text
admin:/>change port eth eth_port_id=CTE0.A3.P0 work_mode=40GE_NOFEC
DANGER: You are about to modify the work mode of Ethernet port. If the work mode of the Ethernet port does not match the work mode of the peer Ethernet port, the operation will interrupt the connection.
Suggestion: Before performing this operation, you are advised to determine the work mode supported by the peer Ethernet port.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
