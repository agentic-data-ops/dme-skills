# delete smartqos_policy


##### Function

The **delete smartqos_policy** command is used to delete one or more specified SmartQoS policies.

##### Format

**delete smartqos_policy** smartqos_policy_id_list=?

##### Parameters

| Parameter                 | Description              | Value                                                                                                                                                                                                                        |
|---------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| smartqos_policy_id_list=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". If you specify multiple SmartQoS policy IDs, use a comma (,) to separate non-consecutive IDs and use a hyphen (-) to connect consecutive IDs, for example, "0,5-8". |

##### Usage Guidelines

-   The SmartQoS policy to be deleted must be in the inactive state. Run the "change smartqos_policy enabled" command to deactivate a SmartQoS policy.
-   Running this command permanently deletes a SmartQoS policy.

##### Example

Delete SmartQoS policy whose ID is "1".

```text
admin:/>delete smartqos_policy smartqos_policy_id_list=1
WARNING: You are about to delete the SmartQoS policy.
Suggestion: Before performing this operation, ensure that the selected SmartQoS policy is correct.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Delete SmartQos policy 1 successfully.
```

##### System Response

None
