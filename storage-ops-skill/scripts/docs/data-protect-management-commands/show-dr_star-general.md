# show dr_star general


##### Function

The **show dr_star general** command is used to query information about DR Star trios.

##### Format

**show dr_star general** \[ dr_star_id=? \]

##### Parameters

| Parameter  | Description      | Value                                                                                                                                                                     |
|------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dr_star_id | DR Star trio ID. | To obtain the value, run "**show dr_star general**". |

##### Usage Guidelines

-   Run the "**show dr_star general**" command to query information about all DR Star trios in the system.
-   Run the "**show dr_star general** dr_star_id=?" command to query details of the specified DR Star trio.

##### Example

Query information about all DR Star trios.

```text

admin:/>show dr_star general

ID                                Name               Health Status  Running Status  Member Type  Disaster Recovery Strategy  Standby Synchronization Mode
--------------------------------  -----------------  -------------  --------------  -----------  --------------------------  ----------------------------
21000422224278250000000500000000  dr1                Normal         Enable          Pair         Hyper Metro                 Incremental Synchronization
21000422224278250000000500000001  dr2                Normal         Enable          Pair         Hyper Metro                 Incremental Synchronization
21000422224278250000000500000002  dr3                Normal         Enable          Pair         Hyper Metro                 Incremental Synchronization

```

Query information about DR Star trio "21000422224278250000000500000000" created using consistency groups.

```text

admin:/>show dr_star general dr_star_id=21000422224278250000000500000000
ID: 21000422224278250000000500000000
Name: dr_cg
Health Status: Normal
Running Status: Enable
Member Type: Consistency Group
Disaster Recovery Strategy: Hyper Metro
Swap Strategy: Automatic
Swap Silent Time: 1 Minute(s)
Local Resource: --
Standby Synchronization Mode: Full Synchronization

```

Query information about DR Star trio "2100d302030405060000000500000001" created using pairs.

```text

admin:/>show dr_star general dr_star_id=2100d302030405060000000500000001
ID: 2100d302030405060000000500000001
Name: dr_pair
Health Status: Normal
Running Status: Enable
Member Type: Pair
Disaster Recovery Strategy: Hyper Metro
Swap Strategy: Automatic
Swap Silent Time: 0 Minute(s)
Local Resource: lzn_A_0000
Standby Synchronization Mode: Incremental Synchronization

```

##### System Response

The following table describes the parameter meanings.

| Parameter                    | Meaning                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                           | DR Star trio ID.                                                                                                                                                                                                                                                                                                                                                                                                    |
| Health Status                | Health status.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Running Status               | Running status.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Member Type                  | Member type.                                                                                                                                                                                                                                                                                                                                                                                                        |
| Disaster Recovery Strategy   | DR policy.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Swap Strategy                | Switchover policy.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Swap Silent Time             | Switchover silent time.                                                                                                                                                                                                                                                                                                                                                                                             |
| Local Resource               | Local resource name.                                                                                                                                                                                                                                                                                                                                                                                                |
| Standby Synchronization Mode | Whether remote replication is in incremental or full synchronization mode after DR Star trio switchover. After a DR Star trio is created, the initial synchronization mode of standby remote replication is full. The synchronization mode changes to incremental if asynchronous remote replication starts and completes synchronization when HyperMetro or synchronous remote replication is in the normal state. |
| Name                         | DR Star trio name.                                                                                                                                                                                                                                                                                                                                                                                                  |
