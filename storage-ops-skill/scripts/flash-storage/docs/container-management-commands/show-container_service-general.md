# show container_service general


##### Function

The **show container_service general** command is used to query container service information.

##### Format

**show container_service general**

##### Parameters

None

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query container service information.

```text
admin:/>show container_service general
Enabled                                      : On
Global Image Repository LUN ID               : 0
Global Image Repository LUN Name             : GLOBAL_LUN_0
Global Image Repository Totol Capacity       : 15.000TB
Global Image Repository Used Capacity        : 15.000GB
Deployed Node List                         : CTE0.A,CTE0.B
Undeployed Node List                       : CTE0.C,CTE0.D
Pool:
Type  ID  Name  Totol Capacity  Used Capacity
-----  --  ----  -------------  ------------
ImageRepositoryPool  0   storage_0             15.000TB   16.000GB
ApplicationPool      0   APPLICATION_IMAGE_0   150.000GB  15.000GB
ApplicationPool      1   APPLICATION_IMAGE_1   150.000GB  1.000GB
```

##### System Response

The following table describes the parameter meanings.

| Parameter                              | Meaning                                                          |
|----------------------------------------|------------------------------------------------------------------|
| Enabled                                | Whether the container service is enabled or disabled.            |
| Global Image Repository LUN Name       | Name of the global image LUN.                                    |
| Global Image Repository LUN ID         | ID of the global image LUN.                                      |
| Global Image Repository Totol Capacity | Total capacity of the global image LUN.                          |
| Global Image Repository Used Capacity  | Used capacity of the global image LUN.                           |
| Deployed Node List                     | List of nodes where the container service has been deployed.     |
| Undeployed Node List                   | List of nodes where the container service has not been deployed. |
| Pool                                   | Image repository storage pool.                                   |
| Type                                   | Type of the container storage pool.                              |
| ID                                     | ID of the container storage pool.                                |
| Name                                   | Name of the container storage pool.                              |
| Totol Capacity                         | Total capacity of the container storage pool.                    |
| Used Capacity                          | Used capacity of the container storage pool.                     |
