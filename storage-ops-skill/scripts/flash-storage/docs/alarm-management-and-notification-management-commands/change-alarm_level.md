# change alarm_level


##### Function

The **change alarm_level** command is used to change the severity of a specified alarm.

##### Format

**change alarm_level** alarm_id=? level=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| alarm_id=? | Alarm ID. | The alarm ID is in the hexadecimal format, for example: "0xF00C90015". |
| level=? | Alarm severity. | The value can be "info", "warning", "major", or "critical", where: "info": indicates a info severity. "warning": indicates a warning severity. "major": indicates a major severity. "critical": indicates a critical severity. |

##### Usage Guidelines

None

##### Example

Change the severity of a specified alarm.

```text
admin:/>change alarm_level alarm_id=0xF00C90150 level=warning
DANGER: You are about to modify the alarm severity. This operation may affect email, SMS, Syslog, and system notifications of the alarm.
Suggestion: Ensure that you need to perform this operation.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
