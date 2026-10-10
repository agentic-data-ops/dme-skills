# create lun_clone general


##### Function

The **create lun_clone general** command is used to create clones. You can create an identical and usable point-in-time duplicate for a data object by running this command.

##### Format

**create lun_clone general** name=? { source_id=? \| source_id_list=? } \[ clone_id=? \] \[ split_speed=? \] { \[ dedup_enable=? \] \[ compress_enable=? \] \| \[ workload_type_id=? \] } \[ io_priority=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name | Name of a clone. | The value contains 1 to 255 characters including letters, digits, hyphens (-), underscores (_), and periods (.). NOTE: When creating clones in a batch, the length of name=? cannot exceed 251 characters. |
| source_id | ID of a source LUN or a source snapshot. | To obtain the value, run "show lun_clone available_lun".<br>To obtain the value, run "show lun_clone available_snapshot". |
| source_id_list | ID list of source LUNs or source snapshots. | To obtain the value, run "show lun_clone available_lun" or "show lun_clone available_snapshot".<br>You can specify multiple LUN or snapshot IDs separated by commas (,), or ID range using hyphens(-), such as: 0, 5-8. |
| clone_id | Clone ID. | The value is an integer ranging from 0 to 65535. |
| split_speed | Split speed. | The value can be "low", "middle", "high", or "highest" where: <br>"low": indicates the low speed.<br>"middle": indicates the medium speed.<br>"high": indicates the high speed.<br>"highest": indicates the highest speed.<br> The default value is "middle". |
| dedup_enable | Indicates whether the deduplication function is enabled. | The value can be "yes" or "no", where <br>"yes": The deduplication function will be enabled.<br>"no": The deduplication function will not be enabled. |
| compress_enable | Indicates whether the compression function is enabled. | The value can be "yes" or "no", where <br>"yes": The compression function will be enabled.<br>"no": The compression function will not be enabled. |
| workload_type_id | ID of the workload. | The value is an integer ranging from 0 to 2048. |
| io_priority | I/O priority of a LUN. | The value can be "low", "middle", or "high", where: <br>"low": indicates the low priority.<br>"middle": indicates the medium priority.<br>"high": indicates the high priority.<br> The default value is "low". |

##### Usage Guidelines

You can create multi-clones for different LUNs in the mean time.

##### Example

Create a clone for LUN "5", and the name is "new".

```text
admin:/>create lun_clone general name=new source_id_list=5
Create lun_clone new successfully.
```

Create a clone simultaneously for LUNs "1", "3", and "4".

```text
admin:/>create lun_clone general name=clone source_id_list=1,3,4
Create lun_clone clone0000 successfully.
Create lun_clone clone0001 successfully.
Create lun_clone clone0002 successfully.
```

##### System Response

None
