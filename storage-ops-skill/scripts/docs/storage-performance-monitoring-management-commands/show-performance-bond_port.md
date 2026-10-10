# show performance bond_port


##### Function

The **show performance bond_port** command is used to display the performance statistics on bonded ports. Use this command when you want to check the real-time performance statistics of bonded ports.

##### Format

**show performance bond_port** bond_port_id=?

**show performance bond_port** bond_port_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| bond_port_id=? | ID of the bonded port whose performance statistics you want to check. | To obtain the value, run the "show bond_port" command. |
| bond_port_id_list=? | List of bonded port IDs whose performance statistics you want to check. | To obtain the value, run the "show bond_port" command.<br>Separate the bond port IDs with commas (,).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   After executing the command, you will be prompted to specify the performance categories you want to check. Enter the one or multiple item numbers (separated by commas) and press "Enter" to check the statistics of the performance categories you have selected.
-   Performance statistics are updated in real time.
-   To exit performance statistics display, enter "q" on the command line interface (CLI).
-   Before you execute this command, ensure that the performance monitoring function is enabled.

##### Example

Check the statistics on all bonded ports.

```text
admin:/>show bond_port

ID     Name   Health Status Running Status MTU  Port ID List
------ ------ ------------- -------------- ---- -----------------------------
139009 regian Normal        Link Down      1500 CTE0.A.IOM1.P2,CTE0.A.IOM1.P3
```

Check the performance statistics on bonded port 139009.

```text
admin:/>show performance bond_port bond_port_id=139009
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
Input item(s) number separated by comma:3,4,5
Bandwidth(MB/s) / Block Bandwidth(MB/s) : 0
Throughput(IOPS)(IO/s)                  : 0
Read Bandwidth(MB/s)                    : 0
```

##### System Response

None
