# show performance link


##### Function

The **show performance link** command is used to query the performance statistics on a link. Run this command to analyze the performance statistics on a link in real time.

##### Format

**show performance link** link_id=?

**show performance link** link_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| link_id=? | ID of a link on which you want to query performance statistics. | To obtain the value, run "show remote_device link". |
| link_id_list=? | ID list of links on which you want to query performance statistics. | To obtain the value, run "show remote_device link".<br>Separate the link IDs with commas (,) or hyphens (-).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" display the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the performance statistics on the read I/Os for link whose ID is "0".

```text
admin:/>show performance link link_id=0
0.Queue Length
1.Throughput(IOPS)(IO/s)
2.Average Read I/O Size(KB)
3.Read Throughput(IOPS)(IO/s)
4.Average Write I/O Size(KB)
5.Write Throughput(IOPS)(IO/s)
6.Service Time(Excluding Queue Time)(ms)
7.Read Bandwidth(MB/s)
8.Write Bandwidth(MB/s)
9.Average IO Size(KB)
10.% Read
11.% Write
12.Max IOPS(IO/s)
13.Failed IOs
14.Failed IOs/sec
15.Failed IO Ratio(%)
16.Average I/O Latency(us)
17.Max. I/O Latency(us)
18.Average Read I/O Latency(us)
19.Average Write I/O Latency(us)
20.Max. Bandwidth(MB/s)
21.Bandwidth(MB/s) / Block Bandwidth(MB/s)
22.Total Bandwidth(KB/s)
23.Sending bandwidth for replication(KB/s)
24.Receiving bandwidth for replication(KB/s)
25.The cumulative count of I/Os
26.The cumulative count of data transferred in Kbytes
27.The cumulative count of all writes
28.The cumulative count of data written in Kbytes
Input item(s) number separated by comma:0
Queue Length : 2
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                          | Meaning                                                   |
|----------------------------------------------------|-----------------------------------------------------------|
| Queue Length                                       | Length of the queue whose link ID is 0.                   |
| Average Read I/O Size(KB)                          | Average size of read I/Os on link 0 (KB).                 |
| The cumulative count of data written in Kbytes     | Accumulated number of KB-based data writes on the link.   |
| The cumulative count of all writes                 | Accumulated number of writes on the link.                 |
| The cumulative count of data transferred in Kbytes | Accumulated count of data transmitted on the link in KB.  |
| The cumulative count of I/Os                       | Total number of I/Os sent by the link.                    |
| Receiving bandwidth for replication(KB/s)          | Receiving bandwidth of the replication link (KB/s).       |
| Sending bandwidth for replication(KB/s)            | Sending bandwidth of the replication link (KB/s).         |
| Total Bandwidth(KB/s)                              | Total Link Bandwidth (KB/s).                              |
| Bandwidth(MB/s)                                    | Link bandwidth (MB/s).                                    |
| Max. Bandwidth(MB/s)                               | Maximum bandwidth (MB/s) of link 0.                       |
| Average Write I/O Latency(us)                      | Average write I/O latency of a link (us).                 |
| Average Read I/O Latency(us)                       | Average read I/O latency of a link (us).                  |
| Max. I/O Latency(us)                               | Maximum I/O latency of a link (us).                       |
| Average I/O Latency(us)                            | Average link I/O latency (us).                            |
| Failed IO Ratio(%)                                 | I/O failure rate (%) of link 0.                           |
| Failed IOs/sec                                     | Failed I/Os of link 0 per second (I/O/s).                 |
| Failed IOs                                         | Total number of I/Os that fail to be executed on link 0.  |
| Max IOPS(IO/s)                                     | Maximum IOPS (I/O/s) of a link.                           |
| % Write                                            | Percentage of write I/Os on link 0.                       |
| % Read                                             | Percentage of read I/Os on link 0.                        |
| Average IO Size(KB)                                | Average I/O size (KB) of a specified link.                |
| Write Bandwidth(MB/s)                              | Indicates the write bandwidth (KB/s) of a specified link. |
| Read Bandwidth(MB/s)                               | Read bandwidth (KB/s) of a specified link.                |
| Service Time(Excluding Queue Time)(ms)             | Service Time (ms).                                        |
| Write Throughput(IOPS)(IO/s)                       | Read I/O throughput (I/O/S) of a specified link.          |
| Average Write I/O Size(KB)                         | Average write I/O size of a specified link (KB).          |
| Read Throughput(IOPS)(IO/s)                        | Read I/O throughput (I/O/S) of a specified link.          |
| Throughput(IOPS)(IO/s)                             | I/O throughput (I/O/S) of a specified link.               |
