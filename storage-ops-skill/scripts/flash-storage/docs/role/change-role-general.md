# change role general


##### Function

The **change role general** command is used to modify basic information about roles.

##### Format

**change role general** id=? { name=? \| description=? }

##### Parameters

| Parameter     | Description                                           | Value                                                                                      |
|---------------|-------------------------------------------------------|--------------------------------------------------------------------------------------------|
| id=?          | Role ID. The value must be an integer from 1 to 1023. | To obtain the value, run the "show role system" command.                                   |
| name=?        | New role name.                                        | The name contains 1 to 63 letters, digits, underscores (\_), periods (.), and hyphens (-). |
| description=? | New description name.                                 | The description contains a maximum of 255 characters.                                      |

##### Usage Guidelines

None

##### Example

Change the name of the role whose ID is "65" to "testrole".

```text
admin:/>change role general id=65 name=testrole
Command executed successfully.
```

##### System Response

None
