# show quorum_server_link general


##### Function

The **show quorum_server_link general** command is used to query the links between the disk array and quorum servers.

##### Format

**show quorum_server_link general** \[ server_id=? \]

##### Parameters

| Parameter   | Description              | Value                                                             |
|-------------|--------------------------|-------------------------------------------------------------------|
| server_id=? | ID of the quorum server. | Run the "show quorum_server general" command to obtain the value. |

##### Usage Guidelines

None

##### Example

To query the links between the disk array and all quorum servers, run the following command.

```text
admin:/>show quorum_server_link general
Link ID Link Status Local Controller Local Port ServerId
--------- ----------- ---------------- ---------- ------------
1 Link Up 0A ENG0.A4.P0 1
2 Link Up 0A ENG0.A4.P1 2
```

To query the link between the disk array and quorum server 1, run the following command.

```text
admin:/>show quorum_server_link general server_id=1
Link ID Link Status Local Controller Local Port ServerId
--------- ----------- ---------------- ---------- ------------
1 Link Up 0A ENG0.A4.P0 1
2 Link Up 0A ENG0.A4.P1 1
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                     |
|------------------|-----------------------------|
| Link ID          | Link ID.                    |
| Link Status      | Link status.                |
| Local Controller | ID of the local controller. |
| Local Port       | Local port.                 |
| Server Id        | ID of the quorum server.    |
