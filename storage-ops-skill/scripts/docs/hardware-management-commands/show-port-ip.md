# show port ip


##### Function

The **show port ip** command is used to query the IP addresses of Ethernet ports (including iSCSI host ports and management network ports).

##### Format

**show port ip** \[ eth_port_id=? \]

##### Parameters

| Parameter     | Description             | Value                                         |
|---------------|-------------------------|-----------------------------------------------|
| eth_port_id=? | ID of an Ethernet port. | To obtain the value, run "show port general". |

##### Usage Guidelines

-   IP addresses are of two types: IPv4 and IPv6.
-   Run the "**show port ip**" command to query the IP addresses of all Ethernet ports.
-   Run the "**show port ip** eth_port_id=?" command to query the IP addresses of a specific Ethernet port,.

##### Example

Query the IP addresses of the Ethernet port whose ID is "CTE0.A7.P0". The ID and output vary depending on a specific product.

```text
admin:/>show port ip eth_port_id=CTE0.A7.P0
-----------------Host_Port-----------------

Port ID : CTE0.A7.P0
Type : Host Port
IPv4 Address : 10.10.10.11
Subnet Mask : 255.255.255.0
IPv4 Gateway : --
IPv6 Address : --
IPv6 Prefix Length : --
IPv6 Gateway : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                    |
|--------------------|----------------------------|
| Port ID            | Port ID.                   |
| Type               | Port type.                 |
| IPv4 Address       | IPv4 address of the port.  |
| Subnet Mask        | Subnet mask of the port.   |
| IPv4 Gateway       | IPv4 gateway of the port.  |
| IPv6 Address       | IPv6 address of the port.  |
| IPv6 Gateway       | IPv6 gateway.              |
| IPv6 Prefix Length | Length of the IPv6 prefix. |
