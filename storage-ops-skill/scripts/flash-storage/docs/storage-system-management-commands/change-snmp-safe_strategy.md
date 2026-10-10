# change snmp safe_strategy


##### Function

The **change snmp safe_strategy** command is used to change the security policy of the SNMP service.

##### Format

**change snmp safe_strategy** \[ pwd_min_length=? \] \[ pwd_max_length=? \] \[ pwd_complex=? \] \[ diff_community=? \] \[ diff_usm_pwd=? \] \[ diff_usm_name=? \] \[ check_time=? \] \[ retry_times=? \] \[ lock_time=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pwd_min_length=? | Minimum length of a community and USM account password. | The value is an integer from 8 to 32. |
| pwd_max_length=? | Maximum length of a community and USM account password. | The value is an integer from 8 to 32. |
| pwd_complex=? | Password complexity. | The value can be "Normal", "Low", or "High", where: <br>"Normal": The password must contain special characters and at least two types of the following characters: uppercase letters, lowercase letters, and digits.<br>"High": The password must contain special characters, uppercase letters, lowercase letters, and digits.<br>"Low": The password contain any types of the following characters: special characters, uppercase letters, lowercase letters and digits.<br> NOTE: The special characters including ` ~ ! @ # $ % ^ & * ( ) - _ = + \ | [ { } ] ; : ' " , < . > / ? and space. |
| diff_community=? | Different read-only and read-write communities. | The value can be "yes" or "no". |
| diff_usm_pwd=? | The USM user authentication password must be different from the encryption password. | The value can be "yes" or "no". |
| check_time=? | Interval for checking consecutive authentication failures. | The value is an integer from 1 to 600, expressed in seconds. |
| retry_times=? | Consecutive authentication failure times. | The value is an integer from 3 to 100. |
| lock_time=? | Network management software IP locking duration. | The value is an integer from 10 to 3600, expressed in seconds. |
| diff_usm_name=? | The USM user password is different from the user name or reversed user name. | The value can be "yes" or "no". |

##### Usage Guidelines

-   If the continuous authentication failure check time is 60 seconds, the continuous authentication failure times is 4 times, and the network management software IP locking duration is 180 seconds, the IP address of the network management software will be locked by the SNMP service for 180 seconds when the software authentication fails for four consecutive times after the access to the SNMP service in 60 seconds. The SNMP service will deny all SNMP request packets from the locked IP address.
-   For security purposes, it is recommended that the password contain at least eight characters and the password complexity mode be set to "Normal" or "High".

##### Example

Set the security policy for the SNMP service. The complexity requirement for the communities and the password of the USM user is "Normal". The read and write communities must be different.

```text
admin:/>change snmp safe_strategy pwd_complex=Normal diff_community=yes
Command executed successfully.
```

Set the security policy for the SNMP service. The continuous authentication failure check time is set to 60 seconds, the number of allowed consecutive authentication failures is set to four times, and the network management software IP address lock duration is set to 180 seconds.

```text
admin:/>change snmp safe_strategy check_time=60 retry_times=4 lock_time=180
Command executed successfully.
```

Set the security policy for the SNMP service. The communities and the password of the USM user contain at least eight characters respectively.

```text
admin:/>change snmp safe_strategy pwd_min_length=8
CAUTION: You are about to change the SNMP security policy.
Suggestion: Set the minimum password length to at least 8 characters.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Set the security policy for the SNMP service. The complexity requirement for the communities and the password of the USM user is "Low".

```text
admin:/>change snmp safe_strategy pwd_complex=Low
CAUTION: You are about to change the SNMP security policy.
Suggestion: Set the password complexity to "Normal" or "High".
Do you wish to continue?(y/n)y
Command executed successfully.
```

Sett the security policy for the SNMP service. The communities and the password of the USM user contain at least eight characters respectively, and the complexity requirement for the communities and the password of the USM user is "Low".

```text
admin:/>change snmp safe_strategy pwd_complex=Low pwd_min_length=8
CAUTION: You are about to change the SNMP security policy.
Suggestion: Set the minimum password length to at least 8 characters.Set the password complexity to "Normal" or "High".
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
