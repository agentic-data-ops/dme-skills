# delete unix_user


##### Function

The **delete unix_user** command is used to delete a UNIX user.

##### Format

**delete unix_user** name=?

##### Parameters

| Parameter | Description            | Value                                                                                                                                                                     |
|-----------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?    | Name of the UNIX user. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |

##### Usage Guidelines

None

##### Example

Query a UNIX user.

```text
admin:/>show unix_user general
User ID User Name Primary Group Name User Type
------- --------- ------------------ ---------
100006  user01    group1             Create
100007  user02    group1             Create
100008  user03    default_group      Create
100009  user04    default_group      Create
```

Delete a UNIX user.

```text
admin:/>delete unix_user name=user01
WARNING: You are going to delete UNIX user. This operation may cause access exceptions.
Suggestion: Before you perform this operation, determine whether the delete is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query a UNIX user.

```text
admin:/>show unix_user general
User ID User Name Primary Group Name User Type
------- --------- ------------------ ---------
100007  user02    group1             Create
100008  user03    default_group      Create
100009  user04    default_group      Create
```

##### System Response

None
