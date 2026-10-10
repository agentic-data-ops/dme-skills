# add notification receiver


##### Function

The **add notification receiver** command is used to add email addresses or phone numbers used to receive alarm or event notifications.

##### Format

**add notification receiver** \[ alarm_level=? \] { email_receiver_list=? \| message_receiver_list=? \| event_email_receiver_list=? \| event_message_receiver_list=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| alarm_level=? | Indicates the alarm severity. Alarms with this severity will be sent. | The value can be "warning", "major", or "critical", where: <br>"warning": warning.<br>"major": major.<br>"critical": critical. |
| email_receiver_list=? | List of email addresses that receive alarms notifications. | Multiple email addresses can be specified and separated by commas (,). Each email address contains 5 to 255 characters. A maximum of 64 email addresses can be configured to receive alarms of the same severity. |
| message_receiver_list=? | List of phone numbers that receive alarm notifications. | Multiple phone numbers can be specified and separated by commas(,). Each phone number contains 3 to 31 characters. A maximum of 64 phone numbers can be configured to receive alarms of the same severity. |
| event_email_receiver_list | Email address list for receiving the event IDs with email notification enabled. | Multiple email addresses can be specified and separated by commas (,). Each email address contains 5 to 255 characters. A maximum of 64 email addresses can be configured to receive event notification emails. |
| event_message_receiver_list=? | Phone number list for receiving the event IDs with short message notification enabled. | Multiple phone numbers can be specified and separated commas (,). Each phone number contains 3 to 31 characters. A maximum of 64 phone numbers can be configured to receive event notification short messages. |

##### Usage Guidelines

-   Before you execute this command to add a phone number to receive alarm or event short messages, ensure that the SMS center number has been configured.
-   Before you execute this command to add an email address to receive alarm or event emails, ensure that the SMTP server has been configured.
-   A maximum of 64 email addresses can be configured for alarms of the same severity.
-   A maximum of 64 phone numbers can be configured for alarms of the same severity.
-   A maximum of 64 email addresses can be configured for events.
-   A maximum of 64 phone numbers can be configured for events.

##### Example

Add "joe@company.com" to the the email address list to receive alarm notifications of severity "warning".

```text
admin:/>add notification receiver alarm_level=warning email_receiver_list=joe@company.com
Command executed successfully.
```

Add "13812345678" to the phone number list to receive alarm notifications of severity "warning".

```text
admin:/>add notification receiver alarm_level=warning message_receiver_list=13812345678
Command executed successfully.
```

##### System Response

None
