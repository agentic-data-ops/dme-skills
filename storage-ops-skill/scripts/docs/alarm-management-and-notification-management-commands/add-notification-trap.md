# add notification trap


##### Function

The **add notification trap** command is used to add a Trap server for receiving alarms.

##### Format

**add notification trap** trap_version=? server_ip=? server_port=? \[ trap_type=? \] \[ usm_user_name=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| trap_version=? | Version of the Trap server. | The value can be "v1", "v2c", or "v3", where: <br>"v1": SNMPv1.<br>"v2c": SNMPv2c.<br>"v3": SNMPv3.<br> NOTE: To ensure compatibility, the system still supports SNMPv1 and SNMP v2c. To ensure data security, it is strongly recommended to use SNMPv3. |
| server_ip=? | Trap server address. The value can be an IP address or domain name. If the value is a domain name, all the IP addresses corresponding to the domain name must point to one server. | The value can be a domain name or an IPv4 or IPv6 address. The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits, and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| server_port=? | Port ID of the Trap server. | The value can be an integer from 1 to 65535. |
| trap_type=? | Type of the Trap server. | The value can be "parsed", "parsed_time_string", "original", "original_time_string", or "all", where: <br>"parsed": sends parsed alarms to a trap server (Trap OID:1.3.6.1.4.1.2011.2.91.10.2.1.0.1).<br>"parsed_time_string": sends parsed alarms to a trap server (Trap OID:1.3.6.1.4.1.2011.2.251.20.1.2.1).<br>"original": sends original alarms that are not parsed to a trap server (Trap OID:1.3.6.1.4.1.34774.4.1.4.2).<br>"original_time_string": sends original alarms that are not parsed to a trap server (Trap OID:1.3.6.1.4.1.2011.2.251.20.2.1.1).<br>"all": sends parsed, parsed_time_string, original, and original_time_string alarms to a trap server. The default value is "all."<br> NOTE: "parsed" and "original" are two forms of one alarm. An original alarm only carries original alarm parameters while a parsed alarm is readable and processed based on the original form. "parsed_time_string" alarms and "parsed" alarms are different in their reported OIDs and time field types. The time field types of "parsed_time_string" alarms and "parsed" alarms are "OCTET STRING" and "DateAndTime" respectively. "original_time_string" alarms and "original" alarms are different in their reported OIDs and time field types. The time field types of "original_time_string" alarms and original alarms are "OCTET STRING" and "DateAndTime" respectively. |
| usm_user_name=? | USM user name of the Trap server. The value contains 4 to 32 characters. | To obtain the value, press "Ctrl+A" or run "show snmp usm" without parameters. The default value is "Kaimse". |

##### Usage Guidelines

-   After a Trap server is added, the storage system sends alarm information to the specified application server or maintenance terminal.
-   When "trap_version" is "v3", a USM user must be specified for the system. You can enter the USM user name by configuring the "usm_user_name" parameter. If the "usm_user_name" parameter is not configured, the system will use the default user name "Kaimse". Before running this command, you need to ensure that the USM user to be used exists. If the USM user does not exist, you can run the "add snmp usm" command to create the USM user.

##### Example

Add a Trap server and set its version, IP address, port ID, type, and USM user name to "v3", "192.168.9.65", "162", "parsed", and "Kaimse", respectively.

```text
admin:/>add notification trap trap_version=v3 server_ip=192.168.9.65 server_port=162 trap_type=parsed usm_user_name=Kaimse
Command executed successfully.
```

##### System Response

None
