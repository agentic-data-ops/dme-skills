# delete rep_port_group


##### Function

The **delete rep_port_group** command is used to delete a replication port group.

##### Format

**delete rep_port_group** \[name=? \| id=?\]

##### Parameters

| Parameter | Description                       | Value                                                   |
|-----------|-----------------------------------|---------------------------------------------------------|
| name=?    | Name of a replication port group. | To obtain the value, run "show rep_port_group general". |
| id=?      | ID of a replication port group.   | To obtain the value, run "show rep_port_group general". |

##### Usage Guidelines

None

##### Example

Delete a replication port group.

```text
admin:/>delete rep_port_group name=fcgroup
Command executed successfully.
```

##### System Response

None
