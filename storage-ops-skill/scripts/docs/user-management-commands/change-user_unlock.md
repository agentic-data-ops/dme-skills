# change user_unlock


##### Function

The **change user_unlock** command is used to unlock a user. If you want to allow a restricted user to log in to a storage system, use this command.

##### Format

**change user_unlock** user_name=?

##### Parameters

| Parameter   | Description     | Value                                                                                                                       |
|-------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------|
| user_name=? | Name of a user. | The value contains 5 to 32 ASCII characters, including digits, letters, and underscores (\_), and must start with a letter. |

##### Usage Guidelines

None

##### Example

Unlock local administrator "testuser".

```text
admin:/>change user_unlock user_name=testuser
Password:**********
Command executed successfully.
```

##### System Response

None
