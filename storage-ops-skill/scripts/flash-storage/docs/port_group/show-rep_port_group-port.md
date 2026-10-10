# show rep_port_group port


##### Function

The **show rep_port_group port** command is used to query information about ports in a replication port group.

##### Format

**show rep_port_group port** rep_port_group_id=? \[ port_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rep_port_group_id=? | ID of a replication port group. | To obtain the value, run "show rep_port_group general". |
| port_type=? | Type of a port that you want to query. | The value can be "FC" or "ETH", where: <br>"FC": indicates Fibre Channel ports.<br>"ETH": indicates ETH ports. |

##### Usage Guidelines

None

##### Example

Query information about ports in replication port group "0". The ID and output vary depending on a specific product.

```text
admin:/>show rep_port_group port rep_port_group_id=0
FC port:

ID              Health Status  Running Status  Type       Working Rate(Mbps)  WWN               Role         Working Mode  Configured Mode  Enabled  Max Speed(Mbps)  Number Of Initiators

--------------  -------------  --------------  ---------  ------------------  ----------------  -----------  ------------  ---------------  -------  ---------------  --------------------

CTE0.A.IOM0.P0  Normal         Link Down       Host Port  --                  200034a2a2fcbb8a  INI and TGT  --            Auto-Adapt       Yes      8000             0

CTE0.B.IOM0.P0  Normal         Link Down       Host Port  --                  201034a2a2fcbb8a  INI and TGT  --            Auto-Adapt       Yes      8000             0

ETH port:

Logical Port Name  Running Status  IPv4 Address    IPv6 Address  Home Port Type  Home Port ID  Current Port Type  Current Port ID  Work Controller ID

-----------------  --------------  --------------  ------------  --------------  ------------  -----------------  ---------------  ------------------

eth_lif_0          Link Up         2.2.2.2         --            ETH             CTE0.A.H2     ETH                CTE0.A.H2        0A
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
| ID | ID of a port. |
| Health Status | Health status of a port. |
| Type | Port type. |
| Working Rate(Mbps) | Work speed of a port. |
| Enabled | Whether the port is enabled. |
| Max Speed(Mbps) | Maximum work speed of a port. |
| WWN | WWN of a port. |
| Channel Number | Channel number of a port. |
