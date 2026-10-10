# change remote_support general


##### Function

The **change remote_support general** command is used to configure basic information about eService.

##### Format

**change remote_support general** \[ center_id=? \] \[ proxy_switch=? \] \[ proxy_address=? \] \[ proxy_port=? \] \[ proxy_username=? \] \[ proxy_password=? \] \[ site_name=? \] \[ trans_type=? \] \[ smtp_authentication=? \] \[ smtp_connection_security=? \] \[ smtp_ca_enabled=? \] \[ smtp_sender=? \] \[ smtp_server_domain_name=? \] \[ smtp_server_port=? \] \[ smtp_server_ip=? \] \[ smtp_email_attachment_size=? \] \[ user=? \] \[ password=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| center_id | Technical support center. | The value contains 1 to 63 characters. |
| proxy_switch | Switch for enabling or disabling a proxy server. | The value can be "off" or "on", where: <br>"off": The switch is turned off.<br>"on": The switch is turned on.<br> The default value is "off". |
| proxy_address | Proxy server address. | The value can be a domain name or an IPv4 address. The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits, and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| proxy_port | Port number of a proxy server. | The value ranges from 1 to 65535. |
| proxy_username | User name for logging in to a proxy server. | The value contains 1 to 63 characters excluding single quotation marks ('). |
| proxy_password | Password for logging in to a proxy server. | The value contains 1 to 63 characters. |
| site_name | Site name. | The value contains 1 to 127 characters excluding single quotation marks ('). |
| trans_type | CHS transfer type. | The options are as follows: <br>"HTTPS": HTTPS protocol.<br>"SMTP": SMTP protocol. |
| smtp_authentication | Whether the email sending server requires account authentication. | The value can be "yes" or "no", where: <br>"yes": Account authentication is required for the email sending server.<br>"no": Account authentication is not required for the email sending server. |
| smtp_connection_security | Secure connection mode between the email sending server and client. | The value can be "none", "ssl/tls", or "starttls", where: <br>"none": The secure connection mode is not used.<br>"ssl/tls": SSL/TLS is used to encrypt connections to ensure connection security.<br>"starttls": The STARTTLS mode is used for secure connection.<br> NOTE: To ensure data transmission security, secure connection is recommended. |
| smtp_ca_enabled | Whether to enable CA certificate authentication when sending emails. | The value can be "yes" or "no", where: <br>"yes": CA certificate authentication is enabled during email sending.<br>"no": CA certificate authentication is disabled during email sending. |
| smtp_sender | Email address of the user who sends an alarm. | The value is a string of 5 to 255 ASCII characters. |
| smtp_server_domain_name | Domain name of the email sending server. | The domain name is a string of 1 to 255 case-insensitive characters, consisting of letters, digits, and hyphens (-). Domain names at different levels are separated by periods (.). The hyphen (-) cannot start or end with the domain name. |
| smtp_server_port | Port number of the SMTP server. | The value is an integer ranging from 1 to 65535. |
| smtp_server_ip | IP address of the email sending server. | IPv4 or IPv6 address. |
| smtp_email_attachment_size | Maximum size of an email attachment. | 1 to 100 MB. |
| user | User name for logging in to the email sending server. NOTE: This parameter is available only when authentication is set to yes. | The value is a string of 1 to 63 ASCII characters, excluding single quotation marks ('). |
| password | Password for logging in to the email sending server. NOTE: This parameter is available only when authentication is set to yes. | The value contains 1 to 63 ASCII characters. |

##### Usage Guidelines

-   This command can be used to configure a technical support center for eService. Messages at the technical support center can be queried by running the "show remote_support technical_support_center" command.
-   This command can be used to configure information about the proxy server of eService.

##### Example

Configure basic information about eService.

```text
admin:/>change remote_support general trans_type=HTTPS center_id=CenterEC proxy_switch=on proxy_address=192.168.10.13 proxy_port=8080 proxy_username=admin proxy_password=**********
WARNING: You are about to change the eService site. If the eService has been enabled, this operation will disable the ongoing service, and the new eService site needs to be re-authenticated.
Suggestion: Before performing this operation, contact technical support engineers and confirm that the selected eService site obeys the local law.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Configure the basic information about the eService service and set trans_type to HTTPS.

```text

admin:/>change remote_support general trans_type=HTTPS
CAUTION: You are about to set the transfer protocol of eService to HTTPS. After this operation, you must perform authentication on DeviceManager or the CLI again to prevent the current device from being disconnected from eService due to no authentication performed or authentication expiration.
Suggestion: Ensure that you want to perform this operation.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Configure the basic information about the eService service and set trans_type to SMTP.

```text
admin:/>change remote_support general trans_type=SMTP smtp_authentication=no smtp_connection_security=none smtp_sender=test@test.com smtp_server_ip=192.168.10.13 smtp_server_port=25 smtp_ca_enabled=no smtp_email_attachment_size=10
CAUTION: You are about to set the transfer protocol of eService to SMTP. After this operation, if the device is disconnected from eService, the disconnection can be detected on eService at least six hours later.
Suggestion: Ensure that you want to perform this operation.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
