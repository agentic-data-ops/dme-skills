# show lun_group mapping_view


##### Function

The **show lun_group mapping_view** command is used to query information about a mapping view related to a specified LUN group.

##### Format

**show lun_group mapping_view** { lun_group_id=? \| lun_group_name=? }

##### Parameters

| Parameter        | Description          | Value                                              |
|------------------|----------------------|----------------------------------------------------|
| lun_group_id=?   | ID of a LUN group.   | To obtain the value, run "show lun_group general". |
| lun_group_name=? | Name of a LUN group. | To obtain the value, run "show lun_group general". |

##### Usage Guidelines

None

##### Example

Query information about a mapping view related to LUN group "0".

```text
admin:/>show lun_group mapping_view lun_group_id=0

Mapping View ID  Mapping View Name
---------------  -----------------
0                MappingTest
```

Query information about a mapping view related to LUN group "LunGroup1".

```text
admin:/>show lun_group mapping_view lun_group_name=LunGroup1

Mapping View ID  Mapping View Name
---------------  -----------------
0                MappingTest
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                 |
|-------------------|-------------------------|
| Mapping View ID   | ID of a mapping view.   |
| Mapping View Name | Name of a mapping view. |
