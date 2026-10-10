# show enclosure


##### Function

The **show enclosure** command is used to query details on the engine and disk enclosure.

##### Format

**show enclosure** \[ enclosure_id=? \]

##### Parameters

| Parameter      | Description                        | Value                                                                                                                                                                             |
|----------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| enclosure_id=? | ID of an engine or disk enclosure. | To obtain the value, run "**show enclosure**" without parameter. |

##### Usage Guidelines

-   To query details on all engines and disk enclosures, run "**show enclosure**".
-   To query details on a specific engine or disk enclosure, run "**show enclosure** enclosure_id=?".

##### Example

Query details on all engines and disk enclosures. The command output varies depending on a specific product and the actual page prevails.

```text
admin:/>show enclosure
ID      Logic Type           Health Status  Running Status  Type                                Temperature(Celsius)
------  -------------------  -------------  --------------  ----------------------------------  --------------------
CTE0    Engine               Normal         Online          3U 2 Controllers Enclosure          28
DAE000  Expansion Enclosure  Normal         Online          2U 25 Slot 2.5 SAS Disks Enclosure  26
```

Query details on the engine whose ID is "CTE0". The command output varies depending on a specific product and the actual page prevails.

```text
admin:/>show enclosure enclosure_id=CTE0

ID : CTE0
Logic Type : Engine
Health Status : Normal
Running Status : Online
Location : SMB0.20U
Type : BMC Controller Enclosure
Temperature(Celsius) : 50
SN : --
MAC : --
Height(U) : 4
Expansion Depth : 0
Electronic Label     : [Board Properties]
BoardType=STLZ02ENGA
BarCode=210235980510F3000007
Item=02359805
Description=OceanStor 5600 V3,STLZ02ENGA,5600 V3(3U,Dual Ctrl,AC,128GB,SPE62C0300)
Manufactured=2015-03-18
VendorName=Huawei
IssueNumber=00
CLEICode=
BOM=
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                            |
|----------------------|------------------------------------|
| ID                   | Enclosure ID.                      |
| Logic Type           | Logical type of the enclosure.     |
| Health Status        | Health status of the enclosure.    |
| Running Status       | Running status of the enclosure.   |
| Location             | Position of the enclosure.         |
| Type                 | Enclosure type.                    |
| Temperature(Celsius) | Enclosure temperature (°C).        |
| SN                   | Enclosure SN.                      |
| MAC                  | MAC address of the enclosure.      |
| Height(U)            | Enclosure height.                  |
| Expansion Depth      | Expansion depth of the enclosure.  |
| Electronic Label     | Electronic label of the enclosure. |
