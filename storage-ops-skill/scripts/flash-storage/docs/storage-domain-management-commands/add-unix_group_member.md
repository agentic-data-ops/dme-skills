# add unix_group_member


##### Function

The **add unix_group_member** command is used to add a UNIX user to a UNIX group.

##### Format

**add unix_group_member** group_name=? user_name=?

##### Parameters

| Parameter    | Description             | Value                                                                                                                                                                     |
|--------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| group_name=? | Name of the UNIX group. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |
| user_name=?  | Name of the UNIX user.  | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |

##### Usage Guidelines

None

##### Example

Add a UNIX user to a UNIX group.

```text
admin:/>add unix_group_member group_name=gp1 user_name=ur01
Command executed successfully.
```

##### System Response

None
