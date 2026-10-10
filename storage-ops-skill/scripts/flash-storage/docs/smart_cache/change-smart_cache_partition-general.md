# change smart_cache_partition general


##### Function

The **change smart_cache_partition general** command is used to change the name of a SmartCache partition.

##### Format

**change smart_cache_partition general** \[ id=? \| name=? \] new_name=?

##### Parameters

| Parameter | Description                         | Value                                                                                                              |
|-----------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| name      | Old name of a SmartCache partition. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |
| id        | SmartCache partition ID.            | The value ranges from 1 to 16.                                                                                     |
| new_name  | New name of a SmartCache partition. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

To run the "**change smart_cache_partition general**" command, you need to specify the old and new names of the SmartCache partition.

##### Example

Change the name of the SmartCache partition with ID "1" to a new one.

```text
admin:/>change smart_cache_partition general id=1 new_name=nscp
Command executed successfully.
```

Change the name of the SmartCache partition with name "scp" to a new one.

```text
admin:/>change smart_cache_partition general name=scp new_name=nscp
Command executed successfully.
```

##### System Response

None
