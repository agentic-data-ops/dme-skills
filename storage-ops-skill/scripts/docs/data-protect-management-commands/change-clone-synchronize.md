# change clone synchronize


##### Function

The **change clone synchronize** command is used to start, stop, pause, and continue clone pair synchronization.

##### Format

**change clone synchronize** { clone_id=? \| clone_name=? } action=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_id=? | ID of a clone pair. | You can run the show clone general command to obtain the value. |
| clone_name=? | Name of a clone pair. | You can run the show clone general command to obtain the value. |
| action=? | Synchronization action. | The value can be "start", "pause", "stop", or "continue", where: <br>"start": starts synchronization.<br>"pause": pauses synchronization.<br>"stop": stops synchronization.<br>"continue": continues synchronization. |

##### Usage Guidelines

-   Before performing this operation, ensure that you have entered the correct clone pair ID.
-   This operation is available only when the clone pair is not in a clone consistency group. To check it, run the "show clone general" command.

##### Example

Start synchronizing the clone pair whose ID is "7".

```text
admin:/>change clone synchronize clone_id=7 action=start
WARNING: You are about to synchronize the clone pair. This operation will use the source object data to overwrite target object data. Before performing this operation, ensure that the target object is not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. To retain data of a target object, back it up first.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity of the source object.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Stop synchronizing the clone pair whose ID is "7".

```text
admin:/>change clone synchronize clone_id=7 action=stop
DANGER: You are about to stop synchronizing data of the source object in the clone pair to the target object. This operation will cause data of the target object to be unavailable.
Suggestion: Before performing this operation, ensure that data of the target object in the clone pair is no longer needed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
