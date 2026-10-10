# change notification email_extend


##### Function

The **change notification email_extend** command is used to enable the email notification function and configure alarm and event notification mailboxes. Use this command if you want to enable the storage system to automatically send notification emails of the following to a specified mailbox: all alarms and the events with the email notification function enabled.

##### Format

**change notification email_extend** enabled=? { smtp_server_ip=? \| smtp_server_domain_name=? } sender=? authentication=? user=? password=? { receiver_email_list=? \| event_receiver_email_list=? } \* connection_security=? smtp_server_port=? \[ function_test=? \] \[ clear_email_title_prefix=? \| email_title_prefix=? \] \[ email_title_level_enable=? \] \[ ca_enabled=? \] \[ email_title_description_enable=? \] \[ email_title_storage_name_enable=? \] \[ email_title_alarm_id_enable=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Whether to enable the email notification function. NOTE: If this parameter is set to no, related configurations are cleared. | The value can be "yes" or "no", where: <br>"yes": enables the email alarm notification function.<br>"no": disables the email alarm notification function.<br> The default value is "no". |
| smtp_server_ip=? | IP address of the SMTP server. | The value can be an IPv4 or IPv6 address. |
| smtp_server_domain_name=? | Domain name of the SMTP server. | The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits, and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| sender=? | Sender email. | The value consists of 5 to 255 ASCII characters. |
| authentication=? | Whether the SMTP server must be verified by a user. | The value can be "yes" or "no", where: <br>"yes": Verification is required.<br>"no": Verification is not required. |
| user=? | Username used to log in to the SMTP server. NOTE: This parameter can be specified when "authentication" is set to "yes". | The value consists of 1 to 63 ASCII characters except single quotation marks ('). |
| password=? | Password used to log in to the SMTP server. NOTE: This parameter can be specified when "authentication" is set to "yes". | The value consists of 1 to 63 ASCII characters. |
| receiver_email_list=? | Recipient mailbox for alarm notification. | Multiple alarm email addresses can be specified. Alarm email addresses of various levels are separated by commas (,) in a sequence of critical, major, and warning. Alarm email addresses of the same level are separated by semicolons (;) from one another. Each email address is 5 to 255 ASCII characters in length. For alarms of the same level, a maximum of 64 alarm email addresses can be added, and 192 alarm email addresses can be added for three levels. |
| event_receiver_email_list=? | Email address list for receiving the event IDs with email notification enabled. | Multiple email addresses can be specified and separated by commas (,). Each email address must be 5 to 255 characters in length. A maximum of 64 email addresses can be configured to receive event notification emails. |
| connection_security=? | Secure connection mode between the email sending server and the client. | The value can be "none", "ssl/tls", or "starttls", where: <br>"none": No secure connection mode is used.<br>"ssl/tls": ssl/tls is used to encrypt connections to ensure connection security.<br>"starttls": starttls is used.<br> NOTE: To ensure data transfer security, secure connection modes are recommended. |
| smtp_server_port=? | Port number of the SMTP server. | The value is an integer between 1 and 65535. |
| email_title_level_enable=? | Whether to show alarm severities in email titles. | The value can be "yes" or "no", where: <br>"yes": shows alarm severities in email titles.<br>"no": does not show alarm severities in email titles. |
| clear_email_title_prefix=? | Clearing the email prefix. | The value must be "yes" which indicate the clear of email prefix. |
| email_title_prefix=? | Email title prefix. | The value consists of 1 to 511 ASCII characters and cannot contain single quotation marks ('). |
| function_test=? | Whether to send a test email after the command is executed. | The value can be "yes" or "no", where: <br>"yes": sends the test email.<br>"no": does not send the test email. |
| ca_enabled=? | Whether the CA certificate is enabled for authentication when emails are sent. | The value can be "yes" or "no", where: <br>"yes": enables the CA certificate when emails are sent.<br>"no": disables the CA certificate when emails are sent. |
| email_title_description_enable=? | Switch of displaying the alarm description in the email title. | The value can be "yes" or "no", where: <br>"yes": shows alarm description in email titles.<br>"no": does not show alarm description in email titles. |
| email_title_storage_name_enable=? | Switch of displaying the storage device name in the email title. | The value can be "yes" or "no", where: <br>"yes": shows storage device name in email titles.<br>"no": does not show storage device name in email titles. |
| email_title_alarm_id_enable=? | Switch of displaying the alarm ID in the email title. | The value can be "yes" or "no", where: <br>"yes": shows alarm ID in email titles.<br>"no": does not show alarm ID in email titles. |

##### Usage Guidelines

The command is used to configure only one mail server. The "add smtp_server general", "remove smtp_server general", "change smtp_server config", and "show smtp_server general" commands are used to configure two mail servers. You are advised to use the preceding four commands to configure mail servers for alarm notification.

-   Before running this command, configure an SMTP server and a valid SMTP account.

-   A maximum of 64 email addresses can be configured for alarms of the same level.

-   A maximum of 64 email addresses can be configured for events.

-   After notification by email is configured, the system sends alarms and the events with email notification function enabled to specified mailboxes by email. The email format is as follows:

Dear XXX users:

System Name: OceanStor.Storage

Location: China

Customer Info: ClientName

ESN: XXXXXXXXXXXXXXXXXXXX

ID: 0x1FFFFFFFFFFFFFFB

Level: Informational

Occurred At: 2015-06-23 15:58:53

Detail: This is a test message.

Repair Suggestion: N/A

-   Each part of the email content is defined as follows:
-   Manufacturer and product type.
-   Device name, for example, "OceanStor.Storage".
-   Client of the storage system, for example, "ClientName".
-   Device SN, for example, XXXXXXXXXXXXXXXXXXXX.
-   Alarm or event ID, which indicates an alarm or event, expressed in the hexadecimal format, for example, "0x1FFFFFFFFFFFFFFB".
-   Alarm or event level. The levels include "info", "warning", "major", and "critical".
-   Time when an alarm or event occurs, for example, "2015-06-23 15:03:36".
-   Alarm or event description, for example, "This Is A Test Message."
-   Alarm or event clearance suggestion, for example, "N/A".

-   The value of "connection_security" must be consistent with the mailbox server configuration. Otherwise, emails cannot be successfully sent.

-   The query command that corresponds to this command is "show notification email_extend".

-   The following parameters or parameter sets are mutually exclusive: "clear_email_title_prefix" and "email_title_prefix".

##### Example

Enable the email alarm notification function and set the sender email address to "a@b.com", SMTP server port to "4232", security connection mode to "ssl/tls", username and password for authenticating the email sending server to "admin" and "123456", email title prefix to "new", and alarm severity display switch to "on"; the CA certificate is enabled when emails are sent.

```text
admin:/>change notification email_extend enabled=yes smtp_server_ip=192.168.3.3 sender=a@b.com authentication=yes user=admin password=****** receiver_email_list=c@d.com connection_security=ssl/tls smtp_server_port=4232 function_test=no email_title_prefix=new email_title_level_enable=yes email_title_description_enable=yes email_title_storage_name_enable=yes email_title_alarm_id_enable=yes ca_enabled=yes
Change configuration successfully.
```

##### System Response

None
