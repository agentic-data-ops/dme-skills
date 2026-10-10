# create logical_port eth


##### Function

The **create logical_port eth** command is used to create a logical port based on an Ethernet port. This version does not support the logical port whose role is management.

##### Format

**create logical_port eth** name=? eth_port_id=? address_family=? ipv4_address=? ipv4_mask=? \[ ipv4_gateway=? \] ipv6_address=? ipv6_mask=? \[ ipv6_gateway=? \] \[ role=? \] \[ protocol_type=? \] \[ is_private=? \] \[ activation_status=? \] \[ failover_enabled=? \] \[ failback_mode=? \] { failover_group_id=? \| failover_group_name=? } \[ ddns_status=? \] \[ dns_zone_name=? \] \[ listen_dns_query_enabled=? \] \[ home_site_wwn=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a logical port. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| eth_port_id=? | Ethernet port ID. | To obtain the value, run the "show port general physical_type=eth" command. |
| address_family=? | Address family of a logical port. | The value can be "IPv4" or "IPv6". |
| ipv4_address=? | IPv4 address of a logical port. | The IPv4 address of the logical port cannot start with 0 or an integer from 224 to 255. |
| ipv4_mask=? | IPv4 subnet mask of a logical port. | The value is a valid IPv4 subnet mask. |
| ipv4_gateway=? | IPv4 gateway of a logical port. | The IPv4 gateway of the logical port cannot start with 0 or an integer from 224 to 255. |
| ipv6_address=? | IPv6 address of a logical port. | The value is a valid IPv6 address. |
| ipv6_mask=? | IPv6 mask of a logical port. | The value is a valid IPv6 subnet mask. |
| ipv6_gateway=? | IPv6 gateway of a logical port. | The value is a valid IPv6 gateway address. |
| role=? | Role of a logical interface. NOTE: This version does not support the logical port whose role is management. | The value can be "management", "service", "management+service", or "replication", where: <br>"management": the role of management.<br>"service": the role of data.<br>"management+service": the role of management and data.<br>"replication": the role of replication. |
| protocol_type=? | Protocol type of a logical port. | The value can be "NFS", "CIFS", "NFS and CIFS", or "iSCSI". |
| is_private=? | Whether a logical port is private. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no". The default value is "no". |
| activation_status=? | Whether a logical port is activated. NOTE: This parameter is supported only by logical ports of the NFS, CIFS, and NFS_and_CIFS protocols or management roles. | The value can be "yes" or "no".The default value is "yes". |
| failover_enabled=? | Whether failover is enabled for a logical port. | The value can be "yes" or "no", where: <br>"yes": enables failover for a logical port.<br>"no": disabled failover for a logical port. |
| failback_mode=? | Failback mode of a logical port. | The value can be "manually" or "automatically", where: <br>"manually": manual failback.<br>"automatically": automatic failback. |
| failover_group_id=? | Failover group ID. | - |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| ddns_status=? | Whether dynamic DNS turns on for a logical port. | The value can be "on" or "off". The default value is "on". |
| dns_zone_name | DNS Zone name. | A name contains a maximum of 255 characters and consists of labels separated by periods (.). A label contains a maximum of 63 characters including letters (case-insensitive), digits, hyphens (-), and underscores (_), and must start with a letter or a digit. To obtain the value, run the "show dns_zone general" command without parameters. |
| listen_dns_query_enabled | Whether the current logical port listens to DNS requests. | The options are as follows: <br>"no": do not listen.<br>"yes": listen. |
| home_site_wwn | Home site WWN of the LIF. | To obtain the value, run the "show system general" command in the user view. |

##### Usage Guidelines

-   When "address_family" is set to "IPv4", "ipv4_address" must be specified.
-   When the value of the parameter "address_family" is "IPv4", the parameter "ipv4_mask" must be specified.
-   When the value of the parameter "address_family" is "IPv6", the parameter "ipv6_address" must be specified.
-   When the value of the parameter "address_family" is set to "IPv6", the parameter "ipv6_mask" must be specified.
-   This version does not support logical ports whose role is management.

##### Example

Create a logical port based on the Ethernet port.

```text
admin:/>create logical_port eth name=lp001 eth_port_id=CTE0.A2.P1 address_family=IPv4 ipv4_address=10.178.1.133 ipv4_mask=255.255.0.0
Command executed successfully.
```

##### System Response

None
