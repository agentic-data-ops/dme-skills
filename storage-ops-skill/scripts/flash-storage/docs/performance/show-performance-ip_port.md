# show performance ip_port


##### Function

The **show performance ip_port** command is used to query the performance statistics on a back-end port. Run this command to analyze the performance statistics on a port in real time.

##### Format

**show performance ip_port** port_id=?

**show performance ip_port** port_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| port_id=? | ID of a port on which you want to query performance statistics. | To obtain the value, run "show port general physical_type=RDMA". |
| port_id_list=? | ID list of ports on which you want to query performance statistics. | To obtain the value, run "show port general physical_type=RDMA".<br>Separate the port IDs with commas (,).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" display the performance statistics for those categories.
-   By default, performance statistics will be refreshed every three seconds. To refresh performance statistics instantly, press "Enter".
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the performance statistics on the read I/Os flowing through port P1 on interface module "1" that resides on controller "1" of controller enclosure "0". The command output varies depending on a specific product.

```text
admin:/>show performance ip_port port_id_list=CTE0.IOM.H1.P0
0.Bandwidth(MB/s) / Block Bandwidth(MB/s)    1.Throughput(IOPS)(IO/s)                     2.Average I/O Latency(us)
```

##### System Response

None
