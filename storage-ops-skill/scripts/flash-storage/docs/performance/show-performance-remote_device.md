# show performance remote_device


##### Function

The **show performance remote_device** command is used to query the real-time performance statistics on a remote device.

##### Format

**show performance remote_device** remote_device_id=?

**show performance remote_device** remote_device_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_device_id=? | ID of a remote device on which you want to query performance statistics. | To obtain the value, run "show remote_device general". |
| remote_device_id_list=? | ID list of remote devices on which you want to query performance statistics. | To obtain the value, run "show remote_device general".<br>Separate the link IDs with commas (,) or hyphens (-).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" display the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the performance statistics on the read I/Os for a remote device whose ID is "0".

```text
admin:/>show performance remote_device remote_device_id=0
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

| Parameter                                          | Meaning                                                                               |
|----------------------------------------------------|---------------------------------------------------------------------------------------|
| Queue Length                                       | Specifies the queue length of a remote device.                                        |
| Average Read I/O Size(KB)                          | Average read I/O size (KB) of a specified remote device.                              |
| The cumulative count of data written in Kbytes     | Specifies the accumulated count of data written to a remote device in the unit of KB. |
| The cumulative count of all writes                 | Specifies the accumulated count of all writes on the remote device.                   |
| The cumulative count of data transferred in Kbytes | Specifies the accumulated count of data transmitted in KB on the remote device.       |
| The cumulative count of I/Os                       | Count of I/Os sent by a specified remote device.                                      |
| Receiving bandwidth for replication(KB/s)          | Specifies the receive bandwidth (KB/s) of the remote device.                          |
| Sending bandwidth for replication(KB/s)            | Specifies the transmit bandwidth (KB/s) of the remote device.                         |
| Total Bandwidth(KB/s)                              | Specifies the total bandwidth (KB/s) of the remote device.                            |
| Bandwidth(MB/s)                                    | Specifies the bandwidth (MB/s) of the remote device.                                  |
| Max. Bandwidth(MB/s)                               | Specifies the maximum bandwidth (MB/s) of the remote device.                          |
| Average Write I/O Latency(us)                      | Average write I/O latency (us) of a specified remote device.                          |
| Average Read I/O Latency(us)                       | Average read I/O latency of a specified remote device (us).                           |
| Max. I/O Latency(us)                               | Specifies the maximum I/O latency (us) of the remote device.                          |
| Average I/O Latency(us)                            | Average I/O latency (us) of a specified remote device.                                |
| Failed IO Ratio(%)                                 | I/O failure rate (%) of a specified remote device.                                    |
| Failed IOs/sec                                     | Number of failed I/Os on the link of a specified remote device per second (I/O/s).    |
| Failed IOs                                         | Total number of I/Os that fail to be executed on a specified remote device.           |
| Max IOPS(IO/s)                                     | Specifies the maximum IOPS (IO/s) of the remote device.                               |
| % Write                                            | Percentage of write I/Os to the total write I/Os on the remote device.                |
| % Read                                             | Percentage of read I/Os on a remote device.                                           |
| Average IO Size(KB)                                | Average I/O size (KB) of a specified remote device.                                   |
| Write Bandwidth(MB/s)                              | Specifies the write bandwidth (KB/s) of the remote device.                            |
| Read Bandwidth(MB/s)                               | Specifies the read bandwidth (KB/s) of the remote device.                             |
| Service Time(Excluding Queue Time)(ms)             | Service Time (ms).                                                                    |
| Write Throughput(IOPS)(IO/s)                       | Read I/O throughput (I/O/S) of a specified remote device.                             |
| Average Write I/O Size(KB)                         | Average write I/O size (KB) of a specified remote device.                             |
| Read Throughput(IOPS)(IO/s)                        | Read I/O throughput (I/O/S) of a specified remote device.                             |
| Throughput(IOPS)(IO/s)                             | I/O throughput (I/O/S) of a specified remote device.                                  |
