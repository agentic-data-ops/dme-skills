# show smart_cache_pool smart_cache_partition


##### Function

The **show smart_cache_pool smart_cache_partition** command is used to query information about SmartCache partitions in a SmartCache pool.

##### Format

**show smart_cache_pool smart_cache_partition** \[ smart_cache_pool_name=? \| smart_cache_pool_id=? \]

##### Parameters

| Parameter               | Description           | Value                                                                                                              |
|-------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------|
| smart_cache_pool_id=?   | SmartCache pool ID.   | The value ranges from1 to 16.                                                                                      |
| smart_cache_pool_name=? | SmartCache pool name. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

None

##### Example

View information about the SmartCache partition of the SmartCache pool with ID "1".

```text
admin:/>show smart_cache_pool smart_cache_partition smart_cache_pool_id=1
ID  Name    SmartCache Pool ID  SmartCache Pool Name  Read Hit Count  Read Hit Ratio  Free Capacity  Total Capacity  User Consumed Capacity  User Consumed Capacity Percentage
--  ------  ------------------  --------------------  --------------  --------------  -------------  --------------  ----------------------  ---------------------------------
2   isssxa  1                   scp                   0               0                   100.000GB       100.000GB                       0  0
```

View information about the SmartCache partition of the SmartCache pool named "scp".

```text
admin:/>show smart_cache_pool smart_cache_partition smart_cache_pool_name=scp
ID  Name    SmartCache Pool ID  SmartCache Pool Name  Read Hit Count  Read Hit Ratio  Free Capacity  Total Capacity  User Consumed Capacity  User Consumed Capacity Percentage
--  ------  ------------------  --------------------  --------------  --------------  -------------  --------------  ----------------------  ---------------------------------
2   isssxa  1                   scp                   0               0                   100.000GB       100.000GB                       0  0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                         | Meaning                                                                |
|-----------------------------------|------------------------------------------------------------------------|
| ID                                | SmartCache partition ID.                                               |
| Name                              | SmartCache partition name.                                             |
| SmartCache Pool ID                | SmartCache pool ID.                                                    |
| SmartCache Pool Name              | Name of the SmartCache pool where the SmartCache partition is located. |
| Read Hit Count                    | SmartCache partition read hits.                                        |
| Read Hit Ratio                    | SmartCache partition read hit ratio.                                   |
| Free Capacity                     | Free capacity.                                                         |
| Total Capacity                    | Total capacity.                                                        |
| User Consumed Capacity            | Used capacity of the SmartCache partition.                             |
| User Consumed Capacity Percentage | Used capacity ratio of the SmartCache partition.                       |
