# show smtp_server general


##### Function

The **show smtp_server general** command is used to query the settings of the email-based alarm notification function.

##### Format

**show smtp_server general**

##### Parameters

None

##### Usage Guidelines

The setting commands that correspond to this command are "change smtp_server config", "add smtp_server general", "remove smtp_server general", "add notification receiver", "remove notification receiver", and "test smtp_server general".

##### Example

Querying the settings of the email-based alarm notification function.

```text
admin:/>show smtp_server general
User Name                          : admin
SMTP Server                        : 192.168.3.3
Sender Email                       : XXXXXX@foxmail.com
Send Enable                        : Yes
Authentication                     : Yes
Connection Security                : SSL/TLS
SMTP Server Port                   : 4232
Title Prefix                       : abc
Level Enable                       : Yes
Description Enable                 : Yes
Storage Name Enable                : Yes
Alarm ID Enable                    : Yes
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning                                                                  |
|---------------------|--------------------------------------------------------------------------|
| User Name           | Username used to log in to the SMTP server.                              |
| SMTP Server         | Address of the SMTP server.                                              |
| Sender Email        | Mailbox that sends alarm notifications.                                  |
| Send Enable         | Whether the email-based alarm notification function is enabled.          |
| Authentication      | Whether account authentication is required for the email sending server. |
| Connection Security | Secure connection mode between the email sending server and the client.  |
| SMTP Server Port    | Port number of the SMTP server.                                          |
| Title Prefix        | Email title prefix.                                                      |
| Level Enable        | Whether to show alarm severities in email titles.                        |
| Description Enable  | Switch of displaying the alarm description in the email title.           |
| Storage Name Enable | Switch of displaying the storage device name in the email title.         |
| Alarm ID Enable     | Switch of displaying the alarm ID in the email title.                    |
