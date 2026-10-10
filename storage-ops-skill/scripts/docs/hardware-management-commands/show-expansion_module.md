# show expansion_module


##### Function

The **show expansion_module** command is used to query details on expansion modules. Run this command if you need to query an expansion module's type, status, and electronic label.

##### Format

**show expansion_module** \[ expansion_module_id=? \]

##### Parameters

| Parameter             | Description                | Value                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expansion_module_id=? | ID of an expansion module. | To obtain the value, run "**show expansion_module**" without parameter.The value contains 1 to 31 characters, including letters, digits, and periods (.). The value cannot start with a digit or a period (.), or end with a period (.). |

##### Usage Guidelines

-   To query details on all expansion modules, run "**show expansion_module**".
-   To query details on a specific expansion module, run "**show expansion_module** expansion_module_id=?".

##### Example

Query details on all expansion modules, run the following command. The command output varies depending on a specific product.

```text
admin:/>show expansion_module

ID Health Status Running Status Type Voltage(V)
-------- ------------- -------------- ---- ----------
DAE000.A Normal Running SAS 3.3
DAE000.B Normal Running SAS 3.3
```

Query details on the expansion module whose ID is "DAE000.A", run the following command. The ID and output vary depending on a specific product.

```text
admin:/>show expansion_module expansion_module_id=DAE000.A

ID : DAE000.A
Health Status : Normal
Running Status : Running
Type : SAS
Logic Version : 130T01
PCB Version : STL1DESA VER.B
SES Version : 10.00T43
Voltage(V) : 3.3
Electronic Label : [Board Properties]
BoardType=STL1DESA
BarCode=02G258D0C5000610
Item=0302G258
Description=PANGEA Hardware Platform,
STL1DESA,Disk Enclosure Cascading Board,1*1
Manufactured=2012-05-30
VendorName=Huawei
IssueNumber=
CLEICode=
BOM=
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| ID | ID of the expansion module. |
| Health Status | Health status of the expansion module. |
| Running Status | Running status of the expansion module. |
| Electronic Label | Electronic label of the expansion module. |
| Type | Type of the expansion module. <br>SAS.<br>Smart SAS.<br>Smart NVMe. |
| Logic Version | Logical version of the expansion module. |
| Voltage(V) | Voltage of the expansion module (V). |
| SES Version | SES version of the of the expansion module. |
| PCB Version | PCB version of the expansion module. |
