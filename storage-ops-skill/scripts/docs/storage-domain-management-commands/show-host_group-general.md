# show host_group general


##### Function

The **show host_group general** command is used to query basic information about host groups.

##### Format

**show host_group general** \[ host_group_id=? \| host_group_name=? \]

##### Parameters

| Parameter         | Description      | Value                                                                                                                                                                                                 |
|-------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| host_group_id=?   | Host group ID.   | To obtain the value, run "**show host_group general**" without parameters. |
| host_group_name=? | Host group name. | To obtain the value, run "**show host_group general**" without parameters. |

##### Usage Guidelines

-   The "**show host_group general**" command is executed to query information about all host groups.
-   The "**show host_group general** host_group_id=?" command is executed to query information about a specified host group.

##### Example

Query information about all host groups.

```text
admin:/>show host_group general

ID  Name
--  -------------
0   host_group001
1   host_group002
```

Query information about host group "1".

```text
admin:/>show host_group general  host_group_id=1

ID  Name             vStore ID
--  -------------    ----------
1   host_group001    1
```

Query information about host group "host_group001".

```text
admin:/>show host_group general  host_group_name=host_group001

ID  Name             vStore ID
--  -------------    ----------
1   host_group001    1
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning               |
|-----------|-----------------------|
| ID        | ID of a host group.   |
| Name      | Name of a host group. |
