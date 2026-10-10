# change unix_user general


##### Function

The **change unix_user general** command is used to change the configuration of a UNIX user.

##### Format

**change unix_user general** name=? { primary_group_name=? \| description=? id=? } \*

##### Parameters

| Parameter            | Description                                  | Value                                                                                                                                                                     |
|----------------------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?               | Name of the UNIX user.                       | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |
| id=?                 | ID of the UNIX user.                         | The value ranges from 0 to 4,294,967,295.                                                                                                                                 |
| primary_group_name=? | Primary group associated with the UNIX user. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |
| description=?        | Description.                                 | The value contains 0 to 255 characters.                                                                                                                                   |

##### Usage Guidelines

None

##### Example

Query the original UNIX user.

```text
admin:/>show unix_user general name=user01
User ID : 100006
User Name : user01
Description :
Primary Group ID : 100001
Primary Group Name : group1
Secondary Group Names :
User Type : Create
```

Modify a UNIX user's information.

```text
admin:/>change unix_user general name=user01 primary_group_name=group2
Command executed successfully.
```

Query the modified UNIX user.

```text
admin:/>show unix_user general name=user01
User ID : 100006
User Name : user01
Description :
Primary Group ID : 100002
Primary Group Name : group2
Secondary Group Names :
User Type : Create
```

##### System Response

None
