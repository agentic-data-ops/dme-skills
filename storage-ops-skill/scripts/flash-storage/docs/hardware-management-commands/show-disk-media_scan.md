# show disk media_scan


##### Function

The **show disk media_scan** command is used to query the disk media scanning information, including the bandwidth and disk usage.

##### Format

**show disk media_scan**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the disk media scanning information, including the bandwidth and disk usage.

```text

admin:/>show disk media_scan
media_scan_enable       : on
scan_max_bandwidth      : 2
disk_io_usage_threshold : 80
```

##### System Response

The following table describes the parameter meanings.

| Parameter               | Meaning                   |
|-------------------------|---------------------------|
| media_scan_enable       | Scaning switch.           |
| scan_max_bandwidth      | Bandwidth.                |
| disk_io_usage_threshold | Disk I/O usage threshold. |
