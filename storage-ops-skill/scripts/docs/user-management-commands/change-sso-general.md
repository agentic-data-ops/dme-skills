# change sso general


##### Function

The **change sso general** command is used to modify the single sign-on (SSO) configuration.

##### Format

**change sso general** switch=? \[ address=? \] \[ port=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| switch | Switch for the SSO function. | The value can be "on" or "off", where: <br>"on": enables the SSO function.<br>"off": disables the SSO function. |
| address | IP address of the SSO server. | The value can be a domain name or an IP address (IPv4 or IPv6). A domain name contains 1 to 255 characters including letters (case insensitive), digits, and hyphens (-). Domain names at different levels are separated by periods (.). A domain name cannot start or end with a hyphen (-). |
| port | Port of the SSO server. | The value is an integer from 1 to 65535. |

##### Usage Guidelines

After the command is executed successfully, the system modifies the SSO configuration based on command parameters.

##### Example

Enable the SSO server whose IP address is "192.168.1.2" and port number is "31943" for the system.

```text
admin:/>change sso general switch=on address=192.168.1.2 port=31943
Command executed successfully.
```

Disable the SSO function for the system.

```text
admin:/>change sso general switch=off
Command executed successfully.
```

##### System Response

None
