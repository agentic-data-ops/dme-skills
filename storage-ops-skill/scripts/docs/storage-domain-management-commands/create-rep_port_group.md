# create rep_port_group


##### Function

The **create rep_port_group** command is used to create a replication port group.

##### Format

**create rep_port_group** name=? \[ id=? \] \[ fc_port_list=? \] \[ eth_logical_port_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a replication port group that you want to create. | The value contains 1 to 31 digits, letters, underscores (_), hyphens (-), and periods (.). |
| id=? | ID of a replication port group that you want to create. | The value ranges from 0 to n minus one. n indicates the maximum number of replication port groups. If you do not specify this parameter, the system automatically allocates an ID for a new replication port group. |
| fc_port_list=? | ID of the FC port that you want to add to a replication port group. | Run "show port general physical_type=FC" to obtain the value.<br>When multiple ports need to be added, separate these port IDs with commas (,). |
| eth_logical_port_list=? | Name of the logical port that you want to add to a replication port group. | Run "show logical_port general" to obtain the value.<br>When multiple ports need to be added, separate these port IDs with commas (,). |

##### Usage Guidelines

None

##### Example

Create a replication port group.

```text
admin:/>create rep_port_group name=fcgroup fc_port_list=CTE0.A2.P0,CTE0.A2.P1
Command executed successfully.
```

##### System Response

None
