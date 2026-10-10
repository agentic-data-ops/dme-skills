# create port_group


##### Function

The **create port_group** command is used to create a port group.

##### Format

**create port_group** name=? \[ port_group_id=? \] \[ port_type=? \] \[ port_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a port group that you want to create. | The value contains 1 to 255 digits, letters, underscores (_), hyphens (-), and periods (.). |
| port_group_id=? | ID of a port group that you want to create. | The value ranges from 0 to n minus one. n indicates the maximum number of port groups. If you do not specify this parameter, the system automatically allocates an ID for a new port group. |
| port_type=? | Type of a port that you want to add to a port group. If you specify this parameter, you must specify parameter port_id_list=?. | "FC": indicates Fibre Channel ports.<br>"ETH": indicates ETH ports.<br>"ROCE": indicates RoCE ports. |
| port_id_list=? | ID of a port that you want to add to a port group. This parameter is available only when you specify parameter port_type=?. | Run "show port general" to obtain the value.<br>When multiple ports need to be added, separate these port IDs with commas (,). |

##### Usage Guidelines

None.

##### Example

Create port group "test_portgroup".

```text
admin:/>create port_group name=test_portgroup
Create port group successfully.
```

##### System Response

None
