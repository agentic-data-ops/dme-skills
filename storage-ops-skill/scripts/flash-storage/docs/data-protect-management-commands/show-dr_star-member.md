# show dr_star member


##### Function

The **show dr_star member** command is used to query information about members of DR Star.

##### Format

**show dr_star member** dr_star_id=?

##### Parameters

| Parameter  | Description | Value                                            |
|------------|-------------|--------------------------------------------------|
| dr_star_id | DR Star ID. | To obtain the value, run "show dr_star general". |

##### Usage Guidelines

The "**show dr_star member** dr_star_id=?" command is used to query information about members of a specified DR Star.

##### Example

Query information about the members of DR Star "200bc79b99520000" of the consistency group type.

```text
admin:/>show dr_star member dr_star_id=200bc79b99520000
ID                Health Status  Running Status  Feature Type                     Local Resource Role  Consistency Group  Local Resource  Remote Resource
----------------  -------------  --------------  -------------------------------  -------------------  -----------------  --------------  ---------------
1a212d4a5e6b0000  Normal         Normal          Hyper Metro                      Preferred            hc_cg              --              --
1a212d4a5e6b0001  Normal         Standby         Asynchronous Remote Replication  Primary              acg1               --              --
212b4a4d4d5a0001  Normal         Normal          Asynchronous Remote Replication  --                   acg2               --              --
```

Query information about the members of DR Star "1a212d4a5e6b0000" of the pair type.

```text
admin:/>show dr_star member dr_star_id=1a212d4a5e6b0000
ID                Health Status  Running Status  Feature Type                     Local Resource Role  Consistency Group  Local Resource  Remote Resource
----------------  -------------  --------------  -------------------------------  -------------------  -----------------  --------------  ---------------
1a212d4a5e6b0000  Normal         Normal          Hyper Metro                      Preferred            --                 lzn_A_0000      lzn_B_0000
1a212d4a5e6b0001  Normal         Standby         Asynchronous Remote Replication  Primary              --                 lzn_A_0000      lzn_C_0000
212b4a4d4d5a0001  Normal         Normal          Asynchronous Remote Replication  --                   --                 --              --
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning                 |
|---------------------|-------------------------|
| ID                  | ID of a DR Star member. |
| Health Status       | Health status.          |
| Running Status      | Running status.         |
| Feature Type        | Feature type.           |
| Local Resource Role | Local role.             |
| Consistency Group   | Consistency group name. |
| Local Resource      | Local resource name.    |
| Remote Resource     | Remote resource name.   |
