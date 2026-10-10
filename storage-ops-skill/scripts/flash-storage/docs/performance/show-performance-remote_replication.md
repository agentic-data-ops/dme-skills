# show performance remote_replication


##### Function

The **show performance remote_replication** command is used to query the performance statistics of a remote replication pair. Run this command to analyze the performance statistics of a remote replication pair in real time.

##### Format

**show performance remote_replication** remote_replication_id=?

**show performance remote_replication** remote_replication_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_replication_id=? | ID of the remote replication pair whose performance statistics you want to collect. | To obtain the value, run "show remote_replication unified". |
| remote_replication_id_list=? | ID list of remote replication pairs whose performance statistics you want to collect. | To obtain the value, run "show remote_replication unified".<br>Separate the IDs of remote replication pairs with commas (,).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   After this command is executed, performance data categories are displayed. You can enter the serial number before a category and press "Enter" to view the category of data. You can enter multiple serial numbers and use commas (,) to separate them.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.
-   "remote_replication_id" is mutually exclusive with "remote_replication_id_list".
-   This CLI command can be used only on the primary array of an asynchronous remote replication pair to query performance statistics.

##### Example

Query the bandwidth data of remote replication pair "fcba35670003".

```text

admin:/>show performance remote_replication remote_replication_id=21007cc3855e80330000000200000004
0.Time Since Last Synchronization(s)    1.Time difference (s)                   2.Bandwidth(MB/s)
3.Logical Bandwidth(MB/s)               4.Synchronization Duration(s)
Input item(s) number separated by comma:0, 1, 2, 3, 4

Time Since Last Synchronization(s) : 4507
Time difference (s)                : 4508
Bandwidth(MB/s)                    : 0.000
Logical Bandwidth(MB/s)            : 0.000
Synchronization Duration(s)        : --

```

Query the time difference between the data synchronization points in time of the primary and secondary resources of remote replication pair "d8490b90ee140004".

```text

admin:/>show performance remote_replication remote_replication_id=21007cc3855e80330000000200000004
0.Time Since Last Synchronization(s)    1.Time difference (s)                   2.Bandwidth(MB/s)
3.Logical Bandwidth(MB/s)               4.Synchronization Duration(s)
Input item(s) number separated by comma:1

Time difference (s) : 4873

```

##### System Response

The following table describes the parameter meanings.

| Parameter                        | Meaning                                                                                                                                                                                      |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bandwidth                        | Physical bandwidth consumed after link compression.                                                                                                                                          |
| Time Since Last Synchronization. | Time difference with the last remote replication synchronization.                                                                                                                            |
| Logical Bandwidth                | Logical bandwidth consumed without link compression.                                                                                                                                         |
| Time Difference                  | Time difference between the data synchronization points in time of the primary and secondary resources in a synchronization period of asynchronous remote replication, expressed in seconds. |
| Synchronization Duration (s)     | Synchronization duration, expressed in seconds.                                                                                                                                              |
