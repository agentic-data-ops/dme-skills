# change protect_group


##### Function

The **change protect_group** command is used to modify the parameters of a protection group.

##### Format

**change protect_group** protect_group_id=? \[ name=? \] \[ description=? \]

##### Parameters

| Parameter        | Description                     | Value                                                                                                             |
|------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------|
| protect_group_id | Protection group ID.            | To obtain the value, run the "show protect_group general" command.                                                |
| name             | Modified protection group name. | The value contains 1 to 255 characters including digits, letters, underscores (\_), hyphens (-), and periods (.). |
| description      | Description.                    | The value contains 1 to 255 characters.                                                                           |

##### Usage Guidelines

None

##### Example

Modify the name of the protection group whose ID is 2 to "test".

```text
admin:/>change protect_group protect_group_id=2 name=test
Command executed successfully.
```

##### System Response

None
