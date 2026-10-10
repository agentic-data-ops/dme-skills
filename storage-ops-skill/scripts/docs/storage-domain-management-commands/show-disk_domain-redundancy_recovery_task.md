# show disk_domain redundancy_recovery_task


##### Function

The **show disk_domain redundancy_recovery_task** command is used to query status of a redundancy recovery task in a disk domain.

##### Format

**show disk_domain redundancy_recovery_task** { disk_domain_id=? \| name=? }

##### Parameters

| Parameter        | Description            | Value                                                |
|------------------|------------------------|------------------------------------------------------|
| disk_domain_id=? | Disk domain ID.        | To obtain the value, run "show disk_domain general". |
| name=?           | Name of a disk domain. | To obtain the value, run "show disk_domain general". |

##### Usage Guidelines

None

##### Example

Query status of a redundancy recovery task in the disk domain whose ID is "0".

```text
admin:/>show disk_domain redundancy_recovery_task disk_domain_id=0
ID                   : 0
Name                 : domain0
Data Size            : 17.625GB
Data Finished Size   : 1.375GB
Remain Time          : 0Day(s) 1Hour(s) 26Minute(s) 4Second(s)
Progress             : 7%
Rate                 : 52 MB/s
```

Query status of a redundancy recovery task in the disk domain whose name is "domain0".

```text
admin:/>show disk_domain redundancy_recovery_task name=domain0
ID                   : 0
Name                 : domain0
Data Size            : 17.625GB
Data Finished Size   : 1.375GB
Remain Time          : 0Day(s) 1Hour(s) 26Minute(s) 4Second(s)
Progress             : 7%
Rate                 : 52 MB/s
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                 |
|--------------------|-------------------------|
| ID                 | Disk domain ID.         |
| name               | Name of a disk domain.  |
| Data Size          | Data size.              |
| Data Finished Size | Size of recovered data. |
| Remain Time        | Remaining time.         |
| Progress           | Progress.               |
| Rate               | Rate.                   |
