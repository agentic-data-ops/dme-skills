# show rep_port_group general


##### Function

The **show rep_port_group general** command is used to query information about replication port groups.

##### Format

**show rep_port_group general** \[ rep_port_group_name=? \| rep_port_group_id=? \]

##### Parameters

| Parameter             | Description                       | Value                                                                                                                                                                                      |
|-----------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| rep_port_group_name=? | Name of a replication port group. | To obtain the value, run "**show rep_port_group general**". |
| rep_port_group_id=?   | ID of a replication port group.   | To obtain the value, run "**show rep_port_group general**". |

##### Usage Guidelines

None

##### Example

Query information about all replication port groups.

```text
admin:/>show rep_port_group general

ID  Name

--  -------

0   test120
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning               |
|-----------|-----------------------|
| ID        | ID of a port group.   |
| Name      | Name of a port group. |
