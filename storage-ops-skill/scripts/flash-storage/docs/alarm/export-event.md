# export event


##### Function

The **export event** command is used to export logs, key logs, Call Home data, event information, diagnostic files, disk enclosure logs, FTDS statistics, or disk data destruction reports of a storage system.

##### Format

**export event** event_type=? ip=? user=? password=? path=? \[ port=? \] \[ protocol=? \] \[ clean_device_file=? \] \[ controller_id=? \] \[ enclosure_id_list=? \] \[ encryption=? \] \[ key=? \] \[ reenter_key=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| event_type=? | Type of the files that you want to export. | The value can be "event", "log", "disk_log", "all_log", "key_log", "hssd_log", "call_home", "diagnostic_file", "enclosure_log", "disk_data_erasure_log", or "ftds_statdata", where: <br>"event": event information.<br>"log": recent logs and disk enclosure logs.<br>"disk_log": disk log information.<br>"all_log": all system logs and disk enclosure logs.<br>"hssd_log": log information about all HSSDs.<br>"call_home": Call Home data.<br>"diagnostic_file": diagnosis file.<br>"enclosure_log": disk enclosure log information.<br>"disk_data_erasure_log": disk data erasure log.<br>"ftds_statdata": FTDS statistics.<br>"key_log": key logs. |
| ip=? | IP address of an FTP or SFTP server. NOTE: To export log files, an FTP server or SFTP server must be available and is accessible to the storage system. | - |
| user=? | Name of a user for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password for logging in to an FTP or SFTP server. | The value contains 1 to 64 characters. |
| path=? | File name and path to an exported log file. | The path must start with a slash (/). The exported file is in the compressed package format. This parameter specifies the path and file name of the exported event or log on the FTP/SFTP server. For example: <br>"/test/" indicates that events or logs are saved in the "test" folder on the FTP/SFTP server. The file name is automatically generated.<br>"/test" indicates that events or logs are saved in the "test" file.<br>If you specify the file name, we recommend you add the file suffix. Add suffix ".tgz" when "event_type" is set to "event", "log", "disk_log", "all_log", "call_home", "hssd_log", "diagnostic_file", or "enclosure_log". If you do not specify the suffix, it will be added on the CLI automatically. |
| port=? | ID of the employed port on an FTP or SFTP server. | The value is an integer from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |
| protocol=? | Protocol type. | The value can be "FTP" or "SFTP" and the default value is "SFTP". To ensure the security of data transfer, you are advised to use SFTP. |
| clean_device_file=? | Whether to delete the event file that resides in the storage system memory after the event file is exported to an FTP or SFTP server. This parameter is valid only when "event_type" is set to "event". | The value can be "yes" or "no", where: <br>"yes": The event file that resides in the storage system memory will be deleted after the event file is exported to an FTP or SFTP server.<br>"no": The event file that resides in the storage system memory will not be deleted after the event file is exported to an FTP or SFTP server.<br> The default value is "yes". |
| controller_id=? | ID of a controller. | Controller IDs are separated by commas (,). The value format is "XA", "XB", "XC", or "XD", where "X" is an integer starting from 0, for example, "0A" and "1C". NOTE: This parameter is visible only when event_type is set to "log", "key_log", "disk_log", "hssd_log", "call_home", "ftds_statdata", or "all_log". |
| enclosure_id_list=? | ID list of disk enclosures. | To obtain the value, run "show expansion_module". This parameter can be specified only when "event_type" is set to "enclosure_log". Disk enclosure IDs are separated by commas (,). |
| encryption=? | Whether to export files in encryption mode. | The value can be "yes" or "no", where: <br>"yes": exports files in encryption mode.<br>"no": exports files without encryption.<br> The default value is "no". |
| key=? | Password used for encrypting exported files. | The password contains 8 to 16 characters.<br>The password must contain special characters !"#$%&'()*+,-./:;<=>?@[\]^`{_|}~ and spaces.<br>The password must contain any two types of uppercase letters, lowercase letters, and digits. |
| reenter_key=? | Confirm the encryption key. | The password contains 8 to 16 characters.<br>The password must contain special characters !"#$%&'()*+,-./:;<=>?@[\]^`{_|}~ and spaces.<br>The password must contain any two types of uppercase letters, lowercase letters, and digits. |

##### Usage Guidelines

-   When this command is executed to export logs, the logs of all controllers will be exported at the same time.
-   This command can export log files only to an FTP server or an SFTP server connected to the storage system.
-   Use this command when you want to export system logs, key logs, Call Home data, events, diagnostic files, disk enclosure logs, FTDS statistics, or disk data erasure logs, and use them to find out the alarm causes or check device running status.

 

Diagnostic files cannot be exported during an upgrade.Prerequisites for using this command:
-   The FTP or SFTP server is accessible to the storage system.
-   The FTP or SFTP service has been started on the server.

-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.
-   It will take several minutes to an hour to collect and export the files whose type is "log", "key_log", "disk_log", "call_home", "all_log", "diagnostic_file", "enclosure_log", "ftds_statdata", or "disk_data_erasure_log".

##### Example

Export certain events to an FTP server, where the IP address of the FTP server is "192.168.8.211", the user name for logging in to the FTP server is "admin", the password is "123456", the exported events will be stored in the root directory of the FTP server, and the exported events will be saved as the "event.tgz" file.

```text
admin:/>export event event_type=event ip=192.168.8.211 user=admin password=****** path=/event.tgz protocol=FTP
Command executed successfully.
```

Export certain logs and disk enclosure logs to an FTP server, where the IP address of the FTP server is "192.168.8.211", the user name for logging in to the FTP server is "admin", the password is "admin", the exported logs will be stored in the root directory of the FTP server, and the exported logs will be saved with the default file name.

```text
admin:/>export event event_type=log ip=192.168.8.211 user=admin password=***** path=/ protocol=FTP
WARNING: It will take minutes to collect and export the data. The longest time required is 1 hour.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Controller ID: 0A
Package Path: /log_controller_0A_MAIN.tgz
Controller ID: 0B
Package Path: /log_controller_0B.tgz
Controller ID: 0A
Package Path: /enclosure_log_DAE[0A0.B].tgz
Controller ID: 0B
Package Path: /enclosure_log_DAE[0A0.A].tgz
Command executed successfully.
```

Export FTDS statistics. The IP address of the FTP server is "192.168.8.221", the user name for logging in to the FTP server is "admin", the password is "123456", the exported log files will be stored in the root directory of the FTP server, and the files will be saved as a file of the default name.

```text
admin:/>export event event_type=ftds_statdata ip=192.168.8.211 user=admin password=***** path=/ protocol=FTP
WARNING: It will take minutes to collect and export the data. The longest time required is 1 hour.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Controller ID: 0A
Package Path: /ftds_statdata_0A.tgz
Controller ID: 0B
Package Path: /ftds_statdata_0B.tgz
Controller ID: 0A
Package Path: /ftds_statdata_DAE[0A0.B].tgz
Controller ID: 0B
Package Path: /ftds_statdata_DAE[0A0.A].tgz
Command executed successfully.
```

Export certain Call Home data to an FTP server, where the IP address of the FTP server is "192.168.8.211", the user name for logging in to the FTP server is "admin", the password is "admin", the exported Call Home data will be stored in the root directory of the FTP server, and the exported Call Home data will be saved with the default file name.

```text
admin:/>export event event_type=call_home ip=192.168.8.211 user=admin password=***** path=/ protocol=FTP
WARNING: It will take minutes to collect and export the data. The longest time required is 10 minutes.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Controller ID: 0A
Package Path: /collector_chs_file_0A.tgz
Controller ID: 0B
Package Path: /collector_chs_file_0B.tgz
Command executed successfully.
```

Export disk logs to an FTP server, where the IP address of the FTP server is "192.168.8.211", the user name for logging in to the FTP server is "admin", the password is "admin", the exported logs will be stored in the root directory of the FTP server, and the exported logs will be saved with the default file name.

```text
admin:/>export event event_type=disk_log ip=192.168.8.211 user=admin password=***** path=/ protocol=FTP
WARNING: It will take minutes to collect and export the data. The longest time required is 1 hour.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Controller ID: 0A
Package Path: /dha_0A.tgz
Controller ID: 0B
Package Path: /dha_0B.tgz
Controller ID: 0A
Package Path: /dha_DAE[0A0.B].tgz
Controller ID: 0B
Package Path: /dha_DAE[0A0.A].tgz
Command executed successfully.
```

Export all logs of the system and disk enclosures to an FTP server, where the IP address of the FTP server is "192.168.8.211", the user name for logging in to the FTP server is "admin", the password is "admin", the exported logs will be stored in the root directory of the FTP server, and the exported logs will be saved with the default file name.

```text
admin:/>export event event_type=all_log ip=192.168.8.211 user=admin password=***** path=/ protocol=FTP
WARNING: It will take minutes to collect and export the data. The longest time required is 1 hour.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Controller ID: 0A
Package Path: /log_controller_0A_MAIN.tgz
Controller ID: 0B
Package Path: /log_controller_0B.tgz
Controller ID: 0A
Package Path: /enclosure_log_DAE[0A0.B].tgz
Controller ID: 0B
Package Path: /enclosure_log_DAE[0A0.A].tgz
Command executed successfully.
```

Export logs of HSSDs to an FTP server, where the IP address of the FTP server is "192.168.8.211", the user name for logging in to the FTP server is "admin", the password is "admin", the exported logs will be stored in the root directory of the FTP server, and the exported logs will be saved with the default file name.

```text
admin:/>export event event_type=hssd_log ip=192.168.8.211 user=admin password=***** path=/ protocol=FTP
WARNING: It will take minutes to collect and export the data. The longest time required is 1 hour.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Controller ID: 0A
Package Path: /hssd_log_0A.tgz
Controller ID: 0B
Package Path: /hssd_log_0B.tgz
Controller ID: 0A
Package Path: /hssd_log_DAE[0A0.B].tgz.tgz
Controller ID: 0B
Package Path: /hssd_log_DAE[0A0.A].tgz.tgz
Command executed successfully.
```

Export key logs. The address of the FTP server is "192.168.8.211", the user name is "admin", and the password is "123456". The log file is saved in the FTP root directory and named by default.

```text
admin:/>export event event_type=key_log ip=192.168.8.211 user=admin password=****** path=/ port=21 protocol=FTP
WARNING: It will take minutes to collect and export the data. The longest time required is 1 hour.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Controller ID: 0A
Package Path: /private_log_0A.tgz
Controller ID: 0B
Package Path: /private_log_0B.tgz
Command executed successfully.
```

Export the diagnosis file. The IP address of the FTP server is "192.168.8.211", the user name is "admin", and the password is "123456". The diagnosis file is saved in the FTP root directory, and the default file name is "DiagnoseInfo.tgz".

```text
admin:/>export event event_type=diagnostic_file ip=192.168.8.211 user=admin password=***** path=/ protocol=FTP
WARNING: It will take minutes to collect and export the data. The longest time required is 10 minutes.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Export disk enclosure logs. The IP address of the FTP server is "192.168.8.211", the user name is "admin", and the password is "admin". The log file is saved in the FTP root directory, and the file name is the default one.

```text
admin:/>export event event_type=enclosure_log ip=192.168.8.211 user=admin password=***** path=/ port=21 protocol=FTP
WARNING:
It will take minutes to collect and export the data. The longest time required is 1 hour.
Are you sure you really want to perform the operation?(y/n)y
Controller ID: 0A
Package Path: /enclosure_log_DAE[0A0.B].tgz
Controller ID: 0B
Package Path: /enclosure_log_DAE[0A0.A].tgz
Command executed successfully.
```

Export disk data erasure logs. The IP address of the FTP server is "192.168.8.211", the user name is "admin", and the password is "123456". The log file is saved in the FTP root directory and named by default.

```text
admin:/>export event event_type=disk_data_erasure_log ip=192.168.8.211 user=admin password=****** path=/ protocol=FTP
Command executed successfully.
```

##### System Response

None
