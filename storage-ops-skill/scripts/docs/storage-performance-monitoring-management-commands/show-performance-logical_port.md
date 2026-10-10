# show performance logical_port


##### Function

The **show performance logical_port** command is used to query performance statistics of a logical port. Running this command analyzes performance statistics of a logical port in real time.

##### Format

**show performance logical_port** logical_port_name=?

**show performance logical_port** logical_port_name_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| logical_port_name=? | Name of a logical port on which you want to query performance statistics. | To obtain the value, run "show logical_port general". |
| logical_port_name_list=? | Name list of logical ports on which you want to query performance statistics. | To obtain the value, run "show logical_port general".<br>Separate the logical port names with commas (,).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   By default, performance statistics will be refreshed every three seconds. To refresh performance statistics instantly, press "Enter".
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query performance statistics of read I/O traffic of logical port "lif001". The command output varies depending on a specific product.

```text

admin:/>show performance logical_port logical_port_name=CTE0.A.MGMT.V4
0.Max. Bandwidth(MB/s)                                   1.Queue Length                                           2.Bandwidth(MB/s) / Block Bandwidth(MB/s)
3.Throughput(IOPS)(IO/s)                                 4.Read Bandwidth(MB/s)                                   5.Average Read I/O Size(KB)
6.Read Throughput(IOPS)(IO/s)                            7.Write Bandwidth(MB/s)                                  8.Average Write I/O Size(KB)
9.Write Throughput(IOPS)(IO/s)                           10.Read I/O Granularity Distribution: [4K,8K)(%)         11.Read I/O Granularity Distribution: [8K,16K)(%)
12.Read I/O Granularity Distribution: [16K,32K)(%)       13.Read I/O Granularity Distribution: [32K,64K)(%)       14.Read I/O Granularity Distribution: [64K,128K)(%)
15.Write I/O Granularity Distribution: [4K,8K)(%)        16.Write I/O Granularity Distribution: [8K,16K)(%)       17.Write I/O Granularity Distribution: [16K,32K)(%)
18.Write I/O Granularity Distribution: [32K,64K)(%)      19.Write I/O Granularity Distribution: [64K,128K)(%)     20.Average IO Size(KB)
21.% Read                                                22.% Write                                               23.Max IOPS(IO/s)
24.Service Time(Excluding Queue Time)(us)                25.Average I/O Latency(us)                               26.Max. I/O Latency(us)
27.Average Read I/O Latency(us)                          28.Average Write I/O Latency(us)                         29.Sending bandwidth for replication(KB/s)
30.Receiving bandwidth for replication(KB/s)             31.The cumulative count of I/Os                          32.The cumulative count of data transferred in Kbytes
33.The cumulative elapsed I/O time(ms)                   34.The cumulative count of all reads                     35.The cumulative count of all writes
36.Read I/O Granularity Distribution: [0K,4K)(%)         37.Read I/O Granularity Distribution: >= 128K(%)         38.Write I/O Granularity Distribution: [0K,4K)(%)
39.Write I/O Granularity Distribution: >= 128K(%)        40.Bandwidth For NFS V3(KB/s)                            41.Bandwidth For NFS V4(KB/s)
42.Bandwidth For NFS(KB/s)                               43.Bandwidth For SMB1(KB/s)                              44.Bandwidth For SMB2(KB/s)
45.Bandwidth For SMB(KB/s)                               46.Read Bandwidth For NFS V3 (KB/s)                      47.Read Bandwidth For NFS V4(KB/s)
48.Read Bandwidth For NFS(KB/s)                          49.Read Bandwidth For SMB1(KB/s)                         50.Read Bandwidth For SMB2(KB/s)
51.Read Bandwidth For SMB (KB/s)                         52.Write Bandwidth For NFS V3 (KB/s)                     53.Write Bandwidth For NFS V4(KB/s)
54.Write Bandwidth For NFS(KB/s)                         55.Write Bandwidth For SMB1(KB/s)                        56.Write Bandwidth For SMB2(KB/s)
57.Write Bandwidth For SMB (KB/s)                        58.OPS For NFS V3                                        59.OPS For NFS V4
60.OPS For NFS                                           61.OPS For SMB1                                          62.OPS For SMB2
63.OPS For SMB                                           64.Read OPS For NFS V3                                   65.Read OPS For NFS V4
66.Read OPS For NFS                                      67.Read OPS For SMB1                                     68.Read OPS For SMB2
69.Read OPS For SMB                                      70.Write OPS For NFS V3                                  71.Write OPS For NFS V4
72.Write OPS For NFS                                     73.Write OPS For SMB1                                    74.Write OPS For SMB2
75.Write OPS For SMB                                     76.Other OPS For NFS V3                                  77.Other OPS For NFS V4
78.Other OPS For NFS                                     79.Other OPS For SMB1                                    80.Other OPS For SMB2
81.Other OPS For SMB                                     82.IO Average Response Time For NFS V3(us)               83.IO Average Response Time For NFS V4(us)
84.IO Average Response Time For NFS(us)                  85.IO Average Response Time For SMB1(us)                 86.IO Average Response Time For SMB2(us)
87.IO Average Response Time For SMB(us)                  88.Read IO Average Response Time For NFS V3(us)          89.Read IO Average Response Time For NFS V4(us)
90.Read IO Average Response Time For NFS(us)             91.Read IO Average Response Time For SMB1(us)            92.Read IO Average Response Time For SMB2(us)
93.Read IO Average Response Time For SMB(us)             94.Write IO Average Response Time For NFS V3(us)         95.Write IO Average Response Time For NFS V4(us)
96.Write IO Average Response Time For NFS(us)            97.Write IO Average Response Time For SMB1(us)           98.Write IO Average Response Time For SMB2(us)
99.Write IO Average Response Time For SMB(us)            100.Other IO Average Response Time For NFS V3(us)        101.Other IO Average Response Time For NFS V4(us)
102.Other IO Average Response Time For NFS(us)           103.Other IO Average Response Time For SMB1(us)          104.Other IO Average Response Time For SMB2(us)
105.Other IO Average Response Time For SMB(us)
Input item(s) number separated by comma:0
```

##### System Response

None
