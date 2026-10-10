# change event_restore address


##### Function

The **change event_restore address** is used to configure dump addresses for system logs.

##### Format

**change event_restore address** ip=? directory=? user=? password=? \[ protocol=? \] \[ function_test=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of an FTP server or SFTP server for storing system logs that you want to dump. | - |
| directory=? | Path to the system logs that you want to dump. | The file save path contains 1 to 255 characters. The value cannot contain special characters !':;|'$<>&-()#?"\*. The value cannot start with a period (.) or end with a space. The first character after a path separator (/) cannot be a period (.). |
| user=? | User name of an FTP server or an SFTP server. | The value consists of 1 to 63 ASCII characters except single quotation marks ('). |
| password=? | Password for logging in to an FTP server or an SFTP server. | The value consists of 1 to 63 characters. |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use "SFTP". |
| function_test=? | Whether to perform the validity test of dump configurations. | The value can be "yes" or "no", where: <br>"yes": The validity of dump configurations is tested.<br>"no": The validity of dump configurations is not tested.<br> The default value is "no". |

##### Usage Guidelines

If the storage system serves as a server in file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.

##### Example

Modify the system log dumping function, where the new IP address of the SFTP server for storing dumped system logs is "192.168.8.211", name of the directory path for storing those logs is "/path/newcopy", and user name and password for logging in to the SFTP server are "admin" and "123456" respectively.

```text
admin:/>change event_restore address ip=192.168.8.211 directory=/path/newcopy user=admin password=******
Command executed successfully.
```

Verify the updated settings.

```text
admin:/>show event_restore
Enable  IP             FTP/SFTP Path  User Name  Protocol
------  -------------  -------------  ---------  ---------
Yes     192.168.8.211  /              admin      SFTP
```

Test the system events dump function. The IP address of the SFTP server for storing dumped system events is "192.168.8.211", the name of the directory for storing those events is "/path/newcopy", and the user name and password for logging in to the SFTP server are "admin" and "123456" respectively.

```text
admin:/>change event_restore address ip=192.168.8.211 directory=/path/newcopy user=admin password=****** function_test=yes
Command executed successfully.

```

##### System Response

None
