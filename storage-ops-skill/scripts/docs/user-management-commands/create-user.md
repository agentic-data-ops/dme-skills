# create user


##### Function

The **create user** command is used to **create user**s or user groups. You can **create user**s in different roles to manage and utilize the storage system by running this command.

##### Format

**create user** type=? user_name=? role_id=? \[ password_never_expire=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Type of a user. | The value can be "local", "domain_user", or "domain_group", where: <br>"local": local user.<br>"domain_user": domain user.<br>"domain_group": domain user group. |
| user_name=? | Name of a user or user group. | For a local user, the value must start with a letter and contain 5 to 32 ASCII characters including digits, letters, and underscores (_).<br>For a domain user or a domain group, the value is 1 to 64 ASCII characters. The start and end characters cannot be spaces (spaces are expressed in "\s"), and cannot contain double quotation marks ("), single quotation marks ('), question marks (?), number signs (#), asterisks (*), colons (:), left parentheses ((), and right parentheses ()). |
| role_id=? | User role ID. | In the system view, you can run the "show role system" command to obtain the system group role. |
| password_never_expire=? | Sets a user password to never expire. If this parameter is set, the user password does not expire. This parameter can be set only when "type" is set to "local". | The value is "yes". |

##### Usage Guidelines

-   This command provides an interactive mode for entering passwords. When you are entering a password, characters are displayed behind asterisks (\*).
-   The password contains 8 to 16 case-sensitive characters.
-   The password must contain special characters including \` \~ ! @ \# $ % ^ & \* ( ) - \_ = + \\ \| \[ { } \] ; :' " , \< . \> / ? and spaces.
-   The password must meet password complexity requirements:
-   When "password complex" is set to "Normal", the password must contain at least two of the following three: lowercase characters, uppercase characters, and digits.
-   when "password complex" is set to "High", the password must contain lowercase characters, uppercase characters, and digits.
-   The password must be different from the user name and user name in reversed order.
-   The password cannot contain three consecutive deduplicate characters.

 

You can run the "change safe_strategy" command to change the password and login policies of a storage system.

##### Example

Create local account "testuser".

```text
admin:/>create user type=local user_name=testuser role_id=2
Password:*********
Reenter password:*********
Command executed successfully.
```

##### System Response

None
