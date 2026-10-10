# change smartqos_policy normalized_io_switch


##### Function

The **change smartqos_policy normalized_io_switch** command is used to enable or disable normalized I/O conversion.

##### Format

**change smartqos_policy normalized_io_switch** switch=?

##### Parameters

| Parameter | Description        | Value                                                                                                                    |
|-----------|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| switch=?  | Enablement status. | The value can be "off" or "on", where "off" indicates to disable the function and "on" indicates to enable the function. |

##### Usage Guidelines

When SmartQoS is used, you can use this command to enable or disable normalized I/O conversion.

##### Example

Enable normalized I/O conversion.

```text
admin:/>change smartqos_policy normalized_io_switch switch=on
Command executed successfully.
```

Disable normalized I/O conversion.

```text
admin:/>change smartqos_policy normalized_io_switch switch=off
Command executed successfully.
```

##### System Response

None
