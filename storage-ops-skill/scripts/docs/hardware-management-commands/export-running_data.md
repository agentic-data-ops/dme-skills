# export running_data


##### Function

The **export running_data** command is used to export storage system configuration information to a .txt file. Such a .txt file can be read by users but cannot be used during configuration information import. If you need to know storage system configuration information, run this command.

##### Format

**export running_data** ip=? user=? password=? running_data_file=? \[ port=? \] \[ protocol=? \] \[ clean_device_file=? \] \[ encryption=? \] \[ key=? \] \[ reenter_key=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of the FTP or SFTP server to which you want to export a configuration information file. | - |
| user=? | User name for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters. |
| running_data_file=? | Path and name of the file that saves the configuration information on an FTP server or an SFTP server. | The file name extension must be ".txt", and the file name cannot contain any of the following special characters: \ / : * ? " < > |. |
| port=? | Port number of an FTP or SFTP server. | The value ranges from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If :protocol" is set to "SFTP", the default value is "22". |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use SFTP. |
| clean_device_file=? | Whether to delete the configuration information file from the storage system memory after the configuration information file is exported to an FTP server or SFTP server. If the parameter is set to "no", you are not allowed to export the system configuration information again within five minutes. | The value can be "yes" or "no", where: <br>"yes": The configuration information file in the storage system memory will be deleted after the configuration information file is exported to an FTP or SFTP server.<br>"no": The configuration information file in the storage system memory will not be deleted after the configuration information file is exported to an FTP or SFTP server.<br> The default value is "yes". |
| encryption=? | Whether to export files in encryption mode. | The value can be "yes" or "no", where: <br>"yes": exports files in encryption mode.<br>"no": exports files without encryption.<br> The default value is "no". |
| key=? | Password used for encrypting exported files. | The password contains 8 to 16 characters.<br>The password must contain special characters !"#$%&'()*+,-./:;<=>?@[\]^`{_|}~ and spaces.<br>The password must contain any two types of uppercase letters, lowercase letters, and digits. |
| reenter_key=? | Confirm the encryption key. | The password contains 8 to 16 characters.<br>The password must contain special characters !"#$%&'()*+,-./:;<=>?@[\]^`{_|}~ and spaces.<br>The password must contain any two types of uppercase letters, lowercase letters, and digits. |

##### Usage Guidelines

-   A configuration file in ".txt" format cannot be used for importing configuration information.
-   This command allows you to export a configuration information file only to an FTP or SFTP server connected to the storage system.

 

Prerequisites for using this command:
-   The FTP or SFTP server is accessible to the storage system.
-   The FTP service or SFTP service on the server has been enabled.
-   The folder for storing a configuration information file has been created.

-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.
-   This operation may leak users' information.
-   If the exported configuration information contains information in Chinese and Japanese, configuration information files must be opened in the UTF-8 format. Otherwise, information in Chinese and Japanese will be displayed abnormally.

##### Example

Export storage system configuration information to a "txt" file. The IP address of the FTP server is "192.168.8.211", the user name is "admin", the password is "12345678", the location is the root directory, and the file name is "configuration_information.txt".

```text
admin:/>export running_data ip=192.168.8.211 user=admin password=******** running_data_file=configuration_information.txt protocol=FTP
WARNING: You are about to export system configuration information.
Suggestion: Confirm that you want to perform the operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
