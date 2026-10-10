# show file export_path


##### Function

The **show file export_path** command is used to export system data to a directory in the storage system and show the directory to users.

##### Format

**show file export_path** file_type=? \[ controller_id=? \] \[ disk_id=? \] \[ encryption=? \] \[ key=? \] \[ reenter_key=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_type=? | File type. | The value can be event, log, running_data, configuration_data, all_log, key_log, smart, workload, call_home, diagnostic_file, isolated_disklog, running_disklog, enclosure_log, or ftds_statdata, where: <br>event: event information file.<br>log: recent logs and disk enclosure logs.<br>running_data: system running data file.<br>configuration_data: system configuration file.<br>all_log: all system logs and disk enclosure logs.<br>smart: SMART information of a disk.<br>workload: service load.<br>call_home: Call Home data.<br>diagnostic_file: diagnostic file.<br>isolated_disklog: isolated disk log information.<br>running_disklog: running disk log information.<br>enclosure_log: disk enclosure log information.<br>ftds_statdata: FTDS statistics.<br>key_log: key logs. |
| controller_id=? | ID of a controller. | Controller IDs are separated by commas (,). The value format is "XA", "XB", "XC", or "XD", where "X" is an integer starting from 0, for example, "0A" and "1C". This parameter is visible only when file_type is set to "log", "all_log", "key_log", "call_home", "smart", "isolated_disklog", or "ftds_statdata". |
| disk_id=? | ID of a disk. | To obtain the value, run "show disk general" without parameters. This parameter can be specified only when "file_type" is set to "running_disklog". |
| enclosure_id=? | Enclosure ID. | This parameter can be specified only when "file_type" is set to "enclosure_log". |
| encryption=? | Whether to export files in encryption mode. | The value can be "yes" or "no", where: <br>"yes": exports files in encryption mode.<br>"no": exports files without encryption.<br> The default value is "no". |
| key=? | Password used for encrypting exported files. | The password contains 8 to 16 characters .2:The password must contain special characters !"#$%&'()*+,-./:;<=>?@[\]^`{_|}~ and spaces.<br>The password must contain any two types of uppercase letters, lowercase letters, and digits. |
| reenter_key=? | Confirm the encryption key. | The password contains 8 to 16 characters.<br>The password must contain special characters !"#$%&'()*+,-./:;<=>?@[\]^`{_|}~ and spaces.<br>The password must contain any two types of uppercase letters, lowercase letters, and digits. |

##### Usage Guidelines

-   Run the "**show file export_path**" command to export system data to a file directory in the storage system and display the directory path to users.
-   Run the "**show file export_path** file_type=? \[ controller_id =? \] \[ disk_id=? \]" command to export the system data of a specified controller to a file directory of the storage system and display the directory path to users (excepting the files whose type is "log", "all_log", "key_log", "call_home", "smart", "workload", "diagnostic_file", "isolated_disklog", "running_disklog", "ftds_statdata", or "enclosure_log").
-   This command is used by the information collection tool to collect system information. It is recommended that this command be used together with the "delete file" command on the same node.

##### Example

Export system configuration data and show the path to users.

```text
admin:/>show file export_path file_type=configuration_data
File Path : /OSM/coffer_data/omm/export_import/db.dat
```

Send a notification of exporting the system Call Home data and return a message about whether the export is successful.

```text
admin:/>show file export_path file_type=call_home
Command executed successfully.
```

Send a notification of exporting the system FTDS statistics and return a message about whether the export is successful.

```text
admin:/>show file export_path file_type=ftds_statdata
Command executed successfully.
```

Send a notification of exporting the system diagnostic file and return a message about whether the export is successful.

```text
admin:/>show file export_path file_type=diagnostic_file
Command executed successfully.
```

Export the log data of a running disk, and return the controller ID and file name of the disk to the user.

```text
admin:/>show file export_path file_type=running_disklog disk_id=DAE010.0
WARNING: You are about to export the logs of the running disk. This operation will cause the storage performance to deteriorate during the collection.
Suggestion: Do not run this command during peak hours.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
File Name : DAE010.0_6SL5P7DL0000N3273PV3.tgz
Controller ID : 0A
```

Send a notification of exporting the disk enclosure log file and return a message about whether the export is successful.

```text
admin:/>show file export_path file_type=enclosure_log
Command executed successfully.
```

Send a notification of exporting the key log information and return a message about whether the export is successful.

```text
admin:/>show file export_path file_type=key_log
Command executed successfully.
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                                                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| File Path     | File storage path.                                                                                                                               |
| File Name     | Disk log name. The value is in the format of "DiskID_SN.tgz". This parameter can be specified only when "file_type" is set to "running_disklog". |
| Controller ID | Controller ID. This parameter can be specified only when "file_type" is set to "running_disklog".                                                |
