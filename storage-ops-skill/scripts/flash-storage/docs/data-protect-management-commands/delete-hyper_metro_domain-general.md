# delete hyper_metro_domain general


##### Function

The **delete hyper_metro_domain general** command is used to delete a HyperMetro domain.

##### Format

**delete hyper_metro_domain general** domain_id=? \[ is_local_delete=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id=? | ID of the HyperMetro domain. | To obtain the value, run "show hyper_metro_domain general". |
| is_local_delete=? | Whether to delete the HyperMetro domain only from the local device. | The value can be "yes" or "no", where: <br>"yes": only deletes the HyperMetro domain from the local device.<br>"no": deletes the HyperMetro domain from both the local and remote devices.<br> The default value is "no". |

##### Usage Guidelines

None

##### Example

Delete HyperMetro domain whose ID is "1".

```text
admin:/>delete hyper_metro_domain general domain_id=1
WARNING: You are going to delete a HyperMetro domain.
This operation may result in abnormal status of HyperMetro pairs in the HyperMetro domain.
Suggestion: Before performing this operation, ensure that no service is using the HyperMetro domain to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
