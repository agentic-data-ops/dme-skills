# show performance nfsv41


##### Function

The show performance nfsv4 command is used to query the performance statistics of NFSv4. When you need to analyze the performance statistics of NFSv4 in real time, run this command.

##### Format

**show performance nfsv41** controller_id=?

**show performance nfsv41** controller_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller_id=? | Controller ID. | You can run the show controller general command to query the value of this parameter. |
| controller_id_list=? | Controller ID list. | You can run the show controller general command to obtain the value.<br>Separate multiple controller IDs with commas (,). Example: 0A,1B. |

##### Usage Guidelines

-   After the command is executed, the system prompts you to select the performance data type. Enter the sequence number (multiple choices are separated by commas) and press Enter to view the performance data of the corresponding type.

-   The performance statistics are refreshed in real-time.

3.Press q to exit the performance data display.

-   Parameters controller_id and controller_id_list are mutually exclusive.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Show the NFSv41 performance statistics of controller "1A".

```text
admin:/>show performance nfsv41 controller_id=1A
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
63.Total NFS readlink OPS
64.Total NFS symlink OPS
65.Total NFS rename OPS
66.Total NFS link OPS
67.Total NFS fsstat OPS
68.Average NFS Lookup response time (us)
69.Average NFS Create response time (us)
70.Average NFS Remove response time (us)
71.Average NFS GetAttr response time (us)
72.Average NFS SetAttr response time (us)
73.Average NFS mkdir response time (us)
74.Average NFS rmdir response time (us)
75.Average NFS readdir response time (us)
76.Average NFS access response time (us)
77.Average NFS readdir plus response time (us)
78.Avg. NFS readlink response time(us)
79.Avg. NFS symlink response time(us)
80.Avg. NFS rename response time(us)
81.Avg. NFS link response time(us)
82.Avg. NFS fsstat response time(us)
83.Average NFS open response time (us)
84.Read I/O Latency Distribution: [200ms,1s)(%)
85.Read I/O Latency Distribution: [1s,3s)(%)
86.Read I/O Latency Distribution: [3s,5s)(%)
87.Read I/O Latency Distribution: [5s,8s)(%)
88.Read I/O Latency Distribution: >= 8s(%)
89.Write I/O Latency Distribution: [200ms,1s)(%)
90.Write I/O Latency Distribution: [1s,3s)(%)
91.Write I/O Latency Distribution: [3s,5s)(%)
92.Write I/O Latency Distribution: [5s,8s)(%)
93.Write I/O Latency Distribution: >= 8s(%)
94.Average Read I/O Size(KB)
95.Average Write I/O Size(KB)
96.Average IO Size(KB)
97.Compound OPS(per second)
98.Average NFS compound response time(us)
Input item(s) number separated by comma:6,8
Read I/O Granularity Distribution: [64K,128K)(%) : 0
Write I/O Granularity Distribution: [1K,2K)(%)   : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                                            | Meaning                                                                      |
|----------------------------------------------------------------------|------------------------------------------------------------------------------|
| Read I/O Granularity Distribution: \[1K,2K)(%)                       | Percentage of the read I/O granularity in \[1 KB, 2 KB).                     |
| Read I/O Granularity Distribution: \[2K,4K)(%)                       | Percentage of the read I/O granularity in \[2 KB, 4 KB).                     |
| Read I/O Granularity Distribution: \[4K,8K)(%)                       | Percentage of the read I/O granularity in \[4 KB, 8 KB).                     |
| Read I/O Granularity Distribution: \[8K,16K)(%)                      | Percentage of the read I/O granularity in \[8 KB, 16 KB).                    |
| Read I/O Granularity Distribution: \[16K,32K)(%)                     | Percentage of the read I/O granularity in \[16 KB, 32 KB).                   |
| Read I/O Granularity Distribution: \[32K,64K)(%)                     | Percentage of the read I/O granularity in \[32 KB, 64 KB).                   |
| Read I/O Granularity Distribution: \[64K,128K)(%)                    | Percentage of the read I/O granularity in \[64 KB, 128 KB).                  |
| Read I/O Granularity Distribution: \[128K,256K)(%)                   | Percentage of the read I/O granularity in \[128 KB, 256 KB).                 |
| Write I/O Granularity Distribution: \[1K,2K)(%)                      | Percentage of the write I/O granularity in \[1 KB, 2 KB).                    |
| Write I/O Granularity Distribution: \[2K,4K)(%)                      | Percentage of the write I/O granularity in \[2 KB, 4 KB).                    |
| Write I/O Granularity Distribution: \[4K,8K)(%)                      | Percentage of the write I/O granularity in \[4 KB, 8 KB).                    |
| Write I/O Granularity Distribution: \[8K,16K)(%)                     | Percentage of the write I/O granularity in \[8 KB, 16 KB).                   |
| Write I/O Granularity Distribution: \[16K,32K)(%)                    | Percentage of the write I/O granularity in \[16 KB, 32 KB).                  |
| Write I/O Granularity Distribution: \[32K,64K)(%)                    | Percentage of the write I/O granularity in \[32 KB, 64 KB).                  |
| Write I/O Granularity Distribution: \[64K,128K)(%)                   | Percentage of the write I/O granularity in \[64 KB, 128 KB).                 |
| Write I/O Granularity Distribution: \[128K,256K)(%)                  | Percentage of the write I/O granularity in \[128 KB, 256 KB).                |
| OPS(per second)                                                      | Number of operations per second.                                             |
| Read I/O Latency Distribution: \[0ms,10ms)(%)                        | Percentage of the read I/O latency within \[0 ms, 10 ms).                    |
| Read I/O Latency Distribution: \[10ms,20ms)(%)                       | Percentage of the read I/O latency within \[10 ms, 20 ms).                   |
| Read I/O Latency Distribution: \[20ms,50ms)(%)                       | Percentage of the read I/O latency within \[20 ms, 50 ms).                   |
| Read I/O Latency Distribution: \[50ms,100ms)(%)                      | Percentage of the read I/O latency between 50 ms and 100 ms.                 |
| Read I/O Latency Distribution: \[100ms,200ms)(%)                     | Percentage of the read I/O latency between 100 ms and 200 ms.                |
| Read I/O Latency Distribution: \>= 200ms(%)                          | Percentage of the read I/O latency greater than 200 ms.                      |
| Write I/O Latency Distribution: \[0ms,10ms)(%)                       | Percentage of the write I/O latency within \[0 ms, 10 ms).                   |
| Write I/O Latency Distribution: \[10ms,20ms)(%)                      | Percentage of the write I/O latency within \[10 ms, 20 ms).                  |
| Write I/O Latency Distribution: \[100ms,200ms)(%)                    | Percentage of the write I/O latency between 100 ms and 200 ms.               |
| Write I/O Latency Distribution: \[20ms,50ms)(%)                      | Percentage of the write I/O latency within \[20 ms, 50 ms).                  |
| Write I/O Latency Distribution: \[50ms,100ms)(%)                     | Percentage of the write I/O latency within \[50 ms, 100 ms).                 |
| Write I/O Latency Distribution: \>= 200ms(%)                         | Percentage of write I/O latency greater than or equal to 200 ms.             |
| Average Latency For Operations(ms)                                   | Average operation delay (ms).                                                |
| Max Latency For Operations(ms)                                       | Maximum operation delay (ms).                                                |
| Throughput(Bps)                                                      | Throughput (bit/s)                                                           |
| Read I/O Granularity Distribution: \[0K,512B)(%)                     | Percentage of the read I/O granularity in \[0 KB, 512 bytes).                |
| Read I/O Granularity Distribution: \[512B,1K)(%)                     | Percentage of the read I/O granularity in \[512 B, 1 KB).                    |
| Read I/O Granularity Distribution: \>= 256K(%)                       | Percentage of read I/Os whose granularity is greater than 256 KB.            |
| Write I/O Granularity Distribution: \[0K,512B)(%)                    | Percentage of the write I/O granularity in \[0 KB, 512 bytes).               |
| Write I/O Granularity Distribution: \[512B,1K)(%)                    | Percentage of the write I/O granularity in \[512 B, 1 KB).                   |
| Write I/O Granularity Distribution: \>= 256K(%)                      | Percentage of write I/Os whose granularity is greater than 256 KB.           |
| Min Latency For Operations(ms)                                       | Minimum operation delay (ms).                                                |
| Average Latency For Operations(ms, accurate to three decimal places) | Average operation delay, in milliseconds, accurate to three decimal places.  |
| Max Latency For Operations(ms, accurate to three decimal places)     | Maximum operation delay, in milliseconds, accurate to three decimal places.  |
| Min Latency For Operations(ms, accurate to three decimal places)     | Minimum operation delay, in milliseconds, accurate to three decimal places.  |
| Throughput(MB/s)                                                     | Throughput (MB/s)                                                            |
| Total NFS getattr OPS                                                | Number of NFS getattr operations processed per second.                       |
| Total NFS lookup OPS                                                 | Number of NFS lookup operations processed per second.                        |
| Total NFS create OPS                                                 | Number of NFS create operations processed per second.                        |
| Total NFS remove OPS                                                 | Number of NFS remove operations processed per second.                        |
| Total NFS setattr OPS                                                | Number of NFS setattr operations processed per second.                       |
| Total NFS mkdir OPS                                                  | Number of NFS mkdir operations processed per second.                         |
| Total NFS rmdir OPS                                                  | Number of NFS RMdir operations processed per second.                         |
| Total NFS access OPS                                                 | Number of NFS access operations processed per second.                        |
| Total NFS readdir OPS                                                | Number of NFS readdir operations processed per second.                       |
| Total NFS readlink OPS                                               | Number of NFS readlink operations processed per second.                      |
| Total NFS readdir plus OPS                                           | Number of NFS readdir plus operations processed per second.                  |
| Total NFS open OPS                                                   | Number of NFS open operations processed per second.                          |
| Average NFS Lookup response time (us)                                | Average time taken for NFS protocol lookup requests.                         |
| Average NFS Create response time (us)                                | Average time required for creating requests for NFS.                         |
| Average NFS Remove response time (us)                                | The average time taken for the NFS protocol to remove requests.              |
| Average NFS GetAttr response time (us)                               | Average time required for NFS getattr requests.                              |
| Average NFS SetAttr response time (us)                               | Average time required for NFS setattr requests.                              |
| Average NFS mkdir response time (us)                                 | Average time required for NFS protocol mkdir requests.                       |
| Average NFS rmdir response time (us)                                 | Average time required for NFS rmdir requests.                                |
| Average NFS readdir response time (us)                               | Average time required for NFS readdir requests.                              |
| Average NFS access response time (us)                                | Average time required for NFS access requests.                               |
| Average NFS readdir plus response time (us)                          | Average time required for NFS readdir plus requests.                         |
| Average NFS open response time (us)                                  | Average time required for NFS protocol open requests.                        |
| Read I/O Latency Distribution: \[200ms,1s)(%)                        | Percentage of the read I/O latency within \[200 ms, 1s).                     |
| Read I/O Latency Distribution: \[1s,3s)(%)                           | Percentage of the read I/O latency within \[1s, 3s).                         |
| Read I/O Latency Distribution: \[3s,5s)(%)                           | Percentage of the read I/O latency within \[3s, 5s).                         |
| Read I/O Latency Distribution: \[5s,8s)(%)                           | Percentage of the read I/O latency within \[5s, 8s).                         |
| Read I/O Latency Distribution: \>= 8s(%)                             | Percentage of read I/O latency greater than or equal to 8s.                  |
| Write I/O Latency Distribution: \[200ms,1s)(%)                       | Percentage of the write I/O latency within \[200 ms, 1s).                    |
| Write I/O Latency Distribution: \[1s,3s)(%)                          | Percentage of the write I/O latency within \[1s, 3s).                        |
| Write I/O Latency Distribution: \[3s,5s)(%)                          | Percentage of the write I/O latency within \[3s, 5s).                        |
| Write I/O Latency Distribution: \[5s,8s)(%)                          | Percentage of the write I/O latency within \[5s, 8s).                        |
| Write I/O Latency Distribution: \>= 8s(%)                            | Percentage of write I/O latency greater than or equal to 8s.                 |
| Average Read I/O Size(KB)                                            | Average read I/O size (KB).                                                  |
| Average Write I/O Size(KB)                                           | Average write I/O size (KB).                                                 |
| Average IO Size                                                      | Average I/O size.                                                            |
| Total NFS symlink OPS                                                | Number of NFS symlink operations processed per second.                       |
| Total NFS rename OPS                                                 | Number of NFS rename operations processed per second.                        |
| Total NFS link OPS                                                   | Number of NFS link operations processed per second.                          |
| Total NFS fsstat OPS                                                 | Number of NFS fsstat operations processed per second.                        |
| Avg. NFS readlink response time(us)                                  | Average time required for NFS readlink requests.                             |
| Avg. NFS symlink response time(us)                                   | Average time required for NFS protocol symlink requests.                     |
| Avg. NFS rename response time(us)                                    | Average time taken for NFS protocol rename requests.                         |
| Avg. NFS link response time(us)                                      | Average time required for NFS link requests.                                 |
| Avg. NFS fsstat response time(us)                                    | Average time required for NFS protocol fsstat requests.                      |
| Compound OPS(per second)                                             | Number of compound requests processed by a controller per second.            |
| Average NFS compound response time(us)                               | Average time required for processing a compound request of the NFS protocol. |
