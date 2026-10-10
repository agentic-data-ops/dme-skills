# show hyper_copy_consistency_group hyper_copy


##### Function

The **show hyper_copy_consistency_group hyper_copy** command is used to query information about members in a HyperCopy consistency group.

##### Format

**show hyper_copy_consistency_group hyper_copy** hyper_copy_consistency_group_id=?

##### Parameters

| Parameter                       | Description                     | Value                                                                 |
|---------------------------------|---------------------------------|-----------------------------------------------------------------------|
| hyper_copy_consistency_group_id | HyperCopy consistency group ID. | To obtain the value, run "show hyper_copy_consistency_group general". |

##### Usage Guidelines

None

##### Example

Query information about members in HyperCopy consistency group "1".

```text
admin:/>show hyper_copy_consistency_group hyper_copy hyper_copy_consistency_group_id=1
ID   Name  Source ID  Source Type   Target ID  Health Status  Running Status  Copy Speed  HyperCopy Cg ID  Sync Start Time  Sync End Time
---  ----  ---------  -----------   ---------  -------------  --------------   ----------  ----------------  ---------------  -------------
2    cl       0          LUN           2         Normal      Unsynchronized        Middle        1              --               --
4    cl1      1          LUN           4         Normal      Unsynchronized        Middle        1              --               --
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                                              |
|-----------------|----------------------------------------------------------------------|
| ID              | HyperCopy pair ID.                                                   |
| Name            | HyperCopy pair name.                                                 |
| Source ID       | ID of a HyperCopy pair source object, including a LUN or a snapshot. |
| Source Type     | Source object type.                                                  |
| Target ID       | ID of a HyperCopy pair target object (only LUN supported).           |
| Health Status   | Health status of a HyperCopy pair.                                   |
| Running Status  | Running status of a HyperCopy pair.                                  |
| Copy Speed      | Copy speed.                                                          |
| HyperCopy Cg ID | HyperCopy consistency group ID.                                      |
| Sync Start Time | Synchronization start time.                                          |
| Sync End Time   | Synchronization end time.                                            |
