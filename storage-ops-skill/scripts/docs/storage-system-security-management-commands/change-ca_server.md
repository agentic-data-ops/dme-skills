# change ca_server


##### Function

The **change ca_server** command is used to modify the CA server configuration.

##### Format

**change ca_server** enabled=? \[ ca_server_addr=? \] \[ update_endpoint=? \] \[ update_lead_time=? \] \[ ca_server_port=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled | Whether to enable automatic certificate update. | The value can be yes or no, where: <br>yes: The automatic certificate update function is enabled.<br>no: The automatic certificate update function is disabled. |
| ca_server_addr | Address of the CA server. | - |
| ca_server_port | Port number of the CA server. | The value is an integer ranging from 1 to 65535. |
| update_endpoint | Endpoint for automatic certificate update. | The value is a string of 1 to 255 ASCII characters. The value cannot contain ':?"<>|* or start with a space or period (.). Path separators / and \ cannot be directly followed by a period (.). |
| update_lead_time | Time before which the certificate is automatically updated, in days. | The value ranges from 7 to 180, in days. |

##### Usage Guidelines

Run the "**change ca_server**" command to modify the CA server configuration.

##### Example

Modify the CA server configuration.

```text
admin:/>change ca_server enabled=yes ca_server_addr=192.168.1.1 ca_server_port=80 update_lead_time=30 update_endpoint=/autoupdate
WARNING: You are about to enable the automatic certificate update function. After this operation, the certificate will be automatically updated before it expires, which may interrupt services that use the certificate.
Suggestion: Before performing this operation, check whether the risk is acceptable.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
