# show performance smartqos_policy


##### Function

The **show performance smartqos_policy** command is used to query the performance statistics of SmartQoS policies.

##### Format

**show performance smartqos_policy** smartqos_policy_id=?

**show performance smartqos_policy** smartqos_policy_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartqos_policy_id=? | ID of the SmartQoS policy whose performance statistics you need to collect. | To obtain the value, run "show smartqos_policy general". |
| smartqos_policy_id_list=? | ID list of SmartQoS policies whose performance statistics you need to collect. | To obtain the value, run "show smartqos_policy general".<br>Multiple IDs are separated by commas (,). A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   After this command is executed, performance data categories are displayed. You can enter the serial number before a category and press "Enter" to view data of the category. You can enter multiple serial numbers and use commas (,) to separate them, or use a hyphen (-) to separate two serial numbers to represent a serial number range.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the I/O throughput of SmartQoS policy "0".

```text
admin:/>show performance smartqos_policy smartqos_policy_id=0

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
10.Read I/O Granularity Distribution: [4K,8K)(%)
11.Read I/O Granularity Distribution: [8K,16K)(%)
12.Read I/O Granularity Distribution: [16K,32K)(%)
13.Read I/O Granularity Distribution: [32K,64K)(%)
14.Read I/O Granularity Distribution: [64K,128K)(%)
15.Write I/O Granularity Distribution: [4K,8K)(%)
16.Write I/O Granularity Distribution: [8K,16K)(%)
17.Write I/O Granularity Distribution: [16K,32K)(%)
18.Write I/O Granularity Distribution: [32K,64K)(%)
19.Write I/O Granularity Distribution: [64K,128K)(%)
20.Average IO Size(KB)
21.% Read
22.% Write
23.Max IOPS(IO/s)
24.Service Time(Excluding Queue Time)(us)
25.Average I/O Latency(us)
26.Max. I/O Latency(us)
27.Average Read I/O Latency(us)
28.Average Write I/O Latency(us)
29.Normalized IOPS (IO/s)
30.Read I/O Granularity Distribution: [0K,4K)(%)
31.Read I/O Granularity Distribution: >= 128K(%)
32.Write I/O Granularity Distribution: [0K,4K)(%)
33.Write I/O Granularity Distribution: >= 128K(%)
34.Normalized Latency (us)
Input item(s) number separated by comma:3
```

##### System Response

None
