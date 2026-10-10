# show user_auth_email_server general


##### Function

The **show user_auth_email_server general** command is used to query configurations of the two-factor authentication email server.

##### Format

**show user_auth_email_server general**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query configurations of the two-factor authentication email server.

```text

admin:/>show user_auth_email_server general

Enabled                       : On
SMTP Server Address           : 192.168.3.3
SMTP Server Port              : 4232
Connection Security           : Not encrypted
Authentication                : On
User                          : username
CA Enabled                    : Yes
Sender                        : send@xxx.com

```

##### System Response

The following table describes the parameter meanings.

| Parameter             | Meaning                                                     |
|-----------------------|-------------------------------------------------------------|
| Enabled               | Whether the authentication email server is enabled.         |
| Authenticate Switch   | Whether SMTP authentication is required.                    |
| Encryption Mode       | Encryption mode.                                            |
| SMTP Server Port      | Port number of the authentication email server.             |
| SMTP Server IP        | IP address of the authentication email server.              |
| Authenticate Username | Authentication user name.                                   |
| Sender Email Address  | Sender email.                                               |
| Enabled CA            | Whether the CA certificate is enabled when emails are sent. |
| Authenticate Username | Authentication user name.                                   |
