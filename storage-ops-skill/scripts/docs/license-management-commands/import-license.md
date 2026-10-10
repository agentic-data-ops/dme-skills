# import license


##### Function

The **import license** command is used to **import license** files. You can activate or update license files by running this command.

##### Format

**import license** ip=? user=? password=? license_path=? \[ port=? \] \[ protocol=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of a File Transfer Protocol (FTP) server or a Secure File Transfer Protocol (SFTP) server. To import a license file, an FTP server or an SFTP server must be available and is accessible to the storage system. | - |
| user=? | Name of a user for logging in to an FTP server or an SFTP server. | The value contains 1 to 64 characters without colons(:). |
| password=? | Password for logging in to an FTP server or an SFTP server. | The value contains 1 to 64 characters. |
| license_path=? | File name of and path to a license file that you want to import. | The file name extension of a correct license file must be .dat. |
| port=? | ID of the employed port on an FTP server or an SFTP server. | The value is an integer ranging from 1 to 65535. <br>If protocol=FTP, the default value is "21".<br>If protocol=SFTP, the default value is "22". |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use Secure File Transfer Protocol (SFTP). |

##### Usage Guidelines

-   A license file can activate a value-added function for the storage system. To enable a value-added function, you must purchase and import a license file for the function.
-   This command can **import license** only from an FTP server or an SFTP server connecting to the storage system.

 

Prerequisites for using this command:
-   The FTP server or SFTP server is accessible to the storage system.
-   The FTP service or SFTP service has been started on the server.

-   The license file to be imported must be valid for the desired value-added function, because this command will override the existing license file and an incorrect license file can fail the desired function.
-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.

##### Example

To import a license file whose name is "license.dat", where the IP address of the FTP server for storing the license file is "10.10.10.1", the user name for accessing the FTP server is "admin", and the user's password is "123456", run the following command.

```text
admin:/>import license ip=10.10.10.1 user=admin password=****** license_path=license.dat protocol=FTP
WARNING: You are about to import a license file. This operation will overwrite the previous license file. Before performing this operation, check whether the license file is correct. If a feature is deleted from the newly imported license, the feature configuration will not be lost, but you cannot perform any management operations, such as adding, deleting, or modifying the feature.
Suggestion: Before you perform this operation, ensure that the license file to be imported is correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

To import a license file whose name is "license.dat", where the IP address of the FTP server for storing the license file is "10.10.10.1", the user name for accessing the FTP server is "admin", and the user's password is "123456", run the following command.

```text
admin:/>import license ip=10.10.10.1 user=admin password=****** license_path=license.dat protocol=FTP
WARNING: The effective capacity in the license file you imported exceeds the system specification. The capacity exceeding the specification cannot be used. This operation will overwrite the previous license file. If a feature is deleted from the newly imported license, the feature configuration will not be lost, but you cannot perform any management operations, such as adding, deleting, or modifying the feature.
Suggestion: Before performing this operation, confirm that the license file to be imported is correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
