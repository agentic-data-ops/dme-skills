# change lun_consistency_group general


##### Function

The **change lun_consistency_group general** command is used to modify the properties of a LUN consistency group.

##### Format

**change lun_consistency_group general** lun_consistency_group_id=? \[ name=? \] \[ description=? \]

##### Parameters

| Parameter                  | Description                             | Value                                                                                                                    |
|----------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| lun_consistency_group_id=? | ID of a LUN consistency group.          | To obtain the value, run the "show lun_consistency_group general" command.                                               |
| name=?                     | Name of a LUN consistency group.        | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |
| description=?              | Description of a LUN consistency group. | \-                                                                                                                       |

##### Usage Guidelines

You can only modify the name and description of a LUN consistency group.

##### Example

Change the name of a LUN consistency group whose ID is 1.

```text
admin:/>change lun_consistency_group general lun_consistency_group_id=1 name=lunCg1
Command executed successfully.
```

##### System Response

None
