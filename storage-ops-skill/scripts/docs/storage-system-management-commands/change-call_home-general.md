# change call_home general


##### Function

The **change call_home general** command is used to set the Call Home service.

##### Format

**change call_home general** switch=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| switch | Whether the Call Home service is enabled. | The value can be "on" or "off", where: <br>"on": Enables the Call Home service.<br>"off": Disables the Call Home service.<br> The default value is "off". |

##### Usage Guidelines

Before executing this command, confirm that the basic configurations of the Call Home service are correct.

##### Example

Set the Call Home service.

```text
admin:/>change call_home general switch=on
CAUTION: You are about to set the eService. The eService can periodically send health status data of the storage array to the eService site. The data includes fault diagnosis data, performance statistics, logs, and configurations. The eService does not send any application data or personal privacy data.
Suggestion: Before performing this operation, ensure that the eService settings are correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
