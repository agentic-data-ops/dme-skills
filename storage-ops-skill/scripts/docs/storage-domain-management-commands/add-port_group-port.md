# add port_group port


##### Function

The **add port_group port** command is used to add ports to a port group. The ID varies depending on a specific product.

##### Format

**add port_group port** { port_group_id=? \| port_group_name=? } port_type=? port_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| port_group_id=? | ID of a port group to which you want to add ports. | To obtain the value, run "show port_group general". |
| port_group_name=? | Name of a port group to which you want to add ports. | To obtain the value, run "show port_group general". |
| port_type=? | Type of a port that you want to add. | "FC": indicates Fibre Channel ports.<br>"ETH": indicates ETH ports.<br>"ROCE": indicates RoCE ports. |
| port_id_list=? | ID of a port that you want to add. | Run "show port general" to obtain the value.<br>When multiple ports need to be added, separate these port IDs with commas (,). |

##### Usage Guidelines

None

##### Example

Add port "ENG0.A1.P1" whose type is "FC" to port group "0".

```text
admin1:/>add port_group port port_group_id=0 port_type=FC port_id_list=ENG0.A1.P1
Add port ENG0.A1.P1 successfully
```

Add port "ENG0.A2.P2" whose type is "ETH" to port group "portgroup1".

```text
admin:/>add port_group port port_group_name=portgroup1 port_type=ETH port_id_list=ENG0.A2.P2
Add port ENG0.A2.P2 successfully
```

Add port "ENG0.A3.P3" whose type is "ROCE" to port group "2".

```text
admin1:/>add port_group port port_group_id=2 port_type=ROCE port_id_list=ENG0.A3.P3
Add port ENG0.A3.P3 successfully
```

##### System Response

None
