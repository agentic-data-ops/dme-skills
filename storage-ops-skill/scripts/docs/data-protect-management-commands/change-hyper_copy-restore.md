# change hyper_copy restore


##### Function

The **change hyper_copy restore** command is used to start, stop, pause, and resume full or differential reverse synchronization of the HyperCopy pair.

##### Format

**change hyper_copy restore** hyper_copy_id=? action=? restore_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hyper_copy_id | HyperCopy pair ID. | To obtain the value, run "show hyper_copy general". |
| restore_type | Reverse synchronization type. | The value can be "fullcopy" or "diffcopy", where: <br>"fullcopy": full copy.<br>"diffcopy": differential copy. |
| action | Reverse synchronization action. | The value can be "start", "pause", "stop", or "continue", where: <br>"start": starts synchronization.<br>"pause": pauses synchronization.<br>"stop": stops synchronization.<br>"continue": continues the copy. |

##### Usage Guidelines

-   Before performing this operation, ensure that you have entered the correct HyperCopy pair ID.
-   This operation is available only when the HyperCopy pair is not in a HyperCopy consistency group. To check it, run the "show hyper_copy general" command.

##### Example

Start full reverse synchronization of HyperCopy pair "7".

```text
admin:/>change hyper_copy restore hyper_copy_id=7 action=start restore_type=fullcopy
WARNING: You are about to restore HyperCopy pair. This operation uses the target object data to overwrite the source object data. Before performing this operation, ensure that the source object is not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. To retain the data of the current source object, back up the source object data first.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity of the target object.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Stop full reverse synchronization of HyperCopy pair "7".

```text
admin:/>change hyper_copy restore hyper_copy_id=7 action=stop
DANGER: You are about to stop restoring data of the target object in HyperCopy pair to the source object. This operation will cause data of the source object in the HyperCopy pair to be unavailable.
Suggestion: Before performing this operation, ensure that data of the source object in the HyperCopy pair is no longer needed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
