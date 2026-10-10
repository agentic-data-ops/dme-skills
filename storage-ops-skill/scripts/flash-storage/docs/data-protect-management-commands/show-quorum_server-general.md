# show quorum_server general


##### Function

The **show quorum_server general** command is used to query third-place quorum servers.

##### Format

**show quorum_server general** \[ server_id=? \]

##### Parameters

| Parameter   | Description              | Value                                                                                                                                                                                                             |
|-------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server_id=? | ID of the quorum server. | Run the "**show quorum_server general**" command to obtain the value. |

##### Usage Guidelines

None

##### Example

Query all quorum servers.

```text
admin:/>show quorum_server general
Server ID  Server Name   Address        Port   Running Status  Usable Cipher Suites  All Cipher Suites
---------  ------------  -------------  -----  --------------  --------------------  -----------------
0          Server_CPS_0  200.46.110.78  30002  Online      --        --
```

Query quorum server "0".

```text
admin:/>show quorum_server general server_id=0
Server ID            : 0
Server Name          : Server_CPS_0
Description          :
Active IP            : 200.46.110.78
Active Port          : 30002
Standby IP           : 200.46.113.253
Standby Port         : 30002
Running Status       : Online
Usable Cipher Suites : --
All Cipher Suites    : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                                  |
|----------------------|------------------------------------------|
| Server ID            | ID of the quorum server.                 |
| Server Name          | Local server name.                       |
| Description          | Local description of a server.           |
| Active IP            | Active IP address of the quorum server.  |
| Active Port          | Active server port of the quorum server. |
| Standby IP           | Standby IP address of the quorum server. |
| Standby Port         | Standby port of the quorum server.       |
| Running Status       | Running status.                          |
| All Cipher Suites    | All cipher suites.                       |
| Usable Cipher Suites | Usable cipher suites.                    |
| Address              | Active IP address of the quorum server.  |
| Port                 | Active server port of the quorum server. |
