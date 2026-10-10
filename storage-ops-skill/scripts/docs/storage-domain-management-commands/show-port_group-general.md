# show port_group general


##### Function

The **show port_group general** command is used to query information about port groups.

##### Format

**show port_group general** \[ port_group_id=? \| port_group_name=? \]

##### Parameters

| Parameter         | Description                                  | Value                                                                                                                                                                                                 |
|-------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port_group_id=?   | ID of a port group that you want to query.   | To obtain the value, run "**show port_group general**" without parameters. |
| port_group_name=? | Name of a port group that you want to query. | To obtain the value, run "**show port_group general**" without parameters. |

##### Usage Guidelines

None.

##### Example

Query information about all port groups.

```text
admin:/>show port_group general

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
