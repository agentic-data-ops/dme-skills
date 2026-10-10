# show windows_group windows_user


##### Function

The **show windows_group windows_user** command is used to show information about Windows users in a Windows user group.

##### Format

**show windows_group windows_user** group_name=?

##### Parameters

| Parameter    | Description                     | Value                                   |
|--------------|---------------------------------|-----------------------------------------|
| group_name=? | Name of the Windows user group. | The value contains 1 to 256 characters. |

##### Usage Guidelines

None

##### Example

Show information about Windows users in a Windows user group.

```text
admin:/>show windows_group windows_user group_name=groupWindows
User Rid     User Name
10001        userWindows
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                    |
|-----------|----------------------------|
| User Rid  | RID of the Windows user.   |
| User Name | Name of the Windows group. |
