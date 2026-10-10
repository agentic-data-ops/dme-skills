# show mapping_view port_group


##### Function

The **show mapping_view port_group** command is used to query port groups in a mapping view.

##### Format

**show mapping_view port_group** { mapping_view_id=? \| mapping_view_name=? }

##### Parameters

| Parameter           | Description        | Value                                                 |
|---------------------|--------------------|-------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.   | To obtain the value, run "show mapping_view general". |
| mapping_view_name=? | Mapping view name. | To obtain the value, run "show mapping_view general". |

##### Usage Guidelines

None.

##### Example

Query port groups in the mapping view whose ID is "1".

```text
admin:/>show mapping_view port_group mapping_view_id=1

Port Group ID  Port Group Name
-------------  ---------------
0              port_group_001
```

Query port groups in the mapping view whose name is "map01".

```text
admin:/>show mapping_view port_group mapping_view_name=map01

Port Group ID  Port Group Name
-------------  ---------------
0              port_group_001
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning               |
|-----------------|-----------------------|
| Port Group ID   | ID of a port group.   |
| Port Group Name | Name of a port group. |
