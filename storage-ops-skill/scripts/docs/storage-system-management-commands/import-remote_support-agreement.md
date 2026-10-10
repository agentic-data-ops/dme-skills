# import remote_support agreement


##### Function

The **import remote_support agreement** command is used to upload the photo of a letter of authorization.

##### Format

**import remote_support agreement** address=? username=? password=? path=? \[ port=? \] \[ protocol=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| address=? | IP address of the FTP or SFTP server. | - |
| username=? | User name of the FTP or SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password of a user allowed by the FTP/SFTP server. | The value contains 1 to 64 characters. |
| path=? | Path storing the photo of a letter of authorization on the FTP/SFTP server. | The value is a character string that ends with file name extension ".jpg" (case insensitive). |
| port=? | Port of the FTP/SFTP server. | The value is an integer ranging from 1 to 65535. <br>If protocol=FTP, the default value is "21".<br>If protocol=SFTP, the default value is "22". |
| protocol=? | Protocol used for transmitting the photo of a letter of authorization. | The value can be "FTP" or "SFTP" and the default value is "SFTP". |

##### Usage Guidelines

This command is used to upload the photo of a letter of authorization. The photo size cannot exceed 20 MB.

 

Prerequisites:

-   Storage systems can correctly access the FTP server or SFTP server over the network.
-   The FTP or SFTP service has been enabled on the server.
-   A directory has been created for storing the photo of a letter of authorization.

If a storage system serves as a server in the file transfer with external systems, the storage system supports SFTP only. If a storage system serves as a client, the storage system supports both FTP and SFTP.

##### Example

Upload the photo or scanned copy of a letter of authorization.

```text
admin:/>import remote_support agreement address=192.168.0.100 username=admin password=****** path=/abc.jpg
Command executed successfully.
```

##### System Response

None
