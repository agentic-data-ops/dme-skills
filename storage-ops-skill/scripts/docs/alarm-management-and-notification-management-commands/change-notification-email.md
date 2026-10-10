# change notification email


##### Function

The **change notification email** command is used to enable the email notification function and configure alarm and event notification mailboxes. Use this command if you want to enable the storage system to automatically send notification emails of the following to a specified mailbox: all alarms and the events with the email notification function enabled.

##### Format

**change notification email** enabled=? { smtp_server_ip=? \| smtp_server_domain_name=? } sender=? auth_enabled=? user=? password=? { receiver_email_list=? \| event_receiver_email_list=? } \* ssl_enabled=? smtp_server_port=? \[ function_test=? \] \[ ca_enabled=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Whether to enable the email notification function. NOTE: If this parameter is set to no, related configurations are cleared. | The value can be "yes" or "no", where: <br>"yes": enables the email alarm notification function.<br>"no": disables the email alarm notification function.<br> The default value is "no". |
| smtp_server_ip=? | IP address of the SMTP server. | The value can be an IPv4 or IPv6 address. |
| smtp_server_domain_name=? | Domain name of the SMTP server. | The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits, and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| sender=? | Mailbox for sending alarm notification emails. | The value consists of 5 to 255 ASCII characters. |
| auth_enabled=? | Whether the SMTP server must be verified by a user. | The value can be "yes" or "no", where: <br>"yes": Verification is required.<br>"no": Verification is not required. |
| user=? | User that logs in to the SMTP server. NOTE: This parameter can be specified when "auth_enabled" is set to "yes". | The value consists of 1 to 63 ASCII characters except single quotation marks ('). |
| password=? | Password of the user that logs in to the SMTP server. NOTE: This parameter can be specified when "auth_enabled" is set to "yes". | The value consists of 1 to 63 ASCII characters. |
| ssl_enabled=? | Whether to enable SSL on the SMTP server. | The value can be "yes" or "no", where: <br>"yes": enables SSL.<br>"no": disables SSL.<br> NOTE: To ensure secure data transmission, you are advised to use SSL encryption. |
| smtp_server_port=? | Port number of the SMTP server. | The value is an integer between 1 and 65535. |
| receiver_email_list=? | Recipient mailbox for alarm notification. | Multiple alarm email addresses can be specified. Alarm email addresses of various levels are separated by commas (,) in a sequence of critical, major, and warning. Alarm email addresses of the same level are separated by semicolons (;) from one another. Each email address is 5 to 255 ASCII characters in length. For alarms of the same level, a maximum of 64 alarm email addresses can be added, and 192 alarm email addresses can be added for three levels. |
| event_receiver_email_list=? | Email address list for receiving the event IDs with email notification enabled. | Multiple email addresses can be specified and separated by commas (,). Each email address contains 5 to 255 characters. A maximum of 64 email addresses can be configured to receive event notification emails. |
| function_test=? | Whether to send a test email after the command is executed. | The value can be "yes" or "no", where: <br>"yes": sends the test email.<br>"no": does not send the test email. |
| ca_enabled=? | Whether the CA certificate is enabled for authentication when emails are sent. | The value can be "yes" or "no", where: <br>"yes": enables the CA certificate when emails are sent.<br>"no": disables the CA certificate when emails are sent. |

##### Usage Guidelines

The command is used to configure only one mail server. The "add smtp_server general", "remove smtp_server general", "change smtp_server config", and "show smtp_server general" commands are used to configure two mail servers. You are advised to use the preceding four commands to configure mail servers.

-   Before running this command, configure an SMTP server and a valid SMTP account.

-   A maximum of 64 email addresses can be configured for alarms of the same level.

-   A maximum of 64 email addresses can be configured for events.

-   After alarm notification by email is configured, the system sends alarms and the events with the email notification function enabled to specified mailboxes by email. The email format is as follows:

Dear XXX users:

System Name: OceanStor.Storage

Location: China

Customer Info: ClientName

ESN: XXXXXXXXXXXXXXXXXXXX

ID: 0x1FFFFFFFFFFFFFFB

Level: Informational

Occurred At: 2015-06-23 15:58:53

Details: This is a test message.

Suggestions: N/A

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

##### Example

Enable the email notification function by configuring the following settings: The email address is "a@b.com", the SMTP server address is "192.168.3.3", and the port ID is "4232"; "SSL" is used, and the server that sends email notifications must be verified by user "admin" with the password of "123456"; the CA is enabled when emails are sent.

```text
admin:/>change notification email enabled=yes smtp_server_ip=192.168.3.3 sender=a@b.com auth_enabled=yes user=admin password=****** receiver_email_list=c@d.com ssl_enabled=yes smtp_server_port=4232 function_test=no ca_enabled=yes
Change configuration successfully.
```

##### System Response

None
