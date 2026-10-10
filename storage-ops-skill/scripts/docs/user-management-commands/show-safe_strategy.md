# show safe_strategy


##### Function

The **show safe_strategy** command is used to view the password and login policies of a storage system.

##### Format

**show safe_strategy**

##### Parameters

None

##### Usage Guidelines

None

##### Example

View the current password and login policies of the storage system.

```text
admin:/>show safe_strategy
ID                            : default
Password Min Length           : 8
Password Max Length           : 16
Password Complex              : Normal
Reduplicate Char Count        : 3
Enable Password Lock          : No
Password Lock Time(Minutes)   : 15
Password Incorrect Times      : 3
Session Expired Time(Minutes) : 30
Min Valid Period(Minutes)     : 5
Max Valid Period(Days)        : 90
Prompt Ahead(Days)            : 7
History Count                 : 0
User Review Enable            : No
User Review Interval(Days)    : 120
Enable Inactive User Lock     : No
Inactive Lock Interval(Days)  : 60
Name Length Limit             : 6
Enable Login Notes            : No
Enable User Notes             : No
User Notes                    :
Max Sessions Per User         : 0
Min Different Char Count      : 0
Max Same Char Count           : 0
Min Upper Char Count          : 0
Min Lower Char Count          : 0
Min Digit Count               : 0
Bind Session to IP            : Yes
```

##### System Response

The following table describes the parameter meanings.

| Parameter                     | Meaning                                                                                                                                                                                                                                              |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                            | ID of safe_strategy.                                                                                                                                                                                                                                 |
| Password Min Length           | Minimum password length.                                                                                                                                                                                                                             |
| Password Max Length           | Maximum password length.                                                                                                                                                                                                                             |
| Password Complex              | Password complexity.                                                                                                                                                                                                                                 |
| Reduplicate Char Count        | Number of the same characters in a password.                                                                                                                                                                                                         |
| Enable Password Lock          | Whether to enable the password lock mechanism. A user will be locked if the failed attempts to log in to the system exceeds the threshold due to an incorrect password.                                                                              |
| Password Lock Time(Minutes)   | Duration before an account is automatically unlocked, expressed in "minutes".                                                                                                                                                                        |
| Password Incorrect Times      | Allowed times for entering an incorrect password.                                                                                                                                                                                                    |
| Session Expired Time(Minutes) | Session timeout period, expressed in "minutes".                                                                                                                                                                                                      |
| Min Valid Period(Minutes)     | Minimum validity period of a new password, expressed in "minutes".                                                                                                                                                                                   |
| Max Valid Period(Days)        | Password validity period, expressed in "days".                                                                                                                                                                                                       |
| Prompt Ahead(Days)            | Number of remaining days before password expiration to display a reminder, expressed in "days".                                                                                                                                                      |
| History Count                 | Number of historical passwords reserved for an account.                                                                                                                                                                                              |
| User Review Enable            | Whether to enable the user account information review mechanism. When the user account information review switch is on, the super administrator needs to periodically audit the numbers and permissions of user accounts to ensure account security. |
| User Review Interval (Days)   | Interval between account information reviews. If the audit interval is set to 0 or 1 day, the system audits user accounts every day.                                                                                                                 |
| Enable Inactive User Lock     | Whether to enable the inactive lock mechanism. An account will be locked after it remains inactive for days that exceed the threshold.                                                                                                               |
| Inactive Lock Interval(Days)  | Number of days before an inactive account is automatically locked.                                                                                                                                                                                   |
| Name Length Limit             | Minimal length of a user name.                                                                                                                                                                                                                       |
| Enable Login Notes            | Whether to enable the login prompt mechanism. If this mechanism is enabled, information about the previous login will be displayed (including login time and login IP address).                                                                      |
| Enable User Notes             | Whether to enable the mechanism of displaying user notes. If the mechanism is enabled, preconfigured user notes will be displayed when an account logs in to the system.                                                                             |
| User Notes                    | User-defined login notification.                                                                                                                                                                                                                     |
| Max Sessions Per User         | Maximum number of sessions per user.                                                                                                                                                                                                                 |
| Min Different Char Count      | Minimum number of different characters.                                                                                                                                                                                                              |
| Max Same Char Count           | Maximum number of identical characters.                                                                                                                                                                                                              |
| Min Upper Char Count          | Minimum number of uppercase letters.                                                                                                                                                                                                                 |
| Min Lower Char Count          | Minimum number of lowercase letters.                                                                                                                                                                                                                 |
| Min Digit Count               | Minimum number of digits.                                                                                                                                                                                                                            |
| Bind Session to IP            | Whether to enable the function of binding a session to an IP address.                                                                                                                                                                                |
