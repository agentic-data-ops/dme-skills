# change hyper_copy_consistency_group synchronize


##### Function

The **change hyper_copy_consistency_group synchronize** command is used to start, pause, continue, and stop member synchronization of a HyperCopy consistency group.

##### Format

**change hyper_copy_consistency_group synchronize** hyper_copy_consistency_group_id_list=? action=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hyper_copy_consistency_group_id_list | HyperCopy consistency group ID. | To obtain the value, run "show hyper_copy_consistency_group general". |
| action | Synchronization action. | The value can be "start", "pause", "stop", or "continue", where: <br>"start": starts synchronization.<br>"pause": pauses synchronization.<br>"stop": stops synchronization.<br>"continue": continues synchronization. |

##### Usage Guidelines

None

##### Example

Start synchronizing HyperCopy consistency group "7".

```text
admin:/>change hyper_copy_consistency_group synchronize hyper_copy_consistency_group_id_list=7 action=start
WARNING: You are about to synchronize HyperCopy consistency group. This operation uses data of source objects in HyperCopy pairs to overwrite data of target objects. Before performing this operation, ensure that target objects of HyperCopy pairs are not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. To retain the data of a target object, back it up first.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity of the source objects.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change HyperCopy consistency group synchronize 7 successfully.
```

Stop synchronizing HyperCopy consistency group "7".

```text
admin:/>change hyper_copy_consistency_group synchronize hyper_copy_consistency_group_id_list=7 action=stop
DANGER: You are about to stop synchronizing data from source objects to target objects in HyperCopy consistency group. This operation will cause data of target objects in HyperCopy pairs to be unavailable.
Suggestion: Before performing this operation, ensure that data of target objects in HyperCopy pairs is no longer needed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change HyperCopy consistency group synchronize 7 successfully.
```

##### System Response

None
