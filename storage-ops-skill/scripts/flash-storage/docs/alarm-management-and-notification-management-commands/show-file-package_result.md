# show file package_result


##### Function

The **show file package_result** command is used to check the file exporting status.

##### Format

**show file package_result** file_type=? \[ disk_id=? \] \[ controller_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_type=? | Type of a file that you want to export. | The value can be log, all_log, key_log, smart, workload, call_home, diagnostic_file, isolated_disklog, running_disklog, enclosure_log, or ftds_statdata, where: <br>log: recent logs and disk enclosure logs.<br>all_log: all system logs and disk enclosure logs.<br>smart: disk SMART information.<br>workload: service load.<br>call_home: Call Home data.<br>diagnostic_file: diagnostic file.<br>isolated_disklog: isolated disk log information.<br>running_disklog: running disk log information.<br>enclosure_log: disk enclosure log information.<br>ftds_statdata: FTDS statistics.<br>key_log: key logs. |
| disk_id=? | ID of a disk. | To obtain the value, run "show disk general" without parameters. This parameter can be specified only when "file_type" is set to "running_disklog". |
| controller_id=? | Controller ID. | This parameter is visible to users only when "file_type" is set to "running_disklog". When disks are on controllers, the format of a controller ID is XA, XB, XC, or XD, where X is an integer starting from 0, for example, "0A" or "1C". When disks are on smart disk enclosures, the format of a controller ID is DAExxx.A or DAExxx.B, where xxx is a hexadecimal integer ranging from 0 to F, for example, "DAE030.A" or "DAE030.B". |

##### Usage Guidelines

None

##### Example

Check the log exporting status where the file type is "log".

```text
admin:/>show file package_result file_type=log
Total Result  Controller ID  Single Result
------------  -------------  -------------
Successful    0A             Successful
--            0B             Successful
```

Check the log exporting status where the file type is "ftds_statdata".

```text
admin:/>show file package_result file_type=ftds_statdata
Total Result  Controller ID  Single Result
------------  -------------  -------------
Successful    0A             Successful
--            0B             Successful
```

Check the export status of key log files. The file type is "key_log".

```text
admin:/>show file package_result file_type=key_log
Total Result  Controller ID  Single Result
------------  -------------  -------------
Successful    0A             Successful
--            0B             Successful
```

Check the export status of Call Home data. The file type is "call_home".

```text
admin:/>show file package_result file_type=call_home
Total Result  Controller ID  Single Result
------------  -------------  -------------
Successful    0A             Successful
--            0B             Successful
```

Check the export status of the diagnosis file. The file type is "diagnostic_file".

```text
admin:/>show file package_result file_type=diagnostic_file
Total Result  Controller ID  Single Result
------------  -------------  -------------
Successful      --       --
```

Check the export status of the running disk log file of the smart disk enclosure. The file type is "running_disklog".

```text
admin:/>show file package_result file_type=running_disklog disk_id=DAE030.0 controller_id=DAE030.A

Total Result  Controller ID  Single Result
------------  -------------  -------------
Successful    --             --
```

Check the export status of the log file of the isolated disk. The file type is "isolated_disklog".

```text
admin:/>show file package_result file_type=isolated_disklog
Total Result  Controller ID  Single Result
------------  -------------  -------------
Successful     0A       Successful
--            0B       Successful
--            1A       Successful
--            1B       Successful
```

Check the export status of disk enclosure logs. The file type is "enclosure_log".

```text
admin:/>show file package_result file_type=enclosure_log
Total Result  Controller ID        Single Result
------------  -------------        -------------
Successful    0A                    Successful
--           0B                    Successful
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                  |
|---------------|----------------------------------------------------------|
| Controller ID | Controller ID.                                           |
| Total Result  | Overall result of exporting logs.                        |
| Single Result | Overall result of exporting logs by a single controller. |
