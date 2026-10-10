# remove net_plane route


##### Function

The **remove net_plane route** command is used to delete a route from a network plane.

##### Format

**remove net_plane route** net_plane_id=? \[ target_ipv4=? \] \[ mask=? \] \[ ipv4_gateway=? \] \[ target_ipv6=? \] \[ prefix_length=? \] \[ ipv6_gateway=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id=? | Network plane ID. | The value ranges from 1 to 1024.<br>To obtain the value, run the "show net_plane general" command without parameters. |
| target_ipv4=? | IPv4 address of the destination network segment. | For example, 192.168.2.0. The IPv4 address cannot start with 0 or 224 to 255. |
| mask=? | IPv4 address mask of the destination network segment. | - |
| ipv4_gateway=? | IPv4 gateway of the destination network segment. | The IPv4 gateway address cannot start with 0 or 224 to 255. |
| target_ipv6=? | IPv6 address of the destination network segment. | For example, 1818::0. |
| prefix_length=? | IPv6 address prefix of the destination network segment. | 1 to 127. |
| ipv6_gateway=? | IPv6 gateway of the destination network segment. | For example, 1818::110. |

##### Usage Guidelines

None

##### Example

Delete a route to the IPv4 network segment from the network plane.

```text
admin:/>remove net_plane route net_plane_id=1 target_ipv4=192.168.10.0 mask=255.255.255.0 ipv4_gateway=172.168.10.111
Command executed successfully.
```

Delete a route to the IPv6 network segment from the network plane.

```text
admin:/>remove net_plane route net_plane_id=1 target_ipv6=2020::0 prefix_len=96 ipv6_gateway=1818::1
Command executed successfully.
```

##### System Response

None
