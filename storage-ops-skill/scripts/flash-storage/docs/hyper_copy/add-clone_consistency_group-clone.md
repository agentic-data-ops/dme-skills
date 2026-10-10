# add clone_consistency_group clone


##### Function

The **add clone_consistency_group clone** command is used to add clone pairs to a specified clone consistency group. Use this command if consistency management is required for clone pairs.

##### Format

**add clone_consistency_group clone** clone_consistency_group_id=? clone_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_consistency_group_id | ID of the clone consistency group to which you want to add members. | To obtain the value, run "show clone_consistency_group general". |
| clone_id_list | ID list of the clone pairs to be added to a clone consistency group. | To obtain the value, run "show clone general". If you want to concurrently add multiple clone pairs to a clone consistency group: <br>Separate multiple clone pair IDs by commas (,). For example, "clone_id_list=1,2,3,4,5".<br>Specify a clone pair ID range using a hyphen (-). For example, "clone_id_list=1-5,7,9-11". |

##### Usage Guidelines

None

##### Example

Add clone pair "2" to clone consistency group "1".

```text
admin:/>add clone_consistency_group clone clone_consistency_group_id=1 clone_id_list=2
Add clone 2 to clone consistency group successfully.
```

##### System Response

None
