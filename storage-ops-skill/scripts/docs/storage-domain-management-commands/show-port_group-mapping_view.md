# show port_group mapping_view


##### Function

The **show port_group mapping_view** command is used to query information about a mapping view of a port group.

##### Format

**show port_group mapping_view** { port_group_id=? \| port_group_name=? }

##### Parameters

| Parameter         | Description                                  | Value                                               |
|-------------------|----------------------------------------------|-----------------------------------------------------|
| port_group_id=?   | ID of a port group that you want to query.   | To obtain the value, run "show port_group general". |
| port_group_name=? | Name of a port group that you want to query. | To obtain the value, run "show port_group general". |

##### Usage Guidelines

None.

##### Example

Query information about a mapping view of port group "0".

```text
admin:/>show port_group mapping_view port_group_id=0

Mapping View ID  Mapping View Name
---------------  -----------------
1                mapping01
```

Query information about a mapping view of port group "portgroup1".

```text
admin:/>show port_group mapping_view port_group_name=portgroup1

Mapping View ID  Mapping View Name
---------------  -----------------
1                mapping01
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                 |
|-------------------|-------------------------|
| Mapping View ID   | ID of a mapping view.   |
| Mapping View Name | Name of a mapping view. |
