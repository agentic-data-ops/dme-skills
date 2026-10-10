# change clone restore


##### Function

The **change clone restore** command is used to start, stop, pause, and resume full or differential reverse synchronization of the clone pair.

##### Format

**change clone restore** { clone_id=? action=? \| clone_name=? action=? } restore_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_id=? | ID of a clone pair. | You can run the show clone general command to obtain the value. |
| clone_name=? | Name of a clone pair. | You can run the show clone general command to obtain the value. |
| action=? | Reverse synchronization action. | The value can be "start", "pause", "stop", or "continue", where: <br>"start": starts reverse synchronization.<br>"pause": pauses reverse synchronization.<br>"stop": stops reverse synchronization.<br>"continue": continues copying. |
| restore_type=? | Reverse synchronization type. | The value can be "fullcopy" or "diffcopy", where: <br>"fullcopy": full copy.<br>"diffcopy": differentiated copy. |

##### Usage Guidelines

-   Before performing this operation, ensure that you have entered the correct clone pair ID.
-   This operation is available only when the clone pair is not in a clone consistency group. To check it, run the "show clone general" command.

##### Example

Start full reverse synchronization of clone pair "7".

```text
admin:/>change clone restore clone_id=7 action=start restore_type=fullcopy
WARNING: You are about to reverse synchronize the clone pair. This operation will use the target object data to overwrite source object data. Before performing this operation, ensure that the source object is not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. To retain data of a source object, back it up first.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity of the target object.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Stop full reverse synchronization of clone pair "7".

```text
admin:/>change clone restore clone_id=7 action=stop
DANGER: You are about to stop reverse synchronizing data of the target object in the clone pair to the source object. This operation will cause data of the source object in the HyperCopy pair to be unavailable.
Suggestion: Before performing this operation, ensure that data of the source object in the clone pair is no longer needed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
