# remove windows_group ad_group


##### Function

The **remove windows_group ad_group** command is used to remove an AD domain user group from a Windows user group.

##### Format

**remove windows_group ad_group** name=? group_name=?

##### Parameters

| Parameter    | Description                       | Value                                           |
|--------------|-----------------------------------|-------------------------------------------------|
| name=?       | Name of the AD domain user group. | The value ranges from 1 byte to 256 characters. |
| group_name=? | Name of the Windows user group.   | The value ranges from 1 byte to 256 characters. |

##### Usage Guidelines

None

##### Example

Remove an AD domain user group from a Windows user group.

```text
admin:/>remove windows_group ad_group name=vendor\\group01 group_name=groupWindows
Command executed successfully.
```

##### System Response

None
