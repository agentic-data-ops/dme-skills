# show smartqos_policy min_goal_reserved


##### Function

The **show smartqos_policy min_goal_reserved** command is used to query the minimum performance of LUNs that have not been added to a lower limit guarantee policy.

##### Format

**show smartqos_policy min_goal_reserved**

##### Parameters

None

##### Usage Guidelines

Run the "**show smartqos_policy min_goal_reserved**" command to query the minimum IOPS and bandwidth of LUNs that have not been added to a lower limit guarantee policy.

##### Example

Query the minimum performance of LUNs that have not been added to a lower limit guarantee policy.

```text
admin:/>show smartqos_policy min_goal_reserved
Normalized IOPS : 200000
Bandwidth(MBps) : 5000
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------|
| Normalized IOPS | Minimum normalized IOPS of the LUNs that have not been added to a lower limit guarantee policy. |
| Bandwidth(MBps) | Minimum bandwidth of the LUNs that have not been added to a lower limit guarantee policy.       |
