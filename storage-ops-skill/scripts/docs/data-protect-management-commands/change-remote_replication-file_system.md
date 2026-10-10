# change remote_replication file_system


##### Function

The **change remote_replication file_system** command is used to modify the settings of a specified file system remote replication pair.

##### Format

**change remote_replication file_system** remote_replication_id=? { compress_enable=? \| recovery_policy=? \| synchronization_rate=? \| synchronization_type=? \[ schedule_rule=? time_of_week=? time_of_day=? time_of_hour=? \| timing_length=? timing_unit=? \] } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_replication_id=? | Remote replication pair ID. | To obtain the value, run "show remote_replication unified". |
| recovery_policy=? | Recovery policy. | The value can be "automatic" or "manual", where: <br>"automatic": When links are recovered, the remote replication is automatically resumed. Data is automatically synchronized from the primary file system to the secondary file system.<br>"manual": When links are recovered, the remote replication needs to be resumed manually. The secondary file system retains the state preserved at the time when links are interrupted. Data is not automatically synchronized from the primary file system to the secondary file system. |
| compress_enable=? | Whether to enable compression. | The value can be "yes" or "no", where: <br>"yes": enables compression.<br>"no": disables compression. |
| synchronization_type=? | Synchronization type. This parameter is available only for asynchronous remote replication. | The value can be "manual", "timed_wait_when_synchronization_begins", "timed_wait_when_synchronization_ends", or "auto", where: <br>"manual": Data needs to be synchronized manually.<br>"timed_wait_when_synchronization_begins": The system starts timing as soon as data synchronization starts.<br>"timed_wait_when_synchronization_ends": The system starts timing as soon as data synchronization ends.<br>"auto": The system determines data synchronization. |
| synchronization_rate=? | Synchronization rate. | The value can be "Low", "Middle", "High", or "Highest", where: <br>"Low": indicates the low rate.<br>"Middle": indicates the medium rate.<br>"High": indicates the high rate.<br>"Highest": indicates the highest rate. |
| schedule_rule=? | Time policy. | The value can be "hourly", "daily", or "weekly", where: <br>"hourly": synchronizes data every hour.<br>"daily": synchronizes data every day.<br>"weekly": synchronizes data every week. |
| time_of_week=? | Time when the synchronization is performed every week. | The value ranges from Monday to Sunday and 00:00 to 23:59. |
| time_of_day=? | Time when the synchronization is performed every day. | The value ranges from 00:00 to 23:59. |
| time_of_hour=? | Time when the synchronization is performed every hour. | The value is an integer ranging from 0 to 59. |
| timing_length=? | Timing period (data synchronization period). This parameter is available only when synchronization_type=? is set to "timed_wait_when_synchronization_begins" or "timed_wait_when_synchronization_ends". | The options are as follows: <br>The unit is minute, and the value ranges from 1 to 1440.<br>The unit is second, and the value ranges from 15 to 59. |
| timing_unit=? | Unit of the synchronization period. | The options are as follows: <br>minute: minute.<br>second: second. |

##### Usage Guidelines

None

##### Example

Change the recovery policy of remote replication pair "2100ef02030405060000000200000000" to "automatic".

```text
admin:/>change remote_replication file_system remote_replication_id=2100ef02030405060000000200000000 recovery_policy=automatic
Command executed successfully.
```

##### System Response

None
