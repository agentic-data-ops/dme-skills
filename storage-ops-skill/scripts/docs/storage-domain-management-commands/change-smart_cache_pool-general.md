# change smart_cache_pool general


##### Function

The **change smart_cache_pool general** command is used to change the name of a SmartCache pool.

##### Format

**change smart_cache_pool general** \[ id=? \| name=? \] new_name=?

##### Parameters

| Parameter | Description                    | Value                                                                                                              |
|-----------|--------------------------------|--------------------------------------------------------------------------------------------------------------------|
| name      | Old name of a SmartCache pool. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |
| id        | ID of a SmartCache pool.       | The value ranges from 1 to 16.                                                                                     |
| new_name  | New name of a SmartCache pool. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

To run the "**change smart_cache_pool general**" command, you need to specify the old and new names of the SmartCache pool.

##### Example

Change the name of the SmartCache pool with ID "1" to a new one.

```text
admin:/>change smart_cache_pool general id=1 new_name=nsc
Command executed successfully.
```

Change the name of the SmartCache pool with name "sc" to a new one.

```text
admin:/>change smart_cache_pool general name=sc new_name=nsc
Command executed successfully.
```

##### System Response

None
