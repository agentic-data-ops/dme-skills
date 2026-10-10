# show host_group mapping_view


##### Function

The **show host_group mapping_view** command is used to query information about a mapping view added to a host group.

##### Format

**show host_group mapping_view** { host_group_id=? \| host_group_name=? }

##### Parameters

| Parameter         | Description      | Value                                               |
|-------------------|------------------|-----------------------------------------------------|
| host_group_id=?   | Host group ID.   | To obtain the value, run "show host_group general". |
| host_group_name=? | Host group name. | To obtain the value, run "show host_group general". |

##### Usage Guidelines

None.

##### Example

Query information about a mapping view added to host group "1".

```text
admin:/>show host_group mapping_view host_group_id=1

Mapping View ID  Mapping View Name
---------------  -----------------
1                test
```

Query information about a mapping view added to host group "HostGroupName".

```text
admin:/>show host_group mapping_view host_group_name=HostGroupName

Mapping View ID  Mapping View Name
---------------  -----------------
1                test
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                 |
|-------------------|-------------------------|
| Mapping View ID   | ID of a mapping view.   |
| Mapping View Name | Name of a mapping view. |
