# show host_group host


##### Function

The **show host_group host** command is used to query information about hosts in a host group.

##### Format

**show host_group host** { host_group_id=? \| host_group_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_group_id=? | ID of a host group that you want to query. | To obtain the value, run "show host_group general". |
| host_group_name=? | Name of a host group that you want to query. | To obtain the value, run "show host_group general". |
| host_name_list=? | Host name list. | You can run the "show host general" command to obtain the ID.<br>If multiple hosts need to be added at the same time, separate the host names with commas (,), for example, hostname1,hostname2,hostname8. |
| host_id_list=? | Host ID list. | You can run the "show host general" command to obtain the ID.<br>If multiple hosts need to be added at the same time, use commas (,) to separate host IDs, or use hyphens (-) to specify host ID ranges, for example, 0,5-8. |

##### Usage Guidelines

None.

##### Example

Query information about hosts in host group "1".

```text
admin:/>show host_group host host_group_id=1

ID  Name         Health Status  Operating System  IP Address  Model  Location
--  -----------  -------------  ----------------  ----------  -----  --------
1   WindowsHost  Normal         Windows           --
```

Query information about hosts in host group "WindowsHost".

```text
admin:/>show host_group host host_group_name=WindowsHost

ID  Name         Health Status  Operating System  IP Address  Model  Location
--  -----------  -------------  ----------------  ----------  -----  --------
1   WindowsHost  Normal         Windows           --
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                            |
|------------------|------------------------------------|
| ID               | Host ID.                           |
| Name             | Host name.                         |
| Health Status    | Health status of the host.         |
| Operating System | Type of the host operating system. |
| IP Address       | Host IP address.                   |
| Model            | Host multipath type.               |
| Location         | Host location.                     |
