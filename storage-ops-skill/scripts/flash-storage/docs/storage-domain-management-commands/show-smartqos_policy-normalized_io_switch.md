# show smartqos_policy normalized_io_switch


##### Function

The **show smartqos_policy normalized_io_switch** command is used to query the switch status of normalized I/O conversion.

##### Format

**show smartqos_policy normalized_io_switch**

##### Parameters

None

##### Usage Guidelines

When SmartQoS is used, you can use this command to check whether normalized I/O conversion is switched on.

##### Example

Query that the switch status of normalized I/O conversion is off.

```text
admin:/>show smartqos_policy normalized_io_switch
Switch : Off
```

Query that the switch status of normalized I/O conversion is on.

```text
admin:/>show smartqos_policy normalized_io_switch
Swtich : On
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                                                                                                                             |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------|
| Switch    | Switch status of normalized I/O conversion. off indicates that the switch is disabled, and on indicates that the switch is enabled. |
