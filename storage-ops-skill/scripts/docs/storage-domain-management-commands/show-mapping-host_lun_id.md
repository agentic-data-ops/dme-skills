# show mapping host_lun_id


##### Function

The **show mapping host_lun_id** command is used to query IDs of mapped host LUNs.

##### Format

**show mapping host_lun_id** { host_id=? \| host_group_id=? } \[ lun_id=? \| lun_group_id=? \]

**show mapping host_lun_id** { host_name=? \| host_group_name=? } \[ lun_name=? \| lun_group_name=? \]

##### Parameters

| Parameter         | Description      | Value                                                                                        |
|-------------------|------------------|----------------------------------------------------------------------------------------------|
| host_id=?         | Host ID.         | The value ranges from 0 to n minus one, where n indicates the maximum number of hosts.       |
| host_group_id=?   | Host group ID.   | The value ranges from 0 to n minus one, where n indicates the maximum number of host groups. |
| lun_id=?          | LUN ID.          | The value ranges from 0 to n minus one, where n indicates the maximum number of LUNs.        |
| lun_group_id=?    | LUN group ID.    | The value ranges from 0 to n minus one, where n indicates the maximum number of LUN groups.  |
| host_name=?       | Host name.       | \-                                                                                           |
| host_group_name=? | Host group name. | \-                                                                                           |
| lun_name=?        | LUN name.        | \-                                                                                           |
| lun_group_name=?  | LUN group name.  | \-                                                                                           |

##### Usage Guidelines

None

##### Example

Query all LUNs mapped to host "2".

```text
admin:/>show mapping host_lun_id host_id=2
LUN ID  LUN Name  Host LUN ID  Mapping Type
------  --------  -----------  ------------
0       lun0000   1            Host Group
1       lun0001   2            Host Group
2       lun0002   3            Host
3       lun0003   4            Host
```

Query all LUNs mapped to host group "1".

```text
admin:/>show mapping host_lun_id host_group_id=1
LUN ID  LUN Name  Host LUN ID  Mapping Type
------  --------  -----------  ------------
0       lun0000   1            Host Group
1       lun0001   2            Host Group
2       lun0002   3            Host Group
3       lun0003   4            Host Group
```

##### System Response

The following table describes the parameter meanings.

| Parameter    | Meaning          |
|--------------|------------------|
| LUN ID       | LUN ID.          |
| LUN Name     | Name of the LUN. |
| Host LUN ID  | Host LUN ID.     |
| Mapping Type | Mapping type.    |
