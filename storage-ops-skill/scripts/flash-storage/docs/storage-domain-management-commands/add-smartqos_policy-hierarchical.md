# add smartqos_policy hierarchical


##### Function

The **add smartqos_policy hierarchical** command is used to add normal SmartQoS policies to a specified hierarchical SmartQoS policy.

##### Format

**add smartqos_policy hierarchical** hierarchical_smartqos_policy_id=? normal_smartqos_policy_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hierarchical_smartqos_policy_id=? | ID of a hierarchical SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| normal_smartqos_policy_id_list=? | IDs of the normal SmartQoS policies that you want to add. | To obtain the value, run "show smartqos_policy general".<br>If you specify multiple normal SmartQoS policy IDs, use a comma (,) to separate non-consecutive IDs and use a hyphen (-) to connect consecutive IDs, for example, "0,5-8".<br> A maximum of 64 SmartQoS policy IDs can be specified at a time. |

##### Usage Guidelines

After you add normal SmartQoS policies to a hierarchical SmartQoS policy, the hierarchical SmartQoS policy will be effective for the SmartQoS policies and their objects.

##### Example

Add SmartQoS policies "3", "4", and "5" to hierarchical SmartQoS policy "0".

```text
admin:/>add smartqos_policy hierarchical hierarchical_smartqos_policy_id=0 normal_smartqos_policy_id_list=3,4,5
CAUTION: You are about to add the SmartQoS policy into the hierarchical SmartQoS policy. This operation may affect performance of objects in the SmartQoS policy.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the selected hierarchical SmartQoS policy and SmartQoS policy object are correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
