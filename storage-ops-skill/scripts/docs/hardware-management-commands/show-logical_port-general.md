# show logical_port general


##### Function

The **show logical_port general** command is used to query detailed information about logical ports in the system.

##### Format

**show logical_port general** \[ logical_port_name=? \| dns_zone_name=? \| listen_dns_query_enabled=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| logical_port_name | Logical port name. | Run the "show logical_port general" command without any parameters to obtain the value. |
| dns_zone_name | DNS zone name. | A name contains 1 to 255 characters and consists of labels separated by periods (.). A label contains 1 to 63 characters including letters (case-insensitive), digits, hyphens (-), and underscores (_), and must start and end with a letter or a digit. Run the "show dns_zone general" command without any parameters to obtain the value. |
| listen_dns_query_enabled | Whether to listen to DNS requests. | "no": does not listen to DNS requests.<br>"yes": listens to DNS requests. |

##### Usage Guidelines

-   To query all logical port information, run "**show logical_port general**".
-   To query specific logical port information, run "**show logical_port general** logical_port_name=?".

##### Example

Query information about all logical ports.

```text
admin:/>show logical_port general
Logical Port Name      Running Status  IPv4 Address    IPv6 Address  Home Port Type  Home Port ID        Current Port Type  Current Port ID     Work Controller ID  vStore ID  Support Protocol
---------------------  --------------  --------------  ------------  --------------  ------------------  -----------------  ------------------  ------------------  ---------  ----------------
ttt2                   Link Down       1.1.1.2         --            ETH             CTE0.B.IOM1.P0      ETH                CTE0.B.IOM1.P0      0B                  --                NFS
ttt3                   Link Down       1.1.1.3         --            ETH             CTE0.B.IOM1.P0      ETH                CTE0.B.IOM1.P0      0B                  --               iSCSI
ttt4                   Link Down       1.1.1.4         --            ETH             CTE0.B.IOM1.P0      ETH                CTE0.B.IOM1.P0      0B                  --                NVMe
ttt5                   Link Down       1.1.1.5         --            ETH             CTE0.B.IOM1.P0      ETH                CTE0.B.IOM1.P0      0B                  --                 --
ttt6                   Link Down       1.1.1.6         --            ETH             CTE0.B.IOM1.P0      ETH                CTE0.B.IOM1.P0      0B                  --                 --
ttt7                   Link Down       1.1.1.7         --            ETH             CTE0.B.IOM1.P0      ETH                CTE0.B.IOM1.P0      0B                  --                NFS
ttt8                   Link Down       1.1.1.8         --            ETH             CTE0.B.IOM1.P0      ETH                CTE0.B.IOM1.P0      0B                  --                NVMe
ttt9                   Link Down       1.1.1.9         --            ETH             CTE0.B.IOM1.P0      ETH                CTE0.B.IOM1.P0      0B                  --                iSCSI
ttt10                  Link Down       1.1.1.10        --
```

Query information about a specific logical port.

```text
admin:/>show logical_port general logical_port_name=lp001
Logical Port Name        : lp001
Running Status           : Link Down
IPv4 Address             : 1.1.1.129
IPv4 Mask                : 255.255.255.0
IPv4 Gateway             : 1.1.1.1
IPv6 Address             : --
IPv6 Mask                : --
IPv6 Gateway             : --
Role                     : Service
Support Protocol         : --
Home Port Type           : ETH
Home Port ID             : CTE0.B.IOM1.P0
Owner Controller ID      : 0B
Current Port Type        : ETH
Current Port ID          : CTE0.B.IOM1.P0
Work Controller ID       : 0B
Activation Status        : Yes
Address Family           : IPv4
Is Private               : No
Failover Group ID        : 0
Failover Enabled         : No
Failback Mode            : --
Failover Group Name      : --
Management Access        : --
vStore ID                : --
DDNS Status              : --
DNS Zone Name            : --
Listen DNS Query Enabled : --
Is Default Logical Port  : No
Logical Type             : Host Port
Work Status              : Working
Home Site WWN            : XXXX
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Logical Port Name | Logical port name. |
| Running Status | Port running status. |
| IPv4 Address | IPv4 address of the logical port. |
| IPv4 Mask | IPv4 subnet mask of the logical port. |
| IPv4 Gateway | IPv4 gateway of the logical port. |
| IPv6 Address | IPv6 address of the logical port. |
| IPv6 Mask | IPv6 mask of the logical port. |
| IPv6 Gateway | IPv6 gateway of the logical port. |
| Role | Port role. |
| Support Protocol | Supported protocol type. |
| Home Port Type | Home port type. |
| Home Port ID | Home port ID. |
| Owner Controller ID | Node where the working port resides. |
| Current Port Type | Working port type. |
| Current Port ID | Working port ID. |
| Work Controller ID | Working controller ID. |
| Activation Status | Activation status. |
| Address Family | IP address family. |
| Is Private | Is configurable or not. |
| Failover Group ID | Failover group ID. |
| Failover Enabled | Whether to enable failover. |
| Failback Mode | Failback mode. |
| Failover Group Name | Failover group name. |
| Management Access | Management access. |
| vStore ID | vStore ID. NOTE: This field is not displayed in the vStore view. |
| DDNS Status | Dynamic DNS status. |
| DNS Zone Name | DNS zone name. |
| Listen DNS Query Enabled | Whether the current logical port listens to DNS requests. |
| Is Default Logical Port | Whether the logical port is created by default. |
| Logical Type | Logical type. |
| Work Status | Work status. |
| Home Site WWN | Home site WWN of the LIF. |
