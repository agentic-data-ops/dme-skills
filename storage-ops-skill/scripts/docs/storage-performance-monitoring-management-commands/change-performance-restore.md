# change performance restore


##### Function

The **change performance restore** command is used to configure the policies for dumping the performance statistics of the storage system.

##### Format

**change performance restore** enabled=? \[ ip=? \] \[ path=? \] \[ user=? \] \[ password=? \] \[ protocol=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Switch of the dumping function for the performance statistics of the storage system. | The value can be "yes" or "no", where: <br>"yes": The dumping for system performance statistics will be enabled.<br>"no": The dumping for system performance statistics will be disabled.<br> The default value is "no". |
| ip=? | IP address of a File Transfer Protocol (FTP) server or a Secure File Transfer Protocol (SFTP) server to which system performance statistics will be dumped. | - |
| path=? | A path under which system performance statistics will be stored. | - |
| user=? | User name of an FTP server or an SFTP server. | The value contains 1 to 63 characters. |
| password=? | Password for logging in to an FTP server or an SFTP server. | The value contains 1 to 63 characters. |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use Secure File Transfer Protocol (SFTP). |

##### Usage Guidelines

-   To configure the switch of the system performance statistics dumping function, the IP address of the FTP server or SFTP server to which performance statistics will be exported, the path to the performance statistics, and the user name and password for logging in to the FTP server or SFTP server, run "**change performance restore** enabled=? ip=? path=? user=? password=?".
-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.

##### Example

To modify the system performance statistics dumping function, where the new IP address of the SFTP server for storing dumped statistics is 192.168.8.211, the name of the folder for storing those statistics is home, and the user name and password for logging in to the SFTP server are "admin" and "123456" respectively, run the following command.

```text
admin:/>change performance restore enabled=yes ip=192.168.8.211 path=home user=admin password=******
Command executed successfully.
```

##### System Response

None
