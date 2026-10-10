# show bbu general


##### Function

The **show bbu general** command is used to query details on BBUs. Run this command if you need to query a BBU's status, voltage, and the ID of the controller module where the BBU resides.

##### Format

**show bbu general** \[ bbu_id=? \]

##### Parameters

| Parameter | Description  | Value                                                                                                                                                                           |
|-----------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bbu_id=?  | ID of a BBU. | To obtain the value, run "**show bbu general**" without parameter. |

##### Usage Guidelines

None.

##### Example

Query details on all BBUs, run the following command. The command output varies depending on a specific product.

```text
admin:/>show bbu general
ID      Health Status  Running Status  Current Voltage(V)  Number Of Discharges
------  -------------  --------------  ------------------  --------------------
CTE0.0  Normal         Online          15.9                18
CTE0.1  Normal         Online          15.9                16
CTE0.2  Normal         Online          15.8                2
```

Query details on the BBU whose ID is "CTE0.0", run the following command. The ID and output vary depending on a specific product.

```text
admin:/>show bbu general bbu_id=CTE0.0
ID                   : CTE0.0
Health Status        : Normal
Running Status       : Online
Current Voltage(V)   : 15.9
Number Of Discharges : 18
Firmware Version     : 30.05T4
Delivered On         : 2014-11-20
Owning Controller    : 0A
Electronic Label     : [Board Properties]
BoardType=STLZ03PWRA
BarCode=210235913710F1000356
Item=02359137
Description=Assembling Components,PANGEA,STLZ03PWRA,Backup Battery Unit
Manufactured=2015-01-20
VendorName=Huawei
IssueNumber=00
CLEICode=
BOM=
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                         |
|----------------------|---------------------------------|
| ID                   | BBU ID.                         |
| Health Status        | Health status of a BBU.         |
| Running Status       | Running status of a BBU.        |
| Current Voltage(V)   | Current voltage of the BBU (V). |
| Number Of Discharges | Times of BBU discharge.         |
| Firmware Version     | Firmware version of the BBU.    |
| Delivered On         | Delivery time of the BBU.       |
| Owning Controller    | Owning controller of the BBU.   |
| Electronic Label     | Electronic label of the BBU.    |
