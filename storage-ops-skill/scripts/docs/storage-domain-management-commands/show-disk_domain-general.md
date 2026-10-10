# show disk_domain general


##### Function

The **show disk_domain general** command is used to query information about disk domains.

##### Format

**show disk_domain general** \[ disk_domain_id=? \]

##### Parameters

| Parameter        | Description     | Value                          |
|------------------|-----------------|--------------------------------|
| disk_domain_id=? | Disk domain ID. | The value ranges from 0 to 63. |

##### Usage Guidelines

-   Run the "**show disk_domain general**" command to query basic information about all disk domains.
-   Run the "**show disk_domain general** disk_domain_id=?" command to query details about a specified disk domain.

##### Example

Query information about disk domain 0.

```text
admin:/>show disk_domain general disk_domain_id=0
ID : 0
Name : DM
Health Status : Normal
Running Status : Online
Total Capacity : 4.830TB
Free Capacity : 4.342TB
Hot Spare Capacity : 499.687GB
Used Hot Spare Capacity : 0.000B
Hot Spare Strategy : Low
Disk Number : 16
Wear Leveling State :  Wear Leveling
Anti Wear Leveling Disk ID :  --
Tier0 Disk Number : 8
Tier0 Total Capacity : 1.410TB
Tier0 Free Capacity : --
Tier0 Hot Spare Capacity : 155.366GB
Tier0 Used Hot Spare Capacity : 0.000B
Tier0 Hot Spare Strategy : Low
Tier1 Disk Number : 8
Tier1 Total Capacity : 3.420TB
Tier1 Free Capacity : --
Tier1 Hot Spare Capacity : 344.321GB
Tier1 Used Hot Spare Capacity : 0.000B
Tier1 Hot Spare Strategy : Low
Tier2 Disk Number : --
Tier2 Total Capacity : --
Tier2 Free Capacity : --
Tier2 Hot Spare Capacity : --
Tier2 Used Hot Spare Capacity : --
Tier2 Hot Spare Strategy : --
Thin Reconstruction : --
Disk Encryption Switch: Off
Controller enclosure : CTE0
Controller      : 0A,0B
Redundancy Strategy : Disk
Redundancy Ability : Disk
```

Query basic information about all disk domains.

```text
admin:/>show disk_domain general
ID Name Health Status Running Status Total Capacity Free Capacity Hot Spare Capacity Used Hot Spare Capacity
-- ---- ------------- -------------- -------------- ------------- ------------------ -----------------------
0  d0   Normal        Online         4.055TB        556.242GB     524.312GB          0.000B
```

##### System Response

The following table describes the parameter meanings.

| Parameter                     | Meaning                                                        |
|-------------------------------|----------------------------------------------------------------|
| ID                            | Disk domain ID.                                                |
| Name                          | Disk domain name.                                              |
| Health Status                 | Health status.                                                 |
| Running Status                | Running status.                                                |
| Total Capacity                | Total capacity of the disk domain.                             |
| Free Capacity                 | Total free capacity of the disk domain.                        |
| Hot Spare Capacity            | Total hot spare capacity of the disk domain.                   |
| Used Hot Spare Capacity       | Total used hot spare capacity of the disk domain.              |
| Hot Spare Strategy            | Hot spare strategy.                                            |
| Disk Number                   | Number of disks.                                               |
| Wear Leveling State           | Disk domain wear leveling state.                               |
| Anti Wear Leveling Disk ID    | ID of the disk for which anti-wear leveling is being executed. |
| Tier0 Disk Number             | Number of disks on tier 0.                                     |
| Tier0 Total Capacity          | Total capacity of tier 0.                                      |
| Tier0 Free Capacity           | Total free capacity of tier 0.                                 |
| Tier0 Hot Spare Capacity      | Hot spare capacity of tier 0.                                  |
| Tier0 Used Hot Spare Capacity | Used hot spare capacity of tier 0.                             |
| Tier0 Hot Spare Strategy      | Hot spare strategy of tier 0.                                  |
| Tier1 Disk Number             | Number of disks on tier 1.                                     |
| Tier1 Total Capacity          | Total capacity of tier 1.                                      |
| Tier1 Free Capacity           | Total free capacity of tier 1.                                 |
| Tier1 Hot Spare Capacity      | Hot spare capacity of tier 1.                                  |
| Tier1 Used Hot Spare Capacity | Used hot spare capacity of tier 1.                             |
| Tier1 Hot Spare Strategy      | Hot spare strategy of tier 1.                                  |
| Tier2 Disk Number             | Number of disks on tier 2.                                     |
| Tier2 Total Capacity          | Total capacity of tier 2.                                      |
| Tier2 Free Capacity           | Total free capacity of tier 2.                                 |
| Tier2 Hot Spare Capacity      | Hot spare capacity of tier 2.                                  |
| Tier2 Used Hot Spare Capacity | Used hot spare capacity of tier 2.                             |
| Tier2 Hot Spare Strategy      | Hot spare strategy of tier 2.                                  |
| Thin Reconstruction           | Whether thin reconstruction is enabled or disabled.            |
| Disk Encryption Switch        | Disk encryption switch.                                        |
| Controller enclosure          | ID list of controller enclosures.                              |
| Controller                    | Controller.                                                    |
| Redundancy Strategy           | Redundancy policy.                                             |
| Redundancy Ability            | Redundancy capability.                                         |
