# show performance file_system


##### Function

The **show performance file_system** command is used to query performance statistics of a file system.

##### Format

**show performance file_system** file_system_id=?

**show performance file_system** file_system_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_system_id=? | File system ID. | To obtain the value, run "show file_system general" without parameters. |
| file_system_id_list=? | ID list of file systems. | To obtain the value, run "show file_system general" without any parameters.<br>Separate multiple IDs with commas (,). Consecutive IP addresses can be represented by a hyphen (-).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   After this command is executed, performance data categories are displayed. You need to type the serial numbers before categories and press "Enter" to view the specific categories of performance data (If you need to type multiple categories, use commas to separate them. Consecutive IDs can be represented by a hyphen). 2:Performance statistics is updated in real time. 3:You can type "q" on the command line interface (CLI) to exit the page that shows performance statistics.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query performance statistics of file system "6".

```text
admin:/>show performance file_system file_system_id=6
0.File Bandwidth(MB/s)
1.Read Bandwidth(MB/s)
2.Write Bandwidth(MB/s)
3.OPS(per second)
4.Read OPS(per second)
5.Write OPS(per second)
6.Service time(us)
7.Average Read OPS Response Time (us)
8.Average Write OPS Response Time (us)
9.Cache page preservation(%)
10.Cache chunk preservation(%)
11.File system snapshot capacity usage (%)
12.The cumulative count of file I/O operations for the object,including metadata I/O operations
13.The cumulative count of bytes transferred for all of the file I/O operations as defined in the "TotalIOs" property
14.The cumulative count of file I/O operations that were directed to the object and that performed a transfer of data from the file contents
15.The cumulative count of file I/O operations that were directed to the object and that performed a transfer of data to the file contents
16.The cumulative count of file I/O operations that were directed to the object and that did not perform a transfer of data either to or from the file contents
17.Total NFS lookup OPS
18.Total NFS create OPS
19.Total NFS remove OPS
20.Total NFS getattr OPS
21.Total NFS setattr OPS
22.Total NFS mkdir OPS
23.Total NFS rmdir OPS
24.Total NFS readdir OPS
25.Total NFS access OPS
26.Total NFS readdir plus OPS
27.Total NFS readlink OPS
28.Total NFS symlink OPS
29.Total NFS rename OPS
30.Total NFS link OPS
31.Total NFS fsstat OPS
32.Other OPS For NFS
33.Total CIFS create OPS
34.Total CIFS query info OPS
35.Total CIFS query dir OPS
36.Total CIFS set info OPS
37.Other OPS For SMB
38.Average NFS Lookup response time (us)
39.Average NFS Create response time (us)
40.Average NFS Remove response time (us)
41.Average NFS GetAttr response time (us)
42.Average NFS SetAttr response time (us)
43.Average NFS mkdir response time (us)
44.Average NFS rmdir response time (us)
45.Average NFS access response time (us)
46.Average NFS readdir response time (us)
47.Average NFS readdir plus response time (us)
48.Avg. NFS readlink response time(us)
49.Avg. NFS symlink response time(us)
50.Avg. NFS rename response time(us)
51.Avg. NFS link response time(us)
52.Avg. NFS fsstat response time(us)
53.Other IO Average Response Time For NFS(us)
54.Average CIFS create response time (us)
55.Average CIFS queryinfo response time (us)
56.Average CIFS querydir response time (us)
57.Average CIFS setinfo response time (us)
58.Other IO Average Response Time For SMB(us)
59.Average Read I/O Size(KB)
60.Average Write I/O Size(KB)
61.Average IO Size(KB)
Input item(s) number separated by comma:5
Service time(us) : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                                                                                                                                    | Meaning                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| File Bandwidth(MB/s)                                                                                                                                         | Average I/O data volume of a file system per second.                                                                                        |
| Read Bandwidth(MB/s)                                                                                                                                         | Bandwidth of all read operations in a specified file system (including forwarding ends).                                                    |
| Write Bandwidth(MB/s)                                                                                                                                        | Average data volume of write requests processed by a module per second.                                                                     |
| OPS(per second)                                                                                                                                              | Collect statistics on the OPS of all operations in a specified file system (including forwarding ends).                                     |
| Read OPS(per second)                                                                                                                                         | Collect statistics on the OPS of all read operations in a specified file system (including forwarding ends).                                |
| Write OPS(per second)                                                                                                                                        | Collect statistics on the OPS of all write operations in a specified file system (including forwarding ends).                               |
| Service Time(us)                                                                                                                                             | Average response latency of all operations in a specified file system (including forwarding ends).                                          |
| Average Read OPS Response Time (us)                                                                                                                          | Average response latency of all read operations in a specified file system (including forwarding ends).                                     |
| Average Write OPS Response Time (us)                                                                                                                         | Average response latency of all write operations in a specified file system (including forwarding ends).                                    |
| Cache page preservation(%)                                                                                                                                   | Cache page size of a LUN or file system.                                                                                                    |
| Cache Chunk Preservation(%)                                                                                                                                  | Cache chunk size of a LUN or file system.                                                                                                   |
| File system snapshot capacity usage (%)                                                                                                                      | Snapshot capacity usage of the file system.                                                                                                 |
| The cumulative count of file I/O operations for the object,including metadata I/O operations                                                                 | Cumulative count of file I/O operations on an object, including metadata I/O operations.                                                    |
| The cumulative count of bytes transferred for all of the file I/O operations as defined in the "TotalIOs" property                                           | Accumulated number of bytes transferred by all file I/O operations defined in the "TotalIOs" attribute.                                     |
| The cumulative count of file I/O operations that were directed to the object and that performed a transfer of data from the file contents                    | Cumulative count of file I/O operations that are directed to an object and perform data transfer from the file content.                     |
| The cumulative count of file I/O operations that were directed to the object and that performed a transfer of data to the file contents                      | Cumulative count of file I/O operations that are directed to an object and transfer data to the file content.                               |
| The cumulative count of file I/O operations that were directed to the object and that did not perform a transfer of data either to or from the file contents | Cumulative count of file I/O operations that are directed to an object but have not been performed to or transmitted from the file content. |
| Total NFS lookup OPS                                                                                                                                         | Number of NFS lookup operations processed per second.                                                                                       |
| Total NFS create OPS                                                                                                                                         | Number of NFS create operations processed per second.                                                                                       |
| Total NFS remove OPS                                                                                                                                         | Number of NFS remove operations processed per second.                                                                                       |
| Total NFS getattr OPS                                                                                                                                        | Number of NFS getattr operations processed per second.                                                                                      |
| Total NFS setattr OPS                                                                                                                                        | Number of NFS setattr operations processed per second.                                                                                      |
| Total NFS mkdir OPS                                                                                                                                          | Number of NFS mkdir operations processed per second.                                                                                        |
| Total NFS rmdir OPS                                                                                                                                          | Number of NFS rmdir operations processed per second.                                                                                        |
| Total NFS readdir OPS                                                                                                                                        | Number of NFS readdir operations processed per second.                                                                                      |
| Total NFS access OPS                                                                                                                                         | Number of NFS access operations processed per second.                                                                                       |
| Total NFS readdir plus OPS                                                                                                                                   | Number of NFS readdir plus operations processed per second.                                                                                 |
| Total NFS readlink OPS                                                                                                                                       | Number of NFS readlink operations per second.                                                                                               |
| Total NFS symlink OPS                                                                                                                                        | Number of NFS symlink operations per second.                                                                                                |
| Total NFS rename OPS                                                                                                                                         | Number of NFS rename operations per second.                                                                                                 |
| Total NFS link OPS                                                                                                                                           | Number of NFS link operations per second.                                                                                                   |
| Total NFS fsstat OPS                                                                                                                                         | Number of NFS fsstat operations per second.                                                                                                 |
| Other OPS For NFS                                                                                                                                            | Number of NFS non-read and write operations processed per second.                                                                           |
| Total CIFS create OPS                                                                                                                                        | Number of CIFS create operations processed per second.                                                                                      |
| Total CIFS queryinfo OPS                                                                                                                                     | Number of CIFS query info operations processed per second.                                                                                  |
| Total CIFS querydir OPS                                                                                                                                      | Number of CIFS querydir operations processed per second.                                                                                    |
| Total CIFS setinfo OPS                                                                                                                                       | Number of CIFS setinfo operations processed per second.                                                                                     |
| Other OPS For SMB                                                                                                                                            | Number of CIFS non-read/write operations processed per second.                                                                              |
| Average NFS Lookup response time (us)                                                                                                                        | Average lookup request time of the NFS protocol.                                                                                            |
| Average NFS Create response time (us)                                                                                                                        | Average create request time of the NFS protocol.                                                                                            |
| Average NFS Remove response time (us)                                                                                                                        | Average remove request time of the NFS protocol.                                                                                            |
| Average NFS GetAttr response time (us)                                                                                                                       | Average duration of getattr requests in the NFS protocol.                                                                                   |
| Average NFS SetAttr response time (us)                                                                                                                       | Average setattr request time of the NFS protocol.                                                                                           |
| Average NFS mkdir response time (us)                                                                                                                         | Average mkdir request time of the NFS protocol.                                                                                             |
| Average NFS rmdir response time (us)                                                                                                                         | Average duration of rmdir requests in the NFS protocol.                                                                                     |
| Average NFS access response time (us)                                                                                                                        | Average access request time of the NFS protocol.                                                                                            |
| Average NFS readdir response time (us)                                                                                                                       | Average readdir request time of the NFS protocol.                                                                                           |
| Average NFS readdir plus response time (us)                                                                                                                  | Average readdir plus request time of the NFS protocol.                                                                                      |
| Avg. NFS readlink response time(us)                                                                                                                          | Avg. NFS readlink response time (us).                                                                                                       |
| Avg. NFS symlink response time(us)                                                                                                                           | Avg. NFS symlink response time (us).                                                                                                        |
| Avg. NFS rename response time(us)                                                                                                                            | Avg. NFS rename response time (us).                                                                                                         |
| Avg. NFS link response time(us)                                                                                                                              | Avg. NFS link response time (us).                                                                                                           |
| Avg. NFS fsstat response time(us)                                                                                                                            | Avg. NFS fsstat response time (us).                                                                                                         |
| Other IO Average Response Time For NFS(us)                                                                                                                   | Average time of responding to NFS non-read and write requests from clients.                                                                 |
| Average CIFS create response time (us)                                                                                                                       | Average create request time of the CIFS protocol.                                                                                           |
| Average CIFS queryinfo response time (us)                                                                                                                    | Average time of CIFS queryinfo requests.                                                                                                    |
| Average CIFS querydir response time (us)                                                                                                                     | Average duration of CIFS querydir requests.                                                                                                 |
| Average CIFS setinfo response time (us)                                                                                                                      | Average duration of CIFS setinfo requests.                                                                                                  |
| Other IO Average Response Time For SMB(us)                                                                                                                   | Average time of responding to CIFS non-read and write requests from clients.                                                                |
| Average Read I/O Size(KB)                                                                                                                                    | Average size of read I/Os from the last sampling point in time till now.                                                                    |
| Average Write I/O Size(KB)                                                                                                                                   | Average size of write I/Os from the last sampling point in time till now.                                                                   |
| Average IO Size(KB)                                                                                                                                          | Average I/O size.                                                                                                                           |
