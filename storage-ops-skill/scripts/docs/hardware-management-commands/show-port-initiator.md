# show port initiator


##### Function

The **show port initiator** command is used to view the WWN information of all initiators that map to a port.

##### Format

**show port initiator** port_type=? port_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| port_type=? | Port type. | The value can be "FC", "ETH", or "BOND_PORT", where: <br>"FC": Fibre Channel port.<br>"ETH": Ethernet port (including an iSCSI host port and management port).<br>"BOND_PORT": bond port. |
| port_id=? | ID of a port. | The value can be: <br>When the "port_type" value is "ETH" or "FC", you can run "show port general" without parameters to obtain the port ID.<br>When the "port_type" value is "BOND_PORT", you can run "show bond_port" to obtain the port ID. |

##### Usage Guidelines

None

##### Example

View information about all initiators that map to port "ENG0.B3.P0".

```text
admin:/>show port initiator port_type=FC port_id=ENG0.B3.P0
WWN  Running Status  Free  Alias  Host ID  Multipath Type  Failover Mode  Path Type  Special Mode Type
----------------  --------------  ----  -----  -------  --------------  -------------  ---------  -----------------
2100373635343332  Online  Yes  --  --  Default  --  --  --
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Multipath Type | Multipathing mode. <br>Default: Huawei multipathing software is used.<br>Third-party: Third-party multipathing software is used. |
| Failover Mode | Failover mode of the initiator. <br>Old ALUA: ALUA of an earlier version.<br>Common ALUA: common ALUA.<br>No ALUA: ALUA not used.<br>Special Mode: special mode. |
| Special Mode Type | Special mode type of the initiator. <br>Mode0: special mode 0.<br>Mode1: special mode 1.<br>Mode2: special mode 2.<br>Mode3: special mode 3. |
| Path Type | Path type of the initiator. <br>Optimized: optimized path.<br>Non-optimized: non-optimized path. |
| WWN | WWN of the FC initiator. |
| Running Status | Running status of the initiator. |
| Free | Use status of the initiator. |
| Alias | Alias of the initiator. |
| Host ID | ID of the host to which the initiator is added. |
| iSCSI IQN | iSCSI initiator IQN. |
| CHAP Enabled | Whether the iSCSI initiator enables the CHAP authentication. |
| CHAP User | CHAP authentication user of the iSCSI initiator. |
