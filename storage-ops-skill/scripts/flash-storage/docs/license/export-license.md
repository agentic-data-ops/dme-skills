# export license


##### Function

The **export license** command is used to **export license** files.

##### Format

**export license** ip=? user=? password=? license_path=? \[ port=? \] \[ protocol=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of an File Transfer Protocol (FTP) server or a Secure File Transfer Protocol (SFTP) server. To export a license file, an FTP server or an SFTP server must be available and is accessible to the storage system. | - |
| user=? | Name of a user for logging in to an FTP server or an SFTP server. | The value contains 1 to 64 characters without colons(:). |
| password=? | Password for logging in to an FTP server or an SFTP server. | The value contains 1 to 64 characters. |
| license_path=? | File name of and path to a license file that you want to export. | The file name extension of a correct license file must be .dat. |
| port=? | ID of the employed port on an FTP server or an SFTP server. | The value is an integer ranging from 1 to 65535. <br>If protocol=FTP, the default value is "21".<br>If protocol=SFTP, the default value is "22". |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use Secure File Transfer Protocol (SFTP). |

##### Usage Guidelines

-   A license file can activate a value-added function for the storage system. To enable a value-added function, you must purchase and import a license file for the function.
-   This command can **export license** only from the storage system to an connecting FTP server or SFTP server.

 

Prerequisites for using this command:
-   The FTP server or SFTP server is accessible to the storage system.
-   The FTP service or SFTP service has been started on the server.

-   The license file to be exported must be valid for the desired value-added function.
-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.

##### Example

Export a license file whose name is "license.dat" and save it under the root directory of the FTP server. The IP address of the FTP server for storing the license file is "192.168.10.109", the user name for accessing the FTP server is "admin", and the user's password is "123456".

```text
admin:/>export license ip=192.168.10.109 user=admin password=****** license_path=license.dat protocol=FTP
Command executed successfully.
```

##### System Response

None
