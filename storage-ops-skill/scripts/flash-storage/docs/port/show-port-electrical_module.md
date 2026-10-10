# show port electrical_module


##### Function

The **show port electrical_module** command is used to query details on all electrical modules in the storage system.

##### Format

**show port electrical_module** \[ port_id=? \]

##### Parameters

| Parameter | Description           | Value                                                                                                                                                                                                   |
|-----------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port_id=? | Electrical module ID. | To obtain the value, run "**show port electrical_module**" without parameters. |

##### Usage Guidelines

-   Running the "**show port electrical_module**" command queries information about all electrical modules.
-   Running the "**show port electrical_module** port_id=?" command queries information about a specified electrical module.

##### Example

Query details on all electrical modules in the storage system. The command output varies depending on a specific product.

```text

admin:/>show port electrical_module

PortID          Health Status  Running Status  Working Rate(Mbps)  Vendor   Model        SN           Item  ExternalModel  Rev
--------------  -------------  --------------  ------------------  -------  -----------  -----------  ----  -------------  ---
CTE0.A.IOM1.P0  Normal         Link Up         100000              Hisense  LTA8531-PC+  U228AH000FL  0     0              0
admin:/>

```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning           |
|--------------------|-------------------|
| PortID             | Port ID.          |
| Health Status      | Health status.    |
| Running Status     | Running status.   |
| Working Rate(Mbps) | Working rate.     |
| Vendor             | Vendor.           |
| Model              | Model.            |
| SN                 | Serial number.    |
| Item               | Item code.        |
| ExternalModel      | External model.   |
| Rev                | Hardware version. |
