# change windows_user general


##### Function

The **change windows_user general** command is used to change the configuration of a Windows user.

##### Format

**change windows_user general** { name=? \| rid=? } { status_enabled=? \| new_name=? \| description=? \| privileges=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rid=? | RID of a Windows user. | The value ranges from 1000 to 4,294,967,295. |
| name=? | Name of a Windows user. | The value consists of the minimal length of a user name (view the minimum length by running the "show windows_user safe_strategy" command) to 20 characters, and cannot contain spaces, control characters, or any of the following special characters: "/\][:;|=,+*?<>@. The last character cannot be a period (.). Run the "show windows_user general" command to query the windows users in the current system. |
| description=? | New description of a Windows user. | The value contains 0 to 255 characters. |
| new_name=? | New name of a Windows user. | The value consists of the minimal length of a user name (view the minimum length by running the "show windows_user safe_strategy" command) to 20 characters, and cannot contain spaces, control characters, or any of the following special characters: "/\][:;|=,+*?<>@. The last character cannot be a period (.). Run the "show windows_user general" command to query the windows users in the current system. |
| status_enabled=? | Whether the Windows user is enabled. | The value can be "true" or "false", where: <br>"true": Enable the Windows user.<br>false: Disable the Windows user. |
| privileges=? | Windows user privileges. | The options are as follows: <br>"None": no privilege.<br>"SeSecurityPrivilege": privilege to operate the SACL.<br>"SeAntiVirusPrivilege": permission to perform antivirus scanning. |

##### Usage Guidelines

None

##### Example

Modify Windows user information.

```text
admin:/>change windows_user general name=userWindows status_enabled=false privileges=None
Command executed successfully.
```

##### System Response

None
