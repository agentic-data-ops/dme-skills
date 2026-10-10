# create windows_group general


##### Function

The create windows_group command is used to create a Windows group.

##### Format

**create windows_group general** name=? \[ rid=? \| description=? \| privileges=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of the Windows group. | The value consists of 1 to 256 characters, and cannot contain control characters or any of the following special characters: "/\][:;|=,+*?<>@. The last character cannot be a period (.). |
| rid=? | RID of the Windows group. | The value ranges from 1000 to 429,496,729,5. |
| description=? | Description of the Windows group. | The value consists of 1 to 255 characters. |
| privileges=? | Windows user group privileges. | The options are as follows: <br>"None": no privilege.<br>"SeSecurityPrivilege": privilege to operate the SACL.<br>"SeAntiVirusPrivilege": permission to perform antivirus scanning. |

##### Usage Guidelines

None

##### Example

Create a windows group.

```text
admin:/>create windows_group general name=groupWindows rid=100001 privileges=SeSecurityPrivilege
Command executed successfully.
```

##### System Response

None
