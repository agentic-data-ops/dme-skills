# show windows_group ad_group


##### Function

The **show windows_group ad_group** command is used to show information about AD domain user groups in a Windows user group.

##### Format

**show windows_group ad_group** group_name=?

##### Parameters

| Parameter    | Description                     | Value                                   |
|--------------|---------------------------------|-----------------------------------------|
| group_name=? | Name of the Windows user group. | The value contains 1 to 256 characters. |

##### Usage Guidelines

None

##### Example

Show information about AD domain user groups in a Windows user group.

```text
admin:/>show windows_group ad_group group_name=groupWindows
Group Name Account Type
---------- --------------
vendor\group01 AD Group
```

##### System Response

The following table describes the parameter meanings.

| Parameter  | Meaning               |
|------------|-----------------------|
| Group Name | Name of the AD group. |
| User Rid   | RID of the AD group.  |
