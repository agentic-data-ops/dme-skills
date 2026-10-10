# show snmp safe_strategy


##### Function

The **show snmp safe_strategy** command is used to query the security policy of the SNMP service.

##### Format

**show snmp safe_strategy**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

To query the security policy of the SNMP service, run the following command.

```text
admin:/>show snmp safe_strategy
Password Min Length : 8
Password Max Length : 32
Password Complex : Normal
Different Community : Yes
Different USM Password : Yes
Different USM Name : Yes
Check Time(s) : 60
Retry Times : 6
Lock Time(s) : 180
```

##### System Response

The following table describes the parameter meanings.

| Parameter              | Meaning                                                                     |
|------------------------|-----------------------------------------------------------------------------|
| Password Min Length    | Minimum length of community and USM user password.                          |
| Password Max Length    | Maximum length of community and USM user password.                          |
| Password Complex       | Password complexity of community and USM user password.                     |
| Different Community    | The read-only community must be different from the read-write community.    |
| Different USM Password | The authentication password must be different from the encryption password. |
| Different USM Name     | The password is different from the user name or reversed user name.         |
| Check Time(s)          | Continuous authentication failure check time.                               |
| Retry Times            | Continuous authentication failure times.                                    |
| Lock Time(s)           | Network management software IP locking time.                                |
