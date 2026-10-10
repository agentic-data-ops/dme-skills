# import remote_support smtp_publickey


##### Function

The **import remote_support smtp_publickey** command is used to upload the public key of the CHS mail channel.

##### Format

**import remote_support smtp_publickey** address=? username=? password=? path=? \[ port=? \] \[ protocol=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| address=? | IP address of the FTP or SFTP server. | The value is a string of 1 to 64 characters, excluding colons. |
| username=? | User name of the FTP or SFTP server. | The value is a string of 1 to 64 characters. |
| password=? | Password of the FTP/SFTP server. | The value is a string of 1 to 64 characters. |
| path=? | Path of the email public key on the FTP/SFTP server. | The value is a string that ends with .pub (case insensitive). |
| port=? | Port number of the FTP/SFTP server. | The value is an integer ranging from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |
| protocol=? | File transfer protocol used to transfer the public key of an email. | The value can be FTP or SFTP. The default value is SFTP. |

##### Usage Guidelines

This command is used to upload the public key of an encrypted mail. The public key cannot exceed 1 MB.

 

Prerequisites:

-   The storage system can access the FTP or SFTP server over the network.
-   The FTP or SFTP service has been enabled on the server.
-   The folder for storing the public key has been created.

If the storage system functions as a server during file transfer with an external system, only the SFTP service is supported. However, when functioning as a client, the storage system supports both FTP and SFTP services.

##### Example

Upload the public key of the CHS mail channel.

```text
admin:/>import remote_support smtp_publickey address=192.168.0.100 username=admin password=****** path=/abc.pub
Command executed successfully.
```

##### System Response

None
