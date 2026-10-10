# show snmp engineid


##### Function

The **show snmp engineid** command is used to query the SNMP controller enclosure ID of a controller.

##### Format

**show snmp engineid** controller=?

##### Parameters

| Parameter  | Description         | Value                                                                                       |
|------------|---------------------|---------------------------------------------------------------------------------------------|
| controller | ID of a controller. | The value is in the format of XA, XB, XC, or XD, where X is an integer ranging from 0 to 3. |

##### Usage Guidelines

Run the "**show snmp engineid** controller=?" command to query the controller enclosure ID of a specified controller.

##### Example

Query the SNMP controller enclosure ID on controller 0A.

```text
admin:/>show snmp engineid controller=0A
SNMP V3 EngineID      : 2102350BSJ10572330510
SNMP V3 EngineID(HEX) : 80 00 13 70 05 32 31 30 32 33 35 30 42 53 4A 31 30 35 37 32 33 33 30 35 31 30
```

##### System Response

The following table describes the parameter meanings.

| Parameter             | Meaning                                                |
|-----------------------|--------------------------------------------------------|
| SNMP V3 EngineID      | SNMPv3 controller enclosure ID.                        |
| SNMP V3 EngineID(HEX) | SNMPv3 controller enclosure ID, in hexadecimal format. |
