# change net_plane


##### Function

The **change net_plane** command is used to modify a network plane.

##### Format

**change net_plane** net_plane_id=? \[ name=? \] \[ vlanid=? \] \[ mtu=? \] \[ ipv4_subset_base=? \] \[ mask=? \] \[ ipv4_subset_range=? \] \[ ipv4_gateway=? \] \[ ipv6_subset_base=? \] \[ prefix_length=? \] \[ ipv6_subset_range=? \] \[ ipv6_gateway=? \] \[ max_pods_per_node=? \] \[ failover_enabled=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id=? | Network plane ID. | The value ranges from 1 to 1024.<br>To obtain the value, run the "show net_plane general" command without parameters. |
| name=? | Name of the network plane. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| vlanid=? | VLAN ID of the network plane. | The value is an integer ranging from 1 to 4094. |
| mtu=? | MTU value of a network plane member port. | The value ranges from 1280 to 9000, in bytes. |
| ipv4_subset_base=? | IPv4 subnet segment of the network plane. | For example, 192.168.2.0. The IPv4 address cannot start with 0 or 224 to 255. |
| mask=? | Subnet mask of the IPv4 subnet of the network plane. | - |
| ipv4_subset_range=? | Available IP address range of the IPv4 subnet of the network plane. | The IPv4 address cannot start with 0 or 224 to 255. |
| ipv4_gateway=? | Gateway of the IPv4 subnet of the network plane. | The IPv4 gateway cannot start with 0 or 224 to 255. |
| ipv6_subset_base=? | IPv6 subnet segment of the network plane. | For example, 1818::0. |
| prefix_length=? | Prefix length of the IPv6 subnet address of the network plane. | 1 to 127. |
| ipv6_subset_range=? | Available IP address range of the IPv6 subnet of the network plane. | For example, 1818::1-1818::100. |
| ipv6_gateway=? | Gateway of the IPv6 subnet of the network plane. | For example, 1818::110. |
| max_pods_per_node=? | Maximum number of pods supported by a single node. | The maximum value ranges from 1 to 15. The maximum value depends on the container scale or product model. |
| failover_enabled=? | Whether to enable IP address failover for the network plane. | "yes": enables the function.<br>"no": disables the function. |

##### Usage Guidelines

Run the "**change net_plane**" command to modify the network plane with a specified ID.

##### Example

Change the name of the network plane whose ID is "1" to "test".

```text
admin:/>change net_plane net_plane_id=1 name=test
Command executed successfully.
```

##### System Response

None
