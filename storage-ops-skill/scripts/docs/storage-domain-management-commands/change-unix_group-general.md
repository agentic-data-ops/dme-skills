# change unix_group general


##### Function

The **change unix_group general** command is used to change the configuration of a UNIX group.

##### Format

**change unix_group general** name=? { description=? id=? } \*

##### Parameters

| Parameter     | Description             | Value                                                                                                                                                                     |
|---------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?        | Name of the UNIX group. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |
| id=?          | ID of the UNIX group.   | The value ranges from 0 to 4,294,967,295.                                                                                                                                 |
| description=? | Description.            | The value contains 0 to 255 characters.                                                                                                                                   |

##### Usage Guidelines

None

##### Example

Query the UNIX user group before the modification.

```text
admin:/>show unix_group general name=group1
Group ID : 100001
Group Name : group1
Description :
Group Type : Create
```

Modify a UNIX user group's information.

```text
admin:/>change unix_group general name=group1 description=unix_group_des id=123
Command executed successfully.
```

Query the modified UNIX user group.

```text
admin:/>show unix_group general name=group1
Group ID : 123
Group Name : group1
Description : unix_group_des
Group Type : Create
```

##### System Response

None
