# test radius configuration


##### Function

The **test radius configuration** command is used to test the connectivity of the RADIUS server.

##### Format

**test radius configuration** address=? port=? scheme=? secret=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| address | RADIUS server address. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value can be a domain name or an IP address (IPv4, IPv6). The domain name is a string of 1 to 255 characters, consisting of case-insensitive letters, digits, and hyphens (-). Domain names at different levels are separated by periods (.). The value cannot start or end with a hyphen (-). |
| port | Port number of the RADIUS server. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value is an integer ranging from 1 to 65535. |
| scheme | Authentication scheme. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value can be "PAP" or "CHAP", where: <br>"PAP": The password authentication protocol scheme is used.<br>"CHAP": The CHAP authentication scheme is used. |
| secret | Shared secret. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value is a string of 8 to 64 characters. |

##### Usage Guidelines

After this command is executed, the connectivity status of the RADIUS server is displayed.

##### Example

Test the connectivity of the RADIUS server with the IP address 192.168.1.2, port number 1812, authentication scheme CHAP, and shared secret 12345678.

```text
admin:/>test radius configuration address=192.168.1.2 port=1812 scheme=CHAP secret=********
Command executed successfully.
```

##### System Response

None
