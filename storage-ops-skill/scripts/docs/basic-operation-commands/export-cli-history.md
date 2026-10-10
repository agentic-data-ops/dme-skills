# export cli history


##### Function

The **export cli history** command is used to export the historical records of executed commands.

##### Format

**export cli history** ip=? user=? password=? path=? \[ port=? \] \[ protocol=? \] \[ encryption=? \] \[ key=? \] \[ reenter_key=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of an FTP or SFTP server to which the command execution history will be exported. NOTE: The FTP server or SFTP server must be accessible to the storage system. | - |
| user=? | Name of a user for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters, excluding colons (:). |
| password=? | Password for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters. |
| path=? | File name of and path to a file for storing the exported history on an FTP server or an SFTP server. The file name must be supported by the FTP and SFTP server. | The file name cannot contain any of the following characters: ' \ / : * ? " < > |. |
| port=? | ID of the employed port on an FTP server or an SFTP server. | The value ranges from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP" and the default value is "SFTP". To ensure the security of data transfer, you are advised to use SFTP. |
| encryption=? | Whether to encrypt files. | The value can be "yes" or "no", where: <br>"yes": enables the encryption.<br>"no": disables the encryption.<br> The default value is "no". |
| key=? | Encryption key. | The value contains 8 to 16 characters. <br>The key must contain special characters.<br>The key must contain at least two of the following: uppercase letters, lowercase letters, and digits. |
| reenter_key=? | Confirm the encryption key. | The value contains 8 to 16 characters. <br>The key must contain special characters.<br>The key must contain at least two of the following: uppercase letters, lowercase letters, and digits. |

##### Usage Guidelines

This command is only used to export the history of executed commands on the current controller to an FTP server or SFTP server connected to the storage system.

 

Prerequisites for using this command:

-   The FTP server or SFTP server is accessible to the storage system.
-   The FTP service or SFTP service has been started on the server.
-   The folder for storing the exported history file has been created on the FTP server or SFTP server.

If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.

##### Example

Export the historical records of executed commands. The IP address of the SFTP server is "192.168.8.211", user name is "admin", password is "123456", the folder that stores the exported record is "path", and the name of the exported file is "test.txt".

```text
admin:/>export cli history ip=192.168.8.211 user=admin password=****** path=/path/test.txt
Command executed successfully.
```

##### System Response

None
