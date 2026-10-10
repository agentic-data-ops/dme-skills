# show system general


##### Function

The **show system general** command is used to query the general system information.

##### Format

**show system general**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the general system information. The command output varies depending on a specific product. In the following command output, the fields related to the product model are replaced by "X".

```text
admin:/>show system general
System Name         : XXX.Storage
Health Status       : Normal
Running Status      : Normal
Total Capacity      : 3.186TB
SN                  : 210235G6EHZ0CX0000XX
Location            :
Product Model       : XXXX
Product Version     : X.X.X
High Water Level(%) : 80
Low Water Level(%)  : 20
WWN                 : XXXX
Time                : 2015-07-07/15:34:05 UTC+08:00
Patch Version       : SPCXXX SPHXXX
Description         :
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| System Name | Device name. |
| Health Status | Indicates the health status. |
| Running Status | Indicates the running status. |
| Total Capacity | In effective capacity mode, this field indicates the total amount of user data that can be written into the storage device. In non-effective capacity mode, this field indicates the total capacity of all storage pools in the storage device. |
| SN | Device serial number. |
| Location | Device location. |
| Product Model | Product model. |
| Product Version | Product version. |
| High Water Level(%) | High water level that is the upper threshold for the amount of the dirty data stored in the cache. When the amount of the dirty data stored in the cache reaches the high water level, the cache starts to synchronize dirty data into disks. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Low Water Level(%) | Low water level that is the low threshold for the amount of dirty data stored in the cache. When the amount of the dirty data stored in the cache falls to the low water level, the cache stops synchronizing dirty data into disks. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Time | Current time. |
| WWN | WWN information of the device. |
| Patch Version | Patch version. |
| Internal Product Model | Internal model. |
| Description | Device description. |
