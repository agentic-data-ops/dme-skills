# change lun_takeover enhance_switch


##### Function

The **change lun_takeover enhance_switch** is used to set the enhanced masquerading switch of a specified LUN.

##### Format

**change lun_takeover enhance_switch** lun_id=? switch=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_id | Takeover LUN ID. | To obtain the value, run "show lun_takeover general" without parameters. |
| switch | Enhanced switch. | The value can be "on" or "off", where: <br>"on": enables the third-party LUN's enhanced masquerading switch.<br>"off": disables the third-party LUN's enhanced masquerading switch. |

##### Usage Guidelines

None

##### Example

Set the enhanced masquerading switch of a specified LUN.

```text
admin:/>change lun_takeover enhance_switch lun_id=0 switch=on
DANGER: You are about to set the enhanced masquerading switch of third-party masquerading LUNs. This operation will change the masquerading information of the third-party masquerading LUN. Ensure that the third-party masquerading LUN is not mapped to the host. If this function is enabled or disabled on the mapped third-party masquerading LUN, service continuity may be influenced. If the masquerading LUN has been configured with HyperMetro, run the same command on the peer array of the HyperMetro LUN.
Suggestion: Ensure that the third-party masquerading LUN is not mapped to the host.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
