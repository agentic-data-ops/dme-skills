# change windows_group general


##### Function

The **change windows_group general** command is used to change the configuration of a Windows user group.

##### Format

**change windows_group general** { name=? \| rid=? } { new_name=? \| description=? \| privileges=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rid=? | RID of a Windows user group. | The value ranges from 1000 to 4,294,967,295. |
| name=? | Name of a Windows user group. | The value contains a maximum of 256 characters, including uppercase and lowercase letters, digits, and special characters. The value cannot contain any of the following printable characters: " " / \ ] [ : | < > + = ; ? * @ , ". The last character cannot be a period (.). |
| new_name=? | New name of a Windows user group. | The value contains a maximum of 256 characters, including uppercase and lowercase letters, digits, and special characters. The value cannot contain any of the following printable characters: " " / \ ] [ : | < > + = ; ? * @ , ". The last character cannot be a period (.). |
| privileges=? | Windows user group privileges. | The options are as follows: <br>"None": no privilege.<br>"SeSecurityPrivilege": privilege to operate the SACL.<br>"SeAntiVirusPrivilege": permission to perform antivirus scanning. |
| description=? | New description of a Windows user group. | The value contains 0 to 255 characters. |

##### Usage Guidelines

None

##### Example

Modify the information about the Windows user group.

```text
admin:/>change windows_group general name=windowsGroup new_name=newgroup privileges=None
Command executed successfully.
```

##### System Response

None
