# remove unix_group_member


##### Function

The **remove unix_group_member** command is used to remove a UNIX user from a UNIX group.

##### Format

**remove unix_group_member** group_name=? user_name=?

##### Parameters

| Parameter    | Description             | Value                                                                                                                                                                     |
|--------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| group_name=? | Name of the UNIX group. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |
| user_name=?  | Name of the UNIX user.  | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |

##### Usage Guidelines

None

##### Example

Remove a UNIX user from a UNIX group.

```text
admin:/>remove unix_group_member group_name=gp1 user_name=user01
Command executed successfully.
```

##### System Response

None
