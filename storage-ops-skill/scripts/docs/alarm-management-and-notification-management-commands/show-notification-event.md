# show notification event


##### Function

The **show notification event** command is used to query the settings of event notifications using traps, short messages, and emails.

##### Format

**show notification event** \[ trap_switch=? \| sms_switch=? \| email_switch=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| trap_switch | Switch of querying whether the trap notification function for a specified event or an event list is enabled. | "on": The trap notification function for a specified event or an event list is enabled.<br>"off": The trap notification function for a specified event or an event list is disabled. |
| sms_switch | Switch of querying whether the short message notification function for a specified event or an event list is enabled. | "on": The short message notification function for a specified event or an event list is enabled.<br>"off": The short message notification function for a specified event or an event list is disabled. |
| email_switch | Switch of querying whether the email notification function for a specified event or an event list is enabled. | "on": The email notification function for a specified event or an event list is enabled.<br>"off": The email notification function for a specified event or an event list is disabled. |

##### Usage Guidelines

The "**show notification event**" command is executed to query the event notification configuration. If no parameter is specified, all events whose trap, SMS, or email notification function is enabled are queried by default. The output is sorted by trap switch.

##### Example

Query the settings of event notifications using traps, short messages, and emails.

```text
admin:/>show notification event
Event ID        Level          Name                                           Alarm Object Type  Trap Switch  Sms Switch  Email Switch
--------------  -------------  ---------------------------------------------  -----------------  -----------  ----------  ------------
0x200F002A0015  Informational  User Login Succeeded                           202                On           Off         On
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                                                 |
|-------------------|---------------------------------------------------------|
| Event ID          | ID of the event that needs to be reported.              |
| Level             | Level of the event that needs to be reported.           |
| Name              | Name of the event that needs to be reported.            |
| Alarm Object Type | Type of the event that needs to be reported.            |
| Trap Switch       | Switch of the trap notification for the event.          |
| Sms Switch        | Switch of the short message notification for the event. |
| Email Switch      | Switch of the email notification for the event.         |
