# show performance nfsv3


##### Function

The **show performance nfsv3** command is used to query the performance statistics for NFSv3. Run this command to analyze the performance statistics for NFSv3 in real time.

##### Format

**show performance nfsv3** controller_id=?

**show performance nfsv3** controller_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller_id=? | ID of a controller. | To obtain the value, run "show controller general". |
| controller_id_list=? | ID list of controllers. | To obtain the value, run "show controller general".<br>Separate the controller IDs with commas (,), such as "0A,1B". |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.
-   "controller_id" is mutually exclusive with "controller_id_list".

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the NFSv3 performance statistics of controller "1A".

```text
admin:/>show performance nfsv3 controller_id=1A
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
50.Other OPS For NFS
51.Other IO Average Response Time For NFS(us)
52.Total NFS lookup OPS
53.Total NFS create OPS
54.Total NFS remove OPS
55.Total NFS getattr OPS
56.Total NFS setattr OPS
57.Total NFS mkdir OPS
58.Total NFS rmdir OPS
59.Total NFS access OPS
60.Total NFS readdir OPS
61.Total NFS readdir plus OPS
62.Total NFS open OPS
63.Average NFS Lookup response time (us)
64.Average NFS Create response time (us)
65.Average NFS Remove response time (us)
66.Average NFS GetAttr response time (us)
67.Average NFS SetAttr response time (us)
68.Average NFS mkdir response time (us)
69.Average NFS rmdir response time (us)
70.Average NFS readdir response time (us)
71.Average NFS access response time (us)
72.Average NFS readdir plus response time (us)
73.Average NFS open response time (us)
74.Read I/O Latency Distribution: [200ms,1s)(%)
75.Read I/O Latency Distribution: [1s,3s)(%)
76.Read I/O Latency Distribution: [3s,5s)(%)
77.Read I/O Latency Distribution: [5s,8s)(%)
78.Read I/O Latency Distribution: >= 8s(%)
79.Write I/O Latency Distribution: [200ms,1s)(%)
80.Write I/O Latency Distribution: [1s,3s)(%)
81.Write I/O Latency Distribution: [3s,5s)(%)
82.Write I/O Latency Distribution: [5s,8s)(%)
83.Write I/O Latency Distribution: >= 8s(%)
84.Average Read I/O Size(KB)
85.Average Write I/O Size(KB)
86.Average IO Size(KB)
87.Total NFS readlink OPS
88.Total NFS symlink OPS
89.Total NFS rename OPS
90.Total NFS link OPS
91.Total NFS fsstat OPS
92.Avg. NFS readlink response time(us)
93.Avg. NFS symlink response time(us)
94.Avg. NFS rename response time(us)
95.Avg. NFS link response time(us)
96.Avg. NFS fsstat response time(us)
Input item(s) number separated by comma:6,8
Read I/O Granularity Distribution: [64K,128K)(%) : 0
Write I/O Granularity Distribution: [1K,2K)(%) : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                                            | Meaning                                                                |
|----------------------------------------------------------------------|------------------------------------------------------------------------|
| Read I/O Granularity Distribution: \[1K,2K)(%)                       | Percentage of read I/Os with size in \[1K,2K).                         |
| Read I/O Granularity Distribution: \[2K,4K)(%)                       | Percentage of read I/Os with size in \[2K,4K).                         |
| Read I/O Granularity Distribution: \[4K,8K)(%)                       | Percentage of read I/Os with size in \[4K,8K).                         |
| Read I/O Granularity Distribution: \[8K,16K)(%)                      | Percentage of read I/Os with size in \[8K,16K).                        |
| Read I/O Granularity Distribution: \[16K,32K)(%)                     | Percentage of read I/Os with size in \[16K,32K).                       |
| Read I/O Granularity Distribution: \[32K,64K)(%)                     | Percentage of read I/Os with size in \[32K,64K).                       |
| Read I/O Granularity Distribution: \[64K,128K)(%)                    | Percentage of read I/Os with size in \[64K,128K).                      |
| Read I/O Granularity Distribution: \[128K,256K)(%)                   | Percentage of read I/Os with size in \[128K,256K).                     |
| Write I/O Granularity Distribution: \[1K,2K)(%)                      | Percentage of write I/Os with size in \[1K,2K).                        |
| Write I/O Granularity Distribution: \[2K,4K)(%)                      | Percentage of write I/Os with size in \[2K,4K).                        |
| Write I/O Granularity Distribution: \[4K,8K)(%)                      | Percentage of write I/Os with size in \[4K,8K).                        |
| Write I/O Granularity Distribution: \[8K,16K)(%)                     | Percentage of write I/Os with size in \[8K,16K).                       |
| Write I/O Granularity Distribution: \[16K,32K)(%)                    | Percentage of write I/Os with size in \[16K,32K).                      |
| Write I/O Granularity Distribution: \[32K,64K)(%)                    | Percentage of write I/Os with size in \[32K,64K).                      |
| Write I/O Granularity Distribution: \[64K,128K)(%)                   | Percentage of write I/Os with size in \[64K,128K).                     |
| Write I/O Granularity Distribution: \[128K,256K)(%)                  | Percentage of write I/Os with size in \[128K,256K).                    |
| OPS(per second)                                                      | Operations per second (OPS).                                           |
| Read I/O Latency Distribution: \[0ms,10ms)(%)                        | Percentage of read I/Os with latency in \[0ms,10ms).                   |
| Read I/O Latency Distribution: \[10ms,20ms)(%)                       | Percentage of read I/Os with latency in \[10ms,20ms).                  |
| Read I/O Latency Distribution: \[20ms,50ms)(%)                       | Percentage of read I/Os with latency in \[20ms,50ms).                  |
| Read I/O Latency Distribution: \[50ms,100ms)(%)                      | Percentage of read I/Os with latency in \[50ms,100ms).                 |
| Read I/O Latency Distribution: \[100ms,200ms)(%)                     | Percentage of read I/Os with latency in \[100ms,200ms).                |
| Read I/O Latency Distribution: \>= 200ms(%)                          | Percentage of read I/Os with latency greater than or equal to 200 ms.  |
| Write I/O Latency Distribution: \[0ms,10ms)(%)                       | Percentage of write I/Os with latency in \[0ms,10ms).                  |
| Write I/O Latency Distribution: \[10ms,20ms)(%)                      | Percentage of write I/Os with latency in \[10ms,20ms).                 |
| Write I/O Latency Distribution: \[20ms,50ms)(%)                      | Percentage of write I/Os with latency in \[20ms,50ms).                 |
| Write I/O Latency Distribution: \[50ms,100ms)(%)                     | Percentage of write I/Os with latency in \[50ms,100ms).                |
| Write I/O Latency Distribution: \[100ms,200ms)(%)                    | Percentage of write I/Os with latency in \[100ms,200ms).               |
| Write I/O Latency Distribution: \>= 200ms(%)                         | Percentage of write I/Os with latency greater than or equal to 200 ms. |
| Average Latency For Operations(ms)                                   | Average latency for operations (ms).                                   |
| Max Latency For Operations(ms)                                       | Maximum latency for operations (ms).                                   |
| Throughput(Bps)                                                      | Throughput (Bps).                                                      |
| Read I/O Granularity Distribution: \[0K,512B)(%)                     | Percentage of read I/Os with size in \[0K,512B).                       |
| Read I/O Granularity Distribution: \[512B,1K)(%)                     | Percentage of read I/Os with size in \[512B,1K).                       |
| Read I/O Granularity Distribution: \>= 256K(%)                       | Percentage of read I/Os with latency greater than or equal to 256 KB.  |
| Write I/O Granularity Distribution: \[0K,512B)(%)                    | Percentage of write I/Os with size in \[0K,512B).                      |
| Write I/O Granularity Distribution: \[512B,1K)(%)                    | Percentage of write I/Os with size in \[512B,1K).                      |
| Write I/O Granularity Distribution: \>= 256K(%)                      | Percentage of write I/Os with latency greater than or equal to 256 KB. |
| Min Latency For Operations(ms)                                       | Minimum latency for operations (ms).                                   |
| Average Latency For Operations(ms, accurate to three decimal places) | Average latency for operations (ms, accurate to three decimal places). |
| Max Latency For Operations(ms, accurate to three decimal places)     | Maximum latency for operations (ms, accurate to three decimal places). |
| Min Latency For Operations(ms, accurate to three decimal places)     | Minimum latency for operations (ms, accurate to three decimal places). |
| Throughput(MB/s)                                                     | Throughput (MB/s).                                                     |
| Total NFS getattr OPS                                                | Number of NFS getattr operations processed per second.                 |
| Total NFS lookup OPS                                                 | Number of NFS lookup operations processed per second.                  |
| Total NFS create OPS                                                 | Number of NFS create operations processed per second.                  |
| Total NFS remove OPS                                                 | Number of NFS remove operations processed per second.                  |
| Total NFS setattr OPS                                                | Number of NFS setattr operations processed per second.                 |
| Total NFS mkdir OPS                                                  | Number of NFS mkdir operations processed per second.                   |
| Total NFS rmdir OPS                                                  | Number of NFS rmdir operations processed per second.                   |
| Total NFS access OPS                                                 | Number of NFS access operations processed per second.                  |
| Total NFS readdir OPS                                                | Number of NFS readdir operations processed per second.                 |
| Total NFS readlink OPS                                               | Number of NFS readlink operations per second.                          |
| Total NFS readdir plus OPS                                           | Number of NFS readdir plus operations processed per second.            |
| Total NFS open OPS                                                   | Number of NFS open operations processed per second.                    |
| Average NFS Lookup response time (us)                                | Average NFS lookup response time.                                      |
| Average NFS Create response time (us)                                | Average NFS create response time.                                      |
| Average NFS Remove response time (us)                                | Average NFS remove response time.                                      |
| Average NFS GetAttr response time (us)                               | Average NFS getattr response time.                                     |
| Average NFS SetAttr response time (us)                               | Average NFS setattr response time.                                     |
| Average NFS mkdir response time (us)                                 | Average NFS mkdir response time.                                       |
| Average NFS rmdir response time (us)                                 | Average NFS rmdir response time.                                       |
| Average NFS readdir response time (us)                               | Average NFS readdir response time.                                     |
| Average NFS access response time (us)                                | Average NFS access response time.                                      |
| Average NFS readdir plus response time (us)                          | Average NFS readdir plus response time.                                |
| Average NFS open response time (us)                                  | Average NFS open response time.                                        |
| Read I/O Latency Distribution: \[200ms,1s)(%)                        | Percentage of read I/Os with latency in \[200ms,1s).                   |
| Read I/O Latency Distribution: \[1s,3s)(%)                           | Percentage of read I/Os with latency in \[1s,3s).                      |
| Read I/O Latency Distribution: \[3s,5s)(%)                           | Percentage of read I/Os with latency in \[3s,5s).                      |
| Read I/O Latency Distribution: \[5s,8s)(%)                           | Percentage of read I/Os with latency in \[5s,8s).                      |
| Read I/O Latency Distribution: \>= 8s(%)                             | Percentage of read I/Os with latency greater than or equal to 8s.      |
| Write I/O Latency Distribution: \[200ms,1s)(%)                       | Percentage of write I/Os with latency in \[200ms,1s).                  |
| Write I/O Latency Distribution: \[1s,3s)(%)                          | Percentage of write I/Os with latency in \[1s,3s).                     |
| Write I/O Latency Distribution: \[3s,5s)(%)                          | Percentage of write I/Os with latency in \[3s,5s).                     |
| Write I/O Latency Distribution: \[5s,8s)(%)                          | Percentage of write I/Os with latency in \[5s,8s).                     |
| Write I/O Latency Distribution: \>= 8s(%)                            | Percentage of write I/Os with latency greater than or equal to 8s.     |
| Average Read I/O Size(KB)                                            | Average read I/O size (KB).                                            |
| Average Write I/O Size(KB)                                           | Average write I/O size (KB).                                           |
| Average IO Size                                                      | Average I/O size.                                                      |
| Total NFS symlink OPS                                                | Number of NFS symlink operations per second.                           |
| Total NFS rename OPS                                                 | Number of NFS rename operations per second.                            |
| Total NFS link OPS                                                   | Number of NFS link operations per second.                              |
| Total NFS fsstat OPS                                                 | Number of NFS fsstat operations per second.                            |
| Avg. NFS readlink response time(us)                                  | Avg. NFS readlink response time (us).                                  |
| Avg. NFS symlink response time(us)                                   | Avg. NFS symlink response time (us).                                   |
| Avg. NFS rename response time(us)                                    | Avg. NFS rename response time (us).                                    |
| Avg. NFS link response time(us)                                      | Avg. NFS link response time (us).                                      |
| Avg. NFS fsstat response time(us)                                    | Avg. NFS fsstat response time (us).                                    |
