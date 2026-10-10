# show windows_group general


##### Function

The **show windows_group general** command is used to query information of Windows user groups.

##### Format

**show windows_group general** \[ name=? \| rid=? \]

##### Parameters

| Parameter | Description                   | Value                                                                                                                                                                                           |
|-----------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?    | Name of a Windows user group. | The value consists of 1 to 256 characters, and cannot contain control characters or any of the following special characters: /\\\]\[:;\|=,+\*?\<\>@. The last character cannot be a period (.). |
| rid=?     | RID of a Windows user group.  | The value ranges from 0 to 4,294,967,295.                                                                                                                                                       |

##### Usage Guidelines

None

##### Example

Query information of Windows groups.

```text
admin:/>show windows_group general
Group RID  Group Name         Group Type  Privileges
---------  -----------------  ----------  -------------------
544        Administrators     default     SeSecurityPrivilege
545        Users              default     None
546        Guests             default     None
547        Power Users        default     None
548        Account Operators  default     None
549        Server Operators   default     None
550        Print Operators    default     None
551        Backup Operators   default     None
552        Replicator         default     None
100001     groupWindows       create      SeSecurityPrivilege,SeAntiVirusPrivilege
```

##### System Response

The following table describes the parameter meanings.

| Parameter  | Meaning                         |
|------------|---------------------------------|
| Group RID  | RID of the Windows user group.  |
| Group Name | Name of the Windows user group. |
| Group Type | Windows user group type.        |
| Privileges | Windows user group privileges.  |
