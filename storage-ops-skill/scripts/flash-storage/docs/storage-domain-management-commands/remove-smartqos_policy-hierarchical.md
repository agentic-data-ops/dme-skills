# remove smartqos_policy hierarchical


##### Function

The **remove smartqos_policy hierarchical** command is used to remove normal SmartQoS policies from a specified hierarchical SmartQoS policy.

##### Format

**remove smartqos_policy hierarchical** hierarchical_smartqos_policy_id=? normal_smartqos_policy_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hierarchical_smartqos_policy_id=? | ID of a hierarchical SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| normal_smartqos_policy_id_list=? | IDs of the normal SmartQoS policies that you want to remove. | To obtain the value, run "show smartqos_policy hierarchical". If you specify multiple normal SmartQoS policy IDs, use a comma (,) to separate non-consecutive IDs and use a hyphen (-) to connect consecutive IDs, for example, "0,5-8". A maximum of 64 SmartQoS policy IDs can be specified at a time. |

##### Usage Guidelines

After you remove normal SmartQoS policies from a hierarchical SmartQoS policy, the hierarchical SmartQoS policy is no longer effective for the removed SmartQoS policies and their objects.

##### Example

Remove SmartQoS policies "3", "4", and "5" from hierarchical SmartQoS policy "0".

```text
admin:/>remove smartqos_policy hierarchical hierarchical_smartqos_policy_id=0 normal_smartqos_policy_id_list=3,4,5
WARNING: You are about to remove the SmartQoS policy from the hierarchical SmartQoS policy. This operation may affect performance of objects in the SmartQoS policy.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the selected hierarchical SmartQoS policy and SmartQoS policy object are correct.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
