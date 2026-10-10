# change hyper_copy synchronize


##### Function

The **change hyper_copy synchronize** command is used to start, stop, pause, and continue HyperCopy pair synchronization.

##### Format

**change hyper_copy synchronize** hyper_copy_id=? action=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hyper_copy_id | HyperCopy pair ID. | To obtain the value, run "show hyper_copy general". |
| action | Synchronization action. | The value can be "start", "pause", "stop", or "continue", where: <br>"start": starts synchronization.<br>"pause": pauses synchronization.<br>"stop": stops synchronization.<br>"continue": continues the copy. |

##### Usage Guidelines

-   Before performing this operation, ensure that you have entered the correct HyperCopy pair ID.
-   This operation is available only when the HyperCopy pair is not in a HyperCopy consistency group. To check it, run the "show hyper_copy general" command.

##### Example

Start synchronizing the HyperCopy pair whose ID is "7".

```text
admin:/>change hyper_copy synchronize hyper_copy_id=7 action=start
WARNING: You are about to synchronize HyperCopy pair. This operation uses the source object data to overwrite the target object data. Before performing this operation, ensure that the target object is not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. To retain the data of the current target object, back up the target object data first.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity of the source object.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Stop synchronizing the HyperCopy pair whose ID is "7".

```text
admin:/>change hyper_copy synchronize hyper_copy_id=7 action=stop
DANGER: You are about to stop synchronizing data of the source object in HyperCopy pair to the target object. This operation will cause data of the target object to be unavailable.
Suggestion: Before performing this operation, ensure that data of the target object in the HyperCopy pair is no longer needed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
