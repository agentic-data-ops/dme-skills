# import container_image


##### Function

The **import container_image** command is used to import an application image software package.

##### Format

**import container_image** ip=? user=? password=? path=? \[ port=? \] \[ protocol=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of the FTP or SFTP server. | - |
| user=? | User name for logging in to the FTP or SFTP server. | The value contains 1 to 64 characters, excluding colons (:). |
| password=? | Password for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters. |
| path=? | Path and name of the software package on the FTP or SFTP server. | The file name extension is ".tgz". |
| port=? | Port number of an FTP or SFTP server. | The value ranges from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |
| protocol=? | Transmission protocol type. | The value can be FTP or SFTP. The default value is SFTP. To ensure data transmission security, you are advised to use the SFTP protocol. |

##### Usage Guidelines

-   This command can be executed only on storage arrays.
-   The FTP or SFTP service has been enabled on the server, and the storage system can access the server normally.
-   The directory may vary according to the server type and configuration. For some servers, a slash (/) needs to be added to a path to indicate a root directory. For other servers, no slash needs to be added. Enter the correct path name according to the actual situation.
-   Before importing an application image software package, ensure that the container service has been enabled.

##### Example

Import an application image software package. The IP address of the SFTP server where the image package is stored is "10.10.10.1", the user name is "admin", and the password is "123456". The imported image package is stored in the root directory of the SFTP server and the file name is "image.tgz".

```text
admin:/>import container_image ip=10.10.10.1 user=admin password=****** path=image.tgz
Download package. SUCCESS
Command executed successfully.
```

##### System Response

None
