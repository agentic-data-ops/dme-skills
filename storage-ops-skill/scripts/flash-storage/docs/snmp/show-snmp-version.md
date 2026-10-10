# show snmp version


##### Function

The **show snmp version** command is used to check the status of the SNMPv1 and SNMPv2c protocols as well as status of the SNMP unique controller enclosure ID switch.

##### Format

**show snmp version**

##### Parameters

None

##### Usage Guidelines

-   By default, the SNMPv1 and SNMPv2c protocols are disabled.
-   By default, the SNMPv3 protocol is enabled.

##### Example

Check the status of the SNMPv1 and SNMPv2c protocols.

```text
admin:/>show snmp version
SNMP V1V2C Switch : Off
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                                                           |
|-------------------|-------------------------------------------------------------------|
| SNMP V1V2C Switch | Whether the SNMPv1 and SNMPv2c protocols are enabled or disabled. |
