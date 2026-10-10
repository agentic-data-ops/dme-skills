# change vlan general


##### Function

The **change vlan general** command is used to change the VLAN maximum transmission unit.

##### Format

**change vlan general** name=? mtu=?

##### Parameters

| Parameter | Description                     | Value                                                     |
|-----------|---------------------------------|-----------------------------------------------------------|
| name=?    | VLAN name.                      | To obtain the value, run the "show vlan general" command. |
| mtu=?     | VLAN maximum transmission unit. | The value is an integer from 1280 to 9000.                |

##### Usage Guidelines

None

##### Example

Change the maximum transmission unit to "1500".

```text
admin:/>change vlan general name=CTE0.A3.P3.1 mtu=1500
DANGER: You are about to modify the MTU settings for VLAN. This operation may interrupt services or cause service exceptions.
Suggestion: Before you perform this operation, determine whether the modification is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

Check the change.

```text
admin:/>show vlan general name=CTE0.A3.P3.1
Name : CTE0.A3.P3.1
Running Status : Link Down
VLAN ID : 1
MTU : 1500
Port Type : ETH
Port ID : CTE0.A3.P3
```

##### System Response

None
