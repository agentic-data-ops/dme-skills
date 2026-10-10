# show performance mode


##### Function

The **show performance mode** command is used to query the performance statistical modes of the current system.

##### Format

**show performance mode** \[**mode=***?*\]

##### Parameters

| Parameter | Description | Value                                                                                                                                                                                                          |
|-----------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mode      | Mode name.  | To obtain the value, run the "**show performance mode**" command without parameters. |

##### Usage Guidelines

-   Run the "**show performance mode**" command to query all the performance statistical modes.
-   Run the "**show performance mode** mode=?" command to query a specific performance statistical mode.

##### Example

Querying all the performance statistical modes.

```text
admin:/>show performance mode

Mode Name           Statistical Object
------------------  ------------------
controller_default  Controller
controller_san      Controller
controller_disk     Controller
```

Querying the performance statistical mode whose name is controller_default.

```text
admin:/>show performance mode mode=controller_default
Mode Name        : controller_default
Statistic Object : Controller
Statistical Item : CPU Usage(%)
Throughput(IOPS)(IO/s)
SCSI IOPS (IO/s)
ISCSI IOPS (IO/s)
Total Disk IOPS(IO/s)
Read Bandwidth(MB/s)
Write Bandwidth(MB/s)
% Hit
Cache Water(%)

```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                            |
|--------------------|------------------------------------|
| Mode Name          | Mode name.                         |
| Statistical Object | Performance statistical object.    |
| Statistical Item   | Performance statistical data type. |
