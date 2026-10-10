# remove windows_group windows_user


##### Function

The **remove windows_group windows_user** command is used to remove an Windows user from a Windows user group.

##### Format

**remove windows_group windows_user** name=? group_name=?

##### Parameters

| Parameter    | Description                     | Value                                     |
|--------------|---------------------------------|-------------------------------------------|
| name=?       | Name of the Windows user.       | The value consists of 1 to 20 characters. |
| group_name=? | Name of the Windows user group. | The value contains 1 to 256 characters.   |

##### Usage Guidelines

None

##### Example

Remove an AD domain user from a Windows user group.

```text
admin:/>remove windows_group windows_user name=user01 group_name=group
Command executed successfully.
```

##### System Response

None
