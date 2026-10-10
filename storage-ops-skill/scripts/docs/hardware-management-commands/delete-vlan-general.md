# delete vlan general


##### Function

The **delete vlan general** command is used to delete a VLAN port.

##### Format

**delete vlan general** name=?

##### Parameters

| Parameter | Description | Value                                         |
|-----------|-------------|-----------------------------------------------|
| name=?    | VLAN name.  | To obtain the value, run "show vlan general". |

##### Usage Guidelines

Before running this command, stop services carried by the VLAN port you want to delete.

##### Example

Delete the VLAN port whose name is "bond_0\_1.23".

```text
admin:/>delete vlan general name=bond_0_1.23
WARNING: You are about to delete VALN. This operation interrupts existing connections of VLAN, and leads to loss of all IP addresses and route configurations of it.
Suggestion: Before you perform this operation, stop all services on the VLAN.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
