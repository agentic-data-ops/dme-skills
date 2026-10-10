# show port fibre_module


##### Function

The **show port fibre_module** command is used to query details on all optical transceivers in the storage system.

##### Format

**show port fibre_module** \[ port_id=? \]

##### Parameters

| Parameter | Description   | Value                                                                                                                                                                                         |
|-----------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port_id=? | ID of a port. | To obtain the value, run "**show port fibre_module**" without parameters. |

##### Usage Guidelines

-   Running the "**show port fibre_module**" command queries information about all optical transceivers.
-   Running the "**show port fibre_module** port_id=?" command queries information about a specified optical transceiver.

##### Example

Query details on all optical transceivers in the storage system. The command output varies depending on a specific product.

```text
admin:/>show port fibre_module

PortID          Health Status  Running Status  Type        Working Rate(Mbps)  Vendor            Model             SN                Item  ExternalModel  Rev  RxPowerReal(uW)              TxPowerReal(uW)
--------------  -------------  --------------  ----------  ------------------  ----------------  ----------------  ----------------  ----  -------------  ---  ---------------------------  ---------------------------
CTE0.A.IOM0.P3  Inconsistent   Link Down       Multi Mode  16000               EMULEX            AFBR-57F5MZ-ELX   AC1630J00L3       --    --             --   0.0                          0.1
CTE0.A.IOM2.P0  Normal         Link Up         Multi Mode  100000              INNOLIGHT         TR-FC85S-N00      INIAF5690312      --    --             --   634.4,511.8,715.8,639.0      1096.6,1096.6,1017.1,1061.0
CTE0.B.IOM1.P0  Normal         Link Down       Multi Mode  10000               HG GENUINE        MTRS-01X11-G      HA19330240001     --    --             --   --                           634.3
CTE0.B.IOM1.P2  Normal         Link Down       Multi Mode  10000               JDSU              PLRXPLSCS43HW     CE32HP076         --    --             --   --                           566.1
CTE0.B.IOM2.P0  Normal         Link Up         Multi Mode  100000              INNOLIGHT         TR-FC85S-N00      INIAP4050111      --    --             --   686.8,720.6,694.0,838.4      860.2,860.2,1036.9,1101.1
DAE030.A.P0     Normal         Link Up         Multi Mode  100000              Hisense           LTA8531-PC+       R9584001261       --    --             --   1182.1,1155.1,1117.3,1069.5  917.5,934.5,951.6,932.9
DAE030.B.P0     Normal         Link Up         Multi Mode  100000              INNOLIGHT         TR-FC85S-N00      INIAP4050117      --    --             --   1026.1,1070.7,1058.7,1108.5  731.8,731.8,813.3,732.2
```

Query the optical transceiver whose ID is "CTE0.A.IOM0.P0". The ID and output vary depending on a specific product.

```text
admin:/>show port fibre_module port_id=CTE0.A.IOM0.P0

PortID             : CTE0.A.IOM0.P0
Health Status      : Normal
Running Status     : Link Down
Type               : Multi Mode
Working Rate(Mbps) : 8000
Vendor             : Hisense
Model              : LTF8503-BC+
SN                 : P2661008340
Item               : --
ExternalModel      : --
Rev                : --
RxPowerReal(uW)    : 634.4,511.8,715.8,639.0
RxPowerMax(uW)     : 1737.8
RxPowerMin(uW)     : 93.3
TxPowerReal(uW)    : 1096.6,1096.6,1017.1,1061.0
TxPowerMax(uW)     : 1737.8
TxPowerMin(uW)     : 144.5
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                  |
|--------------------|--------------------------|
| PortID             | Port ID.                 |
| Health Status      | Health status.           |
| Running Status     | Running status.          |
| Type               | Mode type.               |
| Working Rate(Mbps) | Working rate.            |
| Vendor             | Vendor.                  |
| Model              | Model.                   |
| SN                 | Serial number.           |
| Item               | Item encoding.           |
| ExternalModel      | External model.          |
| Rev                | Hardware version.        |
| RxPowerReal(uW)    | Actual receiving power.  |
| TxPowerReal(uW)    | Actual sending power.    |
| RxPowerMax(uW)     | Maximum receiving power. |
| RxPowerMin(uW)     | Minimum receiving power. |
| TxPowerMax(uW)     | Maximum sending power.   |
| TxPowerMin(uW)     | Minimum sending power.   |
