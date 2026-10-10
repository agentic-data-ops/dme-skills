# remove failover_group bond_port


##### Function

The **remove failover_group bond_port** command is used to remove specified bond ports from a customized failover group.

##### Format

**remove failover_group bond_port** { failover_group_id=? \| failover_group_name=? } { bond_port_list=? \| bond_port_name_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of a failover group. | The value is an integer between 1 and 1024.<br>To obtain the value, run the "show failover_group general" command without parameters. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| bond_port_list=? | List of bond ports. | To obtain the value, run the "show failover_group member" command.<br>When multiple bond ports are entered, separate the port IDs from each other using commas (,). |
| bond_port_name_list=? | List of bond port names. | To obtain the value, run the "show failover_group member" command.<br>When multiple bond ports are entered, separate the port IDs from each other using commas (,). |

##### Usage Guidelines

-   The "failover_group_id" parameter supports only the ID of a customized failover group.
-   The "failover_group_name" parameter supports only the name of a customized failover group.
-   The "bond_port_list" parameter supports one or more bond port IDs.
-   The "bond_port_name_list" parameter supports one or more bond port names.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Remove a bond port from a customized failover group.

```text
admin:/>remove failover_group bond_port failover_group_id=1 bond_port_list=139009
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove bond port 139009 from failover group successfully.
```

You are about to remove a member port from a customized failover group. This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports. Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.

```text
admin:/>remove failover_group bond_port failover_group_id=1 bond_port_list=139009,139010
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove bond port 139009 from failover group successfully.
Remove bond port 139010 from failover group successfully.
```

Remove bond ports from a customized failover group.

```text
admin:/>remove failover_group bond_port failover_group_id=1 bond_port_list=139009,139010
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove bond port 139009 from failover group successfully.
Error: The object does not exist.
Remove bond port 139010 from failover group failed.
```

Remove bond ports from a customized failover group.

```text
admin:/>remove failover_group bond_port failover_group_name=FG001 bond_port_list=139009,139010
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove bond port 139009 from failover group successfully.
Remove bond port 139010 from failover group successfully.
```

Remove bond ports from a customized failover group.

```text
admin:/>remove failover_group bond_port failover_group_name=FG001 bond_port_name_list=139009,139010
DANGER: You are about to remove a member port from a customized failover group.
This operation may interrupt services running on logical ports that are associated with the failover group because no port is available for the failover of the logical ports.
Suggestion: Before performing this operation, ensure that another port in the failover group is available for failover.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove bond port 139009 from failover group successfully.
Remove bond port 139010 from failover group successfully.
```

##### System Response

None
