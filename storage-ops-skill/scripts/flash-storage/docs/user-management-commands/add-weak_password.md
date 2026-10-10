# add weak_password


##### Function

The **add weak_password** command is used to add a user-defined weak password to the weak password dictionary.

##### Format

**add weak_password** weak_password=?

##### Parameters

| Parameter       | Description                                                | Value                                                   |
|-----------------|------------------------------------------------------------|---------------------------------------------------------|
| weak_password=? | Weak password to be added to the weak password dictionary. | The value contains a maximum of 32 characters in a row. |

##### Usage Guidelines

After the command is executed successfully, the weak password entered by the user is added to the current weak password dictionary.

##### Example

Add weak password "Admin@123" to the weak password dictionary.

```text
admin:/>add weak_password weak_password=Admin@123
Command executed successfully.
```

##### System Response

None
