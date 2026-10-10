# create host_group


##### Function

The **create host_group** command is used to create a host group.

##### Format

**create host_group** name=? \[ host_group_id=? \| host_id_list=? \| host_name_list=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Host group name. | The value contains 1 to 255 digits, letters, underscores (_), hyphens (-), and periods (.). |
| host_group_id=? | Host group ID. | The value is an integer ranging from 0 to 8191. If you do not specify this parameter, the system automatically allocates an ID for a new host group. |
| host_id_list=? | Host ID. When this parameter is specified, the host corresponding to the ID is added to a host group. | To obtain the value, run "show host general".<br>When multiple hosts need to be added, separate these host IDs with commas (,), or use the host ID range with hyphens (-), such as: "0,5-8". |
| host_name_list=? | Host name. | To obtain the value, run "show host general".<br>When multiple hosts need to be added, separate these host names with commas (,), such as: "hostname0,hostname1,hostname8". |

##### Usage Guidelines

None.

##### Example

Create host group "test".

```text
admin:/>create host_group name=test
Create host group successfully.
```

##### System Response

None
