# show performance smb2


##### Function

The **show performance smb2** command is used to query performance statistics of the SMB2 protocol. Running this command analyzes performance statistics of SMB2 in real time.

##### Format

**show performance smb2** controller_id=?

**show performance smb2** controller_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller_id=? | ID of a controller. | To obtain the value, run the "show controller general" command. |
| controller_id_list=? | ID list of controllers. | To obtain the value, run the "show controller general" command.<br>Separate the controller IDs with commas (,). |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas (,)) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query SMB2 performance statistics of controller "0B".

```text
admin:/>show performance smb2 controller_id=0B
0.Read I/O Granularity Distribution: [1K,2K)(%)
1.Read I/O Granularity Distribution: [2K,4K)(%)
2.Read I/O Granularity Distribution: [4K,8K)(%)
3.Read I/O Granularity Distribution: [8K,16K)(%)
4.Read I/O Granularity Distribution: [16K,32K)(%)
5.Read I/O Granularity Distribution: [32K,64K)(%)
6.Read I/O Granularity Distribution: [64K,128K)(%)
7.Read I/O Granularity Distribution: [128K,256K)(%)
8.Write I/O Granularity Distribution: [1K,2K)(%)
9.Write I/O Granularity Distribution: [2K,4K)(%)
10.Write I/O Granularity Distribution: [4K,8K)(%)
11.Write I/O Granularity Distribution: [8K,16K)(%)
12.Write I/O Granularity Distribution: [16K,32K)(%)
13.Write I/O Granularity Distribution: [32K,64K)(%)
14.Write I/O Granularity Distribution: [64K,128K)(%)
15.Write I/O Granularity Distribution: [128K,256K)(%)
16.Read Bandwidth(MB/s)
17.Write Bandwidth(MB/s)
18.OPS(per second)
19.Read I/O Latency Distribution: [0ms,10ms)(%)
20.Read I/O Latency Distribution: [10ms,20ms)(%)
21.Read I/O Latency Distribution: [20ms,50ms)(%)
22.Read I/O Latency Distribution: [50ms,100ms)(%)
23.Read I/O Latency Distribution: [100ms,200ms)(%)
24.Read I/O Latency Distribution: >= 200ms(%)
25.Write I/O Latency Distribution: [0ms,10ms)(%)
26.Write I/O Latency Distribution: [10ms,20ms)(%)
27.Write I/O Latency Distribution: [20ms,50ms)(%)
28.Write I/O Latency Distribution: [50ms,100ms)(%)
29.Write I/O Latency Distribution: [100ms,200ms)(%)
30.Write I/O Latency Distribution: >= 200ms(%)
31.Read OPS(per second)
32.Write OPS(per second)
33.Average Latency For Operations(ms)
34.Max Latency For Operations(ms)
35.Throughput(Bps)
36.Read I/O Granularity Distribution: [0K,512B)(%)
37.Read I/O Granularity Distribution: [512B,1K)(%)
38.Read I/O Granularity Distribution: >= 256K(%)
39.Write I/O Granularity Distribution: [0K,512B)(%)
40.Write I/O Granularity Distribution: [512B,1K)(%)
41.Write I/O Granularity Distribution: >= 256K(%)
42.Min Latency For Operations(ms)
43.Average Latency For Operations(ms, accurate to three decimal places)
44.Max Latency For Operations(ms, accurate to three decimal places)
45.Min Latency For Operations(ms, accurate to three decimal places)
46.File Bandwidth(MB/s)
47.Throughput(MB/s)
48.Average Read OPS Response Time (us)
49.Average Write OPS Response Time (us)
50.Other OPS For SMB
51.Other IO Average Response Time For SMB(us)
52.Total CIFS create OPS
53.Total CIFS query info OPS
54.Total CIFS query dir OPS
55.Total CIFS set info OPS
56.Average CIFS create response time (us)
57.Average CIFS queryinfo response time (us)
58.Average CIFS querydir response time (us)
59.Average CIFS setinfo response time (us)
60.Read I/O Latency Distribution: [200ms,1s)(%)
61.Read I/O Latency Distribution: [1s,3s)(%)
62.Read I/O Latency Distribution: [3s,5s)(%)
63.Read I/O Latency Distribution: [5s,8s)(%)
64.Read I/O Latency Distribution: >= 8s(%)
65.Write I/O Latency Distribution: [200ms,1s)(%)
66.Write I/O Latency Distribution: [1s,3s)(%)
67.Write I/O Latency Distribution: [3s,5s)(%)
68.Write I/O Latency Distribution: [5s,8s)(%)
69.Write I/O Latency Distribution: >= 8s(%)
70.Average Read I/O Size(KB)
71.Average Write I/O Size(KB)
72.Average IO Size(KB)
Input item(s) number separated by comma:6,8

Read I/O Granularity Distribution: [64K,128K)(%) : 0
Write I/O Granularity Distribution: [1K,2K)(%)   : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                                            | Meaning                                                                                                   |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Read I/O Granularity Distribution: \[1K,2K)(%)                       | Percentage of read I/Os with size in \[1K,2K).                                                            |
| Read I/O Granularity Distribution: \[2K,4K)(%)                       | Percentage of read I/Os with size in \[2K,4K).                                                            |
| Read I/O Granularity Distribution: \[4K,8K)(%)                       | Percentage of read I/Os with size in \[4K,8K).                                                            |
| Read I/O Granularity Distribution: \[8K,16K)(%)                      | Percentage of read I/Os with size in \[8K,16K).                                                           |
| Read I/O Granularity Distribution: \[16K,32K)(%)                     | Percentage of read I/Os with size in \[16K,32K).                                                          |
| Read I/O Granularity Distribution: \[32K,64K)(%)                     | Percentage of read I/Os with size in \[32K,64K).                                                          |
| Read I/O Granularity Distribution: \[64K,128K)(%)                    | Percentage of read I/Os with size in \[64K,128K).                                                         |
| Read I/O Granularity Distribution: \[128K,256K)(%)                   | Percentage of read I/Os with size in \[128K,256K).                                                        |
| Write I/O Granularity Distribution: \[1K,2K)(%)                      | Percentage of write I/Os with size in \[1K,2K).                                                           |
| Write I/O Granularity Distribution: \[2K,4K)(%)                      | Percentage of write I/Os with size in \[2K,4K).                                                           |
| Write I/O Granularity Distribution: \[4K,8K)(%)                      | Percentage of write I/Os with size in \[4K,8K).                                                           |
| Write I/O Granularity Distribution: \[8K,16K)(%)                     | Percentage of write I/Os with size in \[8K,16K).                                                          |
| Write I/O Granularity Distribution: \[16K,32K)(%)                    | Percentage of write I/Os with size in \[16K,32K).                                                         |
| Write I/O Granularity Distribution: \[32K,64K)(%)                    | Percentage of write I/Os with size in \[32K,64K).                                                         |
| Write I/O Granularity Distribution: \[64K,128K)(%)                   | Percentage of write I/Os with size in \[64K,128K).                                                        |
| Write I/O Granularity Distribution: \[128K,256K)(%)                  | Percentage of write I/Os with size in \[128K,256K).                                                       |
| OPS(per second)                                                      | Operations per second (OPS).                                                                              |
| Read I/O Latency Distribution: \[0ms,10ms)(%)                        | Percentage of read I/Os with latency in \[0ms,10ms).                                                      |
| Read I/O Latency Distribution: \[10ms,20ms)(%)                       | Percentage of read I/Os with latency in \[10ms,20ms).                                                     |
| Read I/O Latency Distribution: \[20ms,50ms)(%)                       | Percentage of read I/Os with latency in \[20ms,50ms).                                                     |
| Read I/O Latency Distribution: \[50ms,100ms)(%)                      | Percentage of read I/Os with latency in \[50ms,100ms).                                                    |
| Read I/O Latency Distribution: \[100ms,200ms)(%)                     | Percentage of read I/Os with latency in \[100ms,200ms).                                                   |
| Read I/O Latency Distribution: \>=200ms(%)                           | Percentage of read I/Os with latency greater than or equal to 200 ms.                                     |
| Write I/O Latency Distribution: \[0ms,10ms)(%)                       | Percentage of write I/Os with latency in \[0ms,10ms).                                                     |
| Write I/O Latency Distribution: \[10ms,20ms)(%)                      | Percentage of write I/Os with latency in \[10ms,20ms).                                                    |
| Write I/O Latency Distribution: \[20ms,50ms)(%)                      | Percentage of write I/Os with latency in \[20ms,50ms).                                                    |
| Write I/O Latency Distribution: \[50ms,100ms)(%)                     | Percentage of write I/Os with latency in \[50ms,100ms).                                                   |
| Write I/O Latency Distribution: \[100ms,200ms)(%)                    | Percentage of write I/Os with latency in \[100ms,200ms).                                                  |
| Write I/O Latency Distribution: \>=200ms(%)                          | Percentage of write I/Os with latency greater than or equal to 200 ms.                                    |
| Average Latency For Operations(ms)                                   | Average latency for operations (ms).                                                                      |
| Max Latency For Operations(ms)                                       | Maximum latency for operations (ms).                                                                      |
| Throughput(Bps)                                                      | Throughput (bps).                                                                                         |
| Read I/O Granularity Distribution: \[0K,512B)(%)                     | Percentage of read I/Os with size in \[0K,512B).                                                          |
| Read I/O Granularity Distribution: \[512B,1K)(%)                     | Percentage of read I/Os with size in \[512B,1K).                                                          |
| Read I/O Granularity Distribution: \>= 256K(%)                       | Percentage of read I/Os with latency greater than or equal to 256 KB.                                     |
| Write I/O Granularity Distribution: \[0K,512B)(%)                    | Percentage of write I/Os with size in \[0K,512B).                                                         |
| Write I/O Granularity Distribution: \[512B,1K)(%)                    | Percentage of write I/Os with size in \[512B,1K).                                                         |
| Write I/O Granularity Distribution: \>= 256K(%)                      | Percentage of write I/Os with latency greater than or equal to 256 KB.                                    |
| Min Latency For Operations(ms)                                       | Minimum latency for operations (ms).                                                                      |
| Average Latency For Operations(ms, accurate to three decimal places) | Average latency for operations (ms, accurate to three decimal places).                                    |
| Max Latency For Operations(ms, accurate to three decimal places)     | Maximum latency for operations (ms, accurate to three decimal places).                                    |
| Min Latency For Operations(ms, accurate to three decimal places)     | Minimum latency for operations (ms, accurate to three decimal places).                                    |
| Throughput(MB/s)                                                     | Throughput (MB/s).                                                                                        |
| Read bandwidth (MB/s)                                                | Read request data amount processed by a module per second.                                                |
| Write bandwidth (MB/s)                                               | Read request data amount processed by a module per second.                                                |
| Read OPS (per second)                                                | Read OPS of a specific file system (including forwarding ends).                                           |
| Write OPS (per second)                                               | Write OPS of a specific file system (including forwarding ends).                                          |
| File Bandwidth                                                       | Data amount of I/Os per second in a specific file system.                                                 |
| Average response time of other CIFS I/Os (us)                        | Average time of responding to CIFS non-read or write requests from clients.                               |
| Average Read OPS Response Time (us)                                  | Average response latency of all read operations in the specific file system (including forwarding ends).  |
| Average Write OPS Response Time (us)                                 | Average response latency of all write operations in the specific file system (including forwarding ends). |
| Other CIFS OPS                                                       | Number of CIFS non-read or write operations processed per second.                                         |
| Total CIFS create OPS                                                | Number of CIFS create operations processed per second.                                                    |
| Total CIFS queryinfo OPS                                             | Number of CIFS queryinfo operations per second.                                                           |
| Total CIFS querydir OPS                                              | Number of CIFS querydir operations per second.                                                            |
| Total CIFS setinfo OPS                                               | Number of CIFS setinfo operations per second.                                                             |
| Average CIFS create response time (us)                               | Average CIFS create response time (us).                                                                   |
| Average CIFS queryinfo response time (us)                            | Average CIFS queryinfo response time (us).                                                                |
| Average CIFS querydir response time (us)                             | Average CIFS querydir response time (us).                                                                 |
| Average CIFS setinfo response time (us)                              | Average CIFS setinfo response time (us).                                                                  |
| Read I/O Latency Distribution: \[200ms,1s)(%)                        | Percentage of read I/Os with latency in \[200ms,1s).                                                      |
| Read I/O Latency Distribution: \[1s,3s)(%)                           | Percentage of read I/Os with latency in \[1s,3s).                                                         |
| Read I/O Latency Distribution: \[3s,5s)(%)                           | Percentage of read I/Os with latency in \[3s,5s).                                                         |
| Read I/O Latency Distribution: \[5s,8s)(%)                           | Percentage of read I/Os with latency in \[5s,8s).                                                         |
| Read I/O Latency Distribution: \>= 8s(%)                             | Percentage of read I/Os with latency greater than or equal to 8s.                                         |
| Write I/O Latency Distribution: \[200ms,1s)(%)                       | Percentage of write I/Os with latency in \[200ms,1s).                                                     |
| Write I/O Latency Distribution: \[1s,3s)(%)                          | Percentage of write I/Os with latency in \[1s,3s).                                                        |
| Write I/O Latency Distribution: \[3s,5s)(%)                          | Percentage of write I/Os with latency in \[3s,5s).                                                        |
| Write I/O Latency Distribution: \[5s,8s)(%)                          | Percentage of write I/Os with latency in \[5s,8s).                                                        |
| Write I/O Latency Distribution: \>= 8s(%)                            | Percentage of write I/Os with latency greater than or equal to 8s.                                        |
| Average Read I/O Size(KB)                                            | Average read I/O size (KB).                                                                               |
| Average IO Size                                                      | Average I/O size.                                                                                         |
| Average Write I/O Size(KB)                                           | Average write I/O size (KB).                                                                              |
