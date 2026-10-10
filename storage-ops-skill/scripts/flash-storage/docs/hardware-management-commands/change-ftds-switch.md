# change ftds switch


##### Function

The **change ftds switch** command is used to enable or disable the Fault Tracing Diagnosing System (FTDS) tracing function. This command can be used to set the main switch (excluding the workload switch), tracing switch, phase switch, latency switch, counting switch, workload collection switch, and workload feature extraction switch.

##### Format

**change ftds switch** { switch=? \| trace_switch=? \| phase_switch=? \| delay_switch=? \| count_switch=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| switch=? | FTDS main switch. | The value can be "On" or "Off", where: <br>"On": enables the FTDS main switch.<br>"Off": disables the FTDS main switch. |
| trace_switch=? | FTDS tracing switch. | The value can be "On" or "Off", where: <br>"On": enables the FTDS tracing switch.<br>"Off": disables the FTDS tracing switch. |
| phase_switch=? | FTDS phase switch. | The value can be "On" or "Off", where: <br>"On": enables the FTDS phase switch.<br>"Off": disables the FTDS phase switch. |
| delay_switch=? | FTDS delay switch. | The value can be "On" or "Off", where: <br>"On": enables the FTDS delay switch.<br>"Off": disables the FTDS delay switch. |
| count_switch=? | FTDS count switch. | The value can be "On" or "Off", where: <br>"On": enables the FTDS count switch.<br>"Off": disables the FTDS count switch. |

##### Usage Guidelines

The FTDS switch is used to track the process and diagnose the storage system, and provides functions including fault diagnosis, phase statistics, latency statistics, I/O counting, workload collection, and workload feature extraction.

##### Example

Enable the FTDS main switch.

```text
admin:/>change ftds switch switch=On
Command executed successfully.
```

Enable the FTDS trace switch.

```text
admin:/>change ftds switch trace_switch=On
Command executed successfully.
```

Enable the FTDS phase switch.

```text
admin:/>change ftds switch phase_switch=On
Command executed successfully.
```

Enable the FTDS delay switch.

```text
admin:/>change ftds switch delay_switch=On
Command executed successfully.
```

Enable the FTDS count switch.

```text
admin:/>change ftds switch count_switch=On
Command executed successfully.
```

##### System Response

None
