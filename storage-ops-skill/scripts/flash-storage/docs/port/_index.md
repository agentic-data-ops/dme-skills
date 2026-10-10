# port

Manage ports (FC, Ethernet, RoCE), bond ports, and IP/route configuration.

| command | function |
|---|---|
| add port ipv4_route | add an IPv4 route for a specific Ethernet port. If the IPv4 address of the storage system and that of an application server reside on different network segments, you can run this command to add a route to connect the storage system to application server. |
| add port ipv6_route | add an IPv6 route for a specific Ethernet port. If the IPv6 address of the storage system and that of a host reside on different network segments, you can run this command to add a route to connect the storage system to the host. |
| change bond_port general | change the MTU of a bond port. |
| change icmp switch | set the ICMP function of all ports.You can run this command to turn on or off icmp function of all ports. |
| change port eth | configure the properties for Ethernet ports (including host ports and management network ports). |
| change port eth_snsd_switch | enable or disable the SNSD function of an Ethernet port. |
| change port fc | modify the properties of a specific Fibre Channel port. |
| change port ipv4_address | change the IPv4 address of a specific port. |
| change port ipv6_address | change the IPv6 address of a specific port. |
| change port roce | configure the properties for RoCE ports. |
| change system management_ip | configure the IP address of a management port on new hardware. Both an IPv4 and IPv6 address can be configured, which is used by terminals to access the disk array. |
| clear port bit_error | clear the bit_error of the port. |
| create bond_port | create an Ethernet bond port. By binding multiple Ethernet ports, you can increase the data transmission bandwidth in parallel mode. The "**create bond_port** iscsi_port_id_list" command is replaced with the "**create bond_port** port_id_list" command. |
| delete bond_port | delete an Ethernet bond port. |
| remove port ipv4_address | remove the IPv4 address of a specified port. |
| remove port ipv4_route | remove an IPv4 route configured for a port. |
| remove port ipv6_address | remove the IPv6 address of a specified port. |
| remove port ipv6_route | remove an IPv6 route configured for a port. |
| remove system management_ip | delete an IP address of a management network port. |
| show bond_port | query bond ports. |
| show bond_port_count | check the number of bond ports. |
| show port bit_error | query port bit errors. |
| show port electrical_module | query details on all electrical modules in the storage system. |
| show port eth_snsd_switch | query the switch status of the SNSD function of an Ethernet port. |
| show port fibre_module | query details on all optical transceivers in the storage system. |
| show port general | query ports on the storage system. |
| show port initiator | view the WWN information of all initiators that map to a port. |
| show port ip | query the IP addresses of Ethernet ports (including iSCSI host ports and management network ports). |
| show port route | query the route settings of ports on the storage system. |
| show route general | query route configuration of storage system ports. |
| show system management_ip | query the IP address of the management port on a controller. |