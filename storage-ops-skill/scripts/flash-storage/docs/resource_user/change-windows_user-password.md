# change windows_user password


##### Function

The **change windows_user password** command is used to modify the password of a Windows user.

##### Format

**change windows_user password** { rid=? \| name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a Windows user. | The value consists of the minimal length of a user name (view the minimum length by running the "show windows_user safe_strategy" command) to 20 characters, and cannot contain spaces, control characters, or any of the following special characters: "/\][:;|=,+*?<>@. The last character cannot be a period (.). Run the "show windows_user general" command to query the windows users in the current system. |
| rid=? | RID of a Windows user. | The value ranges from 1000 to 4,294,967,295. |
| password | User password. | The password contains 6 to 32 characters.<br>"Normal": The password contains at least any two types of special characters, uppercase letters, lowercase letters, and digits. Special characters include `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and spaces.<br>"High": The password must contain special characters, and at least any two types of uppercase letters, lowercase letters, and digits. Special characters include `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and spaces.<br>A character can be consecutively used three times at most in the password.<br>The password cannot be the same as the user name or reversed user name. |
| reenter password | User password. | The password contains 6 to 32 characters.<br>"Normal": The password contains at least any two types of special characters, uppercase letters, lowercase letters, and digits. Special characters include `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and spaces.<br>"High": The password must contain special characters, and at least any two types of uppercase letters, lowercase letters, and digits. Special characters include `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and spaces.<br>A character can be consecutively used three times at most in the password.<br>The password cannot be the same as the user name or reversed user name. |

##### Usage Guidelines

None

##### Example

Modify the password of a Windows user.

```text
admin:/>change windows_user password name=windowsUser
New Password:**********
Reenter password:**********
Command executed successfully.
```

##### System Response

None
