# Hardware Management Commands

Hardware management commands are used to query and modify hardware parameters. Hardware includes controllers, caches, power modules, interface modules, ports, fan modules, expansion modules, BBUs, engines, disk enclosures, hard disks, and DBs.

## bbu

- show bbu general: query details on BBUs. Run this command if you need to query a BBU's status, voltage, and the ID of the controller module where the BBU resides.

## configuration_data

- export configuration_data: export the configuration file that resides in the storage system's memory. Such a configuration file stores important configuration information on the storage system's components and services. Export configuration data regularly and save it securely so that you can restore the configuration when the storage system fails.

## controller

- change controller service_session: change the service duration of a controller.
- change controller starting_point_date: change the service start time of a controller.
- show controller general: query details on controllers.
- show controller io: **show controller io** command is used to query information about concurrent I/Os of a specified controller.

## disk

- change disk light: turn on or turn off the location indicator of a specific disk.
- change disk media_scan: modify settings of disk media scanning.
- change disk precopy: enable or disable the disk precopy function.
- change disk routine_test: **change disk routine_test** command is used to set the status and period for a routine disk test.
- change ssd routeswitch: set the status of a routine SSD test.
- show disk general: query disk information.
- show disk health: **show disk health** command is used to query the health status of a disk.
- show disk in_domain: query information about member disks in a specific disk domain.
- show disk media_scan: query the disk media scanning information, including the bandwidth and disk usage.
- show disk precopy: query the status of the disk precopy function.
- show disk routine_test: query the status and period of a routine disk test.
- show smart_cache_pool disk: query disks in a SmartCache pool.
- show ssd routeswitch: query the status of a routine SSD test.

## dns_zone

- change dns_zone general: modify the name a DNS zone.
- create dns_zone general: create a zone for the built-in DNS server.
- delete dns_zone general: delete a specified zone.
- show dns_zone general: query zone information about the built-in DNS server.

## enclosure

- add net_plane eth_port: add a front-end Ethernet port of a container to the network plane.
- add net_plane route: add a route to a network plane.
- change enclosure id: modify the ID of a disk enclosure.
- change enclosure light: set the status of the location indicator on a specific engine or disk enclosure. You can run this command to query the location of an engine or disk enclosure.
- change enclosure location: change the location of an enclosure in a cabinet.
- change net_plane: modify a network plane.
- create net_plane: create a network plane.
- delete net_plane: delete a network plane.
- remove net_plane eth_port: remove a specified Ethernet port from a network plane.
- remove net_plane ipv4_address: delete the IPv4 address of a network plane.
- remove net_plane ipv4_gateway: delete the IPv4 gateway of a network plane.
- remove net_plane ipv6_address: delete the IPv6 address of a network plane.
- remove net_plane ipv6_gateway: delete the IPv6 gateway of a network plane.
- remove net_plane route: delete a route from a network plane.
- show enclosure: query details on the engine and disk enclosure.
- show net_plane general: query network plane information of a storage system.
- show net_plane member: query information about network plane members on a storage system.
- show net_plane route: query the route information of the network plane on the storage system.

## expansion_module

- show expansion_module: query details on expansion modules. Run this command if you need to query an expansion module's type, status, and electronic label.

## failover_group

- add failover_group bond_port: add bond ports to a customized failover group.
- add failover_group eth_port: add Ethernet ports to a customized failover group.
- add failover_group vlan_port: add VLAN ports to a customized failover group.
- change failover_group general: configure a customized failover group.
- create failover_group general: create a customized failover group.
- delete failover_group general: delete a specified customized failover group.
- remove failover_group bond_port: remove specified bond ports from a customized failover group.
- remove failover_group eth_port: remove Ethernet ports from a customized failover group.
- remove failover_group vlan_port: remove specified VLAN ports from a customized failover group.
- show failover_group count: query the number of failover groups on the storage system.
- show failover_group general: query failover groups on the storage system.
- show failover_group member: query the members in a failover group on the storage system.

## fan

- show assistant_cooling_unit: query details on assistant cooling units.
- show fan: query details on fan modules. Run this command if you need to query a fan module's status, running speed, running level, and electronic label.

## interface_module

- change interface_module: The "**change interface_module**" command is used to configure an interface module mode.
- poweroff interface_module: power off a specific interface module.
- poweron interface_module: power on a specific interface module.
- show interface_module: query information about an interface module.

## logical_port

- add logical_port ipv4_route: add an IPv4 route for the logical port.
- add logical_port ipv6_route: add an IPv6 route for a logical port.
- change logical_port failback: fail back a logical port.
- change logical_port failover_group: configure failover groups for one or more logical ports.
- change logical_port general: configure a logical port.
- create logical_port bond: create a logical port based on a bond port. This version does not support the logical port whose role is management.
- create logical_port eth: create a logical port based on an Ethernet port. This version does not support the logical port whose role is management.
- create logical_port vlan: create a logical port in a virtual local area network (VLAN). This version does not support the logical port whose role is management.
- delete logical_port general: delete the specific logical port.
- remove logical_port ipv4_route: remove the IPv4 route from a logical port.
- remove logical_port ipv6_route: remove the IPv6 route from a logical port.
- show logical_port count: query the count of logical ports in the system.
- show logical_port general: query detailed information about logical ports in the system.
- show logical_port route: check the logical port route.

