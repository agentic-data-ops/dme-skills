# create unix_group


##### Function

The **create unix_group** command is used to create a UNIX group.

##### Format

**create unix_group** name=? \[ id=? \] \[ description=? \]

##### Parameters

| Parameter   | Description             | Value                                                                                                                                                                     |
|-------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?      | Name of the UNIX group. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |
| id=?        | ID of the UNIX group.   | The value ranges from 0 to 4,294,967,295.                                                                                                                                 |
| description | Description.            | The value contains 0 to 255 characters.                                                                                                                                   |

##### Usage Guidelines

None

##### Example

Create a UNIX group.

```text
admin:/>create unix_group name=group1 id=100001
Command executed successfully.
```

Query all UNIX groups.

```text
admin:/>show unix_group general
Group ID Group Type Group Name
-------- ---------- ----------
99999    Default    Administrators
100000   Default    default_group
100001   Create     group1
```

##### System Response

None
