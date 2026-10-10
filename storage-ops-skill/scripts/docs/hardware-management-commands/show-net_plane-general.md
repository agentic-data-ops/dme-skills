# show net_plane general


##### Function

The **show net_plane general** command is used to query network plane information of a storage system.

##### Format

**show net_plane general** \[ net_plane_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id=? | Network plane ID. | The value ranges from 1 to 1024.<br>To obtain the value, run the "show net_plane general" command without parameters. |

##### Usage Guidelines

Run the "**show net_plane general**" command to query information about all network planes.

##### Example

Query information about all network planes.

```text
admin:/>show net_plane general
Net Plane ID      Name     Vlan ID   Mtu                   IPv4 Range                             IPv6 Range                           Failover Enabled
------------      ------   -------   ---------------       ---------------------------            ------------------------             ----------------
1                 test1     1        1280                  192.16.18.1-192.16.18.100              --                                   yes
2                 test2     2        1500                  --                                     1818::1-1818::100                    no

```

Query information about the network plane whose ID is "1".

```text
admin:/>show net_plane general net_plane_id=1
Net Plane ID                    : 1
Name                            : test1
Vlan ID                         : 1
Mtu                             : 1280
IPv4 Subnet                     : 192.16.18.0
IPv4 Mask                       : 255.255.255.0
IPv4 Range                      : 192.16.18.1-192.16.18.100
IPv4 GateWay                    : 192.16.18.110
IPv6 Subnet                     :
IPv6 Prefix  Length             :
IPv6 Range                      : --
IPv6 GateWay                    :
Max Pods Per Node               : 3
Max Pods On Network Plane       : 3
Failover Enabled                : yes
```

##### System Response

The following table describes the parameter meanings.

| Parameter                 | Meaning                                                    |
|---------------------------|------------------------------------------------------------|
| Net Plane ID              | Network plane ID.                                          |
| Name                      | Name of the network plane.                                 |
| Vlan ID                   | VLAN ID of the network plane.                              |
| Mtu                       | MTU of the network plane.                                  |
| IPv4 Subnet               | IPv4 subnet segment of the network plane.                  |
| IPv4 Mask                 | IPv4 subnet mask of the network plane.                     |
| IPv4 Range                | IPv4 subnet address range of the network plane.            |
| IPv4 GateWay              | Gateway of the IPv4 subnet of the network plane.           |
| IPv6 Subnet               | IPv6 subnet segment of the network plane.                  |
| IPv6 Prefix Length        | Length of the IPv6 address prefix.                         |
| IPv6 Range                | IPv6 subnet address range of the network plane.            |
| IPv6 GateWay              | Gateway of the IPv6 subnet of the network plane.           |
| Max Pods Per Node         | Maximum number of pods supported by a single node.         |
| Max Pods on Network Plane | Maximum number of pods supported by a network plane.       |
| Failover Enabled          | Whether address failover is enabled for the network plane. |
