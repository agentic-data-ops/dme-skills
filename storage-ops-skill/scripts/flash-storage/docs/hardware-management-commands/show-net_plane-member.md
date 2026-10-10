# show net_plane member


##### Function

The **show net_plane member** command is used to query information about network plane members on a storage system.

##### Format

**show net_plane member** net_plane_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| net_plane_id | Network plane ID. | The value ranges from 1 to 1024.<br>To obtain the value, run the "show net_plane general" command without parameters. |

##### Usage Guidelines

Run the "**show net_plane member** net_plane_id=?" command to query port information on a specified network plane.

##### Example

Query the port information on the network plane whose ID is "1".

```text
admin:/>show net_plane member net_plane_id=1
ETH Port:
ID              Health Status  Running Status  Type       IPv4 Address  IPv6 Address  MAC                Role         Working Rate(Mbps)
--------------  -------------  --------------  ---------  ------------  ------------  -----------------  -----------  ------------------
CTE0.A.IOM2.P0  Normal         Link Up         --         --            --            d4:94:e8:0d:5d:62  --           25000
CTE0.A.IOM2.P3  Normal         Link Up         --         --            --            d4:94:e8:0d:5d:64  --           25000
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                      |
|--------------------|------------------------------|
| ID                 | ID of a port.                |
| Health Status      | Health status of a port.     |
| Running Status     | Running status of a port.    |
| Type               | Port type.                   |
| IPv4 Address       | IPv4 address of an ETH port. |
| IPv6 Address       | IPv6 address of an ETH port. |
| MAC                | MAC address of an ETH port.  |
| Role               | Role of a port in the link.  |
| Working Rate(Mbps) | Working rate of a port.      |
