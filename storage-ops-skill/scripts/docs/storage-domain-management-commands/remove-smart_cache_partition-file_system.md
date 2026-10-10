# remove smart_cache_partition file_system


##### Function

The **remove smart_cache_partition file_system** command is used to remove file systems from a SmartCache partition.

##### Format

**remove smart_cache_partition file_system** \[ smart_cache_partition_id=? file_system_id_list=? \| smart_cache_partition_name=? file_system_name_list=? \] \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smart_cache_partition_id=? | SmartCache partition ID. | The value ranges from 1 to 16. |
| smart_cache_partition_name=? | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (_), periods (.), and hyphens (-). |
| file_system_id_list=? | File system ID list. | To obtain the value, run "show file_system general". If multiple file system IDs need to be removed from a SmartCache partition: <br>Separate the file system IDs with commas (,). For example, "file_system_id_list=1,2,3,4,5".<br>Specify file system ID ranges and separate the ranges with hyphens (-). For example, "file_system_id_list=1-5,7,9-11". |
| file_system_name_list=? | List of file system names. | To obtain the file system name list, run "show file_system general".If you want to concurrently remove multiple file system names from a SmartCache partition, separate multiple file system names using commas (,). For example, "file_system_name_list=fs1,fs2,fs3,fs4,fs5". |
| vstore_id | vStore ID. | The value ranges from 0 to 1023. |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Remove the file system with ID "1" from the SmartCache partition with ID "1".

```text
admin:/>remove smart_cache_partition file_system smart_cache_partition_id=1 file_system_id_list=1
WARNING: You are about to remove file systems from a SmartCache partition. The operation cannot be undone. This operation will delete the relationship between the file systems and the SmartCache partition, and may affect performance of the file systems.
Suggestion: Before performing this operation, ensure that the selected file systems are no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove smart_cache_partition file_system by batch 1 successfully.
```

Remove the file system named "fs1" from the SmartCache partition named "scp1".

```text
admin:/>remove smart_cache_partition file_system smart_cache_partition_name=scp1 file_system_name_list=fs1
WARNING: You are about to remove file systems from a SmartCache partition. The operation cannot be undone. This operation will delete the relationship between the file systems and the SmartCache partition, and may affect performance of the file systems.
Suggestion: Before performing this operation, ensure that the selected file systems are no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove smart_cache_partition file_system by batch fs1 successfully.
```

Remove the file system with vStore ID 1 named "fs1" from the SmartCache partition named "scp1".

```text
admin:/>remove smart_cache_partition file_system smart_cache_partition_name=scp1 file_system_name_list=fs1 vstore_id=1
WARNING: You are about to remove file systems from a SmartCache partition. The operation cannot be undone. This operation will delete the relationship between the file systems and the SmartCache partition, and may affect performance of the file systems.
Suggestion: Before performing this operation, ensure that the selected file systems are no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove smart_cache_partition file_system by batch fs1 successfully.
```

##### System Response

None
