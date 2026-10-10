# change hyper_cdp_consistency_group cancel_restore


##### Function

**change hyper_cdp_consistency_group cancel_restore** command is used to cancel the restoration of a HyperCDP consistency group.

##### Format

**change hyper_cdp_consistency_group cancel_restore** cdp_consistency_group_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_consistency_group_id=? | ID of a HyperCDP consistency group. | The value is an integer ranging from 0 to 99999.<br>To obtain the value, run "show hyper_cdp_consistency_group universal". |

##### Usage Guidelines

None.

##### Example

Cancel the restoration of HyperCDP consistency group "1".

```text
admin:/>change hyper_cdp_consistency_group cancel_restore cdp_consistency_group_id=1
DANGER: You are about to stop restoring data of HyperCDP objects in a HyperCDP consistency group to LUNs in a protection group. This operation will cause data on LUNs in the protection group to be unavailable.
Suggestion: Before performing this operation, ensure that data on LUNs in the protection group is not required.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
