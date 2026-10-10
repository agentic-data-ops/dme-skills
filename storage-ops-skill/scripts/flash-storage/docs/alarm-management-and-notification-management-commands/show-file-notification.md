# show file notification


##### Function

The **show file notification** command is used to check the path of the exported temporary files.

##### Format

**show file notification** file_type=? \[ interlog_name=? \] controller_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_type=? | File type. | The value can be log, all_log, key_log, smart, workload, call_home, diagnostic_file, isolated_disklog, running_disklog, enclosure_log, or ftds_statdata, where: <br>log: recent logs and disk enclosure logs.<br>all_log: all system logs and disk enclosure logs.<br>smart: disk SMART information.<br>workload: service load.<br>call_home: Call Home data.<br>diagnostic_file: diagnostic file.<br>isolated_disklog: isolated disk log information.<br>running_disklog: running disk log information.<br>enclosure_log: disk enclosure log information.<br>ftds_statdata: FTDS statistics.<br>key_log: key logs. |
| interlog_name=? | Name of an exported running disk log. | The value is in the format of "DiskID_SN.tgz". This parameter can be specified only when "file_type" is set to "running_disklog". |
| controller_id=? | Controller ID. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0, for example, 0A or 1C. Note that when the type of the exported file is running_disklog, if the disk is on a controller, the controller ID is in the format of XA, XB, XC, or XD. X is an integer starting from 0, for example, 0A or 1C. If a disk is installed on a smart disk enclosure, the controller ID is in the format of DAExxx.A,DAExxx.B, where x is a hexadecimal integer ranging from 0 to F, for example, DAE030.A or DAE030.B. |

##### Usage Guidelines

None

##### Example

Check the path of the exported logs in the storage system where the file type is "log" and controller ID is "0A".

```text
admin:/>show file notification file_type=log controller_id=0A
File Path : /OSM/coffer_data/omm/export_import/log_controller_0A_MAIN.tgz
```

Check the path for storing the exported key log files on the array. The file type is "key_log" and the controller ID is "0A".

```text
admin:/>show file notification file_type=key_log controller_id=0A
File Path : /OSM/coffer_data/omm/export_import/private_log_0A.tgz
```

Check the storage path of the exported Call Home data on the array. The file type is "call_home" and the controller ID is "0A".

```text
admin:/>show file notification file_type=call_home controller_id=0A
File Path : /OSM/coffer_data/omm/export_import/chs/export/collector_chs_file_0A.tgz
```

Check the storage path of the exported diagnosis file on the storage array. The file type is "diagnostic_file".

```text
admin:/>show file notification file_type=diagnostic_file
File Path : /OSM/coffer_data/omm/export_import/DiagnoseInfo.tgz
```

Check the storage path of the exported log file of the isolated disk on the storage array. The file type is "isolated_disklog" and the controller ID is "0A".

```text
admin:/>show file notification file_type=isolated_disklog controller_id=0A
File Path : /OSM/coffer_data/omm/export_import/isolated_disklog_0A.tgz
```

Check the storage path of the exported log file of the running disk on the array. The file type is "running_disklog" and the controller ID is "0A".

```text
admin:/>show file notification file_type=running_disklog interlog_name=CTE1.0_210235G7JK10D7000008.tgz controller_id=0A
File Path : /OSM/coffer_data/omm/export_import/CTE1.0_210235G7JK10D7000008.tgz
```

Check the storage path of the exported running log file of the smart disk enclosure on the storage array. The file type is "running_disklog" and the controller ID is "DAE030.B".

```text
admin:/>show file notification file_type=running_disklog interlog_name=DAE030.0_032WEM10J8000766.tgz controller_id=DAE030.B
File Path : /OSM/coffer_data/omm/export_import/DAE030.0_032WEM10J8000766.tgz
```

Check the storage path of the exported disk enclosure log file on the storage array. The file type is "enclosure_log" and the controller ID is "0A".

```text
admin:/>show file notification file_type=enclosure_log controller_id=0A
File Path : /OSM/coffer_data/omm/export_import/enclosure_log_DAE[0A0.A].tgz
```

Check the storage path of the exported disk SMART information log file on the storage array. The file type is "smart" and the controller ID is "0A".

```text
admin:/>show file notification file_type=smart controller_id=0A
File Path : /OSM/coffer_data/omm/export_import/diskinfo_0A.tgz
```

Check the storage path of the exported FTDS statistics log file on the storage array. The file type is "ftds_statdata" and the controller ID is "0A".

```text
admin:/>show file notification file_type=ftds_statdata controller_id=0A
File Path : /OSM/coffer_data/omm/export_import/ftds_statdata_0A.tgz
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning            |
|-----------|--------------------|
| File Path | File storage path. |
