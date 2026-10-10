# show performance storage_pool


##### Function

The **show performance storage_pool** command is used to query the performance statistics on a storage pool. Run this command to analyze the performance statistics on a storage pool in real time.

##### Format

**show performance storage_pool** pool_id=?

**show performance storage_pool** pool_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pool_id=? | ID of a storage pool on which you want to query performance statistics. | To obtain the value, run "show storage_pool general". |
| pool_id_list=? | ID list of storage pools on which you want to query performance statistics. | To obtain the value, run "show storage_pool general".<br>Separate the IDs of storage pool with commas (,). |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas (,)) for the selected categories and pressing "Enter" display the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the performance statistics on the read I/Os for storage pool "0".

```text
admin:/>show performance storage_pool pool_id=0
0.Queue Length
1.Bandwidth(MB/s) / Block Bandwidth(MB/s)
2.Throughput(IOPS)(IO/s)
3.Read Bandwidth(MB/s)
4.Average Read I/O Size(KB)
5.Read Throughput(IOPS)(IO/s)
6.Write Bandwidth(MB/s)
7.Average Write I/O Size(KB)
8.Write Throughput(IOPS)(IO/s)
9.Read I/O Granularity Distribution: [4K,8K)(%)
10.Read I/O Granularity Distribution: [8K,16K)(%)
11.Read I/O Granularity Distribution: [16K,32K)(%)
12.Read I/O Granularity Distribution: [32K,64K)(%)
13.Read I/O Granularity Distribution: [64K,128K)(%)
14.Write I/O Granularity Distribution: [4K,8K)(%)
15.Write I/O Granularity Distribution: [8K,16K)(%)
16.Write I/O Granularity Distribution: [16K,32K)(%)
17.Write I/O Granularity Distribution: [32K,64K)(%)
18.Write I/O Granularity Distribution: [64K,128K)(%)
19.Average IO Size(KB)
20.BE Reqs/sec
21.BE Read Reqs/sec
22.BE Write Reqs/sec
23.BE MBs transferred/sec
24.BE MBs Read/sec
25.BE MBs Written/sec
26.% Read
27.% Write
28.BE % Reads
29.BE % Writes
30.Service Time(Excluding Queue Time)(us)
31.Average I/O Latency(us)
32.Max. I/O Latency(us)
33.Average Read I/O Latency(us)
34.Average Write I/O Latency(us)
35.BE Read Response Time(us)
36.BE Write Response Time(us)
37.BE Avg Response Time(us)
38.Overall Space Saving Ratio
39.Thin LUN Space Saving Rate(%)
40.Read I/O Granularity Distribution: [0K,4K)(%)
41.Read I/O Granularity Distribution: >= 128K(%)
42.Write I/O Granularity Distribution: [0K,4K)(%)
43.Write I/O Granularity Distribution: >= 128K(%)
44.Average utilization of member disks(%)
45.Unmap Command Bandwidth (MB/s)
46.Unmap Command IOPS (IO/s)
47.Avg. Unmap Command Size (KB)
48.Avg. Unmap Command Response Time (us)
49.WRITE SAME Command Bandwidth (MB/s)
50.WRITE SAME Command IOPS (IO/s)
51.Avg. WRITE SAME Command Size (KB)
52.Avg. WRITE SAME Command Response Time (us)
53.Full Copy Command Bandwidth (MB/s)
54.Full Copy Command IOPS (IO/s)
55.Avg. Full Copy Command Size (KB)
56.Avg. Full Copy Command Response Time (us)
57.ODX Command Bandwidth (MB/s)
58.ODX Command IOPS (IO/s)
59.Avg. ODX Command Size (KB)
60.Avg. ODX Command Response Time (us)
61.ODX Write Zero Request Bandwidth (MB/s)
62.ODX Write Zero Request IOPS (IO/s)
63.Avg. ODX Write Zero Request Size (KB)
64.Avg. ODX Write Zero Request Response Time (us)
Input item(s) number separated by comma:3
Read Bandwidth(MB/s) : 0
```

##### System Response

None
