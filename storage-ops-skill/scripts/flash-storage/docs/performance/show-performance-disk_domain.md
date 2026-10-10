# show performance disk_domain


##### Function

The **show performance disk_domain** command is used to query the performance statistics on a disk domain. Run this command to analyze the performance statistics on a disk domain in real time.

##### Format

**show performance disk_domain** \[ disk_domain_id=? \] \[ disk_domain_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disk_domain_id=? | ID of a disk domain on which you want to query performance statistics. | To obtain the value, run "show disk_domain general". |
| disk_domain_id_list=? | ID list of disk domains on which you want to query performance statistics. | To obtain the value, run "show disk_domain general".<br>Separate the IDs of disk domains with commas (,). Consecutive IDs can be represented by using a hyphen (-). |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.
-   "disk_domain_id" is mutually exclusive with "disk_domain_id_list".

##### Example

Query the I/O throughput of disk domain "0".

```text
admin:/>show performance disk_domain disk_domain_id=0
0.Queue Length
1.Bandwidth(MB/s) / Block Bandwidth(MB/s)
2.Throughput(IOPS)(IO/s)
3.Read Bandwidth(MB/s)
4.Average Read I/O Size(KB)
5.Read Throughput(IOPS)(IO/s)
6.Write Bandwidth(MB/s)
7.Average Write I/O Size(KB)
8.Write Throughput(IOPS)(IO/s)
9.Service Time(Excluding Queue Time)(ms)
10.Read I/O Granularity Distribution: [0,4K)(%)
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
24.Average I/O Latency(ms)
25.Max. I/O Latency(ms)
26.Average Read I/O Latency(ms)
27.Average Write I/O Latency(ms)
28.Average IO Size(KB)
29.BE Reqs/sec
30.BE Read Reqs/sec
31.BE Write Reqs/sec
32.BE MBs transferred/sec
33.BE MBs Read/sec
34.BE MBs Written/sec
35.% Read
36.% Write
37.BE % Reads
38.BE % Writes
39.Average I/O Latency(us)
40.Max. I/O Latency(us)
41.Average Read I/O Latency(us)
42.Average Write I/O Latency(us)
43.BE Read Response Time(us)
44.BE Write Response Time(us)
45.BE Avg Response Time(us)
46.Average utilization of member disks(%)
Input item(s) number separated by comma:2
Throughput(IOPS)(IO/s) : 4310
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                           | Meaning                                                                 |
|-----------------------------------------------------|-------------------------------------------------------------------------|
| Usage Ratio(%)                                      | Usage rate.                                                             |
| Queue Length                                        | Queue length.                                                           |
| Bandwidth(MB/s) / Block Bandwidth(MB/s)             | Bandwidth.                                                              |
| Throughput(IOPS)(IO/s)                              | Input/output operations per second.                                     |
| Read Bandwidth(MB/s)                                | Read bandwidth.                                                         |
| Average Read I/O Size(KB)                           | Average read I/O size.                                                  |
| Read Throughput(IOPS)(IO/s)                         | Read operations per second.                                             |
| Write Bandwidth(MB/s)                               | Write bandwidth.                                                        |
| Average Write I/O Size(KB)                          | Average write I/O size.                                                 |
| Write Throughput(IOPS)(IO/s)                        | Write operations per second.                                            |
| Service Time(Excluding Queue Time)(ms)              | Service time (excluding the queue time).                                |
| Read I/O Granularity Distribution: \[0K,1K)(%)      | Proportion of read I/Os with I/O size \[0 KB, 1 KB).                    |
| Read I/O Granularity Distribution: \[1K,2K)(%)      | Proportion of read I/Os with I/O size \[1 KB, 2 KB).                    |
| Read I/O Granularity Distribution: \[2K,4K)(%)      | Proportion of read I/Os with I/O size \[2 KB, 4 KB).                    |
| Read I/O Granularity Distribution: \[4K,8K)(%)      | Proportion of read I/Os with I/O size \[4 KB, 8 KB).                    |
| Read I/O Granularity Distribution: \[8K,16K)(%)     | Proportion of read I/Os with I/O size \[8 KB, 16 KB).                   |
| Read I/O Granularity Distribution: \[16K,32K)(%)    | Proportion of read I/Os with I/O size \[16 KB, 32 KB).                  |
| Read I/O Granularity Distribution: \[32K,64K)(%)    | Proportion of read I/Os with I/O size \[32 KB, 64 KB).                  |
| Read I/O Granularity Distribution: \[64K,128K)(%)   | Proportion of read I/Os with I/O size \[64 KB, 128 KB).                 |
| Read I/O Granularity Distribution: \[128K,256K)(%)  | Proportion of read I/Os with I/O size \[128 KB, 256 KB).                |
| Read I/O Granularity Distribution: \[256K,512K)(%)  | Proportion of read I/Os with I/O size \[256 KB, 512 KB).                |
| Read I/O Granularity Distribution: \>= 512K(%)      | Proportion of read I/Os with I/O size greater than or equal to 512 KB.  |
| Write I/O Granularity Distribution: \[0K,1K)(%)     | Proportion of write I/Os with I/O size \[0 KB, 1 KB).                   |
| Write I/O Granularity Distribution: \[1K,2K)(%      | Proportion of write I/Os with I/O size \[1 KB, 2 KB).                   |
| Write I/O Granularity Distribution: \[2K,4K)(%)     | Proportion of write I/Os with I/O size \[2 KB, 4 KB).                   |
| .Write I/O Granularity Distribution: \[4K,8K)(%)    | Proportion of write I/Os with I/O size \[4 KB, 8 KB).                   |
| Write I/O Granularity Distribution: \[8K,16K)(%).   | Proportion of write I/Os with I/O size \[8 KB, 16 KB).                  |
| Write I/O Granularity Distribution: \[16K,32K)(%)   | Proportion of write I/Os with I/O size \[16 KB, 32 KB).                 |
| Write I/O Granularity Distribution: \[32K,64K)(%)   | Proportion of write I/Os with I/O size \[32 KB, 64 KB).                 |
| Write I/O Granularity Distribution: \[64K,128K)(%)  | Proportion of write I/Os with I/O size \[64 KB, 128 KB).                |
| Write I/O Granularity Distribution: \[128K,256K)(%) | Proportion of write I/Os with I/O size \[128 KB, 256 KB).               |
| Write I/O Granularity Distribution: \[256K,512K)(%) | Proportion of write I/Os with I/O size \[256 KB, 512 KB).               |
| Write I/O Granularity Distribution: \>= 512K(%)     | Proportion of write I/Os with I/O size greater than or equal to 512 KB. |
| Average I/O Latency(ms)                             | Average I/O latency.                                                    |
| Max. I/O Latency(ms)                                | Maximum I/O latency.                                                    |
| Average Read I/O Latency(ms)                        | Average read I/O latency.                                               |
| Average Write I/O Latency(ms)                       | Average write I/O latency.                                              |
| Average IO Size                                     | Average I/O size.                                                       |
| BE Reqs/sec                                         | Number of back-end requests per second.                                 |
| BE Read Reqs/sec                                    | Number of back-end read requests per second.                            |
| BE MBs Read/sec                                     | Back-end read traffic.                                                  |
| Max. I/O Latency(us)                                | Maximum I/O latency.                                                    |
| BE MBs transferred/sec                              | Back-end traffic.                                                       |
| BE Write Reqs/sec                                   | Number of back-end write requests per second.                           |
| BE MBs Written/sec                                  | Back-end write traffic.                                                 |
| % Read                                              | Read ratio (%).                                                         |
| % Write                                             | Write ratio (%).                                                        |
| BE Read Response Time(ms)                           | Back-end read response time.                                            |
| BE Write Response Time(ms)                          | Back-end write response time.                                           |
| BE Avg Response Time(ms)                            | Back-end average response time.                                         |
| BE % Reads                                          | Back-end read ratio (%).                                                |
| BE % Writes                                         | Back-end write ratio (%).                                               |
| Average I/O Latency(us)                             | Average I/O latency.                                                    |
| Average Read I/O Latency(us)                        | Average read I/O latency.                                               |
| Average Write I/O Latency(us)                       | Average write I/O latency.                                              |
