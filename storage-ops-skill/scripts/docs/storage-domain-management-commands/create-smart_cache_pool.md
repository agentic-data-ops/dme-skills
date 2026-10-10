# create smart_cache_pool


##### Function

The creat smart_cache_pool command is used to create a SmartCache pool.

##### Format

**create smart_cache_pool** disk_list=? name=? \[ id=? \] \[ smart_cache_partition_name=? \]

##### Parameters

| Parameter                  | Description                  | Value                                                                                                                    |
|----------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| disk_list                  | ID list of associated disks. | \-                                                                                                                       |
| name                       | Name of a SmartCache pool.   | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |
| id                         | ID of a SmartCache pool.     | The value is an integer ranging from 1 to 16.                                                                            |
| smart_cache_partition_name | SmartCache partition name.   | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-).       |

##### Usage Guidelines

Running the "creat smart_cache_pool" command requires you to enter the ID list of disks used to create a SmartCache pool and the name and ID of the SmartCache pool.

##### Example

Select disks whose IDs range from DAE000.0 to DAE000.7 to create a SmartCache pool and set its ID to "1".

```text
admin:/>create smart_cache_pool disk_list=DAE000.0-7 name=newsmartcache id=1
Command executed successfully.
```

Select disks whose IDs range from DAE000.0 to DAE000.7 to create a SmartCache pool. The ID of the SmartCache pool is not specified.

```text
admin:/>create smart_cache_pool disk_list=DAE000.0-7 name=newsmartcache
Command executed successfully.
```

Select disks with IDs from DAE000.0 to DAE000.7 to create a SmartCache pool, and set the SmartCache ID to "1" and the SmartCache partition name to "newscp".

```text
admin:/>create smart_cache_pool disk_list=DAE000.0-7 name=newsmartcache id=1 smart_cache_partition_name=newscp
Command executed successfully.
```

##### System Response

None
