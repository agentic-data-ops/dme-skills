# show smart_cache_pool general


##### Function

The **show smart_cache_pool general** command is used to query basic information about a SmartCache pool.

##### Format

show smartcache general

##### Parameters

| Parameter | Description                | Value                                                                                                              |
|-----------|----------------------------|--------------------------------------------------------------------------------------------------------------------|
| id        | ID of a SmartCache pool.   | The value ranges from 1 to 16.                                                                                     |
| name      | Name of a SmartCache pool. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

Running the "**show smart_cache_pool general**" command requires you to enter the ID or name of the SmartCache pool you want to query. If neither the ID nor the name is specified, all SmartCache pools are queried.

##### Example

Query basic information about a SmartCache pool.

```text
admin:/>show smart_cache_pool general
ID  Name    SmartCache Switch  Read Hit Count  Read Hit Ratio  User Free Capacity  User Total Capacity  User Consumed Capacity  User Consumed Capacity Percentage
--  ------  -----------------  --------------  --------------  ------------------  -------------------  ----------------------  ---------------------------------
2   isssxa  open               0               0                          4.021TB              4.021TB                  0.000B  0
```

Query basic information about the SmartCache pool whose ID is "2".

```text
admin:/>show smart_cache_pool general id=2
ID                                : 2
Name                              : isssxa
SmartCache Switch                 : open
Read Hit Count                    : 0
Read Hit Ratio                    : 0
User Free Capacity                : 4.021TB
User Total Capacity               : 4.021TB
User Consumed Capacity            : 0.000B
User Consumed Capacity Percentage : 0
```

Query basic information about the SmartCache pool whose name is "isssxa".

```text
admin:/>show smart_cache_pool general name=isssxa
ID                                : 2
Name                              : isssxa
SmartCache Switch                 : open
Read Hit Count                    : 0
Read Hit Ratio                    : 0
User Free Capacity                : 4.021TB
User Total Capacity               : 4.021TB
User Consumed Capacity            : 0.000B
User Consumed Capacity Percentage : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                         | Meaning                                  |
|-----------------------------------|------------------------------------------|
| ID                                | SmartCache pool ID.                      |
| Name                              | SmartCache pool name.                    |
| SmartCache Switch                 | Whether to enable or disable SmartCache. |
| Read Hit Count                    | Hit times of the read SmartCache.        |
| Read Hit Ratio                    | Read SmartCache hit ratio.               |
| User Free Capacity                | Free SmartCache capacity.                |
| User Total Capacity               | Total SmartCache capacity.               |
| User Consumed Capacity            | Used SmartCache capacity.                |
| User Consumed Capacity Percentage | Percentage of used SmartCache capacity.  |
