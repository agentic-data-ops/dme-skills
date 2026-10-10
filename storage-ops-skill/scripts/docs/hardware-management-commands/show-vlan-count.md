# show vlan count


##### Function

The **show vlan count** command is used to query the number of VLANs.

##### Format

**show vlan count** \[ object_type=? \] { object_id=? \| object_name=? }

##### Parameters

| Parameter     | Description                                | Value                                                                                                              |
|---------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| object_type=? | Type of the object associated with a VLAN. | The value is failovergroup.                                                                                        |
| object_id=?   | ID of the object associated with a VLAN.   | The value is an integer between 0 and 8191.                                                                        |
| object_name=? | Object name.                               | The value contains 1 to 255 characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

Parameter object_id must be specified when the parameter object_type is specified.

##### Example

Query the total number of VLANs.

```text
admin:/>show vlan count
VLAN Number : 2
```

View the number of VLANs in the associated group.

```text
admin:/>show vlan count object_type=failovergroup object_name=VLAN-FailoverGroup-10
VLAN Number : 2
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                      |
|-------------|------------------------------|
| VLAN Number | The number of created VLANs. |
