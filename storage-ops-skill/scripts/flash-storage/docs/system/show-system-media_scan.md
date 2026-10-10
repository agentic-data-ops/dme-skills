# show system media_scan


##### Function

The **show system media_scan** command is used to query the disk media scanning information, including the running status and execution period.

##### Format

**show system media_scan**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the disk media scanning information. The command output varies depending on a specific product.

```text
admin:/>show system media_scan

Execute Status                  : Start
IO Type                         : Verify
Period(Days)                    : 30
Single Disk Max Bandwidth(Mbps) : 4
Disk Usage Threshold(%)         : 40
```

##### System Response

The following table describes the parameter meanings.

| Parameter                       | Meaning               |
|---------------------------------|-----------------------|
| Execute Status                  | Execute status.       |
| IO Type                         | I/O type.             |
| Period(Days)                    | Execution period.     |
| Single Disk Max Bandwidth(Mbps) | Bandwidth.            |
| Disk Usage Threshold(%)         | Disk usage threshold. |
