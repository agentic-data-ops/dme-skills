# show notification email_extend


##### Function

The **show notification email_extend** command is used to query mailboxes used for sending and receiving alarms and events.

##### Format

**show notification email_extend**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query mailboxes used for sending and receiving alarms and events.

```text
admin:/>show notification email_extend
User Name                          : admin
SMTP Server IP                     : 192.168.3.3
Sender Email                       : a@b.com
Send Enable                        : Yes
Authentication                     : Yes
Connection Security                : SSL/TLS
Critical Alert Receiver Email List : c@d.com
Major Alert Receiver Email List    : --
Warning Alert Receiver Email List  : --
SMTP Server Port                   : 4232
Title Prefix                       : abc
Level Enable                       : Yes
Event Receiver Email List          : --
Enabled CA                         : No
Description Enable                 : Yes
Storage Name Enable                : Yes
Alarm Id Enable                    : Yes
```

##### System Response

The following table describes the parameter meanings.

| Parameter                          | Meaning                                                                         |
|------------------------------------|---------------------------------------------------------------------------------|
| User Name                          | Name of the user that logs in to the SMTP server.                               |
| SMTP Server IP                     | IP address of the SMTP server.                                                  |
| Sender Email                       | Mailbox that sends alarms.                                                      |
| Send Enable                        | Whether the email-based alarm notification function is enabled.                 |
| Authentication                     | Whether account authentication is required for the email sending server.        |
| Connection Security                | Secure connection mode between the email sending server and the client.         |
| Critical Alert Receiver Email List | Indicates that alarms of the critical severity are sent to the specified email. |
| Major Alert Receiver Email List    | Indicates that alarms of the major severity are sent to the specified email.    |
| Warning Alert Receiver Email List  | Indicates that alarms of the warning severity are sent to the specified email.  |
| SMTP Server Port                   | Port ID of the SMTP server.                                                     |
| Title Prefix                       | Prefix of the email title.                                                      |
| Level Enable                       | Whether to display the alarm severity in the email title.                       |
| Event Receiver Email List          | Email address list for receiving the event IDs with email notification enabled. |
| Enabled CA                         | Whether the CA certificate is enabled for authentication when emails are sent.  |
| Description Enable                 | Switch of displaying the alarm description in the email title.                  |
| Storage Name Enable                | Switch of displaying the storage device name in the email title.                |
| Alarm ID Enable                    | Switch of displaying the alarm ID in the email title.                           |
