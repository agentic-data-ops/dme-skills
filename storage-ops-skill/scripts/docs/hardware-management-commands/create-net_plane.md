# create net_plane


##### Function

The **create net_plane** command is used to create a network plane.

##### Format

**create net_plane** name=? \[ vlanid=? \] \[ mtu=? \] \[ ipv4_subset_base=? \] \[ mask=? \] \[ ipv4_subset_range=? \] \[ ipv4_gateway=? \] \[ ipv6_subset_base=? \] \[ prefix_length=? \] \[ ipv6_subset_range=? \] \[ ipv6_gateway=? \] \[ max_pods_per_node=? \] \[ failover_enabled=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of the network plane to be created. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| vlanid=? | VLAN ID of the network plane. | The value is an integer ranging from 1 to 4094. |
| mtu=? | MTU value of a member port on a network plane. | The value ranges from 1280 to 9000, in bytes. |
| ipv4_subset_base=? | IPv4 subnet segment of the network plane. | For example, 192.168.2.0. The IPv4 address cannot start with 0 or 224 to 255. |
| mask=? | Subnet mask of the IPv4 subnet of the network plane. | - |
| ipv4_subset_range=? | Available IP address range of the IPv4 subnet of the network plane. | The IPv4 address cannot start with 0 or 224 to 255. |
| ipv4_gateway=? | Gateway of the IPv4 subnet of the network plane. | The IPv4 gateway cannot start with 0 or 224 to 255. |
| ipv6_subset_base=? | IPv6 subnet segment of the network plane. | For example, 1818::0. |
| prefix_length=? | Prefix length of the IPv6 subnet address of the network plane. | 1 to 127. |
| ipv6_subset_range=? | Available IP address range of the IPv6 subnet of the network plane. | For example, 1818::1-1818::100. |
| ipv6_gateway=? | Gateway of the IPv6 subnet of the network plane. | For example, 1818::110. |
| max_pods_per_node | Maximum number of pods supported by a single node. | The maximum value ranges from 1 to 15. The maximum value depends on the container scale or product model. |
| failover_enabled | Whether to enable IP address failover for the network plane. | "yes": enables the function.<br>"no": disables the function. |

##### Usage Guidelines

Run the "**create net_plane** name=?" command to create a network plane with a specified name.

##### Example

Create a network plane named "test".

```text
admin:/>create net_plane name=test vlanid=1 ipv4_subset_base=192.16.128.0 mask=255.255.255.0 ipv4_subset_range=192.16.128.1-192.16.128.100 ipv4_gateway=192.16.128.110 max_pods_per_node=3 failover_enabled=yes
Command executed successfully.
```

##### System Response

None
