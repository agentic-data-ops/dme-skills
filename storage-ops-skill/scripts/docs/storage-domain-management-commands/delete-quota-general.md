# delete quota general


##### Function

The **delete quota general** command is used to delete a quota of a file system, or a quota of a specified dtree.

##### Format

**delete quota general** quota_id=?

##### Parameters

| Parameter  | Description | Value                                                      |
|------------|-------------|------------------------------------------------------------|
| quota_id=? | Quota ID.   | To obtain the value, run the "show quota general" command. |

##### Usage Guidelines

Specifying parameter "quota_id" deletes the quota of the specified ID.

##### Example

Delete the quota of ID "3@4097@5".

```text
admin:/>delete quota general quota_id=3@4097@5
WARNING: You are about to delete quota. After this operation, all configurations of this quota are deleted, and space and number of files controlled by the quota are no longer limited.
Suggestion:Before performing this operation, you are advised to ensure that the selected quota type is correct.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
