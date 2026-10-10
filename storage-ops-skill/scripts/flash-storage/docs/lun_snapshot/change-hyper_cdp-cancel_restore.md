# change hyper_cdp cancel_restore


##### Function

The **change hyper_cdp cancel_restore** command is used to cancel the rollback of a HyperCDP object.

##### Format

**change hyper_cdp cancel_restore** cdp_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_id=? | ID of a HyperCDP object. | The value is an integer ranging from 0 to 1999999.<br>To obtain the value, run "show hyper_cdp general". |

##### Usage Guidelines

None.

##### Example

Cancel the rollback of the HyperCDP object whose ID is "1".

```text
admin:/>change hyper_cdp cancel_restore cdp_id=1
DANGER: You are about to stop restoring data of HyperCDP to the source LUN. This operation will cause data on the source LUN to be unavailable.
Suggestion: Before performing this operation, ensure that the source LUN data is not required.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
