# add net_plane eth_port


##### Function

The **add net_plane eth_port** command is used to add a front-end Ethernet port of a container to the network plane.

##### Format

**add net_plane eth_port** net_plane_id=? port_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id | Network plane ID. | The value is an integer ranging from 1 to 1024.<br>To obtain the value, run the "show net_plane general" command without parameters. |
| port_list | List of front-end Ethernet ports of a container. | To obtain the value, run the "show port general physical_type=ETH" command.<br>If you need to enter multiple Ethernet ports, separate them with commas (,). |

##### Usage Guidelines

Run the "**add net_plane eth_port**" command to add a front-end Ethernet port of a container to the network plane.

##### Example

Add multiple Ethernet ports to the network plane.

```text
admin:/>add net_plane eth_port net_plane_id=1 eth_port_list=CTE0.A.IOM2.P0,CTE0.A.IOM2.P1
Add ETH port CTE0.A.IOM2.P0 to network plane successfully.
Add ETH port CTE0.A.IOM2.P1 to network plane successfully.
```

##### System Response

None
