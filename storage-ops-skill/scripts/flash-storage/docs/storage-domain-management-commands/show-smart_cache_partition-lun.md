# show smart_cache_partition lun


##### Function

The **show smart_cache_partition lun** command is used to query LUNs in a SmartCache partition.

##### Format

**show smart_cache_partition lun** \[ smart_cache_partition_id=? \| smart_cache_partition_name=? \]

##### Parameters

| Parameter                    | Description                | Value                                                                                                              |
|------------------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------|
| smart_cache_partition_id=?   | SmartCache partition ID.   | The value ranges from 1 to 16.                                                                                     |
| smart_cache_partition_name=? | SmartCache partition name. | The value contains 1 to 255 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

None

##### Example

Query LUNs in the SmartCache partition by partition ID "1".

```text
admin:/>show smart_cache_partition lun smart_cache_partition_id=1
ID  Name    Storage Pool ID  Capacity   Health Status  Running Status  Type    WWN                               SmartCache Partition ID  SmartCache Partition Hit Ratio
--  ------  ---------------  ---------  -------------  --------------  ------  --------------------------------  -----------------------  ------------------------------
2   lun1    1                100.000GB  Normal         Online          Thick   63334371003638390003c20c00000000  1                        0
```

Query LUNs in the SmartCache partition by partition name "scp".

```text
admin:/>show smart_cache_partition lun smart_cache_partition_name=scp
ID  Name    Storage Pool ID  Capacity   Health Status  Running Status  Type    WWN                               SmartCache Partition ID  SmartCache Partition Hit Ratio
--  ------  ---------------  ---------  -------------  --------------  ------  --------------------------------  -----------------------  ------------------------------
2   lun1    1                100.000GB  Normal         Online          Thick   63334371003638390003c20c00000000  1                        0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                      | Meaning                           |
|--------------------------------|-----------------------------------|
| ID                             | LUN ID.                           |
| Name                           | LUN name.                         |
| Storage Pool ID                | Storage pool ID.                  |
| Capacity                       | LUN capacity.                     |
| Health Status                  | Health status.                    |
| Running Status                 | Running status.                   |
| Type                           | LUN type.                         |
| WWN                            | World Wide Name (WWN) of the LUN. |
| SmartCache Partition ID        | SmartCache partition ID.          |
| SmartCache Partition Hit Ratio | SmartCache partition hit ratio.   |
