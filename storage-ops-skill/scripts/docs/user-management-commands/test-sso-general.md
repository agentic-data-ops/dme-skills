# test sso general


##### Function

The **test sso general** command is used to test the connectivity of the single sign-on (SSO) server.

##### Format

**test sso general** address=? port=?

##### Parameters

| Parameter | Description                   | Value                                                                                                                                                                                                                                                                                         |
|-----------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| address   | IP address of the SSO server. | The value can be a domain name or an IP address (IPv4 or IPv6). A domain name contains 1 to 255 characters including letters (case insensitive), digits, and hyphens (-). Domain names at different levels are separated by periods (.). A domain name cannot start or end with a hyphen (-). |
| port      | Port of the SSO server.       | The value is an integer from 1 to 65535.                                                                                                                                                                                                                                                      |

##### Usage Guidelines

After the command is executed, the connectivity of the SSO server will be returned.

##### Example

Test the connectivity of the SSO server whose IP address is "192.168.1.2" and port number is "31943".

```text
admin:/>test sso general address=192.168.1.2 port=31943
Command executed successfully.
```

##### System Response

None
