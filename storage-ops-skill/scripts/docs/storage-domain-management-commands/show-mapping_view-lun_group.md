# show mapping_view lun_group


##### Function

The **show mapping_view lun_group** command is used to query LUN groups in a mapping view.

##### Format

**show mapping_view lun_group** { mapping_view_id=? \| mapping_view_name=? }

##### Parameters

| Parameter           | Description        | Value                                                 |
|---------------------|--------------------|-------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.   | To obtain the value, run "show mapping_view general". |
| mapping_view_name=? | Mapping view name. | To obtain the value, run "show mapping_view general". |

##### Usage Guidelines

None.

##### Example

Query LUN groups in the mapping view whose ID is "1".

```text
admin:/>show mapping_view lun_group mapping_view_id=1

LUN Group ID  LUN Group Name
------------  --------------
1             lun_group_001
```

Query LUN groups in the mapping view whose name is "map01".

```text
admin:/>show mapping_view lun_group mapping_view_name=map01

LUN Group ID  LUN Group Name
------------  --------------
1             lun_group_001
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning              |
|----------------|----------------------|
| LUN Group ID   | ID of a LUN group.   |
| LUN Group Name | Name of a LUN group. |
