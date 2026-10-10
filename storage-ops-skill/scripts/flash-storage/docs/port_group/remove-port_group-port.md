# remove port_group port


##### Function

The **remove port_group port** command is used to remove a specified port from a port group.

##### Format

**remove port_group port** { port_group_id=? \| port_group_name=? } port_type=? port_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| port_group_id=? | ID of a port group from which you want to remove a port. | To obtain the value, run "show port_group general". |
| port_group_name=? | Name of a port group from which you want to remove a port. | To obtain the value, run "show port_group general". |
| port_type=? | Type of a port that you want to remove. | "FC": indicates Fibre Channel ports.<br>"ETH": indicates ETH ports.<br>"ROCE": indicates RoCE ports. |
| port_id_list=? | ID of a port that you want to remove. | Run "show port general" to obtain the value.<br>When multiple ports need to be removed, separate these port IDs with commas (,). |

##### Usage Guidelines

After a port is removed from a port group, it is no longer in the port group and cannot be managed by the port group.

##### Example

Remove port "ENG0.A0.P0" whose type is "FC" from port group "0". The command output varies depending on a specific product.

```text
admin:/>remove port_group port port_group_id=0 port_type=FC port_id_list=ENG0.A0.P0
WARNING: You are about to remove the port from its owning port group. This operation will interrupt the services on the port.
Suggestion: Before performing this operation, ensure that the selected port and port group are correct, and stop services on the port.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove port ENG0.A0.P0 successfully
```

Remove port "ENG0.A1.P1" whose type is "ETH" from port group "portgroup1". The command output varies depending on a specific product.

```text
admin:/>remove port_group port port_group_name=portgroup1 port_type=ETH port_id_list=ENG0.A1.P1
WARNING: You are about to remove the port from its owning port group. This operation will interrupt the services on the port.
Suggestion: Before performing this operation, ensure that the selected port and port group are correct, and stop services on the port.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove port ENG0.A1.P1 successfully
```

Remove port "ENG0.A2.P2" whose type is "ROCE" from port group "2". The command output varies depending on a specific product.

```text
admin:/>remove port_group port port_group_id=2 port_type=ROCE port_id_list=ENG0.A2.P2
WARNING: You are about to remove the port from its owning port group. This operation will interrupt the services on the port.
Suggestion: Before performing this operation, ensure that the selected port and port group are correct, and stop services on the port.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Remove port ENG0.A2.P2 successfully
```

##### System Response

None
