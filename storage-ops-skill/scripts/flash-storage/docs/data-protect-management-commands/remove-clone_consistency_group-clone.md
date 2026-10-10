# remove clone_consistency_group clone


##### Function

The **remove clone_consistency_group clone** command is used to remove clone pairs from a specified clone consistency group. Use this command if consistency management is not required for clone pairs.

##### Format

**remove clone_consistency_group clone** clone_consistency_group_id=? clone_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_consistency_group_id | ID of the clone consistency group whose members are to be removed. | To obtain the value, run "show clone_consistency_group general". |
| clone_id_list | ID list of the clone pairs removed from a clone consistency group. | To obtain the value, run "show clone_consistency_group clone". If you want to remove multiple clone pairs from a clone consistency group, perform either of the following: <br>Separate multiple clone pair IDs by commas (,). For example, "clone_id_list=1,2,3,4,5".<br>Specify a clone pair ID range using a hyphen (-). For example, "clone_id_list=1-5,7,9-11". |

##### Usage Guidelines

None

##### Example

Remove clone pairs "2" and "3" from clone consistency group "1".

```text
admin:/>remove clone_consistency_group clone clone_consistency_group_id=1 clone_id_list=2,3
WARNING: You are about to remove the clone pair from the clone consistency group. After the removal, the clone pair is not protected by the clone consistency group.
Suggestion: Before performing this operation, ensure that clone pair does not need clone consistency group protection.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove clone 2 from clone consistency group successfully.
Remove clone 3 from clone consistency group successfully.
```

##### System Response

None
