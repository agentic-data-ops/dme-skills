# add smart_cache_partition file_system


##### Function

The **add smart_cache_partition file_system** command is used to add file systems to a SmartCache partition.

##### Format

**add smart_cache_partition file_system** \[ smart_cache_partition_id=? file_system_id_list=? \| smart_cache_partition_name=? file_system_name_list=? \] \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smart_cache_partition_id=? | SmartCache partition ID. | The value ranges from 1 to 16. |
| smart_cache_partition_name=? | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (_), hyphens (-), and periods (.). |
| file_system_id_list=? | File system ID list. | To obtain the value, run "show file_system general". If multiple file systems need to be added: <br>Separate the file system IDs with commas (,). For example, "file_system_id_list=1,2,3,4,5".<br>Specify file system ID ranges by hyphens (-). For example, "file_system_id_list=1-5,7,9-11". |
| file_system_name_list=? | List of file system names. | To obtain the value, run "show file_system general". If multiple file systems need to be added, separate the file system names with commas (,). For example, "file_system_name_list=fs1,fs2,fs3,fs4,fs5". |
| vstore_id | vStore ID. | The value ranges from 0 to 1023. |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Add the file system whose ID is "1" to the SmartCache partition whose ID is "1".

```text
admin:/>add smart_cache_partition file_system smart_cache_partition_id=1 file_system_id_list=1
Add smart_cache_partition file_system by batch 1 successfully.
```

Add the file system whose name is "fs1" to the SmartCache partition whose name is "scp1".

```text
admin:/>add smart_cache_partition file_system smart_cache_partition_name=scp1 file_system_name_list=fs1
Add smart_cache_partition file_system by batch fs1 successfully.
```

Add the file system with vStore ID 1 named "fs1" to the SmartCache partition whose name is "scp1".

```text
admin:/>add smart_cache_partition file_system smart_cache_partition_name=scp1 file_system_name_list=fs1 vstore_id=1
Add smart_cache_partition file_system by batch fs1 successfully.
```

##### System Response

None
