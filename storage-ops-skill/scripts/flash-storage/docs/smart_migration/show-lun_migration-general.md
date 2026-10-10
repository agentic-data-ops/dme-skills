# show lun_migration general


##### Function

The **show lun_migration general** command is used to query the attributes of LUN migration tasks.

##### Format

**show lun_migration general** \[ source_lun_id=? \]

##### Parameters

| Parameter       | Description    | Value                                                                                                                                                                                                                        |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| source_lun_id=? | Source LUN ID. | To obtain the value, run the "**show lun_migration general**" command without parameters. |

##### Usage Guidelines

-   Run the "**show lun_migration general**" command to batch query attributes of all LUN migration tasks.
-   Run the "**show lun_migration general** source_lun_id=?" command to query attributes of a specific LUN migration task.

##### Example

Batch query the attributes of all LUN migration tasks.

```text
admin:/>show lun_migration general
Source LUN ID  Source LUN Name  Target LUN ID  Target LUN Name  Running Status  Speed   Process(%)  Work Mode  Current Max Speed(MB/s)  Max Bandwidth(MB/s)
-------------  ---------------  -------------  ---------------  --------------  ------  ----------  ---------  -----------------------  -------------------
188            lm0000           189            lm0001           Migrated        Middle  --          Auto       --                       --
190            lm0002           191            lm0003           Paused          --      --          Manual     --                       1011

```

Query the attributes of a specific LUN migration task.

```text
admin:/>show lun_migration general source_lun_id=0
Source LUN ID              : 0
Source LUN Name            : LUN_0
Target LUN ID              : 1
Target LUN Name            : LUN_1
Running Status             : Normal
Speed                      : Middle
Process(%)                 : --
Start Time                 : 2019-04-10/11:34:58 UTC+08:00
End Time                   : --
Work Mode                  : Manual
Period Speed               : High
Period Start Day           : 2019-03-22
Period End Day             : 2019-03-24
Period Start Time          : 23:00
Duration                   : 2 hour(s),0 minute(s)
Current Max Speed(MB/s)    : --
Max Bandwidth(MB/s)        : --
Period Max Bandwidth(MB/s) : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                  | Meaning                                    |
|----------------------------|--------------------------------------------|
| Source LUN ID              | Indicates the source LUN ID.               |
| Source LUN Name            | Indicates the source LUN name.             |
| Target LUN ID              | Indicates the target LUN ID.               |
| Target LUN Name            | Indicates the target LUN name.             |
| Running Status             | Indicates the running status.              |
| Speed                      | Indicates the speed.                       |
| Process(%)                 | Indicates the migration progress.          |
| Start Time                 | Indicates the start time of the migration. |
| End Time                   | Indicates the end time of the migration.   |
| Work Mode                  | Indicates the split mode.                  |
| Period Speed               | Migration rate in a specified period.      |
| Period Start Day           | Start day of a specified period.           |
| Period End Day             | End day of a specified period.             |
| Period Start Time          | Start time of a specified period.          |
| Duration                   | Duration of a specified period.            |
| Current Max Speed(MB/s)    | Current maximum migration rate.            |
| Max Bandwidth(MB/s)        | Maximum bandwidth.                         |
| Period Max Bandwidth(MB/s) | Maximum bandwidth in a specified period.   |
