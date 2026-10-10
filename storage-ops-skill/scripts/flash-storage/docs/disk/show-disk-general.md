# show disk general


##### Function

The **show disk general** command is used to query disk information.

##### Format

**show disk general** \[ disk_id=? \]

##### Parameters

| Parameter | Description | Value                                                                                                                                                                               |
|-----------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| disk_id=? | Disk ID.    | To obtain the value, run "**show disk general**" without parameters. |

##### Usage Guidelines

-   Run "**show disk general**" to query information about all disks.
-   Run "**show disk general** disk_id=?" to query information about a specific disk.

##### Example

Query information about all disks. The command output varies depending on a specific product.

```text
admin:/>show disk general
ID      Health Status  Running Status  Type      Capacity   Role       Disk Domain ID  Speed(RPM)  Health Mark  Bar Code              Item      AutoLock State  Key Expiration Time  Manufacture Capacity
------  -------------  --------------  --------  ---------  ---------  --------------  ----------  -----------  --------------------  --------  --------------  -------------------  --------------------
CTE0.0  Normal         Online          NVMe SSD  925.759GB  Free Disk  --              --          --           210235G6BB1000000007  0235G6M8  OFF             --                   960.000GB
CTE0.1  Normal         Online          NVMe SSD  925.759GB  Free Disk  --              --          --           210235G6BB1000000007  0235G6M8  OFF             --                   960.000GB
CTE0.2  Normal         Online          NVMe SSD  925.759GB  Free Disk  --              --          --           210235G6BB1000000007  0235G6M8  OFF             --                   960.000GB
CTE0.3  Normal         Online          NVMe SSD  925.759GB  Free Disk  --              --          --           210235G6BB1000000007  0235G6M8  OFF             --                   960.000GB
CTE0.4  Normal         Online          NVMe SSD  930.759GB  Free Disk  --              --          --           210235G6BB1000000007  0235G6M8  OFF             --                   960.000GB
CTE0.5  Normal         Online          NVMe SSD  930.759GB  Free Disk  --              --          --           210235G6BB1000000007  0235G6M8  OFF             --                   960.000GB
```

Query information about a disk. The command output varies depending on a specific product.

```text
admin:/>show disk general disk_id=DAE000.0
ID : DAE000.0
Health Status : Normal
Running Status : Online
Type : NVMe SSD
Capacity : 561.994GB
Role : Member Disk
Disk Domain ID : 0
Speed(RPM) : 10000
Interface Bandwidth(Mbps) : 12000
Sector Size : 4.062KB
Temperature(Celsius) : 36
Model : HUC101860CS4205
Firmware Version : D3B0
Manufacturer : Hitachi
Serial Number : 03G2173Z
Light Status : Off
Disk Domain Name : DiskDomain001
Disk Domain Tier ID : 0.1
Coffer Disk : No
Run Time(Day) : 39
Progress(%) : 0
Health Mark : --
Multipathing : 0A:normal,0B:normal
Bad Time : --
Bad Type : --
Sense Key : --
Sense Code : --
Fru : --
Bar Code : 210235G6BB1000000007
Bad Rate(%) : --
Capacity Usage(%) : 0
Smart Cache Pool ID : --
Electronic Label : [Board Properties]
BoardType=STLZ5S500
BarCode=210235G6BB1000000007
Item=0235G6M8
Description=PANGEA,STLZ5S500,500GB 7.2K RPM 3G SATA Disk Unit(2.5")
Manufactured=2012-05-31
VendorName=Huawei
IssueNumber=00
CLEICode=
BOM=
AutoLock State : ON
Degree of Wear(%) : --
Estimated Life Remaining(Month) : --
Key Expiration Time : --
Data Erasure Progress(%) : 0
Manufacture Capacity : 600.000GB
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| ID | Disk ID. |
| Health Status | Health status. |
| Running Status | Running status. |
| Type | Disk type. |
| Capacity | Disk capacity. The capacity is calculated based on the sector size of 512 bytes. If the sector size employed by a disk is not 512 bytes, the value may be different from the actual capacity. |
| Role | Role of a disk. |
| Disk Domain ID | Disk domain ID of a disk. |
| Speed(RPM) | Revolutions per minute (rpm). |
| Health Mark | Health score. |
| Interface Bandwidth(Mbps) | Interface bandwidth (Mbit/s). |
| Sector Size | Sector size. |
| Temperature(Celsius) | Temperature (°C). |
| Model | Product model. |
| Firmware Version | Firmware version. |
| Manufacturer | Manufacturer. |
| Serial Number | Serial number. |
| Light Status | Light status. |
| Disk Domain Name | Disk domain name of a disk. |
| Disk Domain Tier ID | Disk domain tier ID of a disk. |
| Coffer Disk | Whether this disk is a coffer disk. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Run Time(Day) | Running period (day). |
| Progress(%) | Progress of reconstruction. |
| Multipathing | Information about paths. |
| Bad Time | Time when the fault occurs. |
| Bad Type | Fault type. |
| Sense Key | Sense key of a disk. |
| Sense Code | Sense code of a disk. |
| Fru | Field replacement unit. |
| Bar Code | Bar code. |
| Bad Rate(%) | Fault rate. |
| Capacity Usage(%) | Capacity usage. |
| Electronic Label | Electronic label. |
| AutoLock State | Whether the encryption functionality is enabled. |
| Degree of Wear(%) | Wearing degree. |
| Estimated Life Remaining(Month) | Estimated remaining life (month). |
| Item | Disk BOM number. |
| Key Expiration Time | Key expiration time. |
| Data Erasure Progress(%) | Progress of data erasure. |
| Manufacture Capacity | Disk capacity defined by the disk manufacturer. |
