# show controller general


##### Function

The **show controller general** command is used to query details on controllers.

##### Format

**show controller general** \[ controller=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller=? | ID of a controller. | The value format is XA, XB, XC, or XD, where X is an integer ranging from 0 to 99. You can run the "show controller general" command to obtain the value. |

##### Usage Guidelines

-   To query details on all controllers, run "**show controller general**".
-   To query details on a specific controller, run "**show controller general** controller=?".

##### Example

Query details on all controllers, run the following command. The command output varies depending on a specific product.

```text
admin:/>show controller general
Controller                : 0A
Health Status             : Normal
Running Status            : Online
CPU                       : Intel 6core 2.1GHz *1
Location                  : CTE0.A
Role                      : Master
Cache Capacity            : 128.000GB
CPU Usage(%)              : 2
Memory Usage(%)           : 85
Temperature(Celsius)      : --
Voltage(V)                : 12.0
Software Version          : 5.60.01.300
PCB Version               : VER.B
SES Version               : --
BMC Version               : 29.00.01T12
Logic Version             : 00.00.300T07
BIOS Version              : 10.01.05T57
All Temperatures(Celsius) : --
Electronic Label          : [Board Properties]
BoardType=STL2SPCC01
BarCode=030WBE10E7000032
Item=03030WBE
Description=Finished Board,PANGEA,STL2SPCC01,Controller Module(1 *Intel 6 Cores , 64GB Cache,1*mSATA),V2R1C01
Manufactured=2014-07-13
VendorName=Huawei
IssueNumber=00
CLEICode=
BOM=
Disk Version: 1:SP826G
Starting Point Date         : 2020-12-17
Session                     : 12

-------------------------------------------------------------------------------------------------------------------------------------------
Controller                : 0B
Health Status             : Normal
Running Status            : Online
CPU                       : Intel 6core 2.1GHz *1
Location                  : CTE0.B
Role                      : Slave
Cache Capacity            : 128.000GB
CPU Usage(%)              : 3
Memory Usage(%)           : 84
Temperature(Celsius)      : --
Voltage(V)                : 12.0
Software Version          : 5.60.01.300
PCB Version               : VER.B
SES Version               : --
BMC Version               : 29.00.01T12
Logic Version             : 00.00.300T07
BIOS Version              : 10.01.05T57
All Temperatures(Celsius) : --
Electronic Label          : [Board Properties]
BoardType=STL2SPCC01A
BarCode=210305607610F1000033
Item=03056076
Description=Finished Board Unit,PANGEA,STL2SPCC01A,Controller Module(1 *Intel 6 Cores , 64GB Cache)
Manufactured=2015-01-23
VendorName=Huawei
IssueNumber=00
CLEICode=
BOM=
Disk Version: 1:SP826G
Starting Point Date         : 2020-12-17
Session                     : 12
```

##### System Response

The following table describes the parameter meanings.

| Parameter                    | Meaning                                                 |
|------------------------------|---------------------------------------------------------|
| Controller                   | Controller ID.                                          |
| Health Status                | Health status of the controller.                        |
| Running Status               | Running status of the controller.                       |
| CPU                          | CPU model of the controller.                            |
| Location                     | Silkscreen of the controller.                           |
| Role                         | Cluster role of the controller.                         |
| Cache Capacity               | Capacity of the controller cache.                       |
| CPU Usage(%)                 | Controller CPU usage (%).                               |
| Memory Usage(%)              | Memory usage of the operating system on the controller. |
| Temperature(Celsius)         | Temperature of the controller (°C).                     |
| Voltage(V)                   | Controller voltage (V).                                 |
| Software Version             | Controller software version.                            |
| PCB Version                  | Controller PCB version.                                 |
| SES Version                  | Controller SES version.                                 |
| BMC Version                  | Controller BMC version.                                 |
| Logic Version                | Controller logical version.                             |
| BIOS Version                 | Controller BIOS version.                                |
| Electronic Label             | Controller electronic label.                            |
| Dirty Data Rate(%)           | Percentage of controller dirty data.                    |
| Multiple Work Mode Supported | Multiple work modes supported by a controller.          |
| Run Mode                     | Running status of the controller.                       |
| Supported Run Mode List      | List of running modes supported by the controller.      |
| Disk Version                 | Controller disk version.                                |
| Starting Point Date          | Service start time of the controller.                   |
| Session                      | Service life of a controller.                           |
