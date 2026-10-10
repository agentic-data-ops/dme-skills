# change rep_port_group


##### Function

The **change rep_port_group** command is used to modify the information about a replication port group.

##### Format

**change rep_port_group** \[ rep_port_group_name=? \| rep_port_group_id=? \] new_name=?

##### Parameters

| Parameter             | Description                               | Value                                                                                       |
|-----------------------|-------------------------------------------|---------------------------------------------------------------------------------------------|
| rep_port_group_id=?   | ID of a replication port group.           | To obtain the value, run "show rep_port_group general".                                     |
| rep_port_group_name=? | Current name of a replication port group. | To obtain the value, run "show rep_port_group general".                                     |
| new_name=?            | New name of a replication port group.     | The value contains 1 to 31 digits, letters, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

None

##### Example

Change the name of a replication port group.

```text
admin:/>change rep_port_group name=fcgroup new_name=ethGroup
Command executed successfully.
```

##### System Response

None
