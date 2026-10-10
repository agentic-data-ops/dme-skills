# create smart_cache_partition


##### Function

The **create smart_cache_partition** command is used to create a SmartCache partition.

##### Format

**create smart_cache_partition** name=? \[ smart_cache_pool_name=? \| smart_cache_pool_id=? \]

##### Parameters

| Parameter               | Description                | Value                                                                                                              |
|-------------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------|
| name=?                  | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), hyphens (-), and periods (.). |
| smart_cache_pool_name=? | SmartCache pool name.      | The value contains 1 to 255 characters, including letters, digits, underscores (\_), hyphens (-), and periods (.). |
| smart_cache_pool_id=?   | SmartCache pool ID.        | The value ranges from 1 to 16.                                                                                     |

##### Usage Guidelines

None

##### Example

Create a SmartCache partition in the SmartCache pool named "sc".

```text
admin:/>create smart_cache_partition name=newpartition smart_cache_pool_name=sc
Command executed successfully.
```

Create a SmartCache partition in the SmartCache pool with ID "1".

```text
admin:/>create smart_cache_partition name=newpartition smart_cache_pool_id=1
Command executed successfully.
```

##### System Response

None
