# show notification trap


##### Function

The **show notification trap** command is used to query the settings of the trap server.

##### Format

**show notification trap** \[ server_id=? \]

##### Parameters

| Parameter   | Description            | Value                                                                                                                                                                                                                                       |
|-------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server_id=? | ID of the trap server. | To obtain the value, run "**show notification trap**" without parameters. The value can be an integer between 0 and 3. |

##### Usage Guidelines

-   To query the settings of all trap servers, run "**show notification trap**".
-   To query the settings of a specific trap server, run "**show notification trap** \[ server_id=? \]".

##### Example

To query the settings of all trap servers.

```text
admin:/>show notification trap
Server ID Server IP Server Port Trap Version Trap Type USM User Name
--------- ------------ ----------- ------------ --------- -------------
0     192.168.10.7 168     v3      Original  Kaimse
1     192.168.9.65 162     v1      All     --
2     192.168.9.04 162     v2c     Parsed    --
3     192.168.19.5 162     v3      All     user
```

To query the settings of the trap server whose ID is "0".

```text
admin:/>show notification trap server_id=0
Server ID Server IP Server Port Trap Version Trap Type USM User Name
--------- ------------ ----------- ------------ --------- -------------
0     192.168.10.7 168     v3      Original  Kaimse
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                                                                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Server ID     | ID of the trap server.                                                                                                                                                             |
| Server IP     | Trap server address. The value can be an IP address or domain name. If the value is a domain name, all the IP addresses corresponding to the domain name must point to one server. |
| Server Port   | Port ID of the trap server.                                                                                                                                                        |
| Trap Version  | Version of the trap server.                                                                                                                                                        |
| Trap Type     | Type of the trap server.                                                                                                                                                           |
| USM User Name | USM user name of the trap server.                                                                                                                                                  |
