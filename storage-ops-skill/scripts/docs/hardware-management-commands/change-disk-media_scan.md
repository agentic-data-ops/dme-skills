# change disk media_scan


##### Function

The **change disk media_scan** command is used to modify settings of disk media scanning.

##### Format

**change disk media_scan** media_scan_enable=? \[ scan_max_bandwidth=? \| disk_io_usage_threshold=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| media_scan_enable=? | Whether to start or stop disk media scanning. | The value can be "on" or "off", where: <br>"on": starts disk media scanning.<br>"off": stops disk media scanning. |
| scan_max_bandwidth=? | Maximum bandwidth occupied by scanning. | The value ranges form 1 to 10, expressed in Mbps. |
| disk_io_usage_threshold=? | Disk I/O usage threshold. When the I/O usage on a disk is greater than the threshold, media scanning is stopped automatically. | The value ranges from 1 to 100, expressed in percentage (%). |

##### Usage Guidelines

None

##### Example

Modify settings of disk media scanning.

```text

admin:/>change disk media_scan media_scan_enable=on disk_io_usage_threshold=80 scan_max_bandwidth=2
Command executed successfully.

```

##### System Response

None
