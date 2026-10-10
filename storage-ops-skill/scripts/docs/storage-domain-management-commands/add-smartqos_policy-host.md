# add smartqos_policy host


##### Function

The **add smartqos_policy host** command is used to add hosts to a SmartQoS policy.

##### Format

**add smartqos_policy host** smartqos_policy_id=? host_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| host_id_list=? | IDs of the hosts that you want to add. | To obtain the value, run "show host general". You can specify multiple host IDs separated by commas (,), or an ID range using hyphens (-), such as: "0,5-8". A maximum of 512 IDs are allowed. |

##### Usage Guidelines

After you add hosts to a SmartQoS policy, the policy will be effective for the added hosts.

##### Example

Add hosts "4", "5", and "6" to SmartQoS policy "0".

```text
admin:/>add smartqos_policy host smartqos_policy_id=0 host_id_list=4-6
WARNING: You are about to add hosts to the SmartQoS policy. This operation may affect the performance of objects in the SmartQoS policy.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the selected SmartQoS policy and hosts are correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
