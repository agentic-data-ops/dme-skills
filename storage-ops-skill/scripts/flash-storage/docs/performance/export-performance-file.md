# export performance file


##### Function

The **export performance file** command is used to export historical performance statistics files.

##### Format

**export performance file** file=? ip=? user=? password=? path=? \[ port=? \] \[ protocol=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file=? | Historical performance statistics file to be exported. | To obtain the value, run "show performance file". |
| ip=? | IP address of an FTP server or an SFTP server. | - |
| user=? | User name of an FTP server or an SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password for logging in to an FTP server or an SFTP server. | The value contains 1 to 64 characters. |
| path=? | Export path to the historical performance statistics file. | Path of the historical performance statistics file to be stored in the FTP/SFTP server. "/test/" indicates that the exported file is saved in the "test" folder on a specified server, and the file name is automatically generated. "/test" indicates that the exported file is saved as the "test" file (Length of every file or folder name is less than 201). |
| port=? | ID of the employed port on an FTP server or an SFTP server. | The value is an integer between 1 and 65535. <br>If the "protocol=" parameter is set to FTP, the default value is "21".<br>If the "protocol=" parameter is set to SFTP, the default value is "22". |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use SFTP. |

##### Usage Guidelines

-   This command allows historical performance statistics files to be exported only to an FTP server or an SFTP server connected to the storage system.

 

Prerequisites for using this command are as follows:
-   The storage system can access the FTP server or SFTP server.
-   The FTP service or SFTP service on the server has been enabled.
-   The folder for storing historical performance statistics files has been created and the folder name must not contain spaces.

-   The storage system can automatically name exported historical performance statistics files with the .tgz file name extension.
-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.

##### Example

Query all performance statistics files.

```text
admin:/>show performance file
File Name                                                          Updated Time                   File Size
-----------------------------------------------------------------  -----------------------------  ----------
PerfData_XXXXX_SN_snystrw623h7d739dmc9_SP0_0_20150729194049.tgz    2015-07-29/19:42:09 UTC+08:00     2.000KB
PerfData_XXXXX_SN_snystrw623h7d739dmc9_SP0_0_20150729193655.tgz    2015-07-29/19:36:57 UTC+08:00     2.000KB
PerfData_XXXXX_SN_snystrw623h7d739dmc9_SP1_0_20150729194049.tgz    2015-07-29/19:42:09 UTC+08:00     1.000KB
PerfData_XXXXX_SN_snystrw623h7d739dmc9_SP1_0_20150729193655.tgz    2015-07-29/19:36:57 UTC+08:00     1.000KB
```

Export the "PerfData_XXXXX_SN_210235G7KA10D9000001_SP0_0\_20131222162515.tgz" file to the "file" folder on an FTP server whose IP address, user name, and password are "192.168.38.11", "admin", and "123456" respectively.

```text
admin:/>export performance file file=PerfData_XXXXX_SN_210235G7KA10D9000001_SP0_0_20131222162515.tgz ip=192.168.38.11 user=admin password=****** path=/file/ protocol=FTP
Command executed successfully.
```

##### System Response

None
