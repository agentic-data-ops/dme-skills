# export kms key


##### Function

The **export kms key** command is used to export the key file of the internal key management service.

##### Format

**export kms key** ip=? user=? password=? path=? \[ protocol=? \] \[ port=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of the FTP or SFTP server. | - |
| user=? | Username for logging in to the FTP server or SFTP server. | The value consists of 1 to 64 characters without colons (:). |
| password=? | Password for logging in to the FTP server or SFTP server. | The value consists of 1 to 64 characters. |
| path=? | Name and path of the key file to be exported. | The file name extension of key files must be .dat. The file name must be supported by the FTP and SFTP server. |
| protocol=? | Transfer protocol type. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use SFTP. |
| port=? | Port number of the FTP or SFTP server. | The value is an integer ranging from 1 to 65535. <br>If protocol=FTP, the default value is "21".<br>If protocol=SFTP, the default value is "22". |

##### Usage Guidelines

-   This command can export the key file of the internal key management service only from the storage system to an FTP server or SFTP server connected to the storage system.

 

Prerequisites for using this command:
-   The FTP server or SFTP server is accessible to the storage system.
-   The FTP service or SFTP service has been started on the server.

-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.

##### Example

Export the key file of the internal key management service. The file name is "InternalKey.dat", the IP address of the FTP server that stores the key file is "192.168.10.109", the user name for accessing the FTP server is "admin", and the password is "123456". The exported the key file is saved to the root directory on the FTP server.

```text
admin:/>export kms key ip=192.168.10.109 user=admin password=****** path=InternalKey.dat protocol=FTP
Command executed successfully.
```

##### System Response

None
