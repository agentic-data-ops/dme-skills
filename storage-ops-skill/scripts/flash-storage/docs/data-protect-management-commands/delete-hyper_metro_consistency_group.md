# delete hyper_metro_consistency_group


##### Function

The **delete hyper_metro_consistency_group** command is used to delete a HyperMetro consistency group.

##### Format

**delete hyper_metro_consistency_group** consistency_group_id=? \[ is_local_delete=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| consistency_group_id=? | ID of the HyperMetro consistency group. | Run the "show hyper_metro_consistency_group general" command without parameters to obtain the value. |
| is_local_delete=? | Whether the consistency group will be deleted from local devices. | The value can be: <br>"yes": The consistency group will be deleted from local devices.<br>"no": The consistency group will not be deleted from local devices.<br> The default value is "no". |

##### Usage Guidelines

None

##### Example

Delete the HyperMetro consistency group whose ID is "21008038bc1e70e90000000100000000".

```text
admin:/>delete hyper_metro_consistency_group consistency_group_id=21008038bc1e70e90000000100000000
WARNING:You are about to delete the HyperMetro consistency group, which cannot be undone.
If you need the configuration later, you must create it again. If the consistency group is deleted locally, perform the operation on both storage arrays. Otherwise, residual configuration of the consistency group exists.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
