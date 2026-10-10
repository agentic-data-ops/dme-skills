# show snapshot_consistency_group snapshot


##### Function

The **show snapshot_consistency_group snapshot** command is used to query information about member snapshots in a specified snapshot consistency group.

##### Format

**show snapshot_consistency_group snapshot** { snapshot_consistency_group_id=? \| snapshot_consistency_group_name=? } \[ snapshot_name_list=? \| snapshot_id_list=? \]

##### Parameters

| Parameter                         | Description                                                                    | Value                                                                                                                                                                                                                      |
|-----------------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| snapshot_consistency_group_id=?   | ID of the snapshot consistency group whose member snapshots are to be queried. | To obtain the value, run the "show snapshot_consistency_group general" command.                                                                                                                                            |
| snapshot_consistency_group_name=? | Name of a snapshot consistency group.                                          | To obtain the value, run the "show snapshot_consistency_group general" command.                                                                                                                                            |
| snapshot_id_list                  | Snapshot ID list.                                                              | Multiple IDs are separated by commas (,), or an ID range is represented using a hyphen(-).                                                                                                                                 |
| snapshot_name_list                | Snapshot name list.                                                            | LUN names are separated by commas (,) or name range is represented using a hyphen(-). The length of the LUN name between a hyphen (-) must be the same as that after a hyphen, and no hyphen (-) is allowed in a LUN name. |

##### Usage Guidelines

None

##### Example

Query information about member snapshots in the snapshot consistency group whose ID is "2".

```text
admin:/>show snapshot_consistency_group snapshot snapshot_consistency_group_id=2
ID    Name                  Source LUN ID  Source LUN Name       Health Status  Running Status  WWN                               Time Stamp
----  --------------------  -------------  --------------------  -------------  --------------  --------------------------------  -----------------------------
2  YvPlaR_445h853330000  1249           Ky_443W543240001      Normal         Activated       694049c100d95366002fbcf2000004e3  2018-04-26/08:39:43 UTC+08:00
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                              |
|-----------------|--------------------------------------|
| ID              | ID of a snapshot.                    |
| Name            | Name of a snapshot.                  |
| Source LUN ID   | Source LUN ID of a snapshot.         |
| Source LUN Name | Source LUN name of a snapshot.       |
| Health Status   | Health status of a snapshot.         |
| Running Status  | Running status of a snapshot.        |
| WWN             | World wide name (WWN) of a snapshot. |
| Time Stamp      | Time when the snapshot is activated. |
