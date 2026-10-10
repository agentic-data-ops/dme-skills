# remove notification receiver


##### Function

The **remove notification receiver** command is used to remove email addresses or phone numbers used to receive alarm or event notifications.

##### Format

**remove notification receiver** \[ alarm_level=? \] { email_receiver_list=? \| message_receiver_list=? \| event_email_receiver_list=? \| event_message_receiver_list=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| alarm_level=? | Alarm severity. | The value can be "warning", "major" or "critical". You can run the "show notification email_extend" or "show notification sms" command to check the severity. |
| email_receiver_list=? | List of emails that receive alarms. | Multiple email addresses can be specified. You can run the "show notification email_extend" command to check the email list. |
| message_receiver_list=? | List of phone numbers that receive alarm notifications. | Multiple phone numbers can be specified. Separate the phone numbers by commas (,). * specify all phone numbers to receive the notification will be removed. Each phone number must be 3 to 31 characters in length. You can run the "show notification sms" command to check the phone number list. |
| event_email_receiver_list=? | Email address list for receiving the event IDs with email notification enabled. | Multiple email addresses can be specified, which are separated by command (,). To obtain the value, run "show notification email_extend". |
| event_message_receiver_list | Phone number list for receiving the event IDs with short message notification enabled. | Multiple phone numbers can be specified. Separate the phone numbers by commas (,). * specify all phone numbers to receive the notification will be removed. Each phone number must be 3 to 31 characters in length. You can run the "show notification sms" command to check the phone number list. |

##### Usage Guidelines

None.

##### Example

Remove "joe@company.com" that receives warning alarms or alarms of higher severities from the recipient emails of alarm notifications.

```text
admin:/>remove notification receiver alarm_level=warning email_receiver_list=joe@company.com
WARNING: You are about to delete the recipient email or phone number of email-based or SMS-based alarm notifications. The recipient email or phone number cannot receive notifications after being deleted.
Suggestion: Before performing this operation, ensure that it is allowed to delete the recipient email or phone number.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Remove 13812345678 that receives warning alarms or alarms of higher severities from the recipient phone numbers of alarm notifications.

```text
admin:/>remove notification receiver alarm_level=warning message_receiver_list=13812345678
WARNING: You are about to delete the recipient email or phone number of email-based or SMS-based alarm notifications. The recipient email or phone number cannot receive notifications after being deleted.
Suggestion: Before performing this operation, ensure that it is allowed to delete the recipient email or phone number.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
