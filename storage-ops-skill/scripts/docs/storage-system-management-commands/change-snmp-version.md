# change snmp version


##### Function

The **change snmp version** command is used to set the status of the SNMPv1 and SNMPv2c protocols and the switch status of the SNMP unique controller enclosure ID function.

##### Format

**change snmp version** v1v2c_switch=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| v1v2c_switch=? | Protocol enablement status. | The value can be "On" or "Off", where: <br>"On": enables a protocol.<br>"Off": disables a protocol. |

##### Usage Guidelines

-   The SNMPv1 and SNMPv2c protocols are disabled by default.
-   The SNMPv3 protocol is enabled by default.
-   The default switch status of the unique controller enclosure ID function is disabled.
-   For compatibility, the system retains the support for SNMPv1 and SNMPv2c. To ensure data security, you are advised to use SNMPv3.

##### Example

Set protocols SNMPv1 and SNMPv2c to "Off".

```text
admin:/>change snmp version v1v2c_switch=Off
Command executed successfully.
```

Set protocols SNMPv1 and SNMPv2c to "On".

```text
admin:/>change snmp version v1v2c_switch=On
CAUTION: You are about to enable SNMPv1 and SNMPv2c. But you are advised to use the secure SNMPv3 protocol only.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
