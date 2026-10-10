# change smartqos_policy min_goal_reserved


##### Function

The **change smartqos_policy min_goal_reserved** command is used to modify the minimum performance of LUNs that have not been added to a lower limit guarantee policy.

##### Format

**change smartqos_policy min_goal_reserved** iops=? bandwidth=?

##### Parameters

| Parameter | Description                                                                                                                                                                           | Value                                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| iops      | Reserved IOPS of the LUNs that have not been added to a lower limit guarantee policy, which cannot be lower than the default reserved IOPS of the system.                             | The value ranges from 100 to 999999999. |
| bandwidth | Reserved bandwidth of the LUNs that have not been added to a lower limit guarantee policy, which cannot be lower than the default reserved bandwidth of the system. The unit is MB/s. | Value range: 1 to 999999999.            |

##### Usage Guidelines

Run the "**change smartqos_policy min_goal_reserved**" command to modify the minimum IOPS and bandwidth of LUNs that have not been added to a lower limit guarantee policy.

##### Example

Modify the reserved IOPS to "200,000" and reserved bandwidth to "5000" (unit: MB/s) for LUNs that have not been added to a lower limit guarantee policy.

```text
admin:/>change smartqos_policy min_goal_reserved iops=200000 bandwidth=5000
DANGER: You are about to change the total reserved performance for LUNs that are not added to the lower limit guarantee policy. This operation may affect system performance.
Suggestion: Before running this command, confirm its impact on system performance.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Modify the reserved IOPS to "200" and reserved bandwidth to "50" (unit: MB/s) for LUNs that have not been added to a lower limit guarantee policy.

```text
admin:/>change smartqos_policy min_goal_reserved iops=200 bandwidth=50
DANGER: You are about to change the total reserved performance for LUNs that are not added to the lower limit guarantee policy. This operation may affect system performance.
Suggestion: Before running this command, confirm its impact on system performance.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Error: The total reserved IOPS and reserved bandwidth of LUNs configured with the lower limit guarantee policy must be larger than or equal to the default values 27000 and 350 MB/s, respectively.
Suggestion: Configure valid performance values based on the error message.
```

##### System Response

None
