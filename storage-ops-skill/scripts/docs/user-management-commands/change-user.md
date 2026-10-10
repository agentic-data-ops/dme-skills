# change user


##### Function

The **change user** command is used to operate users, including resetting users' login passwords, changing user role IDs, forcing users offline, modifying a user's login method, modifying a user's authentication factors, and setting a specified user's password to never expire.

##### Format

**change user** user_name=? { role_id=? \| action=? \| login_method_list=? \| password_never_expire=? \| login_factor=? email=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| user_name=? | User name. | To obtain the value, run "show user". |
| action=? | Operation on the user. | The value can be "reset_password", "offline", or "change_password_next_login", where: <br>"reset_password": resets the user's password.<br>"offline": forces the user offline.<br>"change_password_next_login": changes the user's password upon next login. |
| login_factor=? | Authentication factor type of a user. If this parameter is set to password, only password authentication is required. If this parameter is set to password_emailOTP, both password and one-off email password authentication is required. If this parameter is set to password_radiusOTP, both password and RADIUS one-off password authentication is required. | - |
| role_id=? | New user role ID. | To obtain the value, run "show role system" in the system view. |
| login_method_list=? | Valid login method set for a system user. | The value can be one or multiple of "SFTP", "CLI", "Serial", "DeviceManager", and "RESTful", where multiple values are separated by commas (,). |
| password_never_expire=? | Whether a user password is set to never expire. If this parameter is set to "yes", the password does not expire. If this parameter is set to "no", the password expiration check is performed based on the system security policy. | The value can be "yes" or "no", where: <br>"yes": A password never expires.<br>"no": The setting of a password to never expire is canceled. |
| email=? | Email address for receiving the email one-time password. | - |

##### Usage Guidelines

-   Run the "**change user** user_name=? role_id=?" command to specify a user's role ID. This command can only be used to change the role IDs of non-super administrator users.
-   Run the "**change user** user_name=? action=reset_password" command to reset users' login password. This command can only be used to reset the passwords of non-super administrator users. If the password of a user is entered incorrectly for three consecutive times within five minutes, the user is forced to log out.
-   Run the "**change user** user_name=? action=offline" command to force a specific user offline. This command can only be used to force non-super administrator users offline.
-   Run the "**change user** user_name=? action=change_password_next_login" command to enable a specified user to change its password upon next login. This command can only be used to enable non-super administrator users to change their passwords upon next login.
-   Run the "**change user** user_name=? login_method_list=?" command to set a valid login method for a system user.
-   Run the "**change user** user_name=? password_never_expire=yes" command to set a specified user's password to never expire.
-   Run the "**change user** user_name=? login_factor=?" command to set the authentication factor of a user.

##### Example

Change the role ID of "testuser" to "6".

```text
admin:/>change user user_name=testuser role_id=6
WARNING: You are about to change the user role ID. This operation will change the user's operation permission.
Suggestion: Before performing this operation, ensure that the selected user role ID is correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Reset the login password of "testuser".

```text
admin:/>change user user_name=testuser action=reset_password
New password:**********
Reenter password:**********
Password:**********
Command executed successfully.
```

Force "testuser" offline.

```text
admin:/>change user user_name=testuser action=offline
DANGER: You are about to log off the selected user. After this operation, the user can no longer manage the device unless relogs in to the device.
Suggestion: Before performing this operation, learn about the impact of this operation on the user.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable "testuser" to change its password upon next login.

```text
admin:/>change user user_name=testuser action=change_password_next_login
WARNING: You are about to set changing the password at the next login. The user must change the password upon the next login.
Suggestion: Before performing this operation, learn about the impact of this operation on the user.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Set the login method of "testuser" to "CLI" and "SFTP".

```text
change user user_name=testuser login_method_list=CLI,SFTP
DANGER: You are about to modify the account login method list.
This operation will cause the account to fail to log in to the storage array in methods not recorded in the list.
Suggestion: Before performing this operation, ensure that the login method configuration is correct.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the login method of "testuser".

```text
change user user_name=testuser login_method_list=CLI,SFTP
DANGER: You are about to perform an operation that affects remote replication and HyperMetro services. If the remote device administrator is locked, deleted, or taken offline, or needs to modify the password upon the next login, or you disable the password always valid function, enable password initialization, or deselect the RESTful login mode for the administrator, the administrator cannot authenticate remote replication and HyperMetro services.
Suggestion: Do not perform the preceding operations on the remote device administrator.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Set the password of "testuser" to never expire.

```text
admin:/>change user user_name=testuser password_never_expire=yes
Command executed successfully.
```

Set the authentication factor type of "testuser" to password authentication.

```text
change user user_name=testuser login_factor=password
```

Change the login method of "testuser" to "CLI" and "SFTP".

```text
change user user_name=testuser login_method_list=CLI,SFTP
DANGER: You are about to perform an operation that affects remote replication and HyperMetro services. If the remote device administrator is locked, deleted, or taken offline, or needs to modify the password upon the next login, or you disable the password always valid function, enable password initialization, or deselect the RESTful login mode for the administrator, the administrator cannot authenticate remote replication and HyperMetro services.
Suggestion: Do not perform the preceding operations on the remote device administrator.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
