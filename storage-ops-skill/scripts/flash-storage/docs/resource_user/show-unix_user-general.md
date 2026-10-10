# show unix_user general


##### Function

The **show unix_user general** command is used to query the information of UNIX users.

##### Format

**show unix_user general** \[ name=? \]

##### Parameters

| Parameter | Description            | Value                                                                                                                                                                     |
|-----------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?    | Name of the UNIX user. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |

##### Usage Guidelines

None

##### Example

Query information about all UNIX users.

```text
admin:/>show unix_user general
User ID User Name Primary Group Name User Type
------- --------- ------------------ ---------
100006  user01    group1             Create
100007  user02    group1             Create
100008  user03    default_group      Create
100009  user04    default_group      Create
```

Query information about a specified UNIX user by name.

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

##### System Response

The following table describes the parameter meanings.

| Parameter             | Meaning                                   |
|-----------------------|-------------------------------------------|
| User ID               | UNIX user ID.                             |
| User Name             | UNIX user name.                           |
| Description           | Description.                              |
| Primary Group ID      | Primary group ID of a UNIX user.          |
| Primary Group Name    | Primary group name of a UNIX user.        |
| Secondary Group Names | Secondary group name list of a UNIX user. |
| User Type             | UNIX user type.                           |
