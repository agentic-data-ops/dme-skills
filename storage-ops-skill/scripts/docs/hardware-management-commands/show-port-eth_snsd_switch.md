# show port eth_snsd_switch


##### Function

The **show port eth_snsd_switch** command is used to query the switch status of the SNSD function of an Ethernet port.

##### Format

**show port eth_snsd_switch** eth_port_id=?

##### Parameters

| Parameter   | Description | Value                                         |
|-------------|-------------|-----------------------------------------------|
| eth_port_id | Port ID.    | To obtain the value, run "show port general". |

##### Usage Guidelines

Before performing this operation, ensure that the Ethernet port supports the SNSD function.

##### Example

Query whether the SNSD function of Ethernet port "CTE0.A.H0" is enabled. The ID and command output vary depending on products. The ID and output here are just examples.

```text
admin:/>show port eth_snsd_switch eth_port_id=CTE0.A.H0
ETH Storage Network Smart Discovery Enable:Yes

```

##### System Response

The following table describes the parameter meanings.

| Parameter                                  | Meaning                             |
|--------------------------------------------|-------------------------------------|
| ETH Storage Network Smart Discovery Enable | Switch status of the SNSD function. |
