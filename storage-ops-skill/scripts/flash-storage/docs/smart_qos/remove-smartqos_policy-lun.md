# remove smartqos_policy lun


##### Function

The **remove smartqos_policy lun** command is used to remove LUNs from a specific SmartQoS policy.

##### Format

**remove smartqos_policy lun** smartqos_policy_id=? lun_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| lun_id_list=? | IDs of the LUNs that you want to remove. | To obtain the value, run the "show smartqos_policy general" command. You can specify multiple LUN IDs separated by commas (,), or an ID range using hyphens (-), such as: "0,5-8". A maximum of 512 IDs are allowed. |

##### Usage Guidelines

After you remove LUNs from a SmartQoS policy, the policy is no longer effective for the removed LUNs.

##### Example

Remove LUNs "3", "4", and "5" from SmartQoS policy "0".

```text
admin:/>remove smartqos_policy lun smartqos_policy_id=0 lun_id_list=3,4,5
WARNING: You are about to remove LUN from SmartQoS policy.
This operation may affect LUN performance.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the correct SmartQoS policy and LUN are selected.
Have you read warning message carefully?(y/n)y
Are you sure really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
