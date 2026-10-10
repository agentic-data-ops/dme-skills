# remove smartqos_policy lun_group


##### Function

The **remove smartqos_policy lun_group** command is used to remove LUN groups from a specific SmartQoS policy.

##### Format

**remove smartqos_policy lun_group** smartqos_policy_id=? lun_group_id_list=?

##### Parameters

| Parameter          | Description              | Value                                                                                                  |
|--------------------|--------------------------|--------------------------------------------------------------------------------------------------------|
| smartqos_policy_id | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general".                                               |
| lun_group_id_list  | ID list of LUN groups.   | To obtain the value, run "show smartqos_policy lun_group". You can specify only one LUN group for now. |

##### Usage Guidelines

After you remove LUN groups from a SmartQoS policy, the policy is no longer effective for the removed LUN groups.

##### Example

Remove LUN group "3" from SmartQoS policy "0".

```text
admin:/>remove smartqos_policy lun_group smartqos_policy_id=0 lun_group_id_list=3
WARNING: You are about to remove LUN groups from the SmartQoS policy. This operation may affect the performance of objects in the SmartQoS policy.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the selected SmartQoS policy and LUN group are correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
