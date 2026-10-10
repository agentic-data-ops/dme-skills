# remove smartqos_policy file_system


##### Function

The **remove smartqos_policy file_system** command is used to remove file systems from a specific SmartQoS policy.

##### Format

**remove smartqos_policy file_system** smartqos_policy_id=? file_system_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| file_system_id_list=? | File system IDs. | To obtain the value, run "show smartqos_policy general".<br>Multiple file system IDs are separated by commas (,), or by hyphens (-) to represent an ID range, for example, "0,5-8".<br>A maximum of 512 IDs can be specified. |

##### Usage Guidelines

None

##### Example

Remove file systems whose IDs are "3", "4", and "5" from the SmartQoS policy whose ID is "0".

```text
admin:/>remove smartqos_policy file_system smartqos_policy_id=0 filesystem_id_list=3,4,5
WARNING: You are about to remove file system from traffic control policy.
This operation may affect file system performance.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the correct traffic control policy and file system are selected.
Have you read warning message carefully?(y/n)y
Are you sure really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
