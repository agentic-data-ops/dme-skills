# show fs_snapshot restore


##### Function

The **show fs_snapshot restore** command is used to query information about a snapshot that is being rolled back to.

##### Format

**show fs_snapshot restore** \[ file_system_id=? \| file_system_name=? \]

**show fs_snapshot restore** \[ file_system_id=? \| file_system_name=? \] \[ vstore_id=? \]

##### Parameters

| Parameter          | Description       | Value                                                |
|--------------------|-------------------|------------------------------------------------------|
| file_system_id=?   | File system ID.   | To obtain the value, run "show file_system general". |
| file_system_name=? | File system name. | To obtain the value, run "show file_system general". |
| vstore_id=?        | vStore ID.        | vStore ID. The default value is "0".                 |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query rollback information about the file system whose ID is "1".

```text
admin:/>show fs_snapshot restore file_system_id=1
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
admin:/>show fs_snapshot restore file_system_name=fs1
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

| Parameter              | Meaning               |
|------------------------|-----------------------|
| File System ID         | File system ID.       |
| File System Name       | File system name.     |
| Rollback Snapshot ID   | Target snapshot ID.   |
| Rollback Snapshot Name | Target snapshot name. |
| Rollback Starttime     | Rollback start time.  |
| Rollback Endtime       | Rollback end time.    |
| Rollback Progress      | Rollback progress.    |
| Rollback Status        | Rollback status.      |
| Rollback Speed         | Rollback speed.       |
