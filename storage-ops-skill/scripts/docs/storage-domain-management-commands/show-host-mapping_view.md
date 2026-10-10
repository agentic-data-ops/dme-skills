# show host mapping_view


##### Function

The **show host mapping_view** command is used to query mapping views of a host.

##### Format

**show host mapping_view** { host_id=? \| host_name=? }

##### Parameters

| Parameter   | Description | Value                                         |
|-------------|-------------|-----------------------------------------------|
| host_name=? | Host name.  | To obtain the value, run "show host general". |
| host_id=?   | Host ID.    | \-                                            |

##### Usage Guidelines

None

##### Example

Query mapping views that contain the host whose name is "host1".

```text

admin:/>show host mapping_view host_name=host1

Mapping View ID  Mapping View Name          LUN Group ID  LUN Group Name  Port Group ID  Port Group Name  Host Group ID  Host Group Name
---------------  -------------------------  ------------  --------------  -------------  ---------------  -------------  ---------------
1                map_1616465997111569_idx1  1             lg2             --             --               --             --

```

Query mapping views that contain the host whose ID is "1".

```text
admin:/>show host mapping_view host_id=1
Mapping View ID  Mapping View Name          LUN Group ID  LUN Group Name  Port Group ID  Port Group Name  Host Group ID  Host Group Name
---------------  -------------------------  ------------  --------------  -------------  ---------------  -------------  ---------------
1                map_1616465997111569_idx1  1             lg2             --             --               --             --
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning               |
|-------------------|-----------------------|
| Mapping View ID   | Mapping view ID       |
| Mapping View Name | Mapping view name.    |
| LUN Group ID      | ID of a LUN group.    |
| LUN Group Name    | Name of a LUN group.  |
| Port Group ID     | ID of a port group.   |
| Port Group Name   | Name of a port group. |
| Host Group ID     | Host group ID.        |
| Host Group Name   | Name of a host group. |
