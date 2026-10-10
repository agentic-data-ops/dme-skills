# show performance port


##### Function

The **show performance port** command is used to query the performance statistics on a port. Run this command to analyze the performance statistics on a port in real time.

##### Format

**show performance port** port_id=?

**show performance port** port_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| port_id=? | ID of a port on which you want to query performance statistics. | To obtain the value, run "show port general". |
| port_id_list=? | ID list of ports on which you want to query performance statistics. | To obtain the value, run "show port general".<br>Separate the port IDs with commas (,).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" display the performance statistics for those categories.
-   By default, performance statistics will be refreshed every three seconds. To refresh performance statistics instantly, press "Enter".
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the performance statistics on the read I/Os flowing through port P1 on interface module "1", where the module resides on controller 1 of engine "0". The command output varies depending on a specific product.

```text
admin:/>show performance port port_id=CTE0.A6.P0
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
11.Read I/O Granularity Distribution: [0K,1K)(%)
12.Read I/O Granularity Distribution: [1K,2K)(%)
13.Read I/O Granularity Distribution: [2K,4K)(%)
14.Read I/O Granularity Distribution: [4K,8K)(%)
15.Read I/O Granularity Distribution: [8K,16K)(%)
16.Read I/O Granularity Distribution: [16K,32K)(%)
17.Read I/O Granularity Distribution: [32K,64K)(%)
18.Read I/O Granularity Distribution: [64K,128K)(%)
19.Read I/O Granularity Distribution: [128K,256K)(%)
20.Read I/O Granularity Distribution: [256K,512K)(%)
21.Read I/O Granularity Distribution: >= 512K(%)
22.Write I/O Granularity Distribution: [0K,1K)(%)
23.Write I/O Granularity Distribution: [1K,2K)(%)
24.Write I/O Granularity Distribution: [2K,4K)(%)
25.Write I/O Granularity Distribution: [4K,8K)(%)
26.Write I/O Granularity Distribution: [8K,16K)(%)
27.Write I/O Granularity Distribution: [16K,32K)(%)
28.Write I/O Granularity Distribution: [32K,64K)(%)
29.Write I/O Granularity Distribution: [64K,128K)(%)
30.Write I/O Granularity Distribution: [128K,256K)(%)
31.Write I/O Granularity Distribution: [256K,512K)(%)
32.Write I/O Granularity Distribution: >= 512K(%)
33.Average IO Size(KB)
34.% Read
35.% Write
36.Max IOPS(IO/s)
37.Service Time(Excluding Queue Time)(us)
38.Average I/O Latency(us)
39.Max. I/O Latency(us)
40.Average Read I/O Latency(us)
41.Average Write I/O Latency(us)
42.Sending bandwidth for replication(KB/s)
43.Receiving bandwidth for replication(KB/s)
44.The cumulative count of I/Os
45.The cumulative count of data transferred in Kbytes
46.The cumulative elapsed I/O time(ms)
47.The cumulative count of all reads
48.The cumulative count of all writes
Input item(s) number separated by comma:7
Read Throughput(IOPS)(IO/s) : 0
```

##### System Response

None
