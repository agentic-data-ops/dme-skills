# change domain ad_prefdc


##### Function

The **change domain ad_prefdc** command is used to modify information about the preferred domain controller.

##### Format

**change domain ad_prefdc** { dc_name=? \| clear_dc_name=? }

##### Parameters

| Parameter       | Description                                                   | Value                                                                                           |
|-----------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| dc_name=?       | Name of the preferred domain controller.                      | The value is a string of 1 to 255 characters.                                                   |
| clear_dc_name=? | Whether to clear the name of the preferred domain controller. | The value is "yes", indicating that the name of the prefered domain controller will be cleared. |

##### Usage Guidelines

None

##### Example

Check the pre-modified information about the preferred domain controller.

```text
admin:/>show domain ad_prefdc
Domain Controller Name : testname
```

Modify the information about the preferred domain controller.

```text
admin:/>change domain ad_prefdc dc_name=changename
Command executed successfully.
```

Check the post-modified information about the preferred domain controller.

```text
admin:/>show domain ad_prefdc
Domain Controller Name : changename
```

Clear the information about the preferred domain controller.

```text
admin:/>change domain ad_prefdc clear_dc_name=yes
Command executed successfully.
```

Check the post-clear information about the preferred domain controller.

```text
admin:/>show domain ad_prefdc
Domain Controller Name : --
```

##### System Response

None
