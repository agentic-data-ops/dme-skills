# remove failover_group vlan_port


##### Function

The **remove failover_group vlan_port** command is used to remove specified VLAN ports from a customized failover group.

##### Format

**remove failover_group vlan_port** { failover_group_id=? \| failover_group_name=? } vlan_port_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of a failover group. | The value is an integer between 1 and 1024.<br>To obtain the value, run the "show failover_group general" command without parameters. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| vlan_port_list=? | List of VLAN ports. | To obtain the value, run the "show failover_group member" command.<br>When multiple VLAN ports are entered, separate the port names from each other using commas (,). |

##### Usage Guidelines

-   The "failover_group_id" parameter supports only the ID of a customized failover group.
-   The "failover_group_name" parameter supports only the name of a customized failover group.
-   The "vlan_port_list" parameter supports one or more VLAN port names.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Remove a VLAN port from a customized failover group.

```text
admin:/>remove failover_group vlan_port failover_group_id=1 vlan_port_list=vlan1
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove VLAN port vlan1 from failover group successfully.
```

Remove VLAN ports from a customized failover group.

```text
admin:/>remove failover_group vlan_port failover_group_id=1 vlan_port_list=vlan1,vlan2
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove VLAN port vlan1 from failover group successfully.
Remove VLAN port vlan2 from failover group successfully.
```

Remove VLAN ports from a customized failover group.

```text
admin:/>remove failover_group vlan_port failover_group_id=1 vlan_port_list=vlan1,vlan2
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove VLAN port vlan1 from failover group successfully.
Error: The object does not exist.
Remove VLAN port vlan2 from failover group failed.
```

Remove VLAN ports from a customized failover group.

```text
admin:/>remove failover_group vlan_port failover_group_name=FG001 vlan_port_list=vlan1,vlan2
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove VLAN port vlan1 from failover group successfully.
Remove VLAN port vlan2 from failover group successfully.
```

##### System Response

None
