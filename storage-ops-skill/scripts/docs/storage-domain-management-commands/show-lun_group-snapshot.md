# show lun_group snapshot


##### Function

The **show lun_group snapshot** command is used to query information about snapshots in a specified LUN group.

##### Format

**show lun_group snapshot** { lun_group_id=? \| lun_group_name=? } \[ snapshot_name_list=? \| snapshot_id_list=? \]

##### Parameters

| Parameter            | Description         | Value                                                                                                                                                                                                                                |
|----------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lun_group_id=?       | ID of a LUN group.  | To obtain the value, run "show lun_group general".                                                                                                                                                                                   |
| lun_group_name=?     | LUN group name.     | To obtain the value, run "show lun_group general".                                                                                                                                                                                   |
| snapshot_id_list=?   | Snapshot ID list.   | Snapshot IDs are separated by commas (,) or hyphens (-).                                                                                                                                                                             |
| snapshot_name_list=? | Snapshot name list. | Snapshot names are separated by commas (,) a snapshot name range is represented by a hyphen (-). The snapshot name between and after a hyphen must be in the same format and length, and a snapshot name cannot contain hyphens (-). |

##### Usage Guidelines

None.

##### Example

Query information about snapshots in the LUN group whose ID is "1".

```text
admin:/>show lun_group snapshot lun_group_id=1
Snapshot ID Snapshot Name Health Status Running Status WWN
----------- ------------- ------------- -------------- --------------------------------
128 snap Normal Inactive 6e097961004dfdd7000e1d7b00000080
```

Query information about snapshots in the LUN group whose name is "LunGroup1".

```text
admin:/>show lun_group snapshot lun_group_name=LunGroup1
Snapshot ID Snapshot Name Health Status Running Status WWN
----------- ------------- ------------- -------------- --------------------------------
128 snap Normal Inactive 6e097961004dfdd7000e1d7b00000080
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                              |
|----------------|--------------------------------------|
| Snapshot ID    | Snapshot ID.                         |
| Snapshot Name  | Snapshot name.                       |
| Health Status  | Health status.                       |
| Running Status | Running status.                      |
| WWN            | World Wide Name (WWN) of a snapshot. |
