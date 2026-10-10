# change remote_replication mode


##### Function

The **change remote_replication mode** command is used to change the replication mode of the remote replication pair.

##### Format

**change remote_replication mode** remote_replication_id=? replication_model=? \[ synchronization_type=? \] \[ timing_length=? \] \[ timing_unit=? \] \[ synchronize_schedule=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_replication_id=? | ID of a remote replication task. | To obtain the value, run "show remote_replication general". |
| replication_model=? | Remote replication mode. | The value can be: <br>"asynchronization": indicates asynchronous remote replication.<br>"synchronization": indicates synchronous remote replication. |
| synchronization_type=? | Synchronization type. This parameter is available only when replication_model=? is set to "asynchronization". | The value can be: <br>"manual": Data needs to be synchronized manually.<br>"timed_wait_when_synchronization_begins": The system starts timing as soon as data synchronization starts.<br>"timed_wait_when_synchronization_ends": The system starts timing as soon as data synchronization ends.<br>"specified_time": specifies a time policy. |
| timing_length=? | Timing period (data synchronization period). This parameter is available only when synchronization_type=? is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The value ranges from 1 to 1440, expressed in minutes.<br>The value ranges from 3 to 59, expressed in seconds.<br>The default value is 60 minutes. |
| timing_unit=? | Unit of the synchronization period. | The value can be: <br>"minute": indicates minutes.<br>"second": indicates seconds. |
| synchronize_schedule=? | Schedule for starting the synchronization of remote replication. This parameter is available only when "synchronization_type" is set to "specified_time". | Delivery by week: "{"WEEK":{"WEEKDAY":"[1,3]","TIME":"11:00"}}". "WEEKDAY" indicates the day in a week on which synchronization is enabled and the value ranges from 0 to 6. Multiple days are separated by commas (,). "TIME" indicates the time when synchronization starts on a day and the value ranges from 00:00 to 23:59.<br>Delivery by day: "{"DAY":"01:00"}". where "DAY" indicates the time when synchronization starts every day and the value ranges from 00:00 to 23:59.<br>Delivery by hour: "{"HOUR":"9"}". where "HOUR" indicates the time in each hour when synchronization starts and the value ranges from 0 to 59. |

##### Usage Guidelines

None

##### Example

Change the replcation type of remote replication pair "9747215445131264" to "asynchronization".

```text
admin:/>change remote_replication mode remote_replication_id=9747215445131264 replication_model=asynchronization synchronization_type=manual
Command executed successfully.
```

##### System Response

None
