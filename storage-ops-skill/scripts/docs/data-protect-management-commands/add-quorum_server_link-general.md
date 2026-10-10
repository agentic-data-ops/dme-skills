# add quorum_server_link general


##### Function

The **add quorum_server_link general** command is used to add a link between the disk array and a quorum server.

##### Format

**add quorum_server_link general** server_id=? \[ local_controller=? \] \[ local_port_id=? \] \[ logical_port_name=? \] server_ip=?

##### Parameters

| Parameter           | Description                                            | Value                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server_id=?         | ID of the quorum server.                               | Run the "show quorum_server general" command to obtain the value.                                                                                                                                                          |
| local_port_id=?     | ID of the controller port.                             | Run the "show port general" command to obtain the value. The value contains 1 to 31 characters, including letters, digits, and periods (.). The value cannot start with a digit or a period (.), or end with a period (.). |
| local_controller=?  | ID of the local controller to which the link connects. | The value is in the format of "XA", "XB", "XC", or "XD", where the "X" is an integer such as 0, 1.                                                                                                                         |
| logical_port_name=? | Logical port name.                                     | The value contains 1 to 255 ASCII characters, including letters, digits, underscores (\_), hyphens (-), and periods (.), and must start with a letter or digit.                                                            |
| server_ip=?         | IP address of the quorum server.                       | Run the "show quorum_server general" command to obtain the value.                                                                                                                                                          |

##### Usage Guidelines

None

##### Example

Add a link between quorum server 1 whose IP address is "192.168.0.25" and the disk array, where the controller ID is "0B" and the local port is "ENG0.A4.P0".

```text
admin:/>add quorum_server_link general server_id=1 local_controller=0B local_port_id=ENG0.A4.P0 server_ip=192.168.0.25
Command executed successfully.
```

Add a link between quorum server 0 whose IP address is "192.168.0.25" and the disk array, where the logical port is "CTE0.A2.P2.V4".

```text
admin:/>add quorum_server_link general server_id=0 logical_port_name=CTE0.A2.P2.V4 server_ip=192.168.0.25
Command executed successfully.
```

##### System Response

None
