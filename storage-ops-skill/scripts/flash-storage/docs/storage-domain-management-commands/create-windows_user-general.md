# create windows_user general


##### Function

The **create windows_user general** command is used to create a Windows user.

##### Format

**create windows_user general** name=? \[ rid=? \| description=? \| status_enable=? \| privileges=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a Windows user. | The value consists of the minimal length of a user name (view the minimum length by running the "show windows_user safe_strategy" command) to 20 characters, and cannot contain spaces, control characters, or any of the following special characters: "/\][:;|=,+*?<>@. The last character cannot be a period (.). Run the "show windows_user general" command to query the Windows users in the current system. |
| description=? | Whether the Windows user is enabled. | The value contains 0 to 255 characters. |
| status_enable=? | Status of a Windows user. | The value can be "yes" or "no", where: <br>"true": Enable the Windows user.<br>"false": Disable the Windows user. |
| rid=? | RID of a Windows user. | The value ranges from 1000 to 429,496,729,5. Run the "show windows_user general" command to query the Windows users in the current system. |
| password | User password. | The value contains 6 to 32 characters.<br>"Normal": The password contains at least any two types of special characters, uppercase letters, lowercase letters, and digits. Special characters include `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and spaces.<br>"High": The password must contain special characters, and at least any two types of uppercase letters, lowercase letters, and digits. Special characters include `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and spaces.<br>A character can be consecutively used three times at most in a password.<br>The value must be different from the user name or reversed user name. |
| reenter password | User password. | The value contains 6 to 32 characters.<br>"Normal": The password contains at least any two types of special characters, uppercase letters, lowercase letters, and digits. Special characters include `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and spaces.<br>"High": The password must contain special characters, and at least any two types of uppercase letters, lowercase letters, and digits. Special characters include `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and spaces.<br>A character can be consecutively used three times at most in a password.<br>The value must be different from the user name or reversed user name. |
| privileges=? | Windows user privileges. | The options are as follows: <br>"None": no privilege.<br>"SeSecurityPrivilege": privilege to operate the SACL.<br>"SeAntiVirusPrivilege": permission to perform antivirus scanning. |

##### Usage Guidelines

None

##### Example

Create a Windows user.

```text
admin:/>create windows_user general name=userWindows privileges=None
Password:********
Reenter password:********
Command executed successfully.
```

##### System Response

None
