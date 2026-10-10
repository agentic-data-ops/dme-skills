# add windows_group windows_user


##### Function

The **add windows_group windows_user** command is used to add a Windows user to a Windows user group.

##### Format

**add windows_group windows_user** name=? group_name=?

##### Parameters

| Parameter    | Description                     | Value                                   |
|--------------|---------------------------------|-----------------------------------------|
| name=?       | Name of the Windows user.       | The value contains 1 to 20 characters.  |
| group_name=? | Name of the Windows user group. | The value contains 1 to 256 characters. |

##### Usage Guidelines

None

##### Example

Add a Windows user to a Windows user group.

```text
admin:/>add windows_group windows_user name=vendor\\user01 group_name=groupWindows
Command executed successfully.
```

##### System Response

None
