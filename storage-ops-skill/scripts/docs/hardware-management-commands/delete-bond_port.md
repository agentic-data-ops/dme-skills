# delete bond_port


##### Function

The **delete bond_port** command is used to delete an Ethernet bond port.

##### Format

**delete bond_port** { bond_port_id=? \| bond_port_name=? }

##### Parameters

| Parameter        | Description     | Value                                                  |
|------------------|-----------------|--------------------------------------------------------|
| bond_port_id=?   | Bond port ID.   | To obtain the value, run the "show bond_port" command. |
| bond_port_name=? | Bond port name. | To obtain the value, run the "show bond_port" command. |

##### Usage Guidelines

Before running this command, stop services carried by the Ethernet bond port you want to delete.

##### Example

Delete the Ethernet bond port whose ID is "0".

```text
admin:/>delete bond_port bond_port_id=0
DANGER: You are about to unbind ethernet ports. This operation interrupts all connections of the preceding ethernet ports.
Suggestion: Before performing this operation, stop all services on the preceding ethernet ports.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

Delete the Ethernet bond port whose name is "bond_1\_1".

```text
admin:/>delete bond_port bond_port_name=bond_1_1
DANGER: You are about to unbind ethernet ports. This operation interrupts all connections of the preceding ethernet ports.
Suggestion: Before performing this operation, stop all services on the preceding ethernet ports.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
