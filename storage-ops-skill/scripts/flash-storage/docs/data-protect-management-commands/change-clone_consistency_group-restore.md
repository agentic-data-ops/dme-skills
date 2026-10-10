# change clone_consistency_group restore


##### Function

The **change clone_consistency_group restore** command is used to set reverse synchronization parameters of a clone consistency group.

##### Format

**change clone_consistency_group restore** { clone_consistency_group_id_list=? action=? \| clone_consistency_group_name_list=? action=? } restore_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_consistency_group_id_list=? | List of clone consistency group IDs. | You can run the show clone_consistency_group general command to obtain the value. |
| clone_consistency_group_name_list=? | Clone consistency group name list. | You can run the show clone_consistency_group general command to obtain the value. |
| restore_type=? | Reverse synchronization type. | The value can be "fullcopy" or "diffcopy", where: <br>"fullcopy": full copy.<br>"diffcopy": differential copy. |
| action=? | Reverse synchronization action. | The value can be "start", "pause", "stop", or "continue", where: <br>"start": starts reverse synchronization.<br>"pause": pauses reverse synchronization.<br>"stop": stops reverse synchronization.<br>"continue": continues reverse synchronization. |

##### Usage Guidelines

None

##### Example

For clone consistency group "3", set its reverse synchronization action to "start" and its synchronization type to "fullcopy".

```text
admin:/>change clone_consistency_group restore clone_consistency_group_id_list=3 action=start restore_type=fullcopy
WARNING: You are about to reverse synchronize the clone consistency group. This operation will use data of target objects in clone pairs to overwrite data of source objects. Before performing this operation, ensure that source objects in clone pairs are not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. To retain data of source objects, back it up first.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity of the target objects.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Change clone consistency group restore 3 successfully.
```

For clone consistency group "3", set its reverse synchronization action to "stop".

```text
admin:/>change clone_consistency_group restore clone_consistency_group_id_list=3 action=stop
DANGER: You are about to stop reverse synchronizing data of target objects to source objects in the clone consistency group. This operation will cause data of source objects in clone pairs to be unavailable.
Suggestion: Before performing this operation, ensure that data of source objects in clone pairs is no longer needed.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Change clone consistency group restore 3 successfully.
```

##### System Response

None
