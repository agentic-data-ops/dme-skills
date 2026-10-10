# change notification event


##### Function

The **change notification event** command is used to set the switch of event notifications using a Trap server, SMSs, and emails.

##### Format

**change notification event** { event_id=? \| event_id_list=? } { trap_switch=? \| sms_switch=? \| email_switch=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| event_id=? | ID of the event to be reported. | The value is a hexadecimal number. |
| event_id_list=? | ID list of events to be reported. | An ID is a hexadecimal number.<br>A maximum of 512 event IDs are supported. |
| trap_switch=? | Switch of the Trap notification function for a specified event or an event list. | The value can be "on" or "off", where: <br>"on": enables the Trap notification function for a specified event or an event list.<br>"off": disables the Trap notification function for a specified event or an event list. |
| sms_switch | Switch of the SMS notification function for a specified event or an event list. | The value can be "on" or "off", where: <br>"on": enables the SMS notification function for a specified event or an event list.<br>"off": disables the SMS notification function for a specified event or an event list. |
| email_switch | Switch of the email notification function for a specified event or an event list. | "on": enables the email notification function for a specified event or an event list.<br>"off": disables the email notification function for a specified event or an event list. |

##### Usage Guidelines

After all event notifications are enabled, the system will report events using a Trap server, SMSs, and emails to the specified application server or maintenance terminal.

##### Example

Modify the notification configuration of the event whose ID is 0x200F002A0015.

```text
admin:/>change notification event event_id=0x200F002A0015 trap_switch=on
Change event 0x200F002A0015  switch successfully.
```

Modify the notification configuration of events whose IDs are 0x200F002A0015 and 0x200F002A0019.

```text
admin:/>change notification event event_id_list=0x200F002A0015,0x200F002A0019 trap_switch=on
Change event 0x200F002A0015  switch successfully.
Change event 0x200F002A0019  switch successfully.
```

##### System Response

None
