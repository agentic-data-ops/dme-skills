# show performance system


##### Function

The **show performance system** command is used to query the performance statistics of the storage system. Run this command to analyze the performance statistics of the system in real time.

##### Format

**show performance system**

##### Parameters

None

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

To query the performance statistics of the total I/O number, run the following command.

```text
admin:/>show performance system
0.The cumulative count of I/Os
1.The cumulative count of data transferred in Kbytes
2.The cumulative count of all reads
3.The cumulative count of data read in Kbytes(1024bytes = 1KByte)
4.The cumulative count of all writes
5.The cumulative count of data written in Kbytes
Input item(s) number separated by comma:5
The cumulative count of data written in Kbytes : 21031118
```

##### System Response

None
