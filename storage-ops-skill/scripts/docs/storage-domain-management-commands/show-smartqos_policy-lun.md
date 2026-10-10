# show smartqos_policy lun


##### Function

The **show smartqos_policy lun** command is used to query information about LUNs in a specified SmartQoS policy.

##### Format

**show smartqos_policy lun** smartqos_policy_id=?

##### Parameters

| Parameter            | Description              | Value                                                    |
|----------------------|--------------------------|----------------------------------------------------------|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |

##### Usage Guidelines

Run the "**show smartqos_policy lun** smartqos_policy_id=?" command to query LUN information of a specified SmartQoS policy.

##### Example

Query information about LUNs in SmartQoS policy "0".

```text
admin:/>show smartqos_policy lun smartqos_policy_id=0

ID  Name        Storage Pool ID  Capacity    Health Status
--  ----------  ---------------  ----------  -------------
0   LUN000      0                   5.000GB  Normal
1   LUN001      0                  10.000GB  Normal
2   LUN002      0                   5.000GB  Normal
3   LUN003_001  0                   5.000GB  Normal
Running Status  Type   WWN
--------------  -----  --------------------------------
Online          Thick  63334371003638390003c20c00000000
Online          Thick  63334371003638390003cda700000001
Online          Thick  63334371003638390003d33300000002
Online          Thick  63334371003638390003dd4700000003
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                   |
|-----------------|-------------------------------------------|
| ID              | LUN ID.                                   |
| Name            | LUN name.                                 |
| Storage Pool ID | ID of the storage pool where LUNs reside. |
| Capacity        | LUN capacity.                             |
| Health Status   | Health status.                            |
| Running Status  | Running status.                           |
| Type            | LUN type.                                 |
| WWN             | World Wide Name (WWN) of the LUN.         |
