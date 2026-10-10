# add windows_group ad_group


##### Function

The **add windows_group ad_group** command is used to add a domain user group to a Windows user group.

##### Format

**add windows_group ad_group** name=? group_name=?

##### Parameters

| Parameter    | Description                     | Value                                   |
|--------------|---------------------------------|-----------------------------------------|
| name=?       | Name of the domain user group.  | The value contains 1 to 256 characters. |
| group_name=? | Name of the Windows user group. | The value contains 1 to 256 characters. |

##### Usage Guidelines

None

##### Example

Add a domain user group to a local Windows group.

```text
admin:/>add windows_group ad_group name=vendor\\group01 group_name=groupWindows
Command executed successfully.
```

##### System Response

None
