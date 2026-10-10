# show lun protection


##### Function

The **show lun protection** command is used to query protect information about the specified LUNs of the storage system.

##### Format

**show lun protection** \[ lun_id_list=? \| lun_name_list=? \]

##### Parameters

| Parameter     | Description                                                                          | Value                                                                                                                                                                                                                                                                                                     |
|---------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lun_id_list=? | LUN ID list. This parameter cannot be used along with the lun_name_list=? parameter. | Multiple LUN IDs are separated by commas (,), or an ID range is represented using a hyphen(-).                                                                                                                                                                                                            |
| lun_name_list | LUN name list. This parameter cannot be used along with the lun_id_list=? parameter. | Separate multiple LUN names using commas (,), or use a hyphen (-) to separate two LUN names to represent a LUN range. For a LUN range, the two names before and after the hyphen (-) must be of the same format and length, and the two names before and after the hyphen (-) cannot contain hyphens (-). |

##### Usage Guidelines

None

##### Example

Query information about the specified LUNs whose IDs from 0 to 2.

```text
admin:/>show lun protection lun_id_list=0-2
Name  ID  Snapshots  Clone Pairs  HyperCDP Objects  Remote Replication Pairs  HyperMetro Pairs  DR Star Trios
----  --  ---------  -----------  ----------------  ------------------------  ----------------  -------------
l1    0   0          0            0                 0                         0                 0
l2    1   0          0            0                 0                         0                 0
l3    2   0          0            0                 0                         0                 0
```

Query information about the specified LUNs whose names are "l1", "l2", and "l3".

```text
admin:/>show lun protection lun_name_list=l1,l2,l3
Name  ID  Snapshots  Clone Pairs  HyperCDP Objects  Remote Replication Pairs  HyperMetro Pairs  DR Star Trios
----  --  ---------  -----------  ----------------  ------------------------  ----------------  -------------
l1    0   0          0            0                 0                         0                 0
l2    1   0          0            0                 0                         0                 0
l3    2   0          0            0                 0                         0                 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                | Meaning                                      |
|--------------------------|----------------------------------------------|
| Name                     | LUN name.                                    |
| ID                       | LUN ID.                                      |
| Snapshots                | Number of snapshots of a LUN.                |
| Clone Pairs              | Number of clone pairs of a LUN.              |
| HyperCDP Objects         | Number of HyperCDP objects of a LUN.         |
| Remote Replication Pairs | Number of remote replication pairs of a LUN. |
| HyperMetro Pairs         | Number of HyperMetro pairs of a LUN.         |
| DR Star Trios            | Number of DR Star trios of a LUN.            |
