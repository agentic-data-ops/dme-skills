# add host_group host


##### Function

The **add host_group host** command is used to add hosts to a host group.

##### Format

**add host_group host** { host_group_id=? \| host_group_name=? } { host_id_list=? \| host_name_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_group_id=? | Host group ID. | To obtain the value, run "show host_group general". |
| host_group_name=? | Host group name. | To obtain the value, run "show host_group general". |
| host_id_list=? | Host ID. | To obtain the value, run "show host general".<br>When multiple hosts need to be added, separate these host IDs with commas (,), or use the host ID range with hyphens (-), such as: "0,5-8". |
| host_name_list=? | Host name. | To obtain the value, run "show host general".<br>When multiple hosts need to be added, separate these host names with commas (,), such as: "hostname0,hostname1,hostname8". |

##### Usage Guidelines

None.

##### Example

Add host "1" to host group "1".

```text
admin:/>add host_group host host_group_id=1 host_id_list=1
Add host 1 to host group successfully.
```

Add host "HostName" to host group "HostGroupName".

```text
admin:/>add host_group host host_group_name=HostGroupName host_name_list=HostName
Add host HostName to host group successfully.
```

Add host "HostName" to host group "1".

```text
admin:/>add host_group host host_group_id=1 host_name_list=HostName
Add host HostName to host group successfully.
```

Add host "1" to host group "HostGroupName".

```text
admin:/>add host_group host host_group_name=HostGroupName host_id_list=1
Add host 1 to host group successfully.
```

##### System Response

None
