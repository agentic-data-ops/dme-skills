# change smtp_server config


##### Function

The **change smtp_server config** command is used to configure the email-based alarm notification function. If you want to enable the storage system to automatically send an alarm notification email to a specified mailbox when an alarm is generated, run this command.

##### Format

**change smtp_server config** enabled=? sender=? authentication=? user=? password=? connection_security=? smtp_server_port=? \[ clear_email_title_prefix=? \| email_title_prefix=? \] \[ email_title_level_enable=? \] \[ email_title_description_enable=? \] \[ email_title_storage_name_enable=? \] \[ email_title_alarm_id_enable=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Whether to enable the email-based notification function. | The value can be "yes" or "no". where: <br>"yes": To enable the email-based alarm notification function.<br>"no": Not to enable the email-based alarm notification function. |
| sender=? | Sender email. | The value contains 5 to 255 characters. |
| authentication=? | Whether the SMTP server must be verified by a user. | The value can be "yes" or "no", where: <br>"yes": Verification is required.<br>"no": Verification is not required. |
| user=? | Username used to log in to the SMTP server. NOTE: This parameter can be specified when "authentication" is set to "yes". | The value consists of 1 to 63 ASCII characters except single quotation marks('), double quotation marks (") and question marks (?). |
| password=? | Password used to log in to the SMTP server. NOTE: This parameter can be specified when "authentication" is set to "yes". | The value consists of 1 to 63 ASCII characters except question marks (?). |
| connection_security=? | Secure connection mode between the email sending server and the client. | The value can be "none", "ssl/tls", or "starttls", where: <br>"none": No secure connection mode is used.<br>"ssl/tls": ssl/tls is used to encrypt connections to ensure connection security.<br>"starttls": starttls is used.<br> NOTE: To ensure data transfer security, secure connection modes are recommended. |
| smtp_server_port=? | Port number of the SMTP server. | The value is an integer from 1 to 65535. |
| email_title_prefix=? | Email title prefix. | The value consists of 1 to 511 ASCII characters and cannot contain single quotation marks ('). |
| clear_email_title_prefix=? | Clears the email prefix. | If the value is "yes", the email title prefix is cleared. |
| email_title_level_enable=? | Whether to show alarm severities in email titles. | The value can be "yes" or "no", where: <br>"yes": show alarm severities in email titles.<br>"no": Not to show alarm severities in email titles. |
| email_title_description_enable=? | Switch of displaying the alarm description in the email title. | The value can be "yes" or "no", where: <br>"yes": show alarm description in email titles.<br>"no": Not to show alarm description in email titles. |
| email_title_storage_name_enable=? | Switch of displaying the storage device name in the email title. | The value can be "yes" or "no", where: <br>"yes": show storage device name in email titles.<br>"no": Not to show storage device name in email titles. |
| email_title_alarm_id_enable=? | Switch of displaying the alarm ID in the email title. | The value can be "yes" or "no", where: <br>"yes": show alarm ID in email titles.<br>"no": Not to show alarm ID in email titles. |

##### Usage Guidelines

-   Before running this command, configure an SMTP server and a valid SMTP account.

-   You must configure a sender during the initial configuration.

-   You must configure the username and password when you set authentication to yes for the first time.

-   After alarm notification by email is configured, the system sends alarms to specified mailboxes by email. The email format is as follows:

Dear OceanStor XXXXX users:

System Name: Huawei.Storage

Location: China

Customer Info: ClientName

ESN: XXXXXXXXXXXXXXXXXXXX

ID: 0x1FFFFFFFFFFFFFFB

Level: Informational

Occurred At: 2015-06-23 15:58:53

Details: This is a test message.

Suggestions: N/A

-   Each part of the email content is defined as follows:
-   Manufacturer and product type, for example, OceanStor XXXXX.
-   Device name, for example, Huawei.Storage.
-   Client of the storage system, for example, ClientName.
-   Device SN, for example, XXXXXXXXXXXXXXXXXXXX.
-   Alarm ID, which indicates a certain type of alarm, expressed in the hexadecimal format, for example, 0x1FFFFFFFFFFFFFFB.
-   Alarm severity. Alarm severities include info, warning, major, and critical.
-   Time when an alarm occurs, for example, 2015-06-23 15:03:36.
-   Alarm description, for example, "This Is A Test Message.".
-   Alarm clearance suggestion, for example, N/A.

-   The value of "connection_security" must be consistent with that in the mailbox server configuration. Otherwise, emails cannot be successfully sent.

-   The query command that corresponds to this command is "show notification email_extend".

-   The following parameters or parameter sets are mutually exclusive: clear_email_title_prefix and email_title_prefix.

##### Example

Enable the email-based notification function and set the sender email address to "XXXXXX@foxmail.com", SMTP server port to "4232", security connection mode to "ssl/tls", username and password for authenticating the email sending server to "admin" and "123456", email title prefix to "abc", and alarm severity display switch to "on".

```text
admin:/>change smtp_server config enabled=yes sender=XXXXXX@foxmail.com authentication=yes user=admin password=****** connection_security=ssl/tls smtp_server_port=4232 email_title_prefix=new email_title_level_enable=yes email_title_description_enable=yes email_title_storage_name_enable=yes email_title_alarm_id_enable=yes
Change configuration successfully.
```

##### System Response

None
