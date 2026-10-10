# show performance lun


##### Function

The **show performance lun** command is used to query performance statistics on a logical unit number (LUN). Run this command to analyze the performance statistics on a LUN in real time.

##### Format

**show performance lun** lun_id=?

**show performance lun** lun_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_id=? | ID of a LUN on which you want to query performance statistics. | To obtain the value, run "show lun general". |
| lun_id_list=? | ID list of LUNs on which you want to query performance statistics. | To obtain the value, run "show lun general".<br>Separate IDs of multiple LUNs with commas (,), or ID ranges separated by hyphens (-).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas (,)) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query performance statistics on read I/Os for the LUN whose ID is "1".

```text
admin:/>show performance lun lun_id=1
0.Max. Bandwidth(MB/s)
1.Queue Length
2.Bandwidth(MB/s) / Block Bandwidth(MB/s)
3.Throughput(IOPS)(IO/s)
4.Read Bandwidth(MB/s)
5.Average Read I/O Size(KB)
6.Read Throughput(IOPS)(IO/s)
7.Write Bandwidth(MB/s)
8.Average Write I/O Size(KB)
9.Write Throughput(IOPS)(IO/s)
10.Read I/O Granularity Distribution: [4K,8K)(%)
11.Read I/O Granularity Distribution: [8K,16K)(%)
12.Read I/O Granularity Distribution: [16K,32K)(%)
13.Read I/O Granularity Distribution: [32K,64K)(%)
14.Read I/O Granularity Distribution: [64K,128K)(%)
15.Write I/O Granularity Distribution: [4K,8K)(%)
16.Write I/O Granularity Distribution: [8K,16K)(%)
17.Write I/O Granularity Distribution: [16K,32K)(%)
18.Write I/O Granularity Distribution: [32K,64K)(%)
19.Write I/O Granularity Distribution: [64K,128K)(%)
20.Read Cache Hit Ratio(%)
21.Write Cache Hit Ratio(%)
22.Average IO Size(KB)
23.% Read
24.% Write
25.% Hit
26.Max IOPS(IO/s)
27.Service Time(Excluding Queue Time)(us)
28.Average I/O Latency(us)
29.Max. I/O Latency(us)
30.Average Read I/O Latency(us)
31.Average Write I/O Latency(us)
32.Read I/O Latency Distribution: [0us,500us)(%)
33.Read I/O Latency Distribution: [500us,1ms)(%)
34.Read I/O Latency Distribution: [1ms,2ms)(%)
35.Read I/O Latency Distribution: [2ms,5ms)(%)
36.Read I/O Latency Distribution: [5ms,10ms)(%)
37.Read I/O Latency Distribution: >= 10ms(%)
38.Write I/O Latency Distribution: [0us,500us)(%)
39.Write I/O Latency Distribution: [500us,1ms)(%)
40.Write I/O Latency Distribution: [1ms,2ms)(%)
41.Write I/O Latency Distribution: [2ms,5ms)(%)
42.Write I/O Latency Distribution: [5ms,10ms)(%)
43.Write I/O Latency Distribution: >= 10ms(%)
44.Read and Write I/O Latency Distribution: [0us,500us)(%)
45.Read and Write I/O Latency Distribution: [500us,1ms)(%)
46.Number of failed read I/Os
47.Number of failed write I/Os
48.Max. Read I/O Size(KB)
49.Max. Write I/O Size(KB)
50.Max. I/O Size(KB)
51.The cumulative count of I/Os
52.The cumulative count of data transferred in Kbytes
53.The cumulative elapsed I/O time(ms)
54.The cumulative count of data transferred in Kbytes
55.The cumulative count of all reads
56.The cumulative count of data read in Kbytes(1024bytes = 1KByte)
57.The cumulative count of all writes
58.The cumulative count of data written in Kbytes
59.Cache page preservation(%)
60.Unmap Command Bandwidth (MB/s)
61.Unmap Command IOPS (IO/s)
62.Avg. Unmap Command Size (KB)
63.Avg. Unmap Command Response Time (us)
64.WRITE SAME Command Bandwidth (MB/s)
65.WRITE SAME Command IOPS (IO/s)
66.Avg. WRITE SAME Command Size (KB)
67.Avg. WRITE SAME Command Response Time (us)
68.Full Copy Read Request Bandwidth (MB/s)
69.Full Copy Read Request IOPS (IO/s)
70.Avg. Full Copy Read Request Size (KB)
71.Avg. Full Copy Read Request Response Time (us)
72.Full Copy Write Request Bandwidth (MB/s)
73.Full Copy Write Request IOPS (IO/s)
74.Avg. Full Copy Write Request Size (KB)
75.Avg. Full Copy Write Request Response Time (us)
76.Read I/O Granularity Distribution: [0K,4K)(%)
77.Read I/O Granularity Distribution: >= 128K(%)
78.Write I/O Granularity Distribution: [0K,4K)(%)
79.Write I/O Granularity Distribution: >= 128K(%)
80.VAAI Bandwidth (MB/s)
81.VAAI IOPS (IO/s)
82.Avg. VAAI Size (KB)
83.Avg. VAAI Response Time (us)
84.Copy Read Request Bandwidth
85.Copy Read Request IOPS (IO/s)
86.Avg. Copy Read Request Size (KB)
87.Avg. Copy Read Request Response Time (us)
88.Copy Write Request Bandwidth
89.Copy Write Request IOPS (IO/s)
90.Avg. Copy Write Request Size (KB)
91.Avg. Copy Write Request Response Time (us)
92.ODX Read Request Bandwidth (MB/s)
93.ODX Read Request IOPS (IO/s)
94.Avg. ODX Read Request Size (KB)
95.Avg. ODX Read Request Response Time (us)
96.ODX Write Request Bandwidth (MB/s)
97.ODX Write Request IOPS (IO/s)
98.Avg. ODX Write Request Size (KB)
99.Avg. ODX Write Request Response Time (us)
100.ODX Write Zero Request Bandwidth (MB/s)
101.ODX Write Zero Request IOPS (IO/s)
102.Avg. ODX Write Zero Request Size (KB)
103.Avg. ODX Write Zero Request Response Time (us)
104.I/O Sequentiality(%)
Input item(s) number separated by comma:4
Read Bandwidth(MB/s) : 0
```

##### System Response

None
