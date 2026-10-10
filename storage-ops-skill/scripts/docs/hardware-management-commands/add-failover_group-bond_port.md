# add failover_group bond_port


##### Function

The **add failover_group bond_port** command is used to add bond ports to a customized failover group.

##### Format

**add failover_group bond_port** { failover_group_id=? \| failover_group_name=? } { bond_port_list=? \| bond_port_name_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of a failover group. | The value is an integer from 1 to 1024.<br>To obtain the value, run the "show failover_group general" command without parameters. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| bond_port_list=? | List of bond ports. | To obtain the value, run the "show bond_port" command.<br>When multiple bond ports are entered, separate the port IDs from each other using commas (,). |
| bond_port_name_list=? | List of bond port names. | To obtain the value, run the "show bond_port" command.<br>When multiple bond ports are entered, separate the port IDs from each other using commas (,). |

##### Usage Guidelines

-   The "failover_group_id" parameter supports only the ID of a customized failover group.
-   The "failover_group_name" parameter supports only the name of a customized failover group.
-   The "bond_port_list" parameter supports one or more bond port IDs.
-   The "bond_port_name_list" parameter supports one or more bond port names.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Add a bond port a customized failover group.

```text
admin:/>add failover_group bond_port failover_group_id=1 bond_port_list=139009
Add bond port 139009 to failover group successfully.
```

Add bond ports to a customized failover group.

```text
admin:/>add failover_group bond_port failover_group_id=1 bond_port_list=139009,139010
Add bond port 139009 to failover group successfully.
Add bond port 139010 to failover group successfully.
```

Add bond ports to a customized failover group.

```text
admin:/>add failover_group bond_port failover_group_id=1 bond_port_list=139009,139010
Add bond port 139009 to failover group successfully.
Error: The object does not exist.
Add bond port 139010 to failover group failed.
```

Add bond ports to a customized failover group.

```text
admin:/>add failover_group bond_port failover_group_name=FG001 bond_port_list=139009,139010
Add bond port 139009 to failover group successfully.
Add bond port 139010 to failover group successfully.
```

Add bond ports to a customized failover group.

```text
admin:/>add failover_group bond_port failover_group_name=FG001 bond_port_name_list=139009,139010
Add bond port 139009 to failover group successfully.
Add bond port 139010 to failover group successfully.
```

##### System Response

None