## port

- add port ipv4_route: add an IPv4 route for a specific Ethernet port. If the IPv4 address of the storage system and that of an application server reside on different network segments, you can run this command to add a route to connect the storage system to application server.
- add port ipv6_route: add an IPv6 route for a specific Ethernet port. If the IPv6 address of the storage system and that of a host reside on different network segments, you can run this command to add a route to connect the storage system to the host.
- change bond_port general: change the MTU of a bond port.
- change icmp switch: set the ICMP function of all ports.You can run this command to turn on or off icmp function of all ports.
- change port eth: configure the properties for Ethernet ports (including host ports and management network ports).
- change port eth_snsd_switch: enable or disable the SNSD function of an Ethernet port.
- change port fc: modify the properties of a specific Fibre Channel port.
- change port ipv4_address: change the IPv4 address of a specific port.
- change port ipv6_address: change the IPv6 address of a specific port.
- change port roce: configure the properties for RoCE ports.
- change system management_ip: configure the IP address of a management port on new hardware. Both an IPv4 and IPv6 address can be configured, which is used by terminals to access the disk array.
- clear port bit_error: clear the bit_error of the port.
- create bond_port: create an Ethernet bond port. By binding multiple Ethernet ports, you can increase the data transmission bandwidth in parallel mode. The "**create bond_port** iscsi_port_id_list" command is replaced with the "**create bond_port** port_id_list" command.
- delete bond_port: delete an Ethernet bond port.
- remove port ipv4_address: remove the IPv4 address of a specified port.
- remove port ipv4_route: remove an IPv4 route configured for a port.
- remove port ipv6_address: remove the IPv6 address of a specified port.
- remove port ipv6_route: remove an IPv6 route configured for a port.
- remove system management_ip: delete an IP address of a management network port.
- show bond_port: query bond ports.
- show bond_port_count: check the number of bond ports.
- show port bit_error: query port bit errors.
- show port electrical_module: query details on all electrical modules in the storage system.
- show port eth_snsd_switch: query the switch status of the SNSD function of an Ethernet port.
- show port fibre_module: query details on all optical transceivers in the storage system.
- show port general: query ports on the storage system.
- show port initiator: view the WWN information of all initiators that map to a port.
- show port ip: query the IP addresses of Ethernet ports (including iSCSI host ports and management network ports).
- show port route: query the route settings of ports on the storage system.
- show route general: query route configuration of storage system ports.
- show system management_ip: query the IP address of the management port on a controller.

## power_supply

- show power_supply: query details on power modules, such as the status, manufacturer, and type.

## running_data

- export running_data: export storage system configuration information to a .txt file. Such a .txt file can be read by users but cannot be used during configuration information import. If you need to know storage system configuration information, run this command.

## support

- change dsm copy_num: modify the number of DSM copies.
- change ftds level: set the trace level of Flow Tracing & Diagnosing System (FTDS) function. The level includes subsystem level, key module level, module level, and debug level.
- change ftds switch: enable or disable the Fault Tracing Diagnosing System (FTDS) tracing function. This command can be used to set the main switch (excluding the workload switch), tracing switch, phase switch, latency switch, counting switch, workload collection switch, and workload feature extraction switch.
- change iostat policy: set an I/O statistical policy.
- change protocol service: perform operations on protocol objects, such as migrating LUN reservation information.
- change user_mode current_mode: switch a user view. This command is used when you want to switch from the user view to the developer or engineer view.
- change user_ssh_auth_info general: change the SSH authentication mode of a user.
- reboot storage service: restart storage system services.
- show devicemanager tls_versions: The "**show devicemanager tls_versions**" command is used to query version information of the TLS which is be used to the DeviceManager service on the storage system.
- show diagnose_code: query system diagnose codes.
- show dsm partition_status: query the DSM partition status.
- show ftds level: query the trace level of the Flow Tracing & Diagnosing System (FTDS) function.
- show ftds switch: check whether the Flow Tracing & Diagnosing System (FTDS) function is enabled.
- show iostat policy: **show iostat policy** command is used to view the I/O statistical policy.
- show user_ssh_auth_info general: query the SSH authentication information about users.
- test ldap configuration: test LDAP server configuration information.
- test ntp_server general: test the connectivity of an NTP server.

## vlan

- change vlan general: change the VLAN maximum transmission unit.
- create vlan general: create a VLAN.
- delete vlan general: delete a VLAN port.
- show vlan count: query the number of VLANs.
- show vlan general: check existing VLANs and their properties.
