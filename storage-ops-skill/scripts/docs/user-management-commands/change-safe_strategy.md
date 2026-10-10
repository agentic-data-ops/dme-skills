# change safe_strategy


##### Function

The **change safe_strategy** command is used to change the password and login policies of a storage system.

##### Format

**change safe_strategy** \[ pwd_min_length=? \] \[ pwd_max_length=? \] \[ pwd_complex=? \] \[ reduplicate_char_count=? \] \[ enable_pwd_lock=? \] \[ pwd_lock_time=? \] \[ pwd_incorrect_times=? \] \[ session_expired_time=? \] \[ min_valid_period=? \] \[ max_valid_period=? \] \[ prompt_ahead=? \] \[ history_count=? \] \[ user_review_enable=? \] \[ user_review_interval=? \] \[ enable_inactive_lock=? \] \[ inactive_lock_interval=? \] \[ name_minimal_length=? \] \[ enable_login_notes=? \] \[ enable_user_notes=? \] \[ user_notes=? \] \[ max_sessions_per_user=? \] \[ min_different_char_count=? \] \[ max_same_char_count=? \] \[ min_upper_char_count=? \] \[ min_lower_char_count=? \] \[ min_digit_count=? \] \[ enable_session_bind_ip=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pwd_min_length=? | Minimum length of a password. | The value is an integer from 8 to 32. |
| pwd_max_length=? | Maximum length of a password. | The value is an integer from 8 to 32. |
| pwd_lock_time=? | Duration before an account is automatically unlocked. | The value is "0" or an integer from 3 to 2000, expressed in minutes. If the value is "0", the account will be permanently locked. |
| pwd_complex=? | Password complexity. | The value can be "Normal" or "High", where: <br>"Normal": The password must contain special characters, and at least two of the following three: uppercase letters, lowercase letters, and digits.<br>"High": The password must contain special characters, uppercase letters, lowercase letters, and digits. |
| reduplicate_char_count=? | Maximum number of consecutive same characters in a password. | The value can be "0", "1", "2", "3", "4", "5", "6", "7", "8", or "9". If the value is "0", it means no limit. |
| prompt_ahead=? | Notification threshold for the number of remaining days before password expiration. If this parameter value is specified, the system reports a notification before password expiration based on the specified value. | The value is an integer from 1 to 99, expressed in days, and cannot be greater than the value of "max_valid_period". |
| user_review_interval=? | Account audit interval. | The value is an integer from 0 to 999, expressed in days. If the audit interval is set to 0 or 1 day, the system audits user accounts every day. |
| inactive_lock_interval=? | Number of days before an inactive account is automatically locked. | The value is an integer from 1 to 999, expressed in days. |
| pwd_incorrect_times=? | Allowed times for entering incorrect passwords. | The value is an integer from 1 to 9. |
| enable_pwd_lock=? | Whether to enable the password lock mechanism. After the password lock mechanism is enabled, a user will be locked if the user enters incorrect password for times that exceed the threshold. | The value can be "yes" or "no". |
| session_expired_time=? | Session timeout period. If you have not performed any operation in a timeout period that you have set, the system automatically logs you out. | The value is an integer from 1 to 100, expressed in minutes. |
| min_valid_period=? | Minimum validity period of a new password. | The value is an integer from 0 to 9999, expressed in minutes. |
| max_valid_period=? | Password validity period. | The value is an integer from 0 to 999, expressed in days, and cannot be smaller than the value of "prompt_ahead".If the value is "0", it indicates that the password is valid permanently. |
| history_count=? | Number of historical passwords reserved for an account. | The value is an integer from 0 to 30. If the value is "0", it means no limit. |
| enable_inactive_lock=? | Whether to enable the inactive lock mechanism. After the inactive lock mechanism is enabled, an account will be locked if the account does not login for days that exceed the threshold. | The value can be "yes" or "no". |
| user_review_enable=? | Whether to enable the user account information review mechanism. When the user account information review switch is enabled, the super administrator needs to periodically audit the numbers and permissions of user accounts to ensure account security. | The value can be "yes" or "no". |
| name_minimal_length=? | Minimal length of a user name. | The value is an integer from 5 to 32, expressed in bytes. |
| enable_login_notes=? | Whether to enable the login notification mechanism. If this mechanism is enabled, information about the previous login will be displayed ,including login time and login IP address. | The value can be "yes" or "no". |
| enable_user_notes=? | Whether to enable the mechanism of displaying user-defined login notification. If the mechanism is enabled, preconfigured user notification will be displayed when an account logs in to the system. | The value can be "yes" or "no". |
| user_notes=? | User-defined login notification. | The length of the notification is an integer from 1 to 511, expressed in bytes. |
| max_sessions_per_user=? | Maximum number of sessions per user. | The value is an integer from 0 to 32. If the value is "0", it means no limit. |
| min_different_char_count=? | Minimum number of different characters. | The value is an integer from 0 to 32. If the value is "0", it means no limit. |
| max_same_char_count=? | Maximum number of identical characters. | The value is an integer from 0 to 30. If the value is "0", it means no limit. |
| min_upper_char_count=? | Minimum number of uppercase letters. | The value is an integer from 0 to 30. If the value is "0", it means no limit. |
| min_lower_char_count=? | Minimum number of lowercase letters. | The value is an integer from 0 to 30. If the value is "0", it means no limit. |
| min_digit_count=? | Minimum number of digits. | The value is an integer from 0 to 30. If the value is "0", it means no limit. |
| bind_session_to_ip=? | Whether to enable the function of binding a session to an IP address. | The value can be "yes" or "no". |

##### Usage Guidelines

-   Only when "enable_pwd_lock" is set to "yes", "pwd_lock_time" and "pwd_incorrect_times" can be specified.
-   When "enable_inactive_lock" is set to "yes", "inactive_lock_interval" is mandatory.
-   Only when parameter "max_valid_period" is specified, "prompt_ahead" can be specified.
-   When "user_review_enable" is set to "yes", "user_review_interval" is mandatory.
-   Only when "enable_user_notes" is set to "yes", "user_notes" can be specified.

##### Example

Enable the password lock mechanism and set the allowed times for entering incorrect passwords to "5".

```text
admin:/>change safe_strategy enable_pwd_lock=yes pwd_lock_time=5
Command executed successfully.
```

##### System Response

None
