# change bond_port general


##### Function

The **change bond_port general** command is used to change the MTU of a bond port.

##### Format

**change bond_port general** { bond_port_id=? \| bond_port_name=? } mtu=?

##### Parameters

| Parameter        | Description      | Value                                                  |
|------------------|------------------|--------------------------------------------------------|
| bond_port_id=?   | Bond port ID.    | To obtain the value, run the "show bond_port" command. |
| bond_port_name=? | Bond port name.  | To obtain the value, run the "show bond_port" command. |
| mtu=?            | MTU of the port. | The value is an integer ranging from 1280 to 9000.     |

##### Usage Guidelines

-   Run the "show bond_port" command to query all bond ports.
-   Run the "**change bond_port general** { bond_port_id=? \| bond_port_name=? } mtu=?" command to change the MTU of a specific bond port.

##### Example

Chang the MTU of the bond port whose ID is "139009".

```text
admin:/>change bond_port general bond_port_id=139009 mtu=4000
DANGER:You are about to modify the MTU settings for the bond port. This operation may interrupt services or cause service exceptions.
Suggestion: Before performing this operation, ensure that the modification is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

Chang the MTU of the bond port whose name is "bond_1\_1".

```text
admin:/>change bond_port general bond_port_name=bond_1_1 mtu=4000
DANGER:You are about to modify the MTU settings for the bond port. This operation may interrupt services or cause service exceptions.
Suggestion: Before performing this operation, ensure that the modification is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
