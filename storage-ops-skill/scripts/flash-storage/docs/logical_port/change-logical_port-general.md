# change logical_port general


##### Function

The **change logical_port general** command is used to configure a logical port.

##### Format

**change logical_port general** logical_port_name=? { activation_status=? \| failback_mode=? \| failover_enabled=? \| home_port_type=? { eth_port_id=? \| vlan_name=? \| bond_port_id=? \| bond_port_name=? } \| new_name=? \| owner_controller=? } \* \[ address_family=? \| ipv4_address=? \| ipv4_mask=? \| ipv4_gateway=? \| ipv6_address=? \| ipv6_mask=? \| ipv6_gateway=? \] \[ ddns_status=? \] \[ dns_zone_name=? \| remove_from_dns_zone=? \] \[ listen_dns_query_enabled=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| logical_port_name=? | Logical port name. The value contains 1 to 255 characters, including digits, letters, periods (.), underscores (_), and hyphens (-). | To obtain the value, run "show logical_port general". |
| address_family=? | Address family of the logical port. | The value can be "IPv4" or "IPv6". |
| ipv4_address=? | IPv4 address of the logical port. | The IPv4 address of the logical port cannot start with 0 or an integer from 224 to 255. |
| ipv4_mask=? | IPv4 mask of the logical port. | The value is a valid IPv4 subnet mask. |
| ipv4_gateway=? | IPv4 gateway of the logical port. | The IPv4 gateway of the logical port cannot start with 0 or an integer from 224 to 255. |
| ipv6_address=? | IPv6 address of the logical port. | The value is a valid IPv6 address. |
| ipv6_mask=? | IPv6 mask of the logical port. | The value is a valid IPv6 subnet mask. |
| ipv6_gateway=? | IPv6 gateway of the logical port. | The value is a valid IPv6 gateway address. |
| new_name=? | New name of the logical port. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| home_port_type=? | Type of the new owner port of logical port. | The value can be "eth", "bond", or "vlan". |
| owner_controller=? | New owning controller of logical port. | Controller ID, for example, "0A" or "1B". |
| eth_port_id=? | ID of the Ethernet port to which the logical port belongs. | To obtain the value, run "show port general". |
| vlan_name=? | Name of the VLAN port to which the logical port belongs. | To obtain the value, run "show vlan general". |
| failover_enabled=? | Whether to enable failover for the logical port. | "yes": yes.<br>"no": no. |
| failback_mode=? | Logical port failback mode. | "manually": manual failback.<br>"automatically": automatic failback. |
| activation_status=? | Logical port activation status. NOTE: This parameter is supported only by logical ports of the NFS, CIFS, and NFS_and_CIFS protocols or management roles. | "yes": activated.<br>"no": not activated. |
| bond_port_id=? | ID of the port to which the logical port is bound. | To obtain the value, run "show bond_port". |
| bond_port_name=? | Name of the port to which the logical port is bound. | To obtain the value, run "show bond_port". |
| ddns_status=? | Whether dynamic DNS turns on for a logical port. | The value can be: <br>"on": enables dynamic DNS parsing.<br>"off": disables dynamic DNS parsing.<br> The default value is "on". |
| dns_zone_name | DNS zone name. | A name contains a maximum of 255 characters and consists of labels separated by periods (.). A label contains a maximum of 63 characters including letters (case-insensitive), digits, hyphens (-), and underscores (_), and must start with a letter or a digit. To obtain the value, run the "show dns_zone general" command without parameters. |
| listen_dns_query_enabled | Whether to listen to DNS requests. | The value can be: <br>"no": do not listen.<br>"yes": listen. |
| remove_from_dns_zone | Whether the logical port needs to be removed from the DNS zone when the logical port is configured. | The value can be: <br>"yes": removes the current logical port from the DNS zone where it belongs. |

##### Usage Guidelines

-   When the value of "address_family" is changed to "IPv4", if the current parameter type is "IPv6", the parameters "ipv4_address" and "ipv4_mask" must be specified.
-   When the value of "address_family" is changed to "IPv6", if the current parameter type is "IPv4", the parameters "ipv6_address" and "ipv6_mask" must be specified.

##### Example

Change the IP address, gateway, and mask of a specified logical port.

```text
admin:/>change logical_port general logical_port_name=lp001 address_family=IPv4 ipv4_address=1.1.1.2 ipv4_mask=255.255.255.0 ipv4_gateway=1.1.1.1
DANGER: You are about to modify the properties of the logical port. This operation may interrupt services or cause service exceptions. If this operation also modifies the IP address of this logical port, the configured routes on the IP address that is modified on this logical port will also be cleared. If this operation involves modifying the home port, the logical port failover group will be restored to the default failover group or VLAN failover group.
Suggestion:
1. Before you perform this operation, determine whether the modification is necessary.
2. If this operation involves modifying the home port and the modified failover group is an unexpected failover group, modify the configurations of the failover group again.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the owner controller of a specified logical port.

```text
admin:/>change logical_port general logical_port_name=lp002 owner_controller=0C
DANGER: You are about to modify the properties of the logical port. This operation may interrupt services or cause service exceptions. If this operation also modifies the IP address of this logical port, the configured routes on the IP address that is modified on this logical port will also be cleared. If this operation involves modifying the home port, the logical port failover group will be restored to the default failover group or VLAN failover group.
Suggestion:
1. Before you perform this operation, determine whether the modification is necessary.
2. If this operation involves modifying the home port and the modified failover group is an unexpected failover group, modify the configurations of the failover group again.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
