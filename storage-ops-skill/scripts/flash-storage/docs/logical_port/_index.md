# logical_port

Manage logical ports, including creation, routes, failover, and VLAN configuration.

Manage logical ports, including creation, routes, failover, and VLAN configuration.

| command | function |
|---|---|
| add logical_port ipv4_route | add an IPv4 route for the logical port. |
| add logical_port ipv6_route | add an IPv6 route for a logical port. |
| change logical_port failback | fail back a logical port. |
| change logical_port failover_group | configure failover groups for one or more logical ports. |
| change logical_port general | configure a logical port. |
| create logical_port bond | create a logical port based on a bond port. This version does not support the logical port whose role is management. |
| create logical_port eth | create a logical port based on an Ethernet port. This version does not support the logical port whose role is management. |
| create logical_port vlan | create a logical port in a virtual local area network (VLAN). This version does not support the logical port whose role is management. |
| delete logical_port general | delete the specific logical port. |
| remove logical_port ipv4_route | remove the IPv4 route from a logical port. |
| remove logical_port ipv6_route | remove the IPv6 route from a logical port. |
| show logical_port count | query the count of logical ports in the system. |
| show logical_port general | query detailed information about logical ports in the system. |
| show logical_port route | check the logical port route. |