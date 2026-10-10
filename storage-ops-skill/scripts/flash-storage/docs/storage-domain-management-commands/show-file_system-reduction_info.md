# show file_system reduction_info


##### Function

The **show file_system reduction_info** command is used to query capacity reduction information about a file system.

##### Format

**show file_system reduction_info** file_system_id=?

##### Parameters

| Parameter      | Description     | Value |
|----------------|-----------------|-------|
| file_system_id | File system ID. | \-    |

##### Usage Guidelines

None

##### Example

Query the capacity reduction information of the file system whose ID is "1".

```text
admin:/>show file_system reduction_info file_system_id=1

Total Write Capacity                : 1073741824
Reduction Ratio                     : 3.97:1
Shared Capacity Before Reduction    : 804593664
Shared Capacity After Reduction     : 134688979
Exclusive Capacity Before Reduction : 269148160
Exclusive Capacity After Reduction  : 135588352
Incompressible Capacity             : 0
Shared Capacity Ratio               : 74.93%
Exclusive Capacity Ratio            : 25.06%
Incompressible Ratio                : 0.00%
```

##### System Response

The following table describes the parameter meanings.

| Parameter                           | Meaning                                  |
|-------------------------------------|------------------------------------------|
| Total Write Capacity                | Total write capacity.                    |
| Reduction Ratio                     | Capacity reduction ratio.                |
| Shared Capacity Before Reduction    | Shared capacity before reduction.        |
| Shared Capacity After Reduction     | Shared capacity after reduction.         |
| Exclusive Capacity Before Reduction | Exclusive capacity before reduction.     |
| Exclusive Capacity After Reduction  | Exclusive capacity after reduction.      |
| Incompressible Capacity             | Non-compressible capacity.               |
| Shared Capacity Ratio               | Percentage of shared capacity.           |
| Exclusive Capacity Ratio            | Percentage of exclusive capacity.        |
| Incompressible Ratio                | Percentage of non-compressible capacity. |
