# create clone general


##### Function

The **create clone general** command is used to create a clone pair.

##### Format

**create clone general** { source_id_list=? name=? \| source_name_list=? name=? } \[ dst_id_list=? \] \[ copy_speed=? \] \[ description=? \] \[ io_priority=? \] \[ workload_type_id=? \] \[ compress_enable=? \] \[ dedup_enable=? \] \[ start_synchronize_after_create=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| source_id_list=? | Source LUN ID list or source snapshot ID list. | Use commas (,) to separate multiple source IDs, or use a hyphen (-) to specify an ID range, for example, "1,5-8". |
| source_name_list=? | Source LUN name list or source snapshot name list. | Use commas (,) to separate multiple source names. |
| name=? | Name of a clone pair. | The value is a string of 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| dst_id_list=? | List of target LUN IDs. | Use commas (,) to separate multiple target LUN IDs, or use a hyphen (-) to specify an ID range, for example, "1,5-8". |
| io_priority=? | I/O priority of a LUN. | The value can be "Low", "Middle", or "High", where: <br>"Low": low priority.<br>"Middle": medium priority.<br>"High": high priority.<br> The default value is "Low". |
| workload_type_id=? | ID of a workload type. | The value is an integer ranging from 0 to 2048. |
| compress_enable=? | Whether to enable or disable the compression function. | The value can be "yes" or "no", where: <br>"yes": enables the compression function.<br>"no": disables the compression function. |
| dedup_enable=? | Whether to enable the deduplication function. | The value can be "yes" or "no", where: <br>"yes": enables the deduplication function.<br>"no": disables the deduplication function. |
| start_synchronize_after_create=? | Whether to start data synchronization after a clone pair is created. | The value can be "yes" or "no", where: <br>"yes": synchronization is started immediately after the creation.<br>"no": Synchronization is not started after the creation. |
| copy_speed=? | Copy rate. | The value can be "low", "middle", "high", or "highest", where: <br>"low": low speed.<br>"middle": medium speed.<br>"high": high speed.<br>"highest": highest speed. |
| description=? | Description. | - |

##### Usage Guidelines

None

##### Example

Create a clone pair named "new" for source LUN "5".

```text
admin:/>create clone general source_id_list=5 name=new
Create clone successfully.
admin:/>
```

##### System Response

None
