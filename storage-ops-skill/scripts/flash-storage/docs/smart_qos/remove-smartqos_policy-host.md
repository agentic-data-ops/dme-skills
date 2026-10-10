# remove smartqos_policy host


##### Function

The **remove smartqos_policy host** command is used to remove hosts from a specific SmartQoS policy.

##### Format

**remove smartqos_policy host** smartqos_policy_id=? host_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartqos_policy_id | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| host_id_list | IDs of the hosts that you want to remove. | To obtain the value, run "show smartqos_policy host". You can specify multiple host IDs separated by commas (,), or an ID range using hyphens (-), such as: "0,5-8". A maximum of 512 IDs are allowed. |

##### Usage Guidelines

After you remove hosts from a SmartQoS policy, the policy is no longer effective for the removed hosts.

##### Example

Remove hosts "4", "5", and "6" from SmartQoS policy "0".

```text
admin:/>remove smartqos_policy host smartqos_policy_id=0 host_id_list=4-6
WARNING: You are about to remove hosts from the SmartQoS policy. This operation may affect the performance of objects in the SmartQoS policy.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the selected SmartQoS policy and hosts are correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
