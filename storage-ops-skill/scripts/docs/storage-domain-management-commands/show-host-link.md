# show host link


##### Function

The **show host link** command is used to query details on host links configured for the storage system.

##### Format

**show host link** host_id=? initiator_type=?

**show host link** host_name=? initiator_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_id=? | ID of a host. | To obtain the value, run "show host general". |
| initiator_type=? | Type of an initiator. | The value can be "iSCSI", "FC", or "NVMe_over_RoCE", where: <br>"iSCSI": iSCSI initiators.<br>"FC": Fibre Channel initiators.<br>"NVMe_over_RoCE": NVMe over RoCE initiators. |
| host_name | Host name. | To obtain the value, run "show host general". |

##### Usage Guidelines

-   Run the "**show host link** host_id=?" command to query host link information.
-   Run the "**show host link** host_id=? initiator_type=?" command to query information about links of a specified initiator type of a host.

##### Example

Query details of links of the iSCSI initiator type of the host whose ID is "0".

```text
admin:/>show host link host_id=0

Health Status  Running Status  Initiator Type   Host ID  Initiator ID                                   Target ID                                                              Port        Initiator Alias  IsConfigToPortGroup  Host IP
-------------  --------------  ---------------  -------  ---------------------------------------------  ---------------------------------------------------------------------  ----------  ---------------  -------------------  ------------
Normal         Online          FC Initiator     0        10000090fa6443b2                               200974a063fdafa0                                                       CTE0.A1.P1                   false
Normal         Online          FC Initiator     0        21000024ff540bb4                               200974a063fdafa0                                                       CTE0.A1.P1                   false
Normal         Online          FC Initiator     0        10000090fa6443b2                               200a74a063fdafa0                                                       CTE0.A1.P2                   false
Normal         Online          FC Initiator     0        21000024ff540bb4                               200a74a063fdafa0                                                       CTE0.A1.P2                   false
Normal         Online          FC Initiator     0        2219602e20c16021                               200a74a063fdafa0                                                       CTE0.A1.P2                   false
Normal         Online          FC Initiator     0        10000090fa6443b2                               201874a063fdafa0                                                       CTE0.B1.P0                   false
Normal         Online          FC Initiator     0        21000024ff540bb4                               201874a063fdafa0                                                       CTE0.B1.P0                   false
Normal         Online          iSCSI Initiator  0        iqn.1996-04.de.suse12-sp3-client-8.46.123.184  iqn.2006-08.com.huawei:oceanstor:210074a063fdafa0::20400:8.47.111.122  CTE0.A4.P0                   false                8.47.123.184
```

Query details of links of the iSCSI initiator type of the host whose name is "host001".

```text
admin:/>show host link host_name=host001
Health Status  Running Status  Initiator Type   Host ID  Initiator ID                                   Target ID                                                              Port        Initiator Alias  IsConfigToPortGroup  Host IP
-------------  --------------  ---------------  -------  ---------------------------------------------  ---------------------------------------------------------------------  ----------  ---------------  -------------------  ------------
Normal         Online          FC Initiator     0        10000090fa6443b2                               200974a063fdafa0                                                       CTE0.A1.P1                   false
Normal         Online          FC Initiator     0        21000024ff540bb4                               200974a063fdafa0                                                       CTE0.A1.P1                   false
Normal         Online          FC Initiator     0        10000090fa6443b2                               200a74a063fdafa0                                                       CTE0.A1.P2                   false
Normal         Online          FC Initiator     0        21000024ff540bb4                               200a74a063fdafa0                                                       CTE0.A1.P2                   false
Normal         Online          FC Initiator     0        2219602e20c16021                               200a74a063fdafa0                                                       CTE0.A1.P2                   false
Normal         Online          FC Initiator     0        10000090fa6443b2                               201874a063fdafa0                                                       CTE0.B1.P0                   false
Normal         Online          FC Initiator     0        21000024ff540bb4                               201874a063fdafa0                                                       CTE0.B1.P0                   false
Normal         Online          iSCSI Initiator  0        iqn.1996-04.de.suse12-sp3-client-8.46.123.184  iqn.2006-08.com.huawei:oceanstor:210074a063fdafa0::20400:8.47.111.122  CTE0.A4.P0                   false                8.47.123.184
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning                                    |
|---------------------|--------------------------------------------|
| Health Status       | Health status.                             |
| Running Status      | Link status.                               |
| Initiator Type      | Initiator type.                            |
| Host ID             | Host ID.                                   |
| Initiator ID        | Initiator ID.                              |
| Target ID           | Target ID.                                 |
| Port                | Port.                                      |
| Initiator Alias     | Initiator alias.                           |
| IsConfigToPortGroup | Whether the port is added to a port group. |
| Host IP             | Host IP address.                           |
