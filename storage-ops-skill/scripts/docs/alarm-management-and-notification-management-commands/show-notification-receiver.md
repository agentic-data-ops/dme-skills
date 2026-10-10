# show notification receiver


##### Function

The **show notification receiver** command is used to query the mailboxes used to receive alarm and event emails, or the mobile phone numbers used to receive alarm and event short messages.

##### Format

**show notification receiver** type=?

##### Parameters

| Parameter | Description           | Value                                        |
|-----------|-----------------------|----------------------------------------------|
| type=?    | Alarm recipient type. | The value is email_receiver or sms_receiver. |

##### Usage Guidelines

None

##### Example

Query the mobile phone number that receives alarm and event notification short messages.

```text
admin:/>show notification receiver type=sms_receiver
Critical Alert Receiver Number List    : 139XXXXXXXX
Major Alert Receiver Number List       : --
Warning Alert Receiver Number List     : --
Event Receiver Number List             : --
```

Query the mailbox that receives alarm and event notification emails.

```text
admin:/>show notification receiver type=email_receiver
Critical Alert Receiver Email List : XXXXXX@foxmail.com
Major Alert Receiver Email List    : --
Warning Alert Receiver Email List  : XXXXXX@foxmail.com
Event Receiver Email List          : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                           | Meaning                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Critical Alert Receiver Number List | Mobile phone number that receives critical alarms.                                     |
| Major Alert Receiver Number List    | Mobile phone number that receives major alarms.                                        |
| Warning Alert Receiver Number List  | Mobile phone number that receives warning alarms.                                      |
| Critical Alert Receiver Email List  | Mailbox that receives critical alarms.                                                 |
| Major Alert Receiver Email List     | Mailbox that receives major alarms.                                                    |
| Warning Alert Receiver Email List   | Mailbox that receives warning alarms.                                                  |
| Event Receiver Number List          | Phone number list for receiving the event IDs with short message notification enabled. |
| Event Receiver Email List           | Email address list for receiving the event IDs with email notification enabled.        |
