# show performance host


##### Function

The **show performance host** command is used to query the performance statistics on a host. Run this command to analyze the performance statistics on a host in real time.

##### Format

**show performance host** host_id=?

**show performance host** host_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_id=? | ID of a host. | To obtain the value, run "show host general". |
| host_id_list=? | ID list of hosts. | To obtain the value, run "show host general".<br>Separate the host IDs with commas (,) or hyphens (-).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the performance statistics on the read I/Os for host "0".

```text
admin:/>show performance host host_id=0
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
10.Read I/O Granularity Distribution: [0K,4K)(%)
11.Read I/O Granularity Distribution: [4K,8K)(%)
12.Read I/O Granularity Distribution: [8K,16K)(%)
13.Read I/O Granularity Distribution: [16K,32K)(%)
14.Read I/O Granularity Distribution: [32K,64K)(%)
15.Read I/O Granularity Distribution: [64K,128K)(%)
16.Read I/O Granularity Distribution: >= 128K(%)
17.Write I/O Granularity Distribution: [0K,4K)(%)
18.Write I/O Granularity Distribution: [4K,8K)(%)
19.Write I/O Granularity Distribution: [8K,16K)(%)
20.Write I/O Granularity Distribution: [16K,32K)(%)
21.Write I/O Granularity Distribution: [32K,64K)(%)
22.Write I/O Granularity Distribution: [64K,128K)(%)
23.Write I/O Granularity Distribution: >= 128K(%)
24.Average IO Size(KB)
25.% Read
26.% Write
27.Max IOPS(IO/s)
28.Service Time(Excluding Queue Time)(us)
29.Average I/O Latency(us)
30.Max. I/O Latency(us)
31.Average Read I/O Latency(us)
32.Average Write I/O Latency(us)
33.Unmap Command Bandwidth (MB/s)
34.Unmap Command IOPS (IO/s)
35.Avg. Unmap Command Size (KB)
36.Avg. Unmap Command Response Time (us)
37.WRITE SAME Command Bandwidth (MB/s)
38.WRITE SAME Command IOPS (IO/s)
39.Avg. WRITE SAME Command Size (KB)
40.Avg. WRITE SAME Command Response Time (us)
41.Full Copy Command Bandwidth (MB/s)
42.Full Copy Command IOPS (IO/s)
43.Avg. Full Copy Command Size (KB)
44.Avg. Full Copy Command Response Time (us)
45.ODX Command Bandwidth (MB/s)
46.ODX Command IOPS (IO/s)
47.Avg. ODX Command Size (KB)
48.Avg. ODX Command Response Time (us)
49.ODX Write Zero Request Bandwidth (MB/s)
50.ODX Write Zero Request IOPS (IO/s)
51.Avg. ODX Write Zero Request Size (KB)
52.Avg. ODX Write Zero Request Response Time (us)
Input item(s) number separated by comma:6

Read Throughput(IOPS)(IO/s) : 0
Read Throughput(IOPS)(IO/s) : 0
Read Throughput(IOPS)(IO/s) : 0
Read Throughput(IOPS)(IO/s) : 0
Read Throughput(IOPS)(IO/s) : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                          | Meaning                                                       |
|----------------------------------------------------|---------------------------------------------------------------|
| Max. Bandwidth(MB/s)                               | Maximum bandwidth.                                            |
| Queue Length                                       | Queue length.                                                 |
| Bandwidth(MB/s) / Block Bandwidth(MB/s)            | Bandwidth.                                                    |
| Throughput(IOPS)(IO/s)                             | Input/output operations per second.                           |
| Read Bandwidth(MB/s)                               | Read bandwidth.                                               |
| Average Read I/O Size(KB)                          | Average read I/O size.                                        |
| Read Throughput(IOPS)(IO/s)                        | Read operations per second.                                   |
| Write Bandwidth(MB/s)                              | Write bandwidth.                                              |
| Average Write I/O Size(KB)                         | Average write I/O size.                                       |
| Write Throughput(IOPS)(IO/s)                       | Service time (excluding the queue time).                      |
| Read I/O Granularity Distribution: \[0K,4K)(%)     | Percentage of read I/Os whose sizes range from 0 KB to 4 KB.  |
| Read I/O Granularity Distribution: \[4K,8K)(%)     | Proportion of read I/Os with I/O size \[4 KB, 8 KB).          |
| Read I/O Granularity Distribution: \[8K,16K)(%)    | Proportion of read I/Os with I/O size \[8 KB, 16 KB).         |
| Read I/O Granularity Distribution: \[16K,32K)(%)   | Proportion of read I/Os with I/O size \[16 KB, 32 KB).        |
| Read I/O Granularity Distribution: \[32K,64K)(%)   | Proportion of read I/Os with I/O size \[32 KB, 64 KB).        |
| Read I/O Granularity Distribution: \[64K,128K)(%)  | Proportion of read I/Os with I/O size \[64 KB, 128 KB).       |
| Read I/O Granularity Distribution: \>= 128K(%)     | Proportion of read I/Os whose size is greater than 128 KB.    |
| Write I/O Granularity Distribution: \[0K,4K)(%)    | Percentage of write I/Os whose sizes range from 0 KB to 4 KB. |
| Write I/O Granularity Distribution: \[4K,8K)(%)    | Proportion of write I/Os with I/O size \[4 KB, 8 KB).         |
| Write I/O Granularity Distribution: \[8K,16K)(%)   | Proportion of write I/Os with I/O size \[8 KB, 16 KB).        |
| Write I/O Granularity Distribution: \[16K,32K)(%)  | Proportion of write I/Os with I/O size \[16 KB, 32 KB).       |
| Write I/O Granularity Distribution: \[32K,64K)(%)  | Proportion of write I/Os with I/O size \[32 KB, 64 KB).       |
| Write I/O Granularity Distribution: \[64K,128K)(%) | Proportion of write I/Os with I/O size \[64 KB, 128 KB).      |
| Write I/O Granularity Distribution: \>= 128K(%)    | Percentage of write I/Os whose size is greater than 128 KB.   |
| Average IO Size(KB)                                | Average I/O latency.                                          |
| % Read                                             | Read ratio (%).                                               |
| % Write                                            | Write ratio (%).                                              |
| Max IOPS(IO/s)                                     | Maximum Input/output operations per second.                   |
| Service Time(Excluding Queue Time)(us)             | Service time (excluding the queue time).                      |
| Average I/O Latency(us)                            | Average I/O latency.                                          |
| Max. I/O Latency(us)                               | Maximum I/O latency.                                          |
| Average Read I/O Latency(us)                       | Average read I/O latency.                                     |
| Average Write I/O Latency(us)                      | Average write I/O latency.                                    |
| Unmap Command Bandwidth (MB/s)                     | Bandwidth of the Unmap command.                               |
| Unmap Command IOPS (IO/s)                          | IOPS of the Unmap command.                                    |
| Avg. Unmap Command Size (KB)                       | Average I/O size of the Unmap command.                        |
| Avg. Unmap Command Response Time (us)              | Average I/O response time of the Unmap command.               |
| WRITE SAME Command Bandwidth (MB/s)                | Bandwidth of the Write same command.                          |
| WRITE SAME Command IOPS (IO/s)                     | IOPS of the Write same command.                               |
| Avg. WRITE SAME Command Size (KB)                  | Average I/O size of the Write same command.                   |
| Avg. WRITE SAME Command Response Time (us)         | Average I/O response time of the Write same command.          |
| Full Copy Command Bandwidth (MB/s)                 | Bandwidth of the full copy command.                           |
| Full Copy Command IOPS (IO/s)                      | IOPS of the full copy command.                                |
| Avg. Full Copy Command Size (KB)                   | Average I/O size of the full copy command.                    |
| Avg. Full Copy Command Response Time (us)          | Average I/O response time of a full copy command.             |
| ODX Command Bandwidth (MB/s)                       | Bandwidth of the ODX command.                                 |
| ODX Command IOPS (IO/s)                            | IOPS of the Odx command.                                      |
| Avg. ODX Command Size (KB)                         | Average I/O size of the Odx command.                          |
| Avg. ODX Command Response Time (us)                | Average I/O response time of an Odx command.                  |
| ODX Write Zero Request Bandwidth (MB/s)            | Bandwidth of the ODX zero write command.                      |
| ODX Write Zero Request IOPS (IO/s)                 | IOPS of the ODX zero write command.                           |
| Avg. ODX Write Zero Request Size (KB)              | Average I/O size of the ODX zero write command.               |
| Avg. ODX Write Zero Request Response Time (us)     | Average I/O response time of the ODX write zero command.      |
