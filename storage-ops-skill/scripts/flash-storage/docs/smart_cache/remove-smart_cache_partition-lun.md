# remove smart_cache_partition lun


##### Function

The **remove smart_cache_partition lun** command is used to remove LUNs from a SmartCache partition.

##### Format

**remove smart_cache_partition lun** \[ smart_cache_partition_id=? lun_id_list=? \| smart_cache_partition_name=? lun_name_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smart_cache_partition_id=? | SmartCache partition ID. | The value ranges from 1 to 16. |
| smart_cache_partition_name=? | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (_), periods (.), and hyphens (-). |
| lun_id_list=? | ID list of LUNs or snapshots that you want to remove from a SmartCache partition. | To obtain the value, run "show lun general" or "show snapshot general". If multiple LUNs or snapshots need to be removed from a SmartCache partition: <br>Separate the LUN or snapshot IDs with commas (,). For example, "lun_id_list=1,2,3,4,5".<br>Specify LUN or snapshot ID ranges and separate the ranges with hyphens (-). For example, "lun_id_list=1-5,7,9-11". |
| lun_name_list=? | Name list of LUNs or snapshots removed from a SmartCache partition. | To obtain the LUN name list, run "show lun general". To obtain the snapshot name list, run "show snapshot general". If you want to concurrently remove multiple LUNs or snapshots from a SmartCache partition, separate multiple LUN names or snapshot names using commas (,). For example, "lun_name_list=lun1,lun2,lun3,lun4,lun5". |

##### Usage Guidelines

None

##### Example

Remove the LUN with ID "1" from the SmartCache partition with ID "1".

```text
admin:/>remove smart_cache_partition lun smart_cache_partition_id=1 lun_id_list=1
WARNING: You are about to remove LUNs from a SmartCache partition. This operation cannot be undone. This operation will delete the relationship between the LUNs and the SmartCache partition, and may affect performance of the LUNs.
Suggestion: Before performing this operation, ensure that the selected LUNs are no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove smart_cache_partition lun by batch 1 successfully.
```

Remove the LUN named "lun1" from the SmartCache partition named "scp1".

```text
admin:/>remove smart_cache_partition lun smart_cache_partition_name=scp1 lun_name_list=lun1
WARNING: You are about to remove LUNs from a SmartCache partition. This operation cannot be undone. This operation will delete the relationship between the LUNs and the SmartCache partition, and may affect performance of the LUNs.
Suggestion: Before performing this operation, ensure that the selected LUNs are no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove smart_cache_partition lun by batch lun1 successfully.
```

##### System Response

None
