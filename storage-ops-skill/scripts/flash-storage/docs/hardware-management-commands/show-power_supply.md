# show power_supply


##### Function

The **show power_supply** command is used to query details on power modules, such as the status, manufacturer, and type.

##### Format

**show power_supply** \[ power_supply_id=? \]

##### Parameters

| Parameter         | Description           | Value                                                                                                                                                                                      |
|-------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| power_supply_id=? | ID of a power module. | To obtain the value, run "**show power_supply**" without parameter. |

##### Usage Guidelines

-   To query details on all power modules, run "**show power_supply**".
-   To query details on a specific power module, run "**show power_supply** power_supply_id=?".

##### Example

To query details on all power modules, run the following command. The command output varies depending on a specific product.

```text

admin:/>show power_supply

ID Health Status Running Status Type
-------------- ------------- -------------- -----
CTE0.PSU0 Normal Online AC
CTE0.PSU1 Normal Online AC
DAE000.PSU0 Normal Online AC
DAE000.PSU1 Normal Online AC
```

To query details on the power module whose ID is "CTE0.PSU0", run the following command. The command output varies depending on a specific product.

```text
admin:/>show power_supply power_supply_id=CTE0.PSU0
ID : CTE0.PSU0
Health Status : Normal
Running Status : Online
Type : AC
Manufacturer : XX
Model : HSP480-S12A
Version : 02
Produce Date : 2017-06-01
Serial Number : 21021306712125020282
Item :02310TBR
Electronic Label : [Board Properties]
BoardType=HSP1950-S12A
BarCode=101590000118
Item=02310UWW-001
Description=Function Module,HSP1950-S12A,HSP1950-S12A,1950W platinum AC power supply unit
Manufactured=2017-06-01
VendorName=Huawei
IssueNumber=00
CLEICode=
BOM=
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                               |
|------------------|---------------------------------------|
| ID               | ID of the power module.               |
| Health Status    | Health status of the power module.    |
| Running Status   | Running status of the power module.   |
| Model            | Model of the power module.            |
| Type             | Type of the power module.             |
| Manufacturer     | Manufacturer of the power module.     |
| Vesion           | Version of the power module.          |
| Produce Date     | Produce date of the power module.     |
| Serial Number    | Serial number of the power module.    |
| Item             | BOM code of the power module.         |
| Electronic Label | Electronic label of the power module. |
