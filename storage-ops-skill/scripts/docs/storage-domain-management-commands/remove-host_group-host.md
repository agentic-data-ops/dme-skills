# remove host_group host


##### Function

The **remove host_group host** command is used to remove a specified host from a host group.

##### Format

**remove host_group host** { host_group_id=? \| host_group_name=? } { host_id_list=? \| host_name_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_group_id=? | Host group ID. | To obtain the value, run "show host_group general". |
| host_group_name=? | Host group name. | To obtain the value, run "show host_group general". |
| host_id_list=? | ID of a host that you want to remove. | To obtain the value, run "show host_group host".<br>When multiple hosts need to be removed, separate these host IDs with commas (,), or use the host ID range with hyphens (-), such as: "0,5-8". |
| host_name_list=? | Name of a host that you want to remove. | To obtain the value, run "show host_group host".<br>When multiple hosts need to be removed, separate these host names with commas (,), such as: "HostName1,HostName2,HostName8". |

##### Usage Guidelines

After a host is removed from a host group, it is no longer in the host group and cannot be managed by the host group.

##### Example

Remove host "1" from host group "1".

```text
admin:/>remove host_group host host_group_id=1 host_id_list=1
WARNING: You are about to remove the host from its host group. This operation will disable the host from accessing LUNs associated with its host group.
Suggestion: Before performing this operation, ensure that the selected host and host group are correct and stop services of the hosts running on LUNs associated with the host group.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove host 1 from host group successfully.
```

Remove host "HostName" from host group "1".

```text
admin:/>remove host_group host host_group_name=HostGroupName1 host_id_list=1
WARNING: You are about to remove the host from its host group. This operation will disable the host from accessing LUNs associated with its host group.
Suggestion: Before performing this operation, ensure that the selected host and host group are correct and stop services of the hosts running on LUNs associated with the host group.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove host 1 from host group successfully.
```

Remove host "HostName1" from host group "HostGrouName1".

```text
admin:/>remove host_group host host_group_name=HostGroupName1 host_name_list=HostName1
WARNING: You are about to remove the host from its host group. This operation will disable the host from accessing LUNs associated with its host group.
Suggestion: Before performing this operation, ensure that the selected host and host group are correct and stop services of the hosts running on LUNs associated with the host group.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove host 1 from host group successfully.
```

Remove host "1" from host group "HostGroupName1".

```text
admin:/>remove host_group host host_group_Name=HostGroupName1 host_id_list=1
WARNING: You are about to remove the host from its host group. This operation will disable the host from accessing LUNs associated with its host group.
Suggestion: Before performing this operation, ensure that the selected host and host group are correct and stop services of the hosts running on LUNs associated with the host group.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove host 1 from host group successfully.
```

##### System Response

None
