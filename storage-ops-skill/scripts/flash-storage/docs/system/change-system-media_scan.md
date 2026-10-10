# change system media_scan


##### Function

The **change system media_scan** command is used to modify the settings of disk media scanning.

##### Format

**change system media_scan** { status=? \| scan_io_type=? \| scan_period=? \| scan_max_bandwidth=? \| disk_usage_threshold=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| status=? | Whether to start or stop disk media scanning. | The value can be "start" or "stop", where: <br>"start": Disk media scanning will be started.<br>"stop": Disk media scanning will be stopped. |
| scan_io_type=? | I/O type of media scanning. | The value is "read" or "verify". When the value is "verify", which means read and verification are required. |
| scan_period=? | Recovery scanning period. | The value ranges from 1 to 60, expressed in days. |
| scan_max_bandwidth=? | The maximum bandwidth occupied by scanning. | The value ranges form 1 to 10, expressed in Mbps. |
| disk_usage_threshold=? | Disk usage threshold, indicating the percentage of the occupied disk space in the total disk space. When the percentage of the occupied disk space is greater than the threshold, media scanning is stopped automatically. | The value ranges from 1 to 100, expressed in percentage (%). |

##### Usage Guidelines

None

##### Example

To enable disk media scanning, where the I/O type is "verify", the recovery scanning period is seven days, the maximum bandwidth occupied by scanning is "1Mbps", and the disk usage threshold is "50%", run the following command:

```text
admin:/>change system media_scan status=start scan_io_type=verify scan_period=7 scan_max_bandwidth=1 disk_usage_threshold=50
WARNING: You are going to adjust background scanning parameters. The background scanning parameters include the allowable upper limit for scanning the disk utilization, scanning type, maximum scanning bandwidth, scanning period, and scanning function switch.
Suggestion: Perform this operation based on system reliability need. This operation may affect system performance to some extent.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
