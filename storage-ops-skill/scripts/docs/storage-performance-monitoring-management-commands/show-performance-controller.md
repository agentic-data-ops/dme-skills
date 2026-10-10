# show performance controller


##### Function

The **show performance controller** command is used to query the performance statistics on a controller of the storage system. Run this command to analyze the performance statistics on a controller in real time.

##### Format

**show performance controller** controller_id=? \[ mode=? \] \[ times=? \]

**show performance controller** controller_id_list=? \[ mode=? \] \[ times=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller_id=? | ID of a controller. | To obtain the value, run "show controller general". |
| controller_id_list=? | ID list of controllers. | To obtain the value, run "show controller general".<br>Separate the controller IDs with commas (,). |
| mode=? | Mode name. | To obtain the value, run the "show performance mode" command. |
| times=? | Display times. | The value must be an integer from 1 to 65535. |

##### Usage Guidelines

-   You need to specify the controllers whose statistics you want to query.
-   If parameter times is not specified, the performance data will be refreshed in real time until you press q to exit. If parameter times is specified, the performance data is refreshed for the specified times and then the system automatically exits the performance data query.
-   If parameter mode is not specified, the system will prompt you to enter the serial numbers of performance data types and press Enter to view data of specified types. Use commas (,) to separate multiple serial numbers. Performance data of the specified types will be refreshed in real time.
-   If parameter mode is specified, performance data in the specified mode will be refreshed in real time(You can run the show performance mode mode=? Command to view performance data types.).

##### Example

Query the performance statistics on the read I/Os for controller "0A".

```text
admin:/>show performance controller controller_id=0A
0.Memory Usage(%)
1.Percentage of Cache Flushes to Write Requests(%)
2.Cache Flushing Bandwidth(MB/s)
3.Read Cache Hit Ratio(%)
4.Write Cache Hit Ratio(%)
5.Cache Read Usage(%)
6.Cache Write Usage(%)
7.% Hit
8.Cache Water(%)
9.Cache page utilization(%)
10.Cache chunk utilization(%)
11.Max. Bandwidth(MB/s)
12.Queue Length
13.Bandwidth(MB/s) / Block Bandwidth(MB/s)
14.Throughput(IOPS)(IO/s)
15.Read Bandwidth(MB/s)
16.Average Read I/O Size(KB)
17.Read Throughput(IOPS)(IO/s)
18.Write Bandwidth(MB/s)
19.Average Write I/O Size(KB)
20.Write Throughput(IOPS)(IO/s)
21.Service Time(Excluding Queue Time)(us)
22.Read I/O Granularity Distribution: [0K,4K)(%)
23.Read I/O Granularity Distribution: [4K,8K)(%)
24.Read I/O Granularity Distribution: [8K,16K)(%)
25.Read I/O Granularity Distribution: [16K,32K)(%)
26.Read I/O Granularity Distribution: [32K,64K)(%)
27.Read I/O Granularity Distribution: [64K,128K)(%)
28.Read I/O Granularity Distribution: >= 128K(%)
29.Write I/O Granularity Distribution: [0K,4K)(%)
30.Write I/O Granularity Distribution: [4K,8K)(%)
31.Write I/O Granularity Distribution: [8K,16K)(%)
32.Write I/O Granularity Distribution: [16K,32K)(%)
33.Write I/O Granularity Distribution: [32K,64K)(%)
34.Write I/O Granularity Distribution: [64K,128K)(%)
35.Write I/O Granularity Distribution: >= 128K(%)
36.Average IO Size(KB)
37.% Read
38.% Write
39.Max IOPS(IO/s)
40.Max. I/O Size(KB)
41.Max. Read I/O Size(KB)
42.Max. Write I/O Size(KB)
43.The cumulative count of I/Os
44.The cumulative count of data transferred in Kbytes
45.The cumulative elapsed I/O time(ms)
46.The cumulative count of all reads
47.The cumulative count of data read in Kbytes(1024bytes = 1KByte)
48.The cumulative count of all writes
49.The cumulative count of data written in Kbytes
50.Max. I/O Latency(us)
51.Average I/O Latency(us)
52.Average Read I/O Latency(us)
53.Average Write I/O Latency(us)
54.CPU Usage(%)
55.SCSI IOPS (IO/s)
56.ISCSI IOPS (IO/s)
57.NFS operation count per second
58.CIFS operation count per second
59.Total Disk IOPS(IO/s)
60.READ Disk IOPS(IO/s)
61.WRITE Disk IOPS(IO/s)
62.Disk Max. Usage(%)
63.NFS connection count
64.CIFS session count
65.Unmap Command Bandwidth (MB/s)
66.Unmap Command IOPS (IO/s)
67.Avg. Unmap Command Size (KB)
68.Avg. Unmap Command Response Time (us)
69.WRITE SAME Command Bandwidth (MB/s)
70.WRITE SAME Command IOPS (IO/s)
71.Avg. WRITE SAME Command Size (KB)
72.Avg. WRITE SAME Command Response Time (us)
73.Full Copy Read Request Bandwidth (MB/s)
74.Full Copy Read Request IOPS (IO/s)
75.Avg. Full Copy Read Request Size (KB)
76.Avg. Full Copy Read Request Response Time (us)
77.Full Copy Write Request Bandwidth (MB/s)
78.Full Copy Write Request IOPS (IO/s)
79.Avg. Full Copy Write Request Size (KB)
80.Avg. Full Copy Write Request Response Time (us)
81.ODX Read Request Bandwidth (MB/s)
82.ODX Read Request IOPS (IO/s)
83.Avg. ODX Read Request Size (KB)
84.Avg. ODX Read Request Response Time (us)
85.ODX Write Request Bandwidth (MB/s)
86.ODX Write Request IOPS (IO/s)
87.Avg. ODX Write Request Size (KB)
88.Avg. ODX Write Request Response Time (us)
89.ODX Write Zero Request Bandwidth (MB/s)
90.ODX Write Zero Request IOPS (IO/s)
91.Avg. ODX Write Zero Request Size (KB)
92.Avg. ODX Write Zero Request Response Time (us)
93.AI Cache Hit Ratio(%)
94.Total Block IOPS (IO/s)
95.Total Block Bandwidth (MB/s)
Input item(s) number separated by comma:4
Write Cache Hit Ratio(%) : 0
```

Query performance statistics of controller 0B in controller_san mode once.

```text
admin:/>show performance controller controller_id=0B mode=controller_san times=1
CPU Usage(%)           : 5
Throughput(IOPS)(IO/s) : 0
SCSI IOPS (IO/s)       : 0
ISCSI IOPS (IO/s)      : 0
Total Disk IOPS(IO/s)  : 0
```

##### System Response

None
