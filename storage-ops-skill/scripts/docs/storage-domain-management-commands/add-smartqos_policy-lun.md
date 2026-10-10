# add smartqos_policy lun


##### Function

The **add smartqos_policy lun** command is used to add logical unit numbers (LUNs) to a SmartQoS policy.

##### Format

**add smartqos_policy lun** smartqos_policy_id=? lun_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| lun_id_list=? | IDs of the LUNs that you want to add. | To obtain the value, run "show lun general". You can specify multiple LUN IDs separated by commas (,), or ID range separated by hyphens(-), such as: "0,5-8". A maximum of 512 LUNs can be added. |

##### Usage Guidelines

After LUNs are added to a SmartQoS policy, the policy will be effective for the added LUNs.

##### Example

Add LUNs "3", "4", and "5" to SmartQoS policy "0".

```text
admin:/>add smartqos_policy lun smartqos_policy_id=0 lun_id_list=3,4,5
CAUTION: You are about to add LUN into traffic control policy.
This operation may affect LUN performance.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the correct traffic control policy and LUN are selected.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
