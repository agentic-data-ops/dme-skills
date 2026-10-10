# show alarm_mask


##### Function

The **show alarm_mask** command is used to query information about masked alarms.

##### Format

**show alarm_mask**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query information about masked alarms in the system.

```text
admin:/>show alarm_mask
Alarm ID    Mask Switch  Existed Flag  Alarm Object Type  Alarm Name                         Alarm Level
----------  -----------  ------------  -----------------  ---------------------------------  -----------
0xF0060001  On           False         6                  Management Network Port Is Faulty  Major
0xF0060002  On           False         6                  Expansion Port Link Down           Major
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                               |
|-------------------|---------------------------------------|
| Alarm ID          | ID of a masked alarm.                 |
| Mask Switch       | Switch of the alarm masking function. |
| Existed Flag      | Whether all alarms are cleared.       |
| Alarm Object Type | Alarm object type.                    |
| Alarm Name        | Alarm name.                           |
| Alarm Level       | Alarm severity.                       |
