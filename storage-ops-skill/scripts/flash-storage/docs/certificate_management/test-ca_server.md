# test ca_server


##### Function

The **test ca_server** command is used to test the configuration of a CA server.

##### Format

**test ca_server** \[ ca_server_addr=? \] \[ ca_server_port=? \]

##### Parameters

| Parameter      | Description                   | Value                                            |
|----------------|-------------------------------|--------------------------------------------------|
| ca_server_addr | Address of the CA server.     | \-                                               |
| ca_server_port | Port number of the CA server. | The value is an integer ranging from 1 to 65535. |

##### Usage Guidelines

Run the **test ca_server** command to test the CA server configuration.

##### Example

Test the connectivity of the CA server.

```text
admin:/>test ca_server ca_server_addr=192.168.1.1 ca_server_port=80
Command executed successfully.
```

##### System Response

None
