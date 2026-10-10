# change port eth_snsd_switch


##### Function

The **change port eth_snsd_switch** command is used to enable or disable the SNSD function of an Ethernet port.

##### Format

**change port eth_snsd_switch** eth_port_id=? snsd_enable=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| eth_port_id | Port ID. | To obtain the value, run "show port general". |
| snsd_enable | Whether to enable or disable the SNSD function. | The value can be "yes" or "no", where: <br>"yes": enables the SNSD function.<br>"no": disables the SNSD function.<br> The default value is "no". |

##### Usage Guidelines

Before performing this operation, ensure that the Ethernet port supports the SNSD function.

##### Example

Enable the SNSD function of Ethernet port "CTE0.A.H0". The ID and command output vary depending on products. The ID and output here are just examples.

```text
admin:/>change port eth_snsd_switch eth_port_id=CTE.A.H0 snsd_enable=yes
CAUTION: You are about to enable the SNSD function for a RoCE port.
After this operation, the storage device will send LLDP packets to the switch. If the switch does not support the enhanced feature, alarms may be generated due to incorrect packet statistics.
Suggestion: Before performing this operation, ensure that the enhanced feature is supported by the switch.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Disable the SNSD function of Ethernet port "CTE0.A.H0". The ID and command output vary depending on products. The ID and output here are just examples.

```text
admin:/>change port eth_snsd_switch eth_port_id=CTE.A.H0 snsd_enable=no
CAUTION: You are about to disable the SNSD function for a RoCE port.
After this operation, automatic link setup and fast fault detection will not be supported.
Suggestion: Ensure that you need to perform this operation.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
