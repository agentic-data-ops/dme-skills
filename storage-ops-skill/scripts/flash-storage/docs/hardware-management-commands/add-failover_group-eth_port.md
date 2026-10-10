# add failover_group eth_port


##### Function

The **add failover_group eth_port** command is used to add Ethernet ports to a customized failover group.

##### Format

**add failover_group eth_port** { failover_group_id=? \| failover_group_name=? } eth_port_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of a failover group. | The value is an integer from 1 to 1024.<br>To obtain the value, run the "show failover_group general" command without parameters. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| eth_port_list=? | List of Ethernet ports. | To obtain the value, run the "show port general physical_type=ETH logic_type=Host_Port" command.<br>When multiple Ethernet ports are entered, separate the port names from each other using commas (,). |

##### Usage Guidelines

-   The "failover_group_id" parameter supports only the ID of a customized failover group.
-   The "failover_group_name" parameter supports only the name of a customized failover group.
-   The "eth_port_list" parameter supports one or more Ethernet port names.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Add an Ethernet port to a customized failover group.

```text
admin:/>add failover_group eth_port failover_group_id=1 eth_port_list=CTEO.A1.P1
Add ETH port CTE0.A1.P1 to failover group successfully.
```

Add Ethernet ports to a customized failover group.

```text
admin:/>add failover_group eth_port failover_group_id=1 eth_port_list=CTE0.A1.P1,CTE0.A1.P2
Add ETH port CTE0.A1.P1 to failover group successfully.
Add ETH port CTE0.A1.P2 to failover group successfully.
```

Add Ethernet ports to a customized failover group.

```text
admin:/>add failover_group eth_port failover_group_id=1 eth_port_list=CTE0.A1.P1,CTE0.B1.P2
Add ETH port CTE0.A1.P1 to failover group successfully.
Error: The object does not exist.
Add ETH port CTE0.B1.P2 to failover group failed.
```

Add Ethernet ports to a customized failover group.

```text
admin:/>add failover_group eth_port failover_group_name=FG001 eth_port_list=CTE0.A1.P1,CTE0.A1.P2
Add ETH port CTE0.A1.P1 to failover group successfully.
Add ETH port CTE0.A1.P2 to failover group successfully.
```

##### System Response

None
