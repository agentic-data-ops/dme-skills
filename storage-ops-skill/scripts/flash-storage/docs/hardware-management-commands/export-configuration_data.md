# export configuration_data


##### Function

The **export configuration_data** command is used to export the configuration file that resides in the storage system's memory. Such a configuration file stores important configuration information on the storage system's components and services. Export configuration data regularly and save it securely so that you can restore the configuration when the storage system fails.

##### Format

**export configuration_data** ip=? user=? password=? db_file=? \[ port=? \] \[ protocol=? \] \[ clean_device_file=? \] \[ forcible_export=? \] \[ encryption=? \] \[ key=? \] \[ reenter_key=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of the FTP or SFTP server to which you want to export a configuration file. | - |
| user=? | User name for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters. |
| db_file=? | File name of and path to a configuration file on an FTP or SFTP server. | The file name extension must be ".dat". The file name must be supported by the FTP or SFTP server. |
| port=? | ID of the employed port on an FTP or SFTP server. | The value ranges from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use SFTP. |
| clean_device_file=? | After the configuration file is exported to an FTP or SFTP server, whether to delete the temporary configuration file cached in the storage system memory during configuration file export. | The value can be "yes" or "no", where: <br>"yes": immediately deletes the temporary configuration file cached in the storage system memory.<br>"no": deletes the temporary configuration file cached in the storage system memory after five minutes.<br> The default value is "yes". |
| forcible_export=? | Forcible export flag. | The value can be "yes" or "no", where: <br>"yes": forcibly exports the configuration data without checking whether there are configuration tasks running on the current system. Configuration files forcibly exported cannot be imported to the storage array for restoring configuration.<br>"no": Before the export, check whether there are configuration tasks running on the current system. If yes, stop the export. |
| encryption=? | Whether to export files in encryption mode. | The value can be "yes" or "no", where: <br>"yes": exports files in encryption mode.<br>"no": exports files without encryption.<br> The default value is "no". |
| reenter_key=? | Confirm the encryption key. | The password contains 8 to 16 characters.<br>The password must contain special characters !"#$%&'()*+,-./:;<=>?@[\]^`{_|}~ and spaces.<br>The password must contain any two types of uppercase letters, lowercase letters, and digits. |
| key=? | Password used for encrypting exported files. | The password contains 8 to 16 characters.<br>The password must contain special characters !"#$%&'()*+,-./:;<=>?@[\]^`{_|}~ and spaces.<br>The password must contain any two types of uppercase letters, lowercase letters, and digits. |

##### Usage Guidelines

-   This command allows you to export a configuration file only to an FTP or SFTP server connected to the storage system.

 

Prerequisites for using this command:
-   The FTP server or SFTP server is accessible to the storage system.
-   The FTP service or SFTP service on the server has been enabled.
-   The folder for storing a configuration file has been created.

-   The file name extension must be ".dat". Otherwise, the exported configuration file cannot be used for importing configuration data.
-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.
-   Configuration files forcibly exported by running this command cannot be imported to the storage system for restoring configuration.

##### Example

Export configuration data that resides in the storage system's memory to an FTP server, where the IP address of the FTP server is "192.168.8.211", user name for logging in to the FTP server is "admin", and password is "123456". The exported configuration data will be stored in the root directory of the FTP server, and the exported events will be saved as the "conf.dat" file.

```text
admin:/>export configuration_data ip=192.168.8.211 user=admin password=****** db_file=conf.dat protocol=FTP
WARNING: 1. You are about to export system configuration information. This operation may cause leakage of user information.
2. If the file is forcibly exported, the exported file cannot be imported to the storage array for restoring configuration.
Suggestion: Before performing this operation, confirm that you are fully aware of the previous risks.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
