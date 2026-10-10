# remove net_plane eth_port


##### Function

The **remove net_plane eth_port** command is used to remove a specified Ethernet port from a network plane.

##### Format

**remove net_plane eth_port** net_plane_id=? port_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id | Network plane ID. | The value ranges from 1 to 1024.<br>To obtain the value, run the "show net_plane general" command without parameters. |
| port_list | List of front-end Ethernet ports of a container. | To obtain the value, run the "show port general physical_type=ETH" command.<br>If you need to enter multiple Ethernet ports, separate them with commas (,). |

##### Usage Guidelines

Run the" **remove net_plane eth_port**" command to remove a specified Ethernet port from the network plane.

##### Example

Remove multiple Ethernet ports from the network plane.

```text
admin:/>remove net_plane eth_port net_plane_id=1 eth_port_list=CTE0.A1.P0,CTE0.A1.P1
Remove ETH port CTE0.A1.P0 from net plane successfully.
Remove ETH port CTE0.A1.P1 from net plane successfully.
```

##### System Response

None
