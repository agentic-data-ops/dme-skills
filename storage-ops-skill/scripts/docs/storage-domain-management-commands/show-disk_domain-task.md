# show disk_domain task


##### Function

The **show disk_domain task** command is used to query the status of a reconstruction or pre-copy task in a disk domain.

##### Format

**show disk_domain task** disk_domain_id=?

##### Parameters

| Parameter        | Description     | Value                                                |
|------------------|-----------------|------------------------------------------------------|
| disk_domain_id=? | Disk domain ID. | To obtain the value, run "show disk_domain general". |

##### Usage Guidelines

If no status information is displayed in the command output, no reconstruction or pre-copy tasks are proceeding in the disk domain.

##### Example

Query the status of a reconstruction or pre-copy task in disk domain "0".

```text
admin:/>show disk_domain task disk_domain_id=0
Disk Domain ID       : 0
Type                 : Reconstruct
Disk Enclosure       : DAE101
Disk Slot            : 23
Data Size            : 17.625GB
Data Finished Size   : 1.375GB
Remain Time          : 0Day(s) 1Hour(s) 26Minute(s) 4Second(s)
Progress             : 7%
```

Query the status of a reconstruction or pre-copy task in disk domain "0".

```text
admin:/>show disk_domain task disk_domain_id=0
Disk Domain ID : 0
Type : Reconstruct
Disk Enclosure : DAE101
Disk Slot : 23
Data Size : 17.625GB
Data Finished Size : 1.375GB
Remain Time : 0Day(s) 1Hour(s) 26Minute(s) 4Second(s)
Progress : 7%
-----------------------------------------------------------------
Disk Domain ID : 0
Type : Precopy
Disk Enclosure : DAE000
Disk Slot : 13
Data Size : 19.125GB
Data Finished Size : 2.250GB
Remain Time : 0Day(s) 0Hour(s) 2Minute(s) 58Second(s)
Progress : 11%
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                 |
|--------------------|-------------------------|
| Disk Domain ID     | Disk domain ID.         |
| Type               | Task type.              |
| Disk Enclosure     | Disk enclosure.         |
| Disk Slot          | Disk slot.              |
| Data Size          | Data size.              |
| Data Finished Size | Size of collected data. |
| Remain Time        | Remaining time.         |
| Progress           | Progress.               |
