# show disk health


##### Function

**show disk health** command is used to query the health status of a disk.

##### Format

**show disk health** \[ disk_id=? \]

##### Parameters

| Parameter | Description | Value                                         |
|-----------|-------------|-----------------------------------------------|
| disk_id=? | Disk ID.    | To obtain the value, run "show disk general". |

##### Usage Guidelines

None

##### Example

Query the health status of disk "DAE008.10". The command output varies depending on a specific product.

```text
admin:/>show disk health disk_id=DAE008.10

Disk ID : 298
Health Mark : 255
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                   |
|-------------|---------------------------|
| Disk ID     | Physical ID of the disk.  |
| Health Mark | Health score of the disk. |
