# add smart_cache_pool


##### Function

The **add smart_cache_pool** command is used to add disks to a specified SmartCache pool.

##### Format

**add smart_cache_pool** \[ id=? \| name=? \] disk_list=?

##### Parameters

| Parameter | Description                     | Value                                                                                                              |
|-----------|---------------------------------|--------------------------------------------------------------------------------------------------------------------|
| disk_list | ID list of associated disks.    | \-                                                                                                                 |
| id        | ID of a SmartCache pool.        | The value ranges from 1 to 16.                                                                                     |
| name=?    | Name of a SmartCache partition. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

Running the "**add smart_cache_pool**" command requires you to enter the ID or name of a SmartCache pool and ID list of disks to be added.

##### Example

Add disks to the SmartCache pool whose ID is "2".

```text
admin:/>add smart_cache_pool disk_list=DAE058.2 id=2
Command executed successfully.
```

Add disks to the SmartCache pool whose name is "aaa".

```text
admin:/>add smart_cache_pool disk_list=DAE058.3 name=aaa
Command executed successfully.
```

##### System Response

None
