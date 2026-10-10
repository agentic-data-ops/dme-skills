# show performance snapshot


##### Function

The **show performance snapshot** command is used to query the performance statistics on a snapshot task. Run this command to analyze the performance statistics on a snapshot task in real time.

##### Format

**show performance snapshot** \[ snapshot_id=? \] \[ snapshot_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id=? | ID of a snapshot task on which you want to query performance statistics. | To obtain the value, run "show snapshot general". |
| snapshot_id_list=? | List of snapshot task IDs on which you want to query performance statistics. | To obtain the value, run "show snapshot general".<br>Separate the snapshot task IDs with commas (,) or hyphens (-).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" display the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the performance statistics on the reads for snapshot task "7".

```text
admin:/>show performance snapshot snapshot_id=7
0.Read requests to the snapshot LUN                                     1.Read requests redirected to the source LUN
2.Write requests to the snapshot LUN                                    3.Write requests insufficient for the grain size to the snapshot LUN
Input item(s) number separated by comma:1

Read requests redirected to the source LUN : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                                          | Meaning                                                                       |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Read requests to the snapshot LUN                                  | Number of read requests to the snapshot LUN.                                  |
| Read requests redirected to the source LUN                         | Number of read requests redirected to the snapshot LUN.                       |
| Write requests to the snapshot LUN                                 | Number of write requests to the snapshot LUN.                                 |
| Write requests insufficient for the grain size to the snapshot LUN | Number of write requests insufficient for the grain size to the snapshot LUN. |
