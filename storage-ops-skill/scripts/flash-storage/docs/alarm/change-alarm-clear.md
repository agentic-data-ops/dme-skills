# change alarm clear


##### Function

The **change alarm clear** command is used to clear alarms from the storage system.

##### Format

**change alarm clear** sequence_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| sequence_list=? | Alarm sequence number. | To obtain the value, run "show alarm". You can clear multiple alarms. Use commas (,) to separate alarm serial numbers. |

##### Usage Guidelines

None

##### Example

Cleare alarms whose sequence numbers are "1" and "2".

```text
admin:/>change alarm clear sequence_list=1,2
CAUTION: You are going to clear the selected alarms. If the operation is performed before the upgrade, the pre-upgrade check will not be comprehensively executed. The upgrade may fail.
Suggestion: Before you perform this operation, ensure that the selected faults have been removed.
Do you wish to continue?(y/n)y
Clear alarm 1 successfully.
Clear alarm 2 successfully.
```

##### System Response

None
