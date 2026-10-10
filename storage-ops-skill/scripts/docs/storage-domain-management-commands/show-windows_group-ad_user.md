# show windows_group ad_user


##### Function

The **show windows_group ad_user** command is used to show information about AD domain users in a Windows user group.

##### Format

**show windows_group ad_user** group_name=?

##### Parameters

| Parameter    | Description                     | Value                                   |
|--------------|---------------------------------|-----------------------------------------|
| group_name=? | Name of the Windows user group. | The value contains 1 to 256 characters. |

##### Usage Guidelines

None

##### Example

Show information about AD domain users in a Windows user group.

```text
admin:/>show windows_group ad_user group_name=groupWindows
User Name Account Type
---------- --------------
vendor\user01 AD User
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                   |
|-----------|---------------------------|
| User Name | Name of the Windows user. |
| User Rid  | RID of the Windows user.  |
