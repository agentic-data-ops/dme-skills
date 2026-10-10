# show notification sms


##### Function

The **show notification sms** command is used to check the settings of the SMS-based alarm and event notification function.

##### Format

**show notification sms**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the settings of the SMS-based alarm and event notification functions.

```text
admin:/>show notification sms
Send Enable                         : Enable
SMS Center                          : +8613800280500
Critical Alert Receiver Number List : 13912345678
Major Alert Receiver Number List    : --
Warning Alert Receiver Number List  : --
Event Receiver Number List          : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                           | Meaning                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Send Enable                         | Indicates whether the SMS-based alarm notification function is enabled.                |
| SMS Center                          | Indicates the SMS center number.                                                       |
| Critical Alert Receiver Number List | Indicates that alarms of the severities of critical are sent to the specified number.  |
| Major Alert Receiver Number List    | Indicates that alarms of the severities of major are sent to the specified number.     |
| Warning Alert Receiver Number List  | Indicates that alarms of the severity of warning are sent to the specified number.     |
| Event Receiver Number List          | Phone number list for receiving the event IDs with short message notification enabled. |
