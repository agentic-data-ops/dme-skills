# change port roce


##### Function

The **change port roce** command is used to configure the properties for RoCE ports.

##### Format

**change port roce** port_id=? { mtu=? \| work_mode=? }

##### Parameters

| Parameter   | Description                                                                               | Value                                                            |
|-------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| port_id=?   | Port ID.                                                                                  | To obtain the value, run "show port general physical_type=RoCE". |
| mtu=?       | Size of the largest data packet that can be transmitted on a certain layer of a protocol. | The value ranges from 1280 to 9000 bytes.                        |
| work_mode=? | Work mode of a port.                                                                      | \-                                                               |

##### Usage Guidelines

None.

##### Example

Set the MTU of the RoCE port whose ID is "ENG0.A1.P0" to "1600" bytes. The ID and output vary depending on product models.

```text
admin:/>change port roce port_id=ENG0.A1.P0 mtu=1600
DANGER: You are about to modify the MTU of the port.This operation may interrupt services or cause service exceptions.
Suggestion: Before performing this operation, determine whether the modification is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Set the work mode of the RoCE port "CTE0.A3.P0" to "25GE_NOFEC". The ID and output vary depending on a specific product.

```text
admin:/>change port roce port_id=CTE0.A3.P0 work_mode=25GE_NOFEC
DANGER: You are about to modify the work mode of port. If the work mode of the port does not match the work mode of the peer port, the operation will interrupt the connection.
Suggestion: Before performing this operation, you are advised to determine the work mode supported by the peer port.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
