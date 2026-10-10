# show performance consistency_group


##### Function

The **show performance consistency_group** command is used to query the performance statistics on a remote replication consistency group. Run this command to analyze the performance statistics on a remote replication consistency group in real time.

##### Format

**show performance consistency_group** { consistency_group_id=? \| consistency_group_id_list=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| consistency_group_id=? | ID of a remote replication consistency group whose performance statistics needs to be queried. | To obtain the value, run "show consistency_group general". |
| consistency_group_id_list=? | ID list of remote replication consistency group tasks on which you want to query performance statistics. | To obtain the value, run "show consistency_group general".<br>Separate the IDs of remote replication consistency group tasks with commas (,).<br>A maximum of 50 IDs can be queried. |

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.
-   "consistency_group_id" is mutually exclusive with "consistency_group_id_list".

##### Example

Query the statistics on the synchronization duration of the remote replication consistency group whose ID is "74a063ff51090000".

```text
admin:/>show performance consistency_group consistency_group_id=74a063ff51090000
0.Synchronization Duration(s)
Input item(s) number separated by comma:0
Synchronization Duration(s) : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                   | Meaning                                         |
|-----------------------------|-------------------------------------------------|
| Synchronization Duration(s) | Synchronization duration, expressed in seconds. |
