# show performance elink


##### Function

The **show performance elink** command is used to query performance statistics of heterogeneous links. Running this command analyzes real-time performance statistics of heterogeneous links.

##### Format

**show performance elink** { link_id=? \| link_id_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| link_id=? | ID of the heterogeneous link whose performance you want to query. | To obtain the value, run the "show remote_device elink" command. |
| link_id_list=? | ID list of heterogeneous links whose performance you want to query. | To obtain the value, run the "show remote_device elink" command.<br>Multiple IDs are separated by commas (,), or the ID range is separated by hyphens (-).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas (,)) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query write I/Os statistics of the link whose ID is "268435456".

```text
admin:/>show performance elink link_id=268435465
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
22.The cumulative count of I/Os
23.The cumulative count of data transferred in Kbytes
24.The cumulative count of all writes
25.The cumulative count of data written in Kbytes
Input item(s) number separated by comma:24
The cumulative count of all writes : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                          | Meaning                                     |
|----------------------------------------------------|---------------------------------------------|
| Queue Length                                       | Queue length.                               |
| Throughput(IOPS)(IO/s)                             | Input/output operations per second.         |
| Average Read I/O Size(KB)                          | Average read I/O size.                      |
| Read Throughput(IOPS)(IO/s)                        | Read operations per second.                 |
| Average Write I/O Size(KB)                         | Average write I/O size.                     |
| Write Throughput(IOPS)(IO/s)                       | Write operations per second.                |
| Service Time(Excluding Queue Time)(ms)             | Service time (excluding the queue time).    |
| Read Bandwidth(MB/s)                               | Read bandwidth.                             |
| Write Bandwidth(MB/s)                              | Write bandwidth.                            |
| Average IO Size(KB)                                | Average I/O size.                           |
| % Read                                             | Read ratio (%).                             |
| % Write                                            | Write ratio (%).                            |
| Max IOPS(IO/s)                                     | Maximum input/output operations per second. |
| Failed IOs                                         | Failed I/Os.                                |
| Failed IOs/sec                                     | Number of failed I/Os per second.           |
| Failed IO Ratio(%)                                 | Failed I/O Ratio (%).                       |
| Average I/O Latency(us)                            | Average I/O latency.                        |
| Max. I/O Latency(us)                               | Maximum I/O latency.                        |
| Average Read I/O Latency(us)                       | Average read I/O latency.                   |
| Average Write I/O Latency(us)                      | Average write I/O latency.                  |
| Max. Bandwidth(MB/s)                               | Maximum Bandwidth.                          |
| Bandwidth(MB/s) / Block Bandwidth(MB/s)            | Bandwidth.                                  |
| The cumulative count of I/Os                       | Cumulative count of I/Os.                   |
| The cumulative count of data transferred in Kbytes | Cumulative count of data transferred in KB. |
| The cumulative count of all writes                 | Cumulative count of all writes.             |
| The cumulative count of data written in Kbytes     | Cumulative count of data written in KB.     |
