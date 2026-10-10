# delete user


##### Function

The **delete user** command is used to delete a user or user group. You can delete the users that are no longer required for managing and maintaining the storage system by running this command.

##### Format

**delete user** user_name=?

##### Parameters

| Parameter   | Description                                           | Value                                 |
|-------------|-------------------------------------------------------|---------------------------------------|
| user_name=? | Name of a user or user group that you want to delete. | To obtain the value, run "show user". |

##### Usage Guidelines

-   The user or user group that you delete by running this command can no longer log in to the storage system.
-   This command can delete the user.

##### Example

Delete user "testuser".

```text
admin:/>delete user user_name=testuser
DANGER: You are about to remove the selected user. After this operation, the user can no longer log in.
Suggestion: Before performing this operation, check whether the user can be removed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete remote device administrator "testuser".

```text
admin:/>delete user user_name=testuser
DANGER: You are about to perform an operation that affects remote replication and HyperMetro services. If the remote device administrator is locked, deleted, or taken offline, or needs to modify the password upon the next login, or you disable the password always valid function, enable password initialization, or deselect the RESTful login mode for the administrator, the administrator cannot authenticate remote replication and HyperMetro services.
Suggestion: Do not perform the preceding operations on the remote device administrator.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
