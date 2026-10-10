# change smartqos_policy enabled


##### Function

The **change smartqos_policy enabled** command is used to enable or disable a specified SmartQoS policy.

##### Format

**change smartqos_policy enabled** smartqos_policy_id=? enabled=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| enabled=? | Whether to enable or disable the SmartQoS policy. | The value can be "yes" or "no", where: <br>"yes": enables the SmartQoS policy.<br>"no": disables the SmartQoS policy. |

##### Usage Guidelines

After creating a SmartQoS policy, you must run this command to enable the policy so that the settings associated with the policy can take effect.

##### Example

Enable SmartQoS policy whose ID is "3".

```text
admin:/>change smartqos_policy enabled smartqos_policy_id=3 enabled=yes
CAUTION: You are about to activate the SmartQoS policy. This operation may affect the performance of storage objects.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the SmartQoS policy is correctly configured.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Disable SmartQoS policy whose ID is "0".

```text
admin:/>change smartqos_policy enabled smartqos_policy_id=0 enabled=no
CAUTION: You are about to deactivate the SmartQoS policy. This operation may affect the performance of storage objects.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the SmartQoS policy is correctly selected.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
