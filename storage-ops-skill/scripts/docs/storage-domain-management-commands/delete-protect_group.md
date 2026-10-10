# delete protect_group


##### Function

The **delete protect_group** command is used to delete specified protected groups.

##### Format

**delete protect_group** protect_group_id=?

##### Parameters

| Parameter        | Description         | Value                                    |
|------------------|---------------------|------------------------------------------|
| protect_group_id | Protected group ID. | The value is an integer from 0 to 16383. |

##### Usage Guidelines

If a protected group has LUNs, remove all LUNs from the protected group before deleting it.

##### Example

Delete the protected group whose ID is 5.

```text
admin:/>delete protect_group protect_group_id=5
WARNING: You are about to delete protected group. This operation cannot be undone.
Suggestion: Before performing this operation, ensure that you have correctly selected the protected group and it is no longer required.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
