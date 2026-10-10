# show notification email


##### Function

The **show notification email** command is used to query the settings of the email-based alarm and event notification functions.

##### Format

**show notification email**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the settings of the email-based alarm and event notification functions.

```text
admin:/>show notification email
User Name                          : admin
SMTP Server IP                     : 192.168.3.3
Sender Email                       : a@b.com
Send Enable                        : Yes
Authenticate Enabled               : Yes
SSL Enabled                        : Yes
Critical Alert Receiver Email List : c@d.com
Major Alert Receiver Email List    : --
Warning Alert Receiver Email List  : --
SMTP Server Port                   : 4232
Event Receiver Email List          : --
Enabled CA                         : Yes
```

##### System Response

The following table describes the parameter meanings.

| Parameter                          | Meaning                                                                         |
|------------------------------------|---------------------------------------------------------------------------------|
| User Name                          | Indicates the user name that logs in to the STMP server.                        |
| SMTP Server IP                     | Indicates the IP address of the STMP server.                                    |
| Sender Email                       | Indicates the email that sends the alarms.                                      |
| Send Enable                        | Indicates whether the email-based alarm notification function is enabled.       |
| Authenticate Enabled               | Indicates whether the STMP server must be verified.                             |
| SSL Enabled                        | Indicates whether SSL is enabled for the STMP server.                           |
| Critical Alert Receiver Email List | Indicates that alarms of the critical severity are sent to the specified email. |
| Major Alert Receiver Email List    | Indicates that alarms of the major severity are sent to the specified email.    |
| Warning Alert Receiver Email List  | Indicates that alarms of the warning severity are sent to the specified email.  |
| SMTP Server Port                   | Indicates the port ID of the SMTP server.                                       |
| Event Receiver Email List          | Email address list for receiving the event IDs with email notification enabled. |
| Enabled CA                         | Whether the CA certificate is enabled for authentication when emails are sent.  |
