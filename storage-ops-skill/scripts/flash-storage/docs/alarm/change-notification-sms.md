# change notification sms


##### Function

The **change notification sms** command is used to set the switch of alarm and event notifications by SMS messages. Use this command if you want to enable the storage system to automatically send SMS messages of the following to a specified phone number: all alarms and the events with SMS message notification enabled.

##### Format

**change notification sms** enabled=? sms_center=? { receiver_message_list=? \| event_receiver_message_list=? } \* \[ function_test=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Indicates whether to enable the SMS-based alarm notification function. NOTE: If this parameter is set to no, related configurations are cleared. | The value can be "yes" or "no", where: <br>"yes": To enable the SMS-based alarm notification function.<br>"no": Not to enable the SMS-based alarm notification function. |
| sms_center=? | Indicates the SMS center number. | The value must start with a plus sign (+) followed by a country code and a number. The country code and number must be 2 to 30 digits in length. |
| receiver_message_list=? | Recipient phone number for alarm notification. | Multiple recipient phone numbers can be specified for receiving alarm SMS messages. Alarm phone numbers of various levels are separated by commas (,) in a sequence of critical, major, and warning. Alarm phone numbers of the same level are separated by semicolons (;) from one another. Each phone number is 3 to 31 characters in length. For alarms of the same level, a maximum of 64 alarm phone numbers can be added, and 192 alarm phone number can be added for three levels. |
| function_test=? | Indicates whether to send a test short message after the command is executed. | The value can be "yes" or "no", where: <br>"yes": To send the test short message.<br>"no": Not to send the test short message. |
| event_receiver_message_list=? | Phone number list for receiving the event IDs with short message notification enabled. | Multiple phone numbers can be specified. Separate the phone numbers by commas (,). Each phone number must be 3 to 31 characters in length. A maximum of 64 phone numbers can be configured to receive event notification short messages. |

##### Usage Guidelines

-   A storage device requires an SMS modem to send short messages. Before running this command, ensure that a modem has been correctly installed and configured.

-   A maximum of 64 phone numbers can be configured for alarms of the same level.

-   A maximum of 64 phone numbers can be configured for events.

-   After alarm notification by short message is configured, the system sends alarms and the events with SMS notification function enabled to specified phone numbers by short message. The short message format is as follows:

China;ClientName;Huawei.Storage;XXXXXXXXXXXXXXXXXXXX;0x1FFFFFFFFFFFFFFB;Informational;2015-06-23 15:03:36;This Is A Test Message.

-   Each part of the short message content is separated using semicolons (;) and defined as follows:
-   Geographical location, which can be manually configured, for example, China.
-   Client of the storage system, for example, ClientName.
-   Device name, for example, Huawei.Storage.
-   Device SN, for example, XXXXXXXXXXXXXXXXXXXX.
-   Alarm or event ID, which indicates an alarm or event, expressed in the hexadecimal format, for example, 0x1FFFFFFFFFFFFFFB.
-   Alarm or event level. The levels include info, warning, major, and critical.
-   Time when an alarm or event occurs, for example, 2015-06-23 15:03:36.
-   Alarm or event name, for example, "This Is A Test Message."

##### Example

Enable the SMS-based alarm notification function and set the country code of the phone number that receives alarm notifications to 86, the SMS center number to 13800280500, and the number that receives alarm notifications to 13912345678.

```text
admin:/>change notification sms enabled=yes sms_center=+8613800280500 receiver_message_list=13912345678
Change configuration successfully.
```

##### System Response

None
