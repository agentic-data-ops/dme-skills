# change clone_consistency_group synchronize


##### Function

The **change clone_consistency_group synchronize** command is used to start, pause, continue, and stop member synchronization of a clone consistency group.

##### Format

**change clone_consistency_group synchronize** { clone_consistency_group_id_list=? action=? \| clone_consistency_group_name_list=? action=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_consistency_group_id_list=? | Clone consistency group ID. | You can run the show clone_consistency_group general command to obtain the value. |
| clone_consistency_group_name_list=? | Clone consistency group name list. | You can run the show clone_consistency_group general command to obtain the value. |
| action=? | Synchronization action. | The value can be "start", "pause", "stop", or "continue", where: <br>"start": starts synchronization.<br>"pause": pauses synchronization.<br>"stop": stops synchronization.<br>"continue": continues synchronization. |

##### Usage Guidelines

None

##### Example

Start synchronizing clone consistency group "7".

```text
admin:/>change clone_consistency_group synchronize clone_consistency_group_id_list=7 action=start
WARNING: You are about to synchronize the clone consistency group. This operation will use data of source objects in clone pairs to overwrite data of target objects. Before performing this operation, ensure that target objects in clone pairs are not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. To retain data of target objects, back it up first.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity of the source objects.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change clone consistency group synchronize 7 successfully.
```

Stop synchronizing clone consistency group "7".

```text
admin:/>change clone_consistency_group synchronize clone_consistency_group_id_list=7 action=stop
DANGER: You are about to stop synchronizing data from source objects to target objects in the clone consistency group. This operation will cause data of target objects in clone pairs to be unavailable.
Suggestion: Before performing this operation, ensure that data of target objects in clone pairs is no longer needed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change clone consistency group synchronize 7 successfully.
```

##### System Response

None
