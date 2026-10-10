# remove windows_group ad_user


##### Function

The **remove windows_group ad_user** command is used to remove an AD domain user from a Windows user group.

##### Format

**remove windows_group ad_user** name=? group_name=?

##### Parameters

| Parameter    | Description                     | Value                                      |
|--------------|---------------------------------|--------------------------------------------|
| name=?       | Name of the AD domain user.     | The value consists of 1 to 256 characters. |
| group_name=? | Name of the Windows user group. | The value consists of 1 to 256 characters. |

##### Usage Guidelines

None

##### Example

Remove an AD domain user from a Windows user group.

```text
admin:/>remove windows_group ad_user name=vendor\\user01 group_name=groupWindows
Command executed successfully.
```

##### System Response

None
