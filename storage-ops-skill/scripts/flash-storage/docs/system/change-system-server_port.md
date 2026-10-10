# change system server_port


##### Function

The **change system server_port** command is used to modify port information of the system.

##### Format

**change system server_port** server_name=? port_num=?

##### Parameters

| Parameter     | Description                 | Value                                                    |
|---------------|-----------------------------|----------------------------------------------------------|
| server_name=? | Service name to be changed. | The value can be "SSH".                                  |
| port_num=?    | Port number to be changed.  | The value can be "22" or an integer from 24000 to 24900. |

##### Usage Guidelines

-   The first parameter of this command indicates the name of this service,this command just can be used to modify the port number of SSH service.
-   The second parameter of this command indicates the port number of the service to be changed. The value can be "22" or an integer from 24000 to 24900.
-   If dump servers (for example, for performance statistics file dumping and alarm dumping) are configured and use the SFTP protocol, ensure that port IDs used by the dump servers are consistent with those used by SSH services of the storage array.

##### Example

To change the storage system's port of SSH to "24000",run the following command.

```text
admin:/>change system server_port server_name=SSH port_num=24000
WARNING:You are about to change the SSH service port number. This operation changes the port used to manage the storage system.
Suggestion: Ensure that the SSH port number needs to be changed.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operaton?(y/n)y
Command executed successfully.
```

##### System Response

None
