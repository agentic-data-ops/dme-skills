# show performance lun_migration


##### Function

The **show performance lun_migration** command is used to query the performance statistics of a LUN migration task. Run this command to analyze the performance statistics of a LUN migration task in real time.

##### Format

**show performance lun_migration** source_lun_id=?

##### Parameters

| Parameter       | Description                                                                                   | Value                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| source_lun_id=? | Source LUN ID of the LUN migration task for which performance statistics are to be collected. | To obtain the value, run the "show lun_migration general" command without parameters. |

##### Usage Guidelines

-   After this command is executed, performance data categories are displayed. You can enter the serial number before a category and press "Enter" to view the category of data. You can enter multiple serial numbers and use commas (,) to separate them.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

##### Example

Query the bandwidth performance statistics of the LUN migration task whose source LUN ID is "0".

```text
admin:/>show performance lun_migration source_lun_id=0
0.Bandwidth(MB/s)
Input item(s) number separated by comma:0

Bandwidth(MB/s) : 30.000
```

##### System Response

None
