# show smart_cache_partition file_system


##### Function

The **show smart_cache_partition file_system** command is used to query file systems in a SmartCache partition.

##### Format

**show smart_cache_partition file_system** \[ smart_cache_partition_id=? \| smart_cache_partition_name=? \]

##### Parameters

| Parameter                    | Description                | Value                                                                                                              |
|------------------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------|
| smart_cache_partition_id=?   | SmartCache partition ID.   | The value ranges from 1 to 16.                                                                                     |
| smart_cache_partition_name=? | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query file systems in the SmartCache partition by partition ID "1".

```text
admin:/>show smart_cache_partition file_system smart_cache_partition_id=1
ID  Name    Storage Pool ID  Capacity   Health Status  Running Status  SmartCache Partition ID  SmartCache Partition Hit Ratio
--  ------  ---------------  ---------  -------------  --------------  -----------------------  ------------------------------
2   fs1     1                100.000GB  Normal         Online          1                        0
```

Query file systems in the SmartCache partition by partition name "scp".

```text
admin:/>show smart_cache_partition file_system smart_cache_partition_name=scp
ID  Name    Storage Pool ID  Capacity   Health Status  Running Status  SmartCache Partition ID  SmartCache Partition Hit Ratio
--  ------  ---------------  ---------  -------------  --------------  -----------------------  ------------------------------
2   fs1     1                100.000GB  Normal         Online          1                        0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                      | Meaning                                                  |
|--------------------------------|----------------------------------------------------------|
| ID                             | File system ID.                                          |
| Name                           | File system name.                                        |
| Storage Pool ID                | ID of the storage pool to which the file system belongs. |
| Capacity                       | File system capacity.                                    |
| Health Status                  | Health status.                                           |
| Running Status                 | Running status.                                          |
| SmartCache Partition ID        | SmartCache partition ID.                                 |
| SmartCache Partition Hit Ratio | SmartCache partition hit ratio.                          |
