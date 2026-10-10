# change port fc


##### Function

The **change port fc** command is used to modify the properties of a specific Fibre Channel port.

##### Format

**change port fc** fc_port_id=? { speed=? \| mode=? \| flogin_delay_times=? \| role=? \| fast_write_enable=? \| protocol=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| fc_port_id=? | ID of a port. | To obtain the value, run "show port general physical_type=FC". |
| flogin_delay_times=? | Delay time that the system waits before sending the FLOGIN command. Set a proper delay time based on a specific HBA type. NOTE: FLOGIN, an interactive command in the Fibre Channel protocol, is used to negotiate parameters related to Fibre Channel links. After a storage system and a host interconnect by using an optical fiber, both parties need to send the FLOGIN command to determine the parameters supported by the peer party. | The value can be "500" or "0", expressed in microsecond, where: <br>"500": applicable to the scenario where the server connected to the storage system is equipped with a Brocade 825 HBA.<br>"0": applicable to the scenario where the server connected to the storage system is equipped with other types of HBAs. |
| mode=? | Fibre Channel port mode. | The value can be "FC-AL", "point-to-point", or "auto_adapt", where: <br>"FC-AL": indicates the arbitrated loop mode.<br>"point-to-point": indicates the point-to-point mode.<br>"auto_adapt": indicates the autonegotiation mode. |
| speed=? | Updated port rate. | The value can be "auto_adapt", "2Gbps", "4Gbps", "8Gbps", "16Gbps", or "32Gbps", where: <br>"auto_adapt": The autonegotiation mode is adopted.<br>"2Gbps": The port rate is 2 Gbit/s.<br>"4Gbps": The port rate is 4 Gbit/s.<br>"8Gbps": The port rate is 8 Gbit/s.<br>"16Gbps": The port rate is 16 Gbit/s.<br>"32Gbps": The port rate is 32 Gbit/s. |
| role=? | Role of the Fibre Channel port. | The value can be "ini", "tgt", or "ini_and_tgt", where: <br>"ini": initiator (the 8 Gbit/s Fibre Channel I/O module cannot support this function).<br>"tgt": target.<br>"ini_and_tgt": initiator and target. |
| fast_write_enable=? | State of FastWrite. | The value can be "yes" or "no", where: <br>"yes": FastWrite is enabled.<br>"no": FastWrite is disabled. |
| protocol=? | Protocol type of the Fibre Channel port. | The value can be "FC-SCSI" or "FC-NVMe", the default value is "FC-SCSI", where: <br>"FC-SCSI": SCSI protocol.<br>"FC-NVMe": NVMe protocol. |

##### Usage Guidelines

-   Running this command causes ongoing services between the storage system and host to be interrupted for a short period.
-   If the port mode specified in this command does not match that of the peer Fibre Channel host port, running this command causes the connection between the host and storage system to be interrupted.
-   Before running this command, ensure that the port rate, port mode, and protocol type match those of the peer Fibre Channel host port.
-   If the updated port rate conflicts with the peer port rate, the host and storage system cannot be connected to each other, and services cannot be recovered.

##### Example

Set the properties of the Fibre Channel host port whose ID is "CTE0.A1.P1", where the delay time for sending the FLOGIN command is 0 μs and the port mode is "point-to-point". The ID and output vary depending on a specific product.

```text
admin:/>change port fc fc_port_id=CTE0.A1.P1 flogin_delay_times=0 mode=point-to-point
DANGER: You are about to change the working mode or role of the service port, or modify the fast write or MOR switch of the port. If host services are running on the port, this operation will cause I/O errors. If the topology mode or port attribute of the FC front-end port does not match that of the peer FC port, this operation will interrupt the connection between the host and the storage device.
Suggestion: Before performing this operation, ensure that no host service is running on the port.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Set the protocol type of Fibre Channel port "CTE0.A.IOM1.P0" to FC-NVMe. The ID and command output vary depending on products.

```text
admin:/>change port fc fc_port_id=CTE0.A.IOM1.P0 protocol=FC-NVMe
DANGER: You are about to modify the protocol type of the FC service port. If the protocol types of the front-end and peer FC ports do not match, this operation will result in service interruption and may bring service loss.
Suggestion: Perform this operation under the guidance of R&D engineers.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Set the rate of Fibre Channel port "CTE0.A.IOM1.P0" to 8 Gbit/s. The ID and command output vary depending on products.

```text
admin:/>change port fc fc_port_id=CTE0.A.IOM1.P0 speed=8Gbps
DANGER: You are about to modify the rate of FC front-end port. If its rate is different from that of the peer FC front-end port, the host will be disconnected from the storage system.
Suggestion: Before performing this operation, determine the rate supported by the peer FC port.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
