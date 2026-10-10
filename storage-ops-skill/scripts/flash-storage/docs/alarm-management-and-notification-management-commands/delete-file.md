# delete file


##### Function

The **delete file** command is used to **delete file**s of a specific type from the system memory or system disk, where the files to be deleted have been exported before.

##### Format

**delete file** filetype=? \[ interlog_name=? \] \[ controller_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| filetype=? | File type. | The value can be event, log, running_data, configuration_data, all_log, key_log, smart, workload, call_home, diagnostic_file, isolated_disklog, running_disklog, enclosure_log, or ftds_statdata, where: <br>"event": event information file.<br>"log": recent logs and disk enclosure logs.<br>"running_data": system running data file.<br>"configuration_data": system configuration file.<br>"all_log": all system logs and disk enclosure logs.<br>"smart": SMART information of a disk.<br>"workload": service load.<br>"call_home": Call Home data.<br>"diagnostic_file": diagnostic file.<br>"isolated_disklog": isolated disk log information.<br>"running_disklog": running disk log information.<br>"enclosure_log": disk enclosure log information.<br>"ftds_statdata": FTDS statistics.<br>"key_log": key logs. |
| controller_id=? | Controller ID. | Controller IDs are separated by commas (,). The value format is "XA", "XB", "XC", or "XD", where "X" is an integer starting from 0, for example, "0A" and "1C". Note that this parameter is visible to users only when filetype is set to "log", "all_log", "key_log", "call_home", "workload", "smart", "isolated_disklog", "running_disklog", "ftds_statdata", or "enclosure_log". If the type of the exported file is "running_disklog" and the entered "controller_id" is the ID of a smart disk enclosure, the running logs of the smart disk enclosure are deleted. If the entered "controller_id" is the controller ID, the running disk logs on the controller are deleted. |
| interlog_name=? | Name of an exported running disk log. | This parameter can be specified only when "filetype" is set to "running_disklog". |

##### Usage Guidelines

None

##### Example

Delete the exported event files from the system memory.

```text
admin:/>delete file filetype=event
Command executed successfully.
```

Delete the exported diagnostic files.

```text
admin:/>delete file filetype=diagnostic_file
Command executed successfully.
```

Delete exported running disklog files.

```text
admin:/>delete file filetype=running_disklog interlog_name=CTE1.1_210235G7JK10D7000085.tgz controller_id=1A
Command executed successfully.
```

Delete the exported running disk logs of a smart disk enclosure.

```text
admin:/>delete file filetype=running_disklog interlog_name=DAE068.0_032WEPFSJA000178.tgz controller_id=DAE068.A
Command executed successfully.
```

Delete the exported disk enclosure logs.

```text
admin:/>delete file filetype=enclosure_log controller_id=0A
Command executed successfully.
```

Delete the exported key logs.

```text
admin:/>delete file filetype=key_log controller_id=0A
Command executed successfully.
```

Delete the exported FTDS statistics files from the system memory.

```text
admin:/>delete file filetype=ftds_statdata
Command executed successfully.
```

##### System Response

None
