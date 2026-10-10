# delete smart_cache_partition


##### Function

The **delete smart_cache_partition** command is used to delete a SmartCache partition.

##### Format

**delete smart_cache_partition** \[ name=? \| id=? \]

##### Parameters

| Parameter | Description                | Value                                                                                                              |
|-----------|----------------------------|--------------------------------------------------------------------------------------------------------------------|
| name=?    | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |
| id=?      | SmartCache partition ID.   | The value ranges from 1 to 16.                                                                                     |

##### Usage Guidelines

None

##### Example

Delete a SmartCache partition named "scp".

```text
admin:/>delete smart_cache_partition name=scp
WARNING: You are about to delete a SmartCache partition.
Suggestion: Before performing this operation, ensure that the correct SmartCache partition ID or name is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete a SmartCache partition with ID "1".

```text
admin:/>delete smart_cache_partition id=1
WARNING: You are about to delete a SmartCache partition.
Suggestion: Before performing this operation, ensure that the correct SmartCache partition ID or name is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
