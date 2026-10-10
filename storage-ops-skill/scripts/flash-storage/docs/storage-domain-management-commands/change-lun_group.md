# change lun_group


##### Function

The **change lun_group** command is used to change the name of a LUN group.

##### Format

**change lun_group** { lun_group_id=? \| lun_group_name=? } name=?

##### Parameters

| Parameter        | Description                                        | Value                                                                                        |
|------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------|
| lun_group_id=?   | ID of a LUN group whose name you want to change.   | To obtain the value, run "show lun_group general".                                           |
| lun_group_name=? | Name of a LUN group whose name you want to change. | To obtain the value, run "show lun_group general".                                           |
| name=?           | New name of a LUN group.                           | The value contains 1 to 255 digits, letters, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

None.

##### Example

Change the name of LUN group "2" to "test".

```text
admin:/>change lun_group lun_group_id=2 name=test
Command executed successfully.
```

Change the name of LUN group "lun_group1" to "test".

```text
admin:/>change lun_group lun_group_name=lun_group1 name=test
Command executed successfully.
```

##### System Response

None
