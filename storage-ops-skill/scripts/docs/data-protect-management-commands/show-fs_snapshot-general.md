# show fs_snapshot general


##### Function

The **show fs_snapshot general** command is used to query a snapshot in a file system, including the name, snapshot ID, file system ID, file system name, health status of the snapshot, snapshot creation time, and capacity consumed by the snapshot.

##### Format

**show fs_snapshot general** snapshot_name=? { file_system_name=? \| file_system_id=? } \[ vstore_id=? \]

**show fs_snapshot general** { file_system_name=? \| file_system_id=? } \[ vstore_id=? \]

**show fs_snapshot general** snapshot_id=?

##### Parameters

| Parameter          | Description                                            | Value                                                |
|--------------------|--------------------------------------------------------|------------------------------------------------------|
| snapshot_name=?    | Name of a specified snapshot to be queried.            | The value is the name of an existing snapshot.       |
| snapshot_id=?      | ID of a specified snapshot to be queried.              | The value is the ID of an existing snapshot.         |
| file_system_id=?   | ID of the file system to which the snapshot belongs.   | To obtain the value, run "show file_system general". |
| file_system_name=? | Name of the file system to which the snapshot belongs. | To obtain the value, run "show file_system general". |
| vstore_id=?        | vStore ID.                                             | vStore ID. The default value is "0".                 |

##### Usage Guidelines

-   Before running this command, check whether the name of the snapshot is correct.
-   Before running this command, check whether the ID of the file system to which the snapshot belongs is correct.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the snapshot named "fssnap" of the file system whose ID is "1".

```text
admin:/>show fs_snapshot general snapshot_name=fssnap file_system_id=1
Snapshot ID      : 1@fssnap
Snapshot Name    : fssnap
File System ID   : 1
File System Name : fs1
Description      : fssnap
Health Status    : --
Time Stamp       : 2020-02-17/09:44:05 UTC+08:00
```

Query all snapshots of the file system whose ID is "1".

```text
admin:/>show fs_snapshot general file_system_id=1
Snapshot ID  Snapshot Name  File System ID  File System Name  Description  Health Status  Time Stamp
-----------  -------------  --------------  ----------------  -----------  -------------  -----------------------------
1@s1         s1             1               fs1               s1            --             2020-03-19/20:11:49 UTC+08:00
1@s2         s2             1               fs1               s2            --             2020-03-19/20:12:14 UTC+08:00
1@s3         s3             1               fs1               s3            --             2020-03-19/20:13:24 UTC+08:00
```

Query the snapshot whose ID is "1@fssnap".

```text
admin:/>show fs_snapshot general snapshot_id=1@fssnap
Snapshot ID      : 1@fssnap
Snapshot Name    : fssnap
File System ID   : 1
File System Name : fs1
Description      : fssnap
Health Status    : --
Time Stamp       : 2020-02-17/09:44:05 UTC+08:00
Type             : User Snapshot
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                                                |
|------------------|--------------------------------------------------------|
| Snapshot ID      | ID of the snapshot.                                    |
| Snapshot Name    | Name of the snapshot.                                  |
| File System ID   | ID of the file system to which the snapshot belongs.   |
| File System Name | Name of the file system to which the snapshot belongs. |
| Health Status    | Health status of the snapshot.                         |
| Time Stamp       | Time when the snapshot was created.                    |
| Description      | Description of the snapshot.                           |
| Type             | Type of a snapshot.                                    |
