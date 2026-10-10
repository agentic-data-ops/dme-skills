# delete smart_cache_pool


##### Function

The **delete smart_cache_pool** command is used to delete a SmartCache pool.

##### Format

**delete smart_cache_pool** \[ id=? \| name=? \]

##### Parameters

| Parameter | Description                | Value                                                                                                                    |
|-----------|----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| id        | ID of a SmartCache pool.   | The value ranges from 1 to 16.                                                                                           |
| name      | Name of a SmartCache pool. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

Running the "**delete smart_cache_pool**" command requires you to enter the ID or name of a SmartCache pool.

##### Example

Delete the SmartCache pool whose ID is "1".

```text
admin:/>delete smart_cache_pool id=1
WARNING: You are about to delete the SmartCache pool.
Suggestion: Ensure that the correct SmartCache pool ID or name is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the SmartCache pool whose name is "newsmartcache".

```text
admin:/>delete smart_cache_pool name=newsmartcache
WARNING: You are about to delete the SmartCache pool.
Suggestion: Ensure that the correct SmartCache pool ID or name is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
