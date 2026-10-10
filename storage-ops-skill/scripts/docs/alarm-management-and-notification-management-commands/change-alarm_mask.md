# change alarm_mask


##### Function

The **change alarm_mask** command is used to mask specified alarms.

##### Format

**change alarm_mask** alarm_id_list=? mask_switch=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| alarm_id_list=? | List of IDs of masked alarms. | Multiple IDs are separated by commas(,).<br>An alarm ID is in hexadecimal format, for example:'0xF00C90015'.<br>A maximum of 64 alarm IDs can be specified. |
| mask_switch=? | Switch of the alarm masking function. | The value can be "on" or "off", where: <br>"on": The alarm masking function is enabled.<br>"off": The alarm masking function is disabled. |

##### Usage Guidelines

-   An alarm ID is a hexadecimal number. Separate alarm IDs in the ID list from each other with commas (,). A maximum of 64 alarm IDs are supported.
-   When the alarm masking function is enabled, masked alarms are neither reported to the network management system nor sent by emails, short messages, or Syslogs.

 

The alarm masking function does not affect email test alarms and short message test alarms.

##### Example

Mask two specified alarms.

```text
admin:/>change alarm_mask alarm_id_list=0x100F00A000F,0x100F0C90066 mask_switch=on
WARNING: You are about to enable the alarm masking function. This operation will make the masked alarms are neither reported to the DeviceManager nor sent by email, short message, or syslog. But the alarm masking function does not affect email test alarms and short message test alarms.
Suggestion: Before performing this operation, ensure that the alarms need to be masked.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change alarm 0x100F00A000F mask switch successfully.
Change alarm 0x100F0C90066 mask switch successfully.
```

##### System Response

None
