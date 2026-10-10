# change windows_user safe_strategy


##### Function

The **change windows_user safe_strategy** command is used to change the password and login policies of the Windows user.

##### Format

**change windows_user safe_strategy** \[ pwd_min_length=? \] \[ pwd_max_length=? \] \[ pwd_complex=? \] \[ reduplicate_char_count=? \] \[ pwd_incorrect_times=? \] \[ pwd_valid_period=? \] \[ modify_pwd_valid_period=? \] \[ name_min_length=? \] \[ inactive_lock_interval=? \] \[ sid_prefix=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pwd_min_length=? | Minimum length of a password. | The value is an integer between 6 and 32. |
| pwd_max_length=? | Maximum length of a password. | The value is an integer between 6 and 32. |
| name_min_length=? | Minimal length of a user name. | The value is an integer between 1 and 20, expressed in "Bytes". |
| inactive_lock_interval=? | Number of days before an inactive account is automatically locked. | The value is an integer between 0 and 999, expressed in "days". |
| modify_pwd_valid_period=? | Minimum interval between password changes. | The value is an integer between 0 and 9999, expressed in "minutes". |
| pwd_complex=? | Password complexity. | The value can be "Normal" or "High". <br>"Normal": The password contains at least any two types of special characters, uppercase letters, lowercase letters and digits, special characters including `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and space.<br>"High": The password must contain special characters, and at least any two types of uppercase letters, lowercase letters, and digits, special characters including `~!@#$%^&*()-_=+\|[{}];:'",<.>/? and space. |
| reduplicate_char_count=? | Maximum number of consecutive same characters in a password. | The value is an integer between 0 and 9. If the value is "0", it means no limit. |
| pwd_incorrect_times=? | Allowed times for entering incorrect passwords. | The value is an integer between 0 and 9. If the value is "0", it means no limit. |
| pwd_valid_period=? | Password validity period. | The value is an integer between 0 and 999, expressed in "days". |

##### Usage Guidelines

None

##### Example

Set the allowed times for entering incorrect passwords to "5".

```text
admin:/>change windows_user safe_strategy pwd_incorrect_times=5
Command executed successfully.
```

##### System Response

None
