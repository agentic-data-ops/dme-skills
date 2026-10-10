# change notification trap


##### Function

The **change notification trap** command is used to change the settings of the trap server. Run this command if you want to change the settings of a trap server for receiving alarms.

##### Format

**change notification trap** server_id=? trap_version=? server_ip=? server_port=? \[ trap_type=? \] \[ usm_user_name=? \] \[ function_test=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| server_id=? | ID of the trap server. | The value is an integer between 0 and 3. |
| trap_version=? | Version of the trap server. | The value can be "v1", "v2c", or "v3", where: <br>"v1": indicates SNMPv1.<br>"v2c": indicates SNMPv2c.<br>"v3": indicates SNMPv3.<br> NOTE: To ensure compatibility, the system still supports SNMPv1 and SNMP v2c. To ensure data security, it is strongly recommended to use SNMPv3. |
| server_ip=? | Trap server address. The value can be an IP address or domain name. If the value is a domain name, all the IP addresses corresponding to the domain name must point to one server. | The value can be a domain name or an IPv4 or IPv6 address. The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits, and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| server_port=? | Port ID of the trap server. | The value is an integer between 1 and 65535. |
| function_test=? | Whether or not to send a test alarm notification after the command is executed. | The value can be "yes" or "no", where: <br>"yes": A test alarm notification will be sent after the command is executed.<br>"no": A test alarm notification will not be sent after the command is executed. |
| trap_type=? | Type of the trap server. | The value can be "parsed", "parsed_time_string", "original", "original_time_string", or "all", where: <br>"parsed": sends parsed alarms to a trap server (Trap OID:1.3.6.1.4.1.2011.2.91.10.2.1.0.1).<br>"parsed_time_string": sends parsed alarms to a trap server (Trap OID:1.3.6.1.4.1.2011.2.251.20.1.2.1).<br>"original": sends original alarms that are not parsed to a trap server (Trap OID:1.3.6.1.4.1.34774.4.1.4.2).<br>"original_time_string": sends original alarms that are not parsed to a trap server (Trap OID:1.3.6.1.4.1.2011.2.251.20.2.1.1).<br>"all": sends parsed, parsed_time_string, original, and original_time_string alarms to a trap server. The default value is "all."<br> NOTE: "parsed" and "original" are two forms of one alarm. An original alarm only carries original alarm parameters while a parsed alarm is readable and processed based on the original form. parsed_time_string alarms and parsed alarms are different in their reported OIDs and time field types. The time field types of parsed_time_string alarms and parsed alarms are OCTET STRING and DateAndTime respectively. original_time_string alarms and original alarms are different in their reported OIDs and time field types. The time field types of original_time_string alarms and original alarms are OCTET STRING and DateAndTime respectively. |
| usm_user_name=? | USM user name of the trap server. (The value contains 4 to 32 characters). | To obtain the value, press "Ctrl+A" or run "show snmp usm" without parameters. The default value is "Kaimse". |

##### Usage Guidelines

-   After the configurations of a trap server are modified, the storage system sends alarm information to the specified application server or maintenance terminal based on the new configurations.
-   When "trap_version" is v3, usm_user_name must enter the USM user name obtained by running the "show snmp usm" command. After that, the system will use the configured USM user name to send the SNMPv3 Trap.

##### Example

Change the version, IP address, port ID, type, and USM user name of trap server "1" to "v3", "192.168.3.2", "20001", "parsed", and "user", respectively.

```text
admin:/>change notification trap server_id=1 trap_version=v3 server_ip=192.168.3.2 server_port=20001 trap_type=parsed usm_user_name=user
Change configuration successfully.
```

##### System Response

None
