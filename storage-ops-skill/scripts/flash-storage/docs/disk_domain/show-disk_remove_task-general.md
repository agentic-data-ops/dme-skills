# show disk_remove_task general


##### Function

The **show disk_remove_task general** command is used to query the status of a capacity reduction task of a disk domain.

##### Format

**show disk_remove_task general** { disk_domain_id=? \| disk_domain_name=? }

##### Parameters

| Parameter          | Description            | Value                                                                 |
|--------------------|------------------------|-----------------------------------------------------------------------|
| disk_domain_id=?   | Disk domain ID.        | You can run the show disk_domain general command to obtain the value. |
| disk_domain_name=? | Name of a disk domain. | You can run the show disk_domain general command to obtain the value. |

##### Usage Guidelines

None

##### Example

Query the status of the capacity reduction task of the disk domain whose ID is "0".

```text
admin:/>show disk_remove_task general disk_domain_id=0

Domain ID            : 0
Domain Name          : domain0
Task State           : Running
Progress             : 7%
Remain Time          : 0Day(s) 1Hour(s) 26Minute(s) 4Second(s)
Rate                 : 52 MB/s
Disk List            : DAE058.0, DAE058.1, DAE058.2
Removed Disk List    : DAE058.0
Removing Disk List   : DAE058.1
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                               |
|--------------------|---------------------------------------|
| Domain ID          | Disk domain ID.                       |
| Domain Name        | Name of a disk domain.                |
| Task Status        | Task status.                          |
| Progress           | Progress.                             |
| Remain Time        | Remaining time.                       |
| Rate               | Rate.                                 |
| Disk List          | Disk list.                            |
| Removed Disk List  | List of removed disks.                |
| Removing Disk List | List of disks that are being removed. |
