# change snapshot cancel_restore


##### Function

The **change snapshot cancel_restore** command is used to cancel the rollback of a snapshot.

##### Format

**change snapshot cancel_restore** { snapshot_id=? \| snapshot_name=? }

##### Parameters

| Parameter       | Description    | Value                                             |
|-----------------|----------------|---------------------------------------------------|
| snapshot_id=?   | Snapshot ID.   | To obtain the value, run "show snapshot general". |
| snapshot_name=? | Snapshot name. | To obtain the value, run "show snapshot general". |

##### Usage Guidelines

None

##### Example

Cancel the rollback of snapshot "1".

```text
admin:/>change snapshot cancel_restore snapshot_id=1
DANGER: You are about to stop rolling back the data on snapshot to target object. This operation will cause the data on the target object to be unavailable.
Suggestion: Before performing this operation, ensure that data on the target object is no longer necessary.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
