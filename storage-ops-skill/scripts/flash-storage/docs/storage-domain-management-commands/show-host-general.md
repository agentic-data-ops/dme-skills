# show host general


##### Function

The **show host general** command is used to query the information on hosts.

##### Format

**show host general** \[ host_id=? \| host_name=? \] \[ host_id_list=? \] \[ host_name_list=? \]

##### Parameters

| Parameter        | Description     | Value                                                                                                                                                                                                          |
|------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| host_id=?        | ID of a host.   | To obtain the value, run "**show host general**" without parameters.                            |
| host_name=?      | Host name.      | To obtain the value, run "**show host general**" without parameters.                            |
| host_id_list=?   | Host ID list.   | Use commas (,) to separate multiple IDs or use a hyphen (-) to specify an ID range.                                                                                                                            |
| host_name_list=? | Host name list. | Use commas (,) to separate multiple host names, or use a hyphen (-) to specify a host name range. In the host name range, the formats and lengths of the names before and after a hyphen (-) must be the same. |

##### Usage Guidelines

-   Run the "**show host general**" command to query information about all hosts.
-   Run the "**show host general** host_id=?" command to query information about a specified host.

##### Example

Query information about all hosts.

```text
admin:/>show host general

ID   Name        Health Status   Operating System   IP Address      Model     Location
---  ----------  --------------  ----------------   -------------   --------- -----------
0    Host000     Normal          Windows            --              --        --
1    Host001     Normal          Windows            --              --        --
2    newhost001  Normal          Linux              --              2058      newlocation
3    newhost002  Normal          Linux              192.168.3.53    2458      newlocation
```

Query information about the host whose ID is "1".

```text
admin:/>show host general host_id=1

ID                        : 1
Name                      : Host001
Health Status             : Normal
Operating System          : Windows
IP Address                : --
Model                     : --
Network Name              :
Location                  : --
Access Mode               : Asymmetric
HyperMetro Path Optimized : Yes
SmartQoS Policy ID        : --
Inband Command            : Disable
```

Query information about the host whose name is "name1".

```text
admin:/>show host general host_name=name1

ID                        : 2
Name                      : name1
Health Status             : Normal
Operating System          : Windows
IP Address                : --
Model                     : --
Network Name              :
Location                  : --
Access Mode               : Asymmetric
HyperMetro Path Optimized : Yes
SmartQoS Policy ID        : --
Inband Command            : Disable
```

##### System Response

The following table describes the parameter meanings.

| Parameter                 | Meaning                                                           |
|---------------------------|-------------------------------------------------------------------|
| ID                        | Host ID.                                                          |
| Name                      | Host name.                                                        |
| Health Status             | Health status of the host.                                        |
| Operating System          | Operating system.                                                 |
| IP Address                | IP address of the host.                                           |
| Model                     | Model of the host.                                                |
| Network Name              | Network name of the host.                                         |
| Location                  | Location of the host.                                             |
| Access Mode               | Host access mode.                                                 |
| HyperMetro Path Optimized | Whether the host path to the local HyperMetro array is preferred. |
| SmartQoS Policy ID        | ID of the SmartQoS policy configured for the host.                |
| Inband Command            | Whether to enable the in-band command function.                   |
