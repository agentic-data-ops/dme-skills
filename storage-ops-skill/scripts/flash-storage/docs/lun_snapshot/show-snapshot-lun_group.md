# show snapshot lun_group


##### Function

The **show snapshot lun_group** command is used to query information about the LUN group that is associated with a snapshot.

##### Format

**show snapshot lun_group** { snapshot_id=? \| snapshot_name=? }

##### Parameters

| Parameter       | Description    | Value                                             |
|-----------------|----------------|---------------------------------------------------|
| snapshot_id=?   | Snapshot ID.   | To obtain the value, run "show snapshot general". |
| snapshot_name=? | Snapshot name. | To obtain the value, run "show snapshot general". |

##### Usage Guidelines

None

##### Example

Query information about the LUN group that is associated with snapshot "0".

```text
admin:/>show snapshot lun_group snapshot_id=0

LUN Group ID  LUN Group Name
------------  --------------
0             LUNGroup000
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                |
|----------------|------------------------|
| LUN Group ID   | ID of the LUN group.   |
| LUN Group Name | Name of the LUN group. |
