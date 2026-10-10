# show windows_user general


##### Function

The **show windows_user general** command is used to query information of Windows users.

##### Format

**show windows_user general** \[ rid=? \| name=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rid=? | RID of a Windows user. | The value ranges from 0 to 4,294,967,295. |
| name=? | Name of a Windows user. | The value consists of the minimal length of a user name (view the minimum length by running the "show windows_user safe_strategy" command) to 20 characters, and cannot contain spaces, control characters, or any of the following special characters: "/\][:;|=,+*?<>@. The last character cannot be a period (.).<br>Run the "show windows_user general" command to query the resource users in the current system. |

##### Usage Guidelines

None

##### Example

Query information of Windows users.

```text
admin:/>show windows_user general
User RID User Name Status Enabled Passwd Expired Time(Days) Privileges
------- --------- ---------------- ------------------ ------------------
1001   user01       true        180        None
1002   user02       true        180        None
1003   user03       true        180        None
1004   user04       true        180        SeSecurityPrivilege
```

Query information of a Windows user by RID.

```text
admin:/>show windows_user general rid=100008
User RID User Name Status Enabled Passwd Expired Time(Days) Privileges
------- --------- ---------------- ------------------ ------------------
100008   user03     true              180             None
```

Query information of a Windows user by name.

```text
admin:/>show windows_user general name=user03
User RID User Name Status Enabled Passwd Expired Time(Days) Privileges
------- --------- ---------------- ------------------ ------------------
100008   user03     true              180             SeSecurityPrivilege,SeAntiVirusPrivilege
```

##### System Response

The following table describes the parameter meanings.

| Parameter                 | Meaning                                    |
|---------------------------|--------------------------------------------|
| User RID                  | RID of a Windows user.                     |
| User Name                 | Name of a Windows user.                    |
| Status Enabled            | Status of a Windows user.                  |
| Passwd Expired Time(Days) | Remaining validity period of the password. |
| Privileges                | Windows user privileges.                   |
