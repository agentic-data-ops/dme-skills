# show fs_hyper_cdp general


##### Function

The **show fs_hyper_cdp general** command is used to query a HyperCDP object in a file system, including the name, HyperCDP object ID, file system ID, file system name, health status of the HyperCDP object, HyperCDP object creation time, and capacity consumed by the HyperCDP object.

##### Format

**show fs_hyper_cdp general** cdp_name_list=? { file_system_name=? \| file_system_id=? } \[ vstore_id=? \]

**show fs_hyper_cdp general** { file_system_name=? \| file_system_id=? } \[ vstore_id=? \]

**show fs_hyper_cdp general** cdp_id_list=?

##### Parameters

| Parameter          | Description                                                                                               | Value                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| cdp_name_list=?    | Name of a specified HyperCDP object to be queried. Multiple HyperCDP objects are separated by commas (,). | The value is the name of an existing HyperCDP object. |
| cdp_id_list=?      | ID of a specified HyperCDP object to be queried. Multiple HyperCDP objects are separated by commas (,).   | The value is the ID of an existing HyperCDP object.   |
| file_system_id=?   | ID of the file system to which the HyperCDP object belongs.                                               | To obtain the value, run "show file_system general".  |
| file_system_name=? | Name of the file system to which the HyperCDP object belongs.                                             | To obtain the value, run "show file_system general".  |
| vstore_id=?        | vStore ID.                                                                                                | vStore ID. The default value is "0".                  |

##### Usage Guidelines

-   Before running this command, check whether the name of the HyperCDP object is correct.
-   Before running this command, check whether the ID of the file system to which the HyperCDP object belongs is correct.

##### Example

Query the HyperCDP object named "fssnap" of the file system whose ID is "1".

```text
admin:/>show fs_hyper_cdp general cdp_name_list=fssnap file_system_id=1
Snapshot ID      : 1@fssnap
Snapshot Name    : fssnap
File System ID   : 1
File System Name : fs1
Description      : fssnap
Health Status    : --
Time Stamp       : 2020-02-17/09:44:05 UTC+08:00
```

Query all HyperCDP objects of the file system whose ID is "1".

```text
admin:/>show fs_hyper_cdp general file_system_id=1
Snapshot ID  Snapshot Name  File System ID  File System Name  Description  Health Status  Time Stamp
-----------  -------------  --------------  ----------------  -----------  -------------  -----------------------------
1@s1         s1             1               fs1               s1            --             2020-03-19/20:11:49 UTC+08:00
1@s2         s2             1               fs1               s2            --             2020-03-19/20:12:14 UTC+08:00
1@s3         s3             1               fs1               s3            --             2020-03-19/20:13:24 UTC+08:00
```

Query the HyperCDP object whose ID is "1@fssnap".

```text
admin:/>show fs_hyper_cdp general cdp_id_list=1@fssnap
Snapshot ID      : 1@fssnap
Snapshot Name    : fssnap
File System ID   : 1
File System Name : fs1
Description      : fssnap
Health Status    : --
Time Stamp       : 2020-02-17/09:44:05 UTC+08:00
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                                                       |
|------------------|---------------------------------------------------------------|
| Snapshot ID      | ID of the HyperCDP object.                                    |
| Snapshot Name    | Name of the HyperCDP object.                                  |
| File System ID   | ID of the file system to which the HyperCDP object belongs.   |
| File System Name | Name of the file system to which the HyperCDP object belongs. |
| Health Status    | Health status of the HyperCDP object.                         |
| Time Stamp       | Time when the HyperCDP object was created.                    |
| Description      | Description of the HyperCDP object.                           |
