# create unix_user general


##### Function

The **create unix_user general** command is used to create a UNIX user.

##### Format

**create unix_user general** name=? primary_group_name=? \[ id=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of the UNIX user. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (_). The name cannot start with a hyphen (-). |
| primary_group_name=? | Name of the primary group to which the UNIX user belongs. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (_). The name cannot start with a hyphen (-). |
| id=? | ID of the UNIX user. | The value ranges from 0 to 4,294,967,295. Run the "show unix_user general" command to query the UNIX users in the current system. |
| description=? | Indicates the description. | The value contains 0 to 255 characters. |

##### Usage Guidelines

None

##### Example

Create a UNIX user.

```text
admin:/>create unix_user general name=user01 primary_group_name=group1
Command executed successfully.
```

Query a UNIX user.

```text
admin:/>show unix_user general
User ID User Name Primary Group Name User Type
------- --------- ------------------ ---------
100006  user01    group1             Create
```

##### System Response

None
