# show vlan general


##### Function

The **show vlan general** command is used to check existing VLANs and their properties.

##### Format

**show vlan general** \[ name=? \]

**show vlan general** \[ object_type=? { object_id=? \| object_name=? } \]

##### Parameters

| Parameter     | Description  | Value                                                                                                                                                                        |
|---------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?        | VLAN name.   | To obtain the value, run the "**show vlan general**" command. |
| object_type   | Object type. | To obtain the value, run the "**show vlan general**" command. |
| object_id     | Object ID.   | To obtain the value, run the "**show vlan general**" command. |
| object_name=? | Object name. | The value contains 1 to 255 characters, including digits, letters, underscores (\_), hyphens (-), and periods (.).                                                           |

##### Usage Guidelines

None

##### Example

Check the properties of all VLANs.

```text
admin:/>show vlan general

Name             Running Status VLAN ID MTU  Port Type  Port ID

---------------- -------------- ------- ---- ---------- --------------
CTE0.IOM.H1.P0.1 Link Down      1       1500 ETH        CTE0.IOM.H1.P0
CTE0.IOM.H1.P1.1 Link Down      1       1500 ETH        CTE0.IOM.H1.P1

```

Check the properties of a specific VLAN.

```text
admin:/>show vlan general name=CTE0.IOM.H1.P0.1
Name : CTE0.IOM.H1.P0.1
Running Status : Link Down
VLAN ID : 1
MTU : 1500
Port Type : ETH
Port ID : CTE0.IOM.H1.P0
```

Check objects associated with a VLAN.

```text
admin:/>show vlan general object_type=failovergroup object_id=0
Name             Running Status VLAN ID MTU  Port Type  Port ID
---------------- -------------- ------- ---- ---------- --------------
CTE0.IOM.H1.P0.1 Link Down      1       1500 ETH        CTE0.IOM.H1.P0
CTE0.IOM.H1.P1.1 Link Down      1       1500 ETH        CTE0.IOM.H1.P1
```

Check objects associated with a VLAN.

```text
admin:/>show vlan general object_type=failovergroup object_name=System-defined
Name             Running Status VLAN ID MTU  Port Type  Port ID
---------------- -------------- ------- ---- ---------- --------------
CTE0.IOM.H1.P0.1 Link Down      1       1500 ETH        CTE0.IOM.H1.P0
CTE0.IOM.H1.P1.1 Link Down      1       1500 ETH        CTE0.IOM.H1.P1
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                             |
|----------------|-------------------------------------|
| Name           | VLAN name.                          |
| Running Status | Running status of the VLAN.         |
| VLAN ID        | VLAN ID.                            |
| MTU            | MTU of the VLAN.                    |
| Port Type      | Type of the VLAN port.              |
| Port ID        | ID of the port created by the VLAN. |
