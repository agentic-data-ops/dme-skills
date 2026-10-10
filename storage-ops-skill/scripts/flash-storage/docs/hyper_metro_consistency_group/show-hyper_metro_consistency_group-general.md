# show hyper_metro_consistency_group general


##### Function

The **show hyper_metro_consistency_group general** command is used to query a HyperMetro consistency group.

##### Format

**show hyper_metro_consistency_group general** \[ consistency_group_id=? \]

##### Parameters

| Parameter              | Description                             | Value                                                                                                                                                                                                                                                                     |
|------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| consistency_group_id=? | ID of the HyperMetro consistency group. | Run the "**show hyper_metro_consistency_group general**" command without parameters to obtain the value. |

##### Usage Guidelines

None

##### Example

Query HyperMetro consistency group 2100ef02030405060000000100000000 .

```text

admin:/>show hyper_metro_consistency_group general consistency_group_id=2100ef02030405060000000100000000

ID                         : 2100ef02030405060000000100000000
Name                       : lx_test_cg
Health Status              : Normal
Running Status             : Paused
Sync Rate                  : Middle
Role                       : Preferred
Recovery Policy            : Automatic
Domain Id                  : ef02030405060100
Domain Name                : HyperMetroDomain_000
Description                :
Sync Direction             : Local to Remote
Isolation Switch           : Close
Isolation Threshold(ms)    : 200
Lock Mode                  : --
Write Secondary Timeout(s) : 30
Bandwidth(MB/s)            : --
Local Protection Group Id  : --
Remote Protection Group Id : --
DR Star ID                 : --

```

Query all HyperMetro consistency groups in the device.

```text
admin:/>show hyper_metro_consistency_group general
ID                                Name   Health Status  Running Status    Role       Sync Direction
--------------------------------  -----  -------------  --------------  ---------  ---------  ----------------
21008038bc1e70e90000000100000000  HCCG1  Normal         Paused          --         Preferred  Local to Remote
```

##### System Response

The following table describes the parameter meanings.

| Parameter                  | Meaning                                                                                          |
|----------------------------|--------------------------------------------------------------------------------------------------|
| ID                         | ID of the consistency group.                                                                     |
| Name                       | Name of the consistency group.                                                                   |
| Health Status              | Health status. The value can be "Normal" or "Fault".                                             |
| Running Status             | Running status of the consistency group.                                                         |
| Sync Rate                  | Synchronization rate. The value can be "High", "Middle", "Low", or "Highest".                    |
| Role                       | Whether it is the preferred end.                                                                 |
| Recovery Policy            | Recovery policy.                                                                                 |
| Domain Id                  | Domain ID.                                                                                       |
| Domain Name                | Domain name.                                                                                     |
| Description                | Description.                                                                                     |
| Sync Direction             | Synchronization direction. The value can be "Local to Remote" or "Remote to Local".              |
| Isolation Switch           | Isolation switch.                                                                                |
| Isolation Threshold(ms)    | Isolation threshold.                                                                             |
| Lock Mode                  | Lock mode used by the HyperMetro pair. The value can be "Optimistic Mode" or "Pessimistic Mode". |
| Write Secondary Timeout    | Timeout period of I/O writing the secondary end (unit: second).                                  |
| Bandwidth                  | Bandwidth.                                                                                       |
| Local Protection Group Id  | Local protection group ID.                                                                       |
| Remote Protection Group Id | Remote protection group ID.                                                                      |
| DR Star ID                 | DR Star trio ID.                                                                                 |
