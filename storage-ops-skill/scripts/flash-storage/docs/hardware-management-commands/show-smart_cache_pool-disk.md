# show smart_cache_pool disk


##### Function

The **show smart_cache_pool disk** command is used to query disks in a SmartCache pool.

##### Format

**show smart_cache_pool disk** \[ smart_cache_pool_name=? \| smart_cache_pool_id=? \]

##### Parameters

| Parameter             | Description           | Value                                                                                                              |
|-----------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------|
| smart_cache_pool_id   | SmartCache pool ID.   | The value ranges from 1 to 16.                                                                                     |
| smart_cache_pool_name | SmartCache pool name. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

None.

##### Example

Query disks in the SmartCache pool whose ID is "1".

```text
admin:/>show smart_cache_pool disk smart_cache_pool_id=1
ID       Health Status  Running Status  Type     Capacity   Logic Type
-------  -------------  --------------  -------  ---------  ----------
CTE0.10  Normal         Online          SCM SSD  185.747GB  Cache Disk
```

Query disks in the SmartCache pool whose name is "scp".

```text
admin:/>show smart_cache_pool disk smart_cache_pool_name=scp
ID       Health Status  Running Status  Type     Capacity   Logic Type
-------  -------------  --------------  -------  ---------  ----------
CTE0.11  Normal         Online          SCM SSD  185.747GB  Cache Disk
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                              |
|----------------|------------------------------------------------------|
| ID             | Disk ID.                                             |
| Health Status  | Health status of a disk.                             |
| Running Status | Running status of a disk.                            |
| Type           | Disk type. The value can be "3" (SSD) or "17" (SCM). |
| Capacity       | Disk capacity.                                       |
| Logic Type     | Logic type.                                          |
