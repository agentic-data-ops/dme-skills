# add rep_port_group port


##### Function

The **add rep_port_group port** command is used to add ports to a replication port group.

##### Format

**add rep_port_group port** \[ rep_port_group_name=? \| rep_port_group_id=? \] \[ fc_port_list=? \] \[ eth_logical_port_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rep_port_group_name=? | Name of a replication port group. | To obtain the value, run "show rep_port_group general". |
| rep_port_group_id=? | ID of a replication port group. | To obtain the value, run "show rep_port_group general". |
| fc_port_list=? | ID of the FC port that you want to add to a replication port group. | Run "show port general physical_type=FC" to obtain the value.<br>When multiple ports need to be added, separate these port IDs with commas (,). |
| eth_logical_port_list=? | ID of the logical port that you want to add to a replication port group. | Run "show logical_port general" to obtain the value.<br>When multiple ports need to be added, separate these port names with commas (,). |

##### Usage Guidelines

None

##### Example

Add the FC port to the replication port group.

```text
admin:/>add rep_port_group port rep_port_group_name=fcgroup fc_port_list=CTE0.B2.P0,CTE0.B2.P1
WARNING: You are about to add the ports to the replication port group.
Before performing this operation, check whether the selected ports are host service ports. If yes, the replication link may disconnect.
Suggestion: Before performing this operation, plan the network and ensure that the replication service and host service do not share ports.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
