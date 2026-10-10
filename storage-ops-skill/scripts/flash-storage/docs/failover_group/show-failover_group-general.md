# show failover_group general


##### Function

The **show failover_group general** command is used to query failover groups on the storage system.

##### Format

**show failover_group general** \[ failover_group_id=? \| failover_group_name=? \| service_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of the failover group to be queried. | The value is an integer between 0 and 8191. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| service_type | Service type of the failover group. NOTE: The "NAS" parameter is only available on devices that support NAS services. | - |

##### Usage Guidelines

-   You can run the "**show failover_group general**" command to query information about all failover groups.
-   You can run the "**show failover_group general** failover_group_id=?" command to query information about a specific failover group.
-   You can run the "**show failover_group general** failover_group_name=?" command to query information about a specific failover group.
-   You can run the "**show failover_group general** service_type=?" command to query information about all failover groups with a specific service type.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query all failover groups.

```text
admin:/>show failover_group general
Failover Group ID Name                  Description                Group Type Service Type
----------------- --------------------- -------------------------- ---------- ------------
0                 System-defined        System-FailoverGroup       System     NAS
1                 SAN-failoverGroup1    Customized-FailoverGroup   Customized SAN
2                 SAN-failoverGroup2    Customized-FailoverGroup   Customized SAN
3                 SAN-failoverGroup3    Customized-FailoverGroup   Customized SAN
4097              VLAN-FailoverGroup-1  VLAN-FailoverGroup         VLAN       NAS
4098              VLAN-FailoverGroup-2  VLAN-FailoverGroup         VLAN       NAS
4101              VLAN-FailoverGroup-5  VLAN-FailoverGroup         VLAN       NAS
4102              VLAN-FailoverGroup-6  VLAN-FailoverGroup         VLAN       NAS
4104              VLAN-FailoverGroup-8  VLAN-FailoverGroup         VLAN       NAS
4184              VLAN-FailoverGroup-88 VLAN-FailoverGroup         VLAN       NAS
```

Query failover group "0".

```text
admin:/>show failover_group general failover_group_id=0
Failover Group ID : 0
Name : System-defined
Description : System-FailoverGroup
Group Type : System
Service Type : NAS
```

Query information about all failover groups whose service type is NAS.

```text
admin:/>show failover_group general service_type=NAS
Failover Group ID Name                  Description                Group Type Service Type
----------------- --------------------- -------------------------- ---------- ------------
0                 System-defined        System-FailoverGroup       System     NAS
4097              VLAN-FailoverGroup-1  VLAN-FailoverGroup         VLAN       NAS
4098              VLAN-FailoverGroup-2  VLAN-FailoverGroup         VLAN       NAS
4101              VLAN-FailoverGroup-5  VLAN-FailoverGroup         VLAN       NAS
4102              VLAN-FailoverGroup-6  VLAN-FailoverGroup         VLAN       NAS
4104              VLAN-FailoverGroup-8  VLAN-FailoverGroup         VLAN       NAS
4184              VLAN-FailoverGroup-88 VLAN-FailoverGroup         VLAN       NAS
```

Query information about all failover groups whose service type is SAN.

```text
admin:/>show failover_group general service_type=SAN
Failover Group ID Name                  Description                Group Type Service Type
----------------- --------------------- -------------------------- ---------- ------------
1                 SAN-failoverGroup1    Customized-FailoverGroup   Customized SAN
2                 SAN-failoverGroup2    Customized-FailoverGroup   Customized SAN
3                 SAN-failoverGroup3    Customized-FailoverGroup   Customized SAN
```

Query failover group with name "System-defined".

```text
admin:/>show failover_group general failover_group_name=System-defined
Failover Group ID : 0
Name : System-defined
Description : System-FailoverGroup
Group Type : System
Service Type : NAS
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                             |
|-------------------|-------------------------------------|
| Failover Group ID | ID of the failover group.           |
| Name              | Name of the failover group.         |
| Description       | Descriptions of the failover group. |
| Group Type        | Type of the failover group.         |
| Service Type      | Service type of the failover group. |
