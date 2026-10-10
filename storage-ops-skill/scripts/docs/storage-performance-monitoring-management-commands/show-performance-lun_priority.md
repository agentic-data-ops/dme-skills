# show performance lun_priority


##### Function

The **show performance lun_priority** command is used to query the real-time performance statistics of LUNs with a specified I/O priority.

##### Format

**show performance lun_priority** io_priority=? \[ controller_id=? \] \[ controller_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller_id=? | Owning controller ID of LUNs. | To obtain the value, run "show controller general". |
| io_priority=? | I/O priority of LUNs. | The value can be: <br>"Low": The I/O priority is low.<br>"Middle": The I/O priority is middle.<br>"High": The I/O priority is high. |
| controller_id_list=? | List of owning controller IDs of LUNs. | To obtain the value, run "show controller general". When multiple owning controllers of LUNs need to be added, separate these owning controller IDs of LUNs with commas (,). |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing one or multiple numbers (separated by commas (,)) and pressing "Enter" display the performance statistics for corresponding categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the performance statistics of LUNs with I/O priority "Low" on controller "0A".

```text
admin:/>show performance lun_priority io_priority=Low controller_id=0A
0.Bandwidth(MB/s) / Block Bandwidth(MB/s)
1.Throughput(IOPS)(IO/s)
2.Read Bandwidth(MB/s)
3.Read Throughput(IOPS)(IO/s)
4.Write Bandwidth(MB/s)
5.Write Throughput(IOPS)(IO/s)
6.Average I/O Latency(ms)
7.Average Read I/O Latency(ms)
8.Average Write I/O Latency(ms)
9.Average I/O Latency(us)
10.Average Read I/O Latency(us)
11.Average Write I/O Latency(us)
Input item(s) number separated by comma:0
Bandwidth(MB/s) / Block Bandwidth(MB/s) : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                               | Meaning                         |
|-----------------------------------------|---------------------------------|
| Bandwidth(MB/s) / Block Bandwidth(MB/s) | Bandwidth.                      |
| Throughput(IOPS)(IO/s)                  | I/O operations per second.      |
| Read Bandwidth(MB/s)                    | Read bandwidth.                 |
| Read Throughput(IOPS)(IO/s)             | Read operations per second.     |
| Write Bandwidth(MB/s)                   | Write bandwidth.                |
| Write Throughput(IOPS)(IO/s)            | Write operations per second.    |
| Average I/O Latency(ms)                 | Average I/O latency (ms).       |
| Average Read I/O Latency(ms)            | Average read I/O latency (ms).  |
| Average Write I/O Latency(ms)           | Average write I/O latency (ms). |
| Average I/O Latency(us)                 | Average I/O latency (us).       |
| Average Read I/O Latency(us)            | Average read I/O latency (us).  |
| Average Write I/O Latency(us)           | Average write I/O latency (us). |
