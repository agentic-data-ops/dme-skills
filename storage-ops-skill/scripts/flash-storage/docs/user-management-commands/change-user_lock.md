# change user_lock


##### Function

The **change user_lock** command is used to lock a user. If you want to prevent a user from logging in to a storage system, use this command.

##### Format

**change user_lock** user_name=?

##### Parameters

| Parameter   | Description     | Value                                                                                                                       |
|-------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------|
| user_name=? | Name of a user. | The value contains 5 to 32 ASCII characters, including digits, letters, and underscores (\_), and must start with a letter. |

##### Usage Guidelines

You can run "change user_unlock" to unlock a user.

##### Example

Lock local administrator "testuser".

```text
admin:/>change user_lock user_name=testuser
Command executed successfully.
```

Lock local remote device administrator "testuser".

```text
admin:/>change user_lock user_name=testuser
DANGER: You are about to perform an operation that affects remote replication and HyperMetro services. If the remote device administrator is locked, deleted, or taken offline, or needs to modify the password upon the next login, or you disable the password always valid function, enable password initialization, or deselect the RESTful login mode for the administrator, the administrator cannot authenticate remote replication and HyperMetro services.
Suggestion: Do not perform the preceding operations on the remote device administrator.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
