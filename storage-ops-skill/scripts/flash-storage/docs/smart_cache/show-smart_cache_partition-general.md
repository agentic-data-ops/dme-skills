# show smart_cache_partition general


##### Function

The **show smart_cache_partition general** command is used to query SmartCache partitions.

##### Format

**show smart_cache_partition general** \[ name=? \| id=? \]

##### Parameters

| Parameter | Description                | Value                                                                                                              |
|-----------|----------------------------|--------------------------------------------------------------------------------------------------------------------|
| id=?      | SmartCache partition ID.   | The value ranges from 1 to 16.                                                                                     |
| name=?    | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

None

##### Example

Query all SmartCache partitions.

```text
admin:/>show smart_cache_partition general
ID  Name    SmartCache Pool ID  SmartCache Pool Name  Read Hit Count  Read Hit Ratio  Free Capacity  Total Capacity  User Consumed Capacity  User Consumed Capacity Percentage
--  ------  ------------------  --------------------  --------------  --------------  -------------  --------------  ----------------------  ---------------------------------
2   isssxa  1                   scp                   0               0                   100.000GB       100.000GB                  0.000B  0
```

Query the SmartCache partition with ID "2".

```text
admin:/>show smart_cache_partition general id=2
ID                                : 2
Name                              : isssxa
SmartCache Pool ID                : 1
SmartCache Pool Name              : scp
Read Hit Count                    : 0
Read Hit Ratio                    : 0
Free Capacity                     : 100.000GB
Total Capacity                    : 100.000GB
User Consumed Capacity            : 0.000B
User Consumed Capacity Percentage : 0
```

Query basic information about the SmartCache partition with name "isssxa".

```text
admin:/>show smart_cache_partition general name=isssxa
ID                                : 2
Name                              : isssxa
SmartCache Pool ID                : 1
SmartCache Pool Name              : scp
Read Hit Count                    : 0
Read Hit Ratio                    : 0
Free Capacity                     : 100.000GB
Total Capacity                    : 100.000GB
User Consumed Capacity            : 0.000B
User Consumed Capacity Percentage : 0
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
| Total Capacity                    | Total capacity of the SmartCache partition.                            |
| User Consumed Capacity            | Used capacity of the SmartCache partition.                             |
| User Consumed Capacity Percentage | Used capacity ratio of the SmartCache partition.                       |
