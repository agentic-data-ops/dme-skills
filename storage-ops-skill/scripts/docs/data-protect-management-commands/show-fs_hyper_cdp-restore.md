# show fs_hyper_cdp restore


##### Function

The **show fs_hyper_cdp restore** command is used to query information about a HyperCDP object that is being rolled back to.

##### Format

**show fs_hyper_cdp restore** \[ file_system_id_list=? \| file_system_name_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_system_id_list | File system ID. | To obtain the value, run "show file_system general". You can specify multiple file system names separated by commas (,). |
| file_system_name_list | File system name. | To obtain the value, run "show file_system general". You can specify multiple file system IDs separated by commas (,). |

##### Usage Guidelines

None

##### Example

Query rollback information about the file system whose ID is "1".

```text
admin:/>show fs_hyper_cdp restore file_system_id_list=1
File System ID         : 1
File System Name       : fs1
Rollback Snapshot ID   : --
Rollback Snapshot Name : --
Rollback Starttime     : --
Rollback Endtime       : --
Rollback Progress      : --
Rollback Status        : Idle
Rollback Speed         : Middle
admin:/>
```

Query rollback information about the file system whose name is "fs1".

```text
admin:/>show fs_hyper_cdp restore file_system_name_list=fs1
File System ID         : 1
File System Name       : fs1
Rollback Snapshot ID   : 1@snap1
Rollback Snapshot Name : snap1
Rollback Starttime     : 2020-03-28/15:34:23 UTC+08:00
Rollback Endtime       : --
Rollback Progress      : 50
Rollback Status        : Rollbacking
Rollback Speed         : High
admin:/>
```

##### System Response

The following table describes the parameter meanings.

| Parameter              | Meaning                      |
|------------------------|------------------------------|
| File System ID         | File system ID.              |
| File System Name       | File system name.            |
| Rollback Snapshot ID   | Target HyperCDP object ID.   |
| Rollback Snapshot Name | Target HyperCDP object name. |
| Rollback Starttime     | Rollback start time.         |
| Rollback Endtime       | Rollback end time.           |
| Rollback Progress      | Rollback progress.           |
| Rollback Status        | Rollback status.             |
| Rollback Speed         | Rollback speed.              |
