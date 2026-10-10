# create lun_migration


##### Function

The **create lun_migration** command is used to create LUN migration.

##### Format

**create lun_migration** source_lun_id=? target_lun_id=? \[ speed=? \] \[ max_bandwidth=? \] \[ work_mode=? \] \[ period_speed=? \] \[ period_max_bandwidth=? \] \[ period_start_day=? \] \[ period_end_day=? \] \[ period_start_time=? \] \[ duration=? \]

##### Parameters

| Parameter              | Description                              | Value                                                                                      |
|------------------------|------------------------------------------|--------------------------------------------------------------------------------------------|
| source_lun_id=?        | ID of a source LUN.                      | Run the "show lun general" command without parameters to obtain the value.                 |
| target_lun_id=?        | ID of a target LUN.                      | Run the "show lun general" command without parameters to obtain the value.                 |
| speed=?                | Data migration speed of a LUN.           | The value can be "Low", "Middle", "High", or "Highest", and the default value is "Middle". |
| max_bandwidth=?        | Maximum bandwidth.                       | The value is an integer from 1 to 1024.                                                    |
| work_mode=?            | Split mode of a LUN migration.           | The value can be "Auto" or "Manual", and the default value is "Auto".                      |
| period_speed=?         | Migration rate in a specified period.    | The value can be "Low", "Middle", "High", or "Highest", and the default value is "Middle". |
| period_max_bandwidth=? | Maximum bandwidth in a specified period. | The value is an integer from 1 to 1024.                                                    |
| period_start_day=?     | Start day of a specified period.         | The value is from 2000-01-01 to 2035-12-31.                                                |
| period_end_day=?       | End day of a specified period.           | The value is from 2000-01-01 to 2035-12-31.                                                |
| period_start_time=?    | Start time of a specified period.        | The value is from 00:00 to 23:59.                                                          |
| duration=?             | Duration of a specified period.          | The value is from 00:00 to 23:59.                                                          |

##### Usage Guidelines

None

##### Example

Create LUN migration.

```text
admin:/>create lun_migration source_lun_id=5 target_lun_id=7
WARNING: You are about to create a migration relationship between the source LUN and target LUN.
Migration starts immediately after the relationship is established, and the data on the target LUN will be overwritten by that on the source LUN after the migration.
Suggestion: Before performing this operation, ensure that the selected source LUN and target LUN are correct and the target LUN is not being read or written by hosts. If the capacity of the target LUN is larger than that of the source LUN, scan for the source LUN again after the migration is complete.
Have you read warning message carefully?(y/n)Y
Are you sure you really want to perform the operation?(y/n)Y
Command executed successfully.
```

Create LUN migration at the highest migration speed.

```text
admin:/>create lun_migration source_lun_id=5 target_lun_id=7 speed=Highest
WARNING: You are about to create a migration relationship between the source LUN and target LUN.
Migration starts immediately after the relationship is established, and the data on the target LUN will be overwritten by that on the source LUN after the migration.
If you perform synchronization at the highest speed, the service load may be too heavy, SmartMigration pairs may be disconnected, and host performance may be affected.
Suggestion:
1. Before performing this operation, ensure that the selected source LUN and target LUN are correct and the target LUN is not being read or written by hosts. If the capacity of the target LUN is larger than that of the source LUN, scan for the source LUN again after the migration is complete.
2. Select the high speed. If you select the highest speed, check the performance of the data receiving device and services running on the host.
Have you read warning message carefully?(y/n)Y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create LUN migration at the specified speed in a period.

```text
admin:/>create lun_migration source_lun_id=0 target_lun_id=1 period_speed=High period_start_day=2019-03-12 period_end_day=2019-03-12 period_start_time=08:00 duration=01:00
WARNING: You are about to create a migration relationship between the source LUN and target LUN.
Migration starts immediately after the relationship is established, and the data on the target LUN will be overwritten by that on the source LUN after the migration.
Suggestion: Before performing this operation, ensure that the selected source LUN and target LUN are correct and the target LUN is not being read or written by hosts. If the capacity of the target LUN is larger than that of the source LUN, scan for the source LUN again after the migration is complete.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
