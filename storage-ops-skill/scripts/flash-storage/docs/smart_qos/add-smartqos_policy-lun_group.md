# add smartqos_policy lun_group


##### Function

The **add smartqos_policy lun_group** command is used to add LUN groups to a SmartQoS policy.

##### Format

**add smartqos_policy lun_group** smartqos_policy_id=? lun_group_id_list=?

##### Parameters

| Parameter            | Description              | Value                                                                                          |
|----------------------|--------------------------|------------------------------------------------------------------------------------------------|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general".                                       |
| lun_group_id_list=?  | ID list of LUN groups.   | To obtain the value, run "show lun_group general". You can specify only one LUN group for now. |

##### Usage Guidelines

After LUN groups are added to a SmartQoS policy, the policy will be effective for the LUN groups.

##### Example

Add LUN group "1" to SmartQoS policy "0".

```text
admin:/>add smartqos_policy lun_group smartqos_policy_id=0 lun_group_id_list=1
CAUTION: You are about to add LUN groups to the SmartQoS policy. This operation may affect the performance of objects in the SmartQoS policy.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the selected SmartQoS policy and LUN group are correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
