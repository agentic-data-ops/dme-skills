# change lun_migration


##### Function

The **change lun_migration** command is used to change the LUN migration properties.

##### Format

**change lun_migration** source_lun_id=? \[ speed=? \] \[ max_bandwidth=? \] \[ work_mode=? \] \[ period_speed=? \] \[ period_max_bandwidth=? \] \[ period_start_day=? \] \[ period_end_day=? \] \[ period_start_time=? \] \[ duration=? \]

##### Parameters

| Parameter              | Description                              | Value                                                                                      |
|------------------------|------------------------------------------|--------------------------------------------------------------------------------------------|
| source_lun_id=?        | ID of a source LUN.                      | To obtain the value, run the "show lun_migration general" command without parameters.      |
| speed=?                | LUN migration speed.                     | The value can be "Low", "Middle", "High", or "Highest".                                    |
| max_bandwidth=?        | Maximum bandwidth.                       | The value is an integer from 1 to 1024.                                                    |
| work_mode=?            | LUN migration split mode.                | The value can be "Auto" or "Manual", and the default value is "Auto".                      |
| period_speed=?         | Migration rate in a specified period.    | The value can be "Low", "Middle", "High", or "Highest", and the default value is "Middle". |
| period_max_bandwidth=? | Maximum bandwidth in a specified period. | The value is an integer from 1 to 1024.                                                    |
| period_start_day=?     | Start day of a specified period.         | The value is from 2000-01-01 to 2035-12-31.                                                |
| period_end_day=?       | End day of a specified period.           | The value is from 2000-01-01 to 2035-12-31.                                                |
| period_start_time=?    | Start time of a specified period.        | The value is from 00:00 to 23:59.                                                          |
| duration=?             | Duration of a specified period.          | The value is from 00:00 to 23:59.                                                          |

##### Usage Guidelines

None

##### Example

Change the LUN migration speed.

```text
admin:/>change lun_migration source_lun_id=5 speed=High
Command executed successfully.
```

Change the LUN migration split mode.

```text
admin:/>change lun_migration source_lun_id=5 work_mode=Manual
Command executed successfully.
```

Change the LUN migration speed to the highest speed.

```text
admin:/>change lun_migration source_lun_id=5 speed=Highest
WARNING: You are about to select the "Highest" speed for synchronization.
After the operation, a SmartMigration pair will be synchronized at the highest speed, which may cause overloaded services, disconnection of the SmartMigration pair, and deteriorated host performance.
Suggestion: Select the "High" speed. If you select the "Highest" speed, check the performance of the data receiving end and host services to prevent the disconnection of the SmartMigration pair during synchronization and to ensure host performance.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the specified speed in a period for LUN migration.

```text
admin:/>change lun_migration source_lun_id=0 period_speed=High period_start_day=2019-03-12 period_end_day=2019-03-12 period_start_time=08:00 duration=01:00
Command executed successfully.
```

##### System Response

None
