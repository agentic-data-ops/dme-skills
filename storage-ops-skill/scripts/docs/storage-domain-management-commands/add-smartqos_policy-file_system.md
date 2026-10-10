# add smartqos_policy file_system


##### Function

The **add smartqos_policy file_system** command is used to add file systems to a SmartQoS policy.

##### Format

**add smartqos_policy file_system** smartqos_policy_id=? file_system_id_list=?

##### Parameters

| Parameter             | Description              | Value                                                    |
|-----------------------|--------------------------|----------------------------------------------------------|
| smartqos_policy_id=?  | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |
| file_system_id_list=? | File system IDs.         | \-                                                       |

##### Usage Guidelines

None

##### Example

Add file systems whose IDs are "3", "4", and "5" to the SmartQoS policy whose ID is "0".

```text
admin:/>add smartqos_policy file_system smartqos_policy_id=0 file_system_id_list=3,4,5
CAUTION: You are about to add file system into traffic control policy.
This operation may affect file system performance.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the correct traffic control policy and file system are selected.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
