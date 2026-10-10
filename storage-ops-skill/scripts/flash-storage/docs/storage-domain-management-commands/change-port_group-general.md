# change port_group general


##### Function

The **change port_group general** command is used to change the name of a port group.

##### Format

**change port_group general** { port_group_id=? \| port_group_name=? } name=?

##### Parameters

| Parameter         | Description                                       | Value                                                                                        |
|-------------------|---------------------------------------------------|----------------------------------------------------------------------------------------------|
| port_group_id=?   | ID of a port group whose name you want to change. | To obtain the value, run "show port_group general".                                          |
| port_group_name=? | Port group name.                                  | To obtain the value, run "show port_group general".                                          |
| name=?            | New name of a port group.                         | The value contains 1 to 255 digits, letters, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

None.

##### Example

Change the name of port group "0" to "test120".

```text
admin:/>change port_group general port_group_id=0 name=test120
Command executed successfully.
```

Change the name of port group "portgroup1" to "test120".

```text
admin:/>change port_group general port_group_name=portgroup1 name=test120
Command executed successfully.
```

##### System Response

None
