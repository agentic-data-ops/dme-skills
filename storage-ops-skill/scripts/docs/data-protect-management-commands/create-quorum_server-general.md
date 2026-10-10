# create quorum_server general


##### Function

The **create quorum_server general** command is used to create a third-place quorum server.

##### Format

**create quorum_server general** active_ip=? server_name=? \[ active_server_port=? \| description=? \] \*

##### Parameters

| Parameter            | Description                     | Value                                                                                                                                                                  |
|----------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| active_ip=?          | Active IP of the quorum server. | Active IP of the quorum server.                                                                                                                                        |
| server_name=?        | Local server name.              | The value contains 1 to 31 ASCII characters including digits, letters, underscores (\_), hyphens (-), and periods (.), the first character must be a letter or number. |
| active_server_port=? | Server communication port ID.   | The value is an integer ranging from 1 to 65535. If this parameter is not specified, the system uses the default port 30002.                                           |
| description=?        | Local description of a server.  | The value consists of 1 to 127 characters, including digits, letters, underscores(\_), hyphens(-) and dots(.).                                                         |

##### Usage Guidelines

None

##### Example

Create a third-place quorum server whose IP address is "10.100.2.210" and server name is "cps0".

```text
admin:/>create quorum_server general active_ip=10.100.2.210 server_name=cps0
Command executed successfully.
```

##### System Response

None
