# add hyper_copy_consistency_group hyper_copy


##### Function

The **add hyper_copy_consistency_group hyper_copy** command is used to add HyperCopy pairs to a specified HyperCopy consistency group. Use this command if consistency management is required for HyperCopy pairs.

##### Format

**add hyper_copy_consistency_group hyper_copy** hyper_copy_consistency_group_id=? hyper_copy_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hyper_copy_consistency_group_id | ID of the HyperCopy consistency group to which you want to add members. | To obtain the value, run "show hyper_copy_consistency_group general". |
| hyper_copy_id_list | ID list of the HyperCopy pairs to be added to a HyperCopy consistency group. | To obtain the value, run "show hyper_copy general". If you want to concurrently add multiple HyperCopy pairs to a HyperCopy consistency group: <br>Separate multiple HyperCopy pair IDs by commas (,). For example, "hyper_copy_id_list=1,2,3,4,5".<br>Specify a HyperCopy pair ID range using a hyphen (-). For example, "hyper_copy_id_list=1-5,7,9-11". |

##### Usage Guidelines

None

##### Example

Add HyperCopy pair "2" to HyperCopy consistency group "1".

```text
admin:/>add hyper_copy_consistency_group hyper_copy hyper_copy_consistency_group_id=1 hyper_copy_id_list=2
Add HyperCopy 2 to HyperCopy consistency group successfully.
```

##### System Response

None
