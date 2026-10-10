# clear cifs connection


##### Function

The **clear cifs connection** command is used to close the network connection of the specified client or server.

##### Format

**clear cifs connection** controller=? { server_ip=? \| client_ip=? } \[ port=? \]

##### Parameters

| Parameter  | Description        | Value                                                                                                                             |
|------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| controller | Controller ID.     | The value is in the format of "XA" or "XB" or "XC" or "XD", where "X" is an integer ranging from 0 to 3, for example: "0A", "1C". |
| server_ip  | Server IP address. | The value is an IPv4 or IPv6 address.                                                                                             |
| client_ip  | Client IP address. | The value is an IPv4 or IPv6 address.                                                                                             |
| port       | Port number.       | The value is an integer ranging from 0 to 65535.                                                                                  |

##### Usage Guidelines

Running this command may interrupt services. Therefore, exercise caution when running this command.

##### Example

Close the CIFS connection.

```text
admin:/>clear cifs connection controller=0A server_ip=10.46.23.120
WARNING: You are about to disconnect the service network of the client. This operation will interrupt client services.
Suggestion: Confirm that you know about the impact before running this command.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
