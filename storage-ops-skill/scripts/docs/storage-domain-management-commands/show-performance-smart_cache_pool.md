# show performance smart_cache_pool


##### Function

The **show performance smart_cache_pool** command is used to query performance information about a SmartCache pool.

##### Format

**show performance smart_cache_pool** \[ smart_cache_pool_id=? \| smart_cache_pool_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smart_cache_pool_id | SmartCache pool ID. | The value ranges from 1 to 16. |
| smart_cache_pool_id_list | SmartCache pool ID list. | To obtain the value, run the "show smart_cache_pool general" command. To query multiple SmartCache pools: <br>Use commas (,) to separate SmartCache pool IDs, for example, "smart_cache_id_list=1,2,3,4,5".<br>Specify SmartCache ID ranges by hyphens (-), for example, "smart_cache_id_list=1-5,7,9-11". |

##### Usage Guidelines

None.

##### Example

Query performance information about the SmartCache pool with ID "1".

```text
admin:/>show performance smart_cache_pool smart_cache_pool_id=1
0.Read SmartCache Hit Ratio(%)
Input item(s) number separated by comma:0
Read SmartCache Hit Ratio(%) : 0
```

Query performance information about SmartCache pools with IDs "1" and "2".

```text
admin:/>show performance smart_cache_pool smart_cache_pool_id_list=1,2
0.Read SmartCache Hit Ratio(%)
Input item(s) number separated by comma:0
ID  Read SmartCache Hit Ratio(%)
--  ----------------------------
1   100
2   44
```

##### System Response

The following table describes the parameter meanings.

| Parameter    | Meaning                         |
|--------------|---------------------------------|
| readHitRatio | SmartCache pool read hit ratio. |
| id           | SmartCache pool ID.             |
