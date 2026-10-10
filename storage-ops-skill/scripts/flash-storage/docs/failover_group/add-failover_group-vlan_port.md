# add failover_group vlan_port


##### Function

The **add failover_group vlan_port** command is used to add VLAN ports to a customized failover group.

##### Format

**add failover_group vlan_port** { failover_group_id=? \| failover_group_name=? } vlan_port_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of a failover group. | The value is an integer from 1 to 1024.<br>To obtain the value, run the "show failover_group general" command without parameters. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| vlan_port_list=? | List of VLAN ports. | To obtain the value, run the "show vlan general" command.<br>When multiple VLAN ports are entered, separate the port names from each other using commas (,). |

##### Usage Guidelines

-   The "failover_group_id" parameter supports only the ID of a customized failover group.
-   The "failover_group_name" parameter supports only the name of a customized failover group.
-   The "vlan_port_list" parameter supports one or more VLAN port names.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Add a VLAN port to a customized failover group.

```text
admin:/>add failover_group vlan_port failover_group_id=1 vlan_port_list=vlan1
Add VLAN port vlan1 to failover group successfully.
```

Add VLAN ports to a customized failover group.

```text
admin:/>add failover_group vlan_port failover_group_id=1 vlan_port_list=vlan1,vlan2
Add VLAN port vlan1 to failover group successfully.
Add VLAN port vlan2 to failover group successfully.
```

Add VLAN ports to a customized failover group.

```text
admin:/>add failover_group vlan_port failover_group_id=1 vlan_port_list=vlan1,vlan2
Add VLAN port vlan1 to failover group successfully.
Error: The object does not exist.
Add VLAN port vlan2 to failover group failed.
```

Add VLAN ports to a customized failover group.

```text
admin:/>add failover_group vlan_port failover_group_name=FG001 vlan_port_list=vlan1,vlan2
Add VLAN port vlan1 to failover group successfully.
Add VLAN port vlan2 to failover group successfully.
```

##### System Response

None
