# remove rep_port_group port


##### Function

The **remove rep_port_group port** command is used to remove ports from a replication port group.

##### Format

**remove rep_port_group port** \[ rep_port_group_name=? \| rep_port_group_id=? \] \[ fc_port_list=? \] \[ eth_logical_port_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rep_port_group_name=? | Name of a replication port group. | To obtain the value, run "show rep_port_group general". |
| rep_port_group_id=? | ID of a replication port group. | To obtain the value, run "show rep_port_group general". |
| fc_port_list=? | ID of the FC port that you want to remove. | Run "show port general physical_type=FC" to obtain the value.<br>When multiple ports need to be removed, separate these port IDs with commas (,). |
| eth_logical_port_list=? | Name of the logical port that you want to remove. | Run "show logical_port general" to obtain the value.<br>When multiple ports need to be removed, separate these port names with commas (,). |

##### Usage Guidelines

None

##### Example

Remove the FC port from the replication port group.

```text
admin:/>remove rep_port_group port rep_port_group_name=fcgroup fc_port_list=CTE0.B2.P0,CTE0.B2.P1
Command executed successfully.
```

##### System Response

None
