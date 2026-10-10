# delete weak_password


##### Function

The **delete weak_password** command is used to delete a weak password from the weak password dictionary.

##### Format

**delete weak_password** weak_password=?

##### Parameters

| Parameter       | Description                  | Value                                                                                                                                                                                                         |
|-----------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| weak_password=? | Weak password to be deleted. | You can run the "show weak_password_dictionary" command to query all weak passwords in the current weak password dictionary. The value is a non-null character string of a maximum of 32 characters in a row. |

##### Usage Guidelines

-   After the command is executed successfully, the current weak password dictionary does not contain the specified weak password.
-   If the weak password is not stored in the current weak password dictionary, a success message is returned.

##### Example

Delete weak password "Admin@123" from the weak password dictionary.

```text
admin:/>delete weak_password weak_password=Admin@123
Command executed successfully.
```

##### System Response

None
