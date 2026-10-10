# show remote_support general


##### Function

The **show remote_support general** command is used to query basic configuration information about eService.

##### Format

**show remote_support general**

##### Parameters

None

##### Usage Guidelines

This command is used to query information about the proxy server and technical support center of eService.

##### Example

Query basic configuration information about eService.

```text
admin:/>show remote_support general

Technical Support Center     : Enterprise in Romania region
Proxy Switch                 : On
Proxy Server Port            : 80
Proxy Server Address         : 192.168.0.100
Proxy User Name              :
Site Name                    : Foo .Inc
Trans Type                   : SMTP
SMTP Server IP               : 192.168.3.3
SMTP Authentication          : Yes
SMTP Server Port             : 4232
SMTP Enabled CA              : No
SMTP Connection Security     : SSL/TLS
SMTP Sender Email            : a@b.com
SMTP Email Attachment Size   : 10

```

Query the basic configuration information of the eService service.

```text
admin:/>show remote_support general

Technical Support Center   : Enterprise in Romania region
Proxy Switch               : On
Proxy Server Port          : 80
Proxy Server Address       : 192.168.0.100
Proxy User Name            :
Site Name                  : Foo .Inc
Trans Type                 : HTTPS
SMTP Server IP             : --
SMTP Authentication        : --
SMTP Server Port           : --
SMTP Enabled CA            : --
SMTP Connection Security   : --
SMTP Sender Email          : --
SMTP Email Attachment Size : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                  | Meaning                                                                  |
|----------------------------|--------------------------------------------------------------------------|
| Support Center ID          | ID.                                                                      |
| Technical Support Center   | Name of the technical support center.                                    |
| Proxy Switch               | Proxy switch.                                                            |
| Proxy Server Port          | Port number of a proxy server.                                           |
| Proxy Server Address       | Address of a proxy server.                                               |
| Proxy User Name            | User name of a proxy server.                                             |
| Site Name                  | Site name.                                                               |
| Trans Type                 | CHS transfer type.                                                       |
| SMTP Server IP             | IP address of the email sending server.                                  |
| SMTP Authenticate          | Whether account authentication is required for the email sending server. |
| SMTP Server Port           | Port number of the SMTP server.                                          |
| SMTP Enabled CA            | Whether to enable CA certificate authentication when sending emails.     |
| SMTP Connection Security   | Secure connection mode between the email sending server and client.      |
| SMTP Sender Email          | Email address of the user who sends an alarm.                            |
| SMTP Email Attachment Size | Maximum size of an email attachment.                                     |
