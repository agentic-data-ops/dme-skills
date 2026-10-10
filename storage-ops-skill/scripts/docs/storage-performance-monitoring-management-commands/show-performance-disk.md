# show performance disk


##### Function

The **show performance disk** command is used to query the performance statistics of a disk. Running this command analyzes the performance statistics of a disk in real time.

##### Format

**show performance disk** \[ disk_id=? \] \[ disk_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disk_id=? | ID of a disk on which you want to query performance statistics. | To obtain the value, run "show disk general". |
| disk_id_list=? | List of disk IDs on which you want to query performance statistics. | To obtain the value, run "show disk general".<br>Separate multiple IDs with commas (,), or a hyphen (-) to represent an ID range.<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas (,)) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the I/O throughput for the disk in slot "0" of enclosure "CTE0".

```text
admin:/>show performance disk disk_id=CTE0.0
0.Max. Bandwidth(MB/s)
1.Usage Ratio(%)
2.Queue Length
3.Bandwidth(MB/s) / Block Bandwidth(MB/s)
4.Throughput(IOPS)(IO/s)
5.Read Bandwidth(MB/s)
6.Average Read I/O Size(KB)
7.Read Throughput(IOPS)(IO/s)
8.Write Bandwidth(MB/s)
9.Average Write I/O Size(KB)
10.Write Throughput(IOPS)(IO/s)
11.Read I/O Granularity Distribution: [4K,8K)(%)
12.Read I/O Granularity Distribution: [8K,16K)(%)
13.Read I/O Granularity Distribution: [16K,32K)(%)
14.Read I/O Granularity Distribution: [32K,64K)(%)
15.Read I/O Granularity Distribution: [64K,128K)(%)
16.Write I/O Granularity Distribution: [4K,8K)(%)
17.Write I/O Granularity Distribution: [8K,16K)(%)
18.Write I/O Granularity Distribution: [16K,32K)(%)
19.Write I/O Granularity Distribution: [32K,64K)(%)
20.Write I/O Granularity Distribution: [64K,128K)(%)
21.Average IO Size(KB)
22.Complete SCSI commands per second
23.Verify commands per second
24.% Read
25.% Write
26.Max IOPS(IO/s)
27.Service Time(Excluding Queue Time)(us)
28.Average I/O Latency(us)
29.Max. I/O Latency(us)
30.Average Read I/O Latency(us)
31.Average Write I/O Latency(us)
32.The cumulative count of I/Os
33.The cumulative count of data transferred in Kbytes
34.The cumulative elapsed I/O time(ms)
35.The cumulative count of all reads
36.The cumulative count of data read in Kbytes(1024bytes = 1KByte)
37.The cumulative count of all writes
38.The cumulative count of data written in Kbytes
39.Read I/O Granularity Distribution: [0K,4K)(%)
40.Read I/O Granularity Distribution: >= 128K(%)
41.Write I/O Granularity Distribution: [0K,4K)(%)
42.Write I/O Granularity Distribution: >= 128K(%)
Input item(s) number separated by comma:5
Read Bandwidth (MB/s) : 11
```

##### System Response

None
