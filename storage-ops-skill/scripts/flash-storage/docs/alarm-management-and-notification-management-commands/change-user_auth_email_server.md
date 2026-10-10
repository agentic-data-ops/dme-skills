# change user_auth_email_server


##### Function

The **change user_auth_email_server** command is used to modify configurations of the two-factor authentication email server.

##### Format

**change user_auth_email_server** enabled=? smtp_server_address=? sender=? authentication=? user=? password=? connection_security=? smtp_server_port=? \[ ca_enabled=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled | Whether the authentication email server is enabled. | The value can be "yes" or "no", where: <br>"yes": enables the two-factor authentication email notification function.<br>"no": disables the two-factor authentication email notification function.<br> The default value is "no". |
| smtp_server_address | Address of the authentication email server. | The value can be an IP address or domain name. |
| sender | Sender email. | The value consists of 5 to 255 ASCII characters. |
| authentication | Whether SMTP authentication is required. | The value can be "yes" or "no", where: <br>"yes": SMTP authentication is required.<br>"no": SMTP authentication is not required. |
| user | User name used to log in to the SMTP server. NOTE: This parameter can be specified when "authentication" is set to "yes". | The value consists of 1 to 63 ASCII characters except single quotation marks ('). |
| password | Password used to log in to the SMTP server. NOTE: This parameter can be specified when "authentication" is set to "yes". | The value consists of 1 to 63 ASCII characters. |
| connection_security | Secure connection mode between the email sending server and the client. | The value can be "none", "ssl/tls", or "starttls", where: <br>"none": No secure connection mode is used.<br>"ssl/tls": SSL/TLS is used to encrypt connections to ensure connection security.<br>"starttls": STARTTLS is used for secure connection.<br> NOTE: To ensure data transfer security, you are advised to use a secure connection mode. |
| smtp_server_port | SMTP port number. | The value is an integer ranging from 1 to 65535. |
| ca_enabled | Whether the CA certificate is enabled when emails are sent. | The value can be "yes" or "no", where: <br>"yes": enables the CA certificate when emails are sent.<br>"no": disables the CA certificate when emails are sent. |

##### Usage Guidelines

None

##### Example

Enable the two-factor authentication function by configuring the following parameters: The email address is "a@b.com", the SMTP server IP address is "192.168.3.3", and the port ID is "4232". Parameter "SSL" is used, and user "admin" (with password "123456") of the server that sends email notifications must be verified. The CA certificate is enabled when emails are sent.

```text

admin:/>change user_auth_email_server enabled=yes smtp_server_address=192.168.3.3 sender=a@b.com authentication=yes user=admin password=****** connection_security=ssl/tls smtp_server_port=4232 ca_enabled=yes

Change configuration successfully.

```

##### System Response

None
