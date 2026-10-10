# show interface_module


##### Function

The **show interface_module** command is used to query information about an interface module.

##### Format

**show interface_module** \[ interface_module_id=? \]

##### Parameters

| Parameter             | Description                | Value                                                                                                                                                                                                                                                                                      |
|-----------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| interface_module_id=? | ID of an interface module. | To obtain the value, run "**show interface_module**" without parameters. The value contains 1 to 31 characters, including letters, digits, and periods (.). |

##### Usage Guidelines

-   Run the "**show interface_module**" command to query details on all interface modules.
-   Run the "**show interface_module** interface_module_id=?" command to query details on a specific interface module.

##### Example

Query details on all interface modules. The command output varies depending on a specific product.

```text

admin:/>show interface_module

ID         Health Status  Running Status  Model                             Usage Type
---------  -------------  --------------  --------------------------------  --------------
CTE0.A0    Normal         Running         4x12G SAS QSFP Interface Module   Storage
CTE0.A3    Normal         Running         4 port SmartIO I/O Module         Storage
CTE0.A4    Normal         Running         4 port SmartIO I/O Module         Storage
CTE0.A7    Normal         Running         4xGE Electrical Interface Module  Storage
CTE0.B0    Normal         Running         4x12G SAS QSFP Interface Module   Storage
CTE0.B3    Normal         Running         4 port SmartIO I/O Module         Storage
CTE0.B4    Normal         Running         4 port SmartIO I/O Module         Storage
CTE0.B7    Normal         Running         4xGE Electrical Interface Module  Storage
CTE0.SMM0  Normal         Running         Management Board                  Storage
CTE0.SMM1  Normal         Running         Management Board                  Storage

```

Query details on the interface module whose ID is "CTE0.A3". The ID and output vary depending on a specific product.

```text

admin:/>show interface_module interface_module_id=CTE0.A3

ID                           : CTE0.A3
Health Status                : Normal
Running Status               : Running
Model                        : 4 port SmartIO I/O Module
Logic Version                : --
PCB Version                  : VER.B
Temperature(Celsius)         : --
Electronic Label             : [Board Properties]
BoardType=STL2IIC4OA
BarCode=022PUJ10F1000078
Item=03022PUJ
Description=Manufactured Board,PANGEA,STL2IIC4OA,4 port SmartIO I/O module(SFP+,without optical transceiver),2*1
Manufactured=2015-01-25
VendorName=Huawei
IssueNumber=00
CLEICode=
BOM=

Multiple Work Mode Supported : Yes
Run Mode                     : FC
Supported Run Mode List      : FC,Ethernet
Usage Type                   : Storage
admin:/>

```

##### System Response

The following table describes the parameter meanings.

| Parameter                    | Meaning                                                   |
|------------------------------|-----------------------------------------------------------|
| ID                           | Interface module ID.                                      |
| Health Status                | Health status of an interface module.                     |
| Running Status               | Running status of an interface module.                    |
| Model                        | Interface module type.                                    |
| Logic Version                | Logical version of an interface module.                   |
| PCB Version                  | PCB version of an interface module.                       |
| Temperature(Celsius)         | Temperature of an interface module (°C).                  |
| Electronic Label             | Electronic labels of an interface module.                 |
| Multiple Work Mode Supported | Whether an interface module supports multiple work modes. |
| Run Mode                     | Running mode of an interface module.                      |
| Supported Run Mode List      | List of running modes supported by an interface module.   |
| Usage Type                   | Usage of an interface module.                             |
