# add smart_cache_partition lun


##### Function

The **add smart_cache_partition lun** command is used to add LUNs to a SmartCache partition.

##### Format

**add smart_cache_partition lun** \[ smart_cache_partition_id=? lun_id_list=? \| smart_cache_partition_name=? lun_name_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smart_cache_partition_id=? | SmartCache partition ID. | The value ranges from 1 to 16. |
| smart_cache_partition_name=? | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (_), hyphens (-), and periods (.). |
| lun_id_list=? | ID list of LUNs or snapshots that you want to add to the SmartCache partition. | To obtain the value, run "show lun general" or "show snapshot general". If multiple LUNs or snapshots need to be added: <br>Separate the LUN or snapshot IDs with commas (,). For example, "lun_id_list=1,2,3,4,5".<br>Specify LUN or snapshot ID ranges by hyphens (-). For example, "lun_id_list=1-5,7,9-11". |
| lun_name_list=? | Name list of LUNs or snapshots that you want to add to the SmartCache partition. | To obtain the value, run "show lun general" or "show snapshot general". If multiple LUNs or snapshots need to be added, separate the LUN or snapshot names with commas (,). For example, "lun_name_list=lun1,lun2,lun3,lun4,lun5". |

##### Usage Guidelines

None

##### Example

Add the LUN whose ID is "1" to the SmartCache partition whose ID is "1".

```text
admin:/>add smart_cache_partition lun smart_cache_partition_id=1 lun_id_list=1
Add smart_cache_partition lun by batch 1 successfully.
```

Add the LUN whose name is "lun1" to the SmartCache partition whose name is "scp1".

```text
admin:/>add smart_cache_partition lun smart_cache_partition_name=scp1 lun_name_list=lun1
Add smart_cache_partition lun by batch lun1 successfully.
```

##### System Response

None
