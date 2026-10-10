# change radius configuration


##### Function

The **change radius configuration** command is used to modify the RADIUS configuration.

##### Format

**change radius configuration** switch=? address=? port=? scheme=? secret=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| switch | Whether to enable the RADIUS service. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value can be "on" or "off", where: <br>"on": enables the RADIUS service.<br>"off": disables the RADIUS service. |
| address | RADIUS server address. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value can be a domain name or an IP address (IPv4, IPv6). The domain name is a string of 1 to 255 characters, consisting of case-insensitive letters, digits, and hyphens (-). Domain names at different levels are separated by periods (.). The value cannot start or end with a hyphen (-). |
| port | Port number of the RADIUS server. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value is an integer ranging from 1 to 65535. |
| scheme | Authentication scheme. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value can be "PAP" or "CHAP", where: <br>"PAP": The password authentication protocol scheme is used.<br>"CHAP": The CHAP authentication scheme is used. |
| secret | Shared secret. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value is a string of 8 to 64 characters. |

##### Usage Guidelines

After this command is executed successfully, the system modifies the RADIUS configuration based on the parameters in the command.

##### Example

Modify the RADIUS configuration as follows: Enable the RADIUS service and change the RADIUS server address to 1.1.1.1, port number to 1812, authentication scheme to CHAP, and shared secret to 12345678.

```text
admin:/>change radius configuration switch=on address=1.1.1.1 port=1812 scheme=CHAP secret=********
Command executed successfully.
```

##### System Response

None
