# show windows_user safe_strategy


##### Function

The **show windows_user safe_strategy** command is used to view the password and login policies of the Windows user.

##### Format

**show windows_user safe_strategy**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the password and login policies of the Windows user.

```text
admin:/>show windows_user safe_strategy
Password Min Length : 8
Password Max Length : 16
Password Complex : Normal
Reduplicate Char Count : 3
Password Incorrect Times : 3
Pwd Valid Period(Days) : 90
Modify Pwd Valid Period(Minutes) : 5
Inactive Lock Interval(Days) : 60
Name Length Limit : 6
SID Prefix : S-1-6-88
```

##### System Response

The following table describes the parameter meanings.

| Parameter                        | Meaning                                                            |
|----------------------------------|--------------------------------------------------------------------|
| Password Min Length              | Minimum length of a password.                                      |
| Password Max Length              | Maximum length of a password.                                      |
| Pwd Valid Period(Days)           | Password validity period.                                          |
| Reduplicate Char Count           | Maximum number of consecutive same characters in a password.       |
| Password Incorrect Times         | Allowed times for entering incorrect passwords.                    |
| Inactive Lock Interval(Days)     | Number of days before an inactive account is automatically locked. |
| Modify Pwd Valid Period(Minutes) | Minimum interval between password changes.                         |
| Password Complex                 | Password complexity.                                               |
| Name Length Limit                | Minimal length of a user name.                                     |
