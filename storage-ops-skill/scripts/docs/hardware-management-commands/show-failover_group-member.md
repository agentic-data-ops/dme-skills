# show failover_group member


##### Function

The **show failover_group member** command is used to query the members in a failover group on the storage system.

##### Format

**show failover_group member** { failover_group_id=? \| failover_group_name=? } \[ type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of the failover group. | The value is an integer between 0 and 8191. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| type=? | Type of the object in the failover group. | The value can be "eth_port", "bond_port", or "vlan", where: <br>"eth_port": Ethernet port.<br>"bond_port": bond port.<br>"vlan": VLAN port. |

##### Usage Guidelines

-   You can run the "**show failover_group member** failover_group_id=?" command to query the Ethernet ports, bond ports, and VLAN ports in a specified failover group. Fibre Channel ports in a failover group cannot be queried.
-   You can run the "**show failover_group member** failover_group_id=0 type=?" command to query information about a failover group with a specified port type.
-   You can run the "**show failover_group member** failover_group_name=?" command to query the Ethernet ports, bond ports, and VLAN ports in a specified failover group. Fibre Channel ports in a failover group cannot be queried.
-   You can run the "**show failover_group member** failover_group_name=? type=?" command to query information about a failover group with a specified port type.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the Ethernet network ports, bond ports, and VLAN ports in failover group "0".

```text
admin:/>show failover_group member failover_group_id=0
ETH Port:
ID              Health Status  Running Status  Type       IPv4 Address  IPv6 Address  MAC                Role         Working Rate(Mbps)
--------------  -------------  --------------  ---------  ------------  ------------  -----------------  -----------  ------------------
CTE0.A.H0       Normal         Link Up         Host Port  --            --            d4:94:e8:0d:5d:62  INI and TGT  1000
CTE0.A.H1       Normal         Link Up         Host Port  --            --            d4:94:e8:0d:5d:64  INI and TGT  1000
CTE0.A.H2       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:61  INI and TGT  --
CTE0.A.H3       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:63  INI and TGT  --
CTE0.A.IOM0.P0  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ea  INI and TGT  --
CTE0.A.IOM0.P1  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:eb  INI and TGT  --
CTE0.A.IOM0.P2  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ec  INI and TGT  --
CTE0.A.IOM0.P3  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ed  INI and TGT  --
CTE0.B.H2       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:3e  INI and TGT  --
CTE0.B.H3       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:40  INI and TGT  --
CTE0.B.IOM0.P0  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:52  INI and TGT  --
CTE0.B.IOM0.P1  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:53  INI and TGT  --
CTE0.B.IOM0.P2  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:54  INI and TGT  --
CTE0.B.IOM0.P3  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:55  INI and TGT  --
Bond Port:
ID            Name      Health Status  Running Status  MTU   Port ID List
------------  --------  -------------  --------------  ----  -------------------
549772730113  bond_1_1  Normal         Link Up         1500  CTE0.B.H0,CTE0.B.H1
VLAN:
Name         Running Status  VLAN ID  MTU   Port Type  Port ID
-----------  --------------  -------  ----  ---------  ---------
bond_1_1.1   Link Up         1        1500  Bond       bond_1_1
```

Query the Ethernet network ports in failover group "0".

```text
admin:/>show failover_group member failover_group_id=0 type=eth_port
ID              Health Status  Running Status  Type       IPv4 Address  IPv6 Address  MAC                Role         Working Rate(Mbps)
--------------  -------------  --------------  ---------  ------------  ------------  -----------------  -----------  ------------------
CTE0.A.H0       Normal         Link Up         Host Port  --            --            d4:94:e8:0d:5d:62  INI and TGT  1000
CTE0.A.H1       Normal         Link Up         Host Port  --            --            d4:94:e8:0d:5d:64  INI and TGT  1000
CTE0.A.H2       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:61  INI and TGT  --
CTE0.A.H3       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:63  INI and TGT  --
CTE0.A.IOM0.P0  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ea  INI and TGT  --
CTE0.A.IOM0.P1  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:eb  INI and TGT  --
CTE0.A.IOM0.P2  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ec  INI and TGT  --
CTE0.A.IOM0.P3  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ed  INI and TGT  --
CTE0.B.H2       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:3e  INI and TGT  --
CTE0.B.H3       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:40  INI and TGT  --
CTE0.B.IOM0.P0  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:52  INI and TGT  --
CTE0.B.IOM0.P1  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:53  INI and TGT  --
CTE0.B.IOM0.P2  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:54  INI and TGT  --
CTE0.B.IOM0.P3  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:55  INI and TGT  --
```

Query the bond port in failover group "0".

```text
admin:/>show failover_group member failover_group_id=1 type=bond_port
ID            Name      Health Status  Running Status  MTU   Port ID List
------------  --------  -------------  --------------  ----  -------------------
549772730113  bond_1_1  Normal         Link Up         1500  CTE0.B.H0,CTE0.B.H1
```

Query VLAN port in failover group "4184".

```text
admin:/>show failover_group member failover_group_id=4184 type=vlan

Name         Running Status  VLAN ID  MTU   Port Type  Port ID
-----------  --------------  -------  ----  ---------  ---------
bond_1_1.1   Link Up         1        1500  Bond       bond_1_1
```

Query the Ethernet network ports, bond ports, and VLAN ports in failover group "System-defined".

```text
admin:/>show failover_group member failover_group_name=System-defined
ETH Port:
ID              Health Status  Running Status  Type       IPv4 Address  IPv6 Address  MAC                Role         Working Rate(Mbps)
--------------  -------------  --------------  ---------  ------------  ------------  -----------------  -----------  ------------------
CTE0.A.H0       Normal         Link Up         Host Port  --            --            d4:94:e8:0d:5d:62  INI and TGT  1000
CTE0.A.H1       Normal         Link Up         Host Port  --            --            d4:94:e8:0d:5d:64  INI and TGT  1000
CTE0.A.H2       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:61  INI and TGT  --
CTE0.A.H3       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:63  INI and TGT  --
CTE0.A.IOM0.P0  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ea  INI and TGT  --
CTE0.A.IOM0.P1  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:eb  INI and TGT  --
CTE0.A.IOM0.P2  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ec  INI and TGT  --
CTE0.A.IOM0.P3  Normal         Link Down       Host Port  --            --            04:9f:ca:05:33:ed  INI and TGT  --
CTE0.B.H2       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:3e  INI and TGT  --
CTE0.B.H3       Normal         Link Down       Host Port  --            --            d4:94:e8:0d:5d:40  INI and TGT  --
CTE0.B.IOM0.P0  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:52  INI and TGT  --
CTE0.B.IOM0.P1  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:53  INI and TGT  --
CTE0.B.IOM0.P2  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:54  INI and TGT  --
CTE0.B.IOM0.P3  Normal         Link Down       Host Port  --            --            7c:a2:3e:e1:f4:55  INI and TGT  --
Bond Port:
ID            Name      Health Status  Running Status  MTU   Port ID List
------------  --------  -------------  --------------  ----  -------------------
549772730113  bond_1_1  Normal         Link Up         1500  CTE0.B.H0,CTE0.B.H1
VLAN:
Name         Running Status  VLAN ID  MTU   Port Type  Port ID
-----------  --------------  -------  ----  ---------  ---------
bond_1_1.1   Link Up         1        1500  Bond       bond_1_1
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                                          |
|-----------|--------------------------------------------------|
| ETH Port  | Indicates the Ethernet port in a failover group. |
| Bond Port | Bond port in a failover group.                   |
| VLAN      | VLAN port in a failover group.                   |
