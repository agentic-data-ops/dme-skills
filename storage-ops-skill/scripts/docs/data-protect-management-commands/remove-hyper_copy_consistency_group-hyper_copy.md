# remove hyper_copy_consistency_group hyper_copy


##### Function

The **remove hyper_copy_consistency_group hyper_copy** command is used to remove HyperCopy pairs from a specified HyperCopy consistency group. Use this command if consistency management is not required for HyperCopy pairs.

##### Format

**remove hyper_copy_consistency_group hyper_copy** hyper_copy_consistency_group_id=? hyper_copy_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hyper_copy_consistency_group_id | ID of the HyperCopy consistency group whose members are to be removed. | To obtain the value, run "show hyper_copy_consistency_group general". |
| hyper_copy_id_list | ID list of the HyperCopy pairs removed from a HyperCopy consistency group. | To obtain the value, run "show hyper_copy_consistency_group hyper_copy". If you want to remove multiple HyperCopy pairs from a HyperCopy consistency group, perform either of the following: <br>Separate multiple HyperCopy pair IDs by commas (,). For example, "hyper_copy_id_list=1,2,3,4,5".<br>Specify a HyperCopy pair ID range using a hyphen (-). For example, "hyper_copy_id_list=1-5,7,9-11". |

##### Usage Guidelines

None

##### Example

Remove HyperCopy pairs "2" and "3" from HyperCopy consistency group "1".

```text
admin:/>remove hyper_copy_consistency_group hyper_copy hyper_copy_consistency_group_id=1 hyper_copy_id_list=2,3
WARNING: You are about to remove HyperCopy pair  from the HyperCopy consistency group . After the removal, the HyperCopy pair is not protected by the HyperCopy consistency group.
Suggestion: Before performing this operation, ensure that HyperCopy pair does not need HyperCopy consistency group protection.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove HyperCopy 2 from HyperCopy consistency group successfully.
Remove HyperCopy 3 from HyperCopy consistency group successfully.
```

##### System Response

None
