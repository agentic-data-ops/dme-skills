# change quorum_server general


##### Function

The **change quorum_server general** command is used to change the information about a third-place quorum server.

##### Format

**change quorum_server general** server_id=? { \[ active_ip=? \] \[ active_server_port=? \] \| \[ standby_ip=? \] \[ standby_server_port=? \] \| \[ server_name=? \] \| \[ description=? \] \| \[ cipher_name=? \] } \*

##### Parameters

| Parameter             | Description                              | Value                                                                                                                                                                  |
|-----------------------|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server_id=?           | ID of the quorum server.                 | Run the "show quorum_server general" command obtain the value.                                                                                                         |
| active_ip=?           | Active IP address of the quorum server.  | \-                                                                                                                                                                     |
| active_server_port=?  | Active port of the quorum server.        | The value is an integer ranging from 1 to 65535.                                                                                                                       |
| standby_ip=?          | Standby IP address of the quorum server. | \-                                                                                                                                                                     |
| standby_server_port=? | Standby port of the quorum server.       | The value is an integer ranging from 1 to 65535.                                                                                                                       |
| server_name=?         | Local server name.                       | The value contains 1 to 31 ASCII characters including digits, letters, underscores (\_), hyphens (-), and periods (.). The first character must be a letter or number. |
| description=?         | Local description of a server.           | The value consists of 1 to 127 characters, including digits, letters, underscores (\_), hyphens (-), and periods (.).                                                  |
| cipher_name           | Cipher suite name.                       | Valid cipher suite name.                                                                                                                                               |

##### Usage Guidelines

None

##### Example

Change an active IP address of the quorum server 1.

```text
admin:/>change quorum_server general server_id=1 active_ip=192.168.2.201
CAUTION: You are about to modify the configuration of the quorum server.
If you enter an incorrect IP address, port ID or cipher suite name, the quorum server will not work.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent service exceptions.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Change the standby IP address of the quorum server 1.

```text
admin:/>change quorum_server general server_id=1 standby_ip=192.168.2.202
CAUTION: You are about to modify the configuration of the quorum server.
If you enter an incorrect IP address, port ID or cipher suite name, the quorum server will not work.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent service exceptions.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Change the cipher list of the quorum server 1.

```text

admin:/>change quorum_server general server_id=1 cipher_name=AES256+RSA+SHA256
WARNING: You are about to modify the arbitration cipher suite. This operation will cause re-authentication between the storage array and all quorum servers. The quorum links will be temporarily disconnected and then reconnected. If an insecure cipher suite name is entered, this operation may pose security risks. If you enter an incorrect cipher suite name, the quorum server may be unavailable.
Suggestion: Before performing this operation, ensure that the operation and parameters are correct to prevent service exceptions.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)
Command executed successfully.
```

##### System Response

None
