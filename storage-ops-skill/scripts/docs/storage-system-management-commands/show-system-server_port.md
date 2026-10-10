# show system server_port


##### Function

The **show system server_port** command is used to query the port information about a specific service.

##### Format

**show system server_port** server_name=?

##### Parameters

| Parameter     | Description                             | Value                   |
|---------------|-----------------------------------------|-------------------------|
| server_name=? | The server name which need to be query. | The value can be "SSH". |

##### Usage Guidelines

None

##### Example

To query system port infomation, run the following command. The command output varies depending on cli interface.

```text
admin:/>show system server_port server_name=SSH
Server Name : SSH
Port Number: 24000
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning      |
|-------------|--------------|
| Server Name | Server name. |
| Port Number | Port number. |
