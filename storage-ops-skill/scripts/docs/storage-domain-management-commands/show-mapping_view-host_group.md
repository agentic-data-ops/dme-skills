# show mapping_view host_group


##### Function

The **show mapping_view host_group** command is used to query host groups in a mapping view.

##### Format

**show mapping_view host_group** { mapping_view_id=? \| mapping_view_name=? }

##### Parameters

| Parameter           | Description        | Value                                                 |
|---------------------|--------------------|-------------------------------------------------------|
| mapping_view_id=?   | Mapping view ID.   | To obtain the value, run "show mapping_view general". |
| mapping_view_name=? | Mapping view name. | To obtain the value, run "show mapping_view general". |

##### Usage Guidelines

None.

##### Example

Query host groups in the mapping view whose ID is "1".

```text
admin:/>show mapping_view host_group mapping_view_id=1

Host Group ID  Host Group Name
-------------  ---------------
0              host_group_001
```

Query host groups in the mapping view whose name is "map01".

```text
admin:/>show mapping_view host_group mapping_view_name=map01

Host Group ID  Host Group Name
-------------  ---------------
0              host_group_001
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning               |
|-----------------|-----------------------|
| Host Group ID   | ID of a host group.   |
| Host Group Name | Name of a host group. |
