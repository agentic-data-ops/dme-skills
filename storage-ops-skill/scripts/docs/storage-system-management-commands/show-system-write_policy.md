# show system write_policy


##### Function

The **show system write_policy** command is used to display the current cache write policy of the system.

##### Format

**show system write_policy**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Display the current cache write policy of the system.

```text
admin:/>show system write_policy
Write Protect Switch      : Enable
Write Protect Time(hours) : 192Hour(s)
```

##### System Response

The following table describes the parameter meanings.

| Parameter                 | Meaning                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Write Protect Switch      | System write protection switch.                                                                                         |
| Write Protect Time(hours) | Period that the system runs in a single controller environment before the write policy is switched to write protection. |
