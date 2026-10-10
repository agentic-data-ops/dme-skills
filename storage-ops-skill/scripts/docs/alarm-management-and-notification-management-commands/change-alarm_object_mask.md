# change alarm_object_mask


##### Function

The change alarm_mask command is used to mask alarms of specified objects.

##### Format

**change alarm_object_mask** object_type_list=? mask_switch=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| object_type_list=? | List of types of masked objects. | Objects saved in the configuration file.<br>The ID list of object is separated by commas (,), or the ID range is separated by hyphens (-). The value is from 0 to 65535, for example: "0,5-8". A maximum of 64 object types are supported. |
| mask_switch=? | Switch of the alarm masking function. | The value can be "on" or "off". where: <br>"on": The object masking function is enabled.<br>"off": The object masking function is disabled. |

##### Usage Guidelines

An object type ranges from 0 to 65,535. Separate object types in the type list from each other with commas (,) or hyphens (-), for example, "0,5-8". A maximum of 64 object types are supported.

##### Example

Mask alarms of two specified objects.

```text
admin:/>change alarm_object_mask object_type_list=6,49 mask_switch=on
WARNING: You are about to enable the alarms of specified objects masking function. This operation will make the masked alarms of specified objects are neither reported to the DeviceManager nor sent by email, short message, or syslog. But the alarm masking function does not affect email test alarms and short message test alarms.
Suggestion: Before performing this operation, ensure that the alarms of specified objects need to be masked.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change object 6 mask switch successfully.
Change object 49 mask switch successfully.
```

##### System Response

None
