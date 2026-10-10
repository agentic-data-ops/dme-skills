# change fs_hyper_metro_domain split


##### Function

The **change fs_hyper_metro_domain split** command is used to split a file system-based HyperMetro domain.

##### Format

**change fs_hyper_metro_domain split** domain_id=? \[ stop_role=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id=? | File system HyperMetro domain ID. | You can run the "show fs_hyper_metro_domain general" command to obtain the value. |
| stop_role=? | Select the site to be stopped. | The value can be "Preferred" or "Non-preferred", where: <br>"Preferred": preferred site.<br>"Non-preferred": non-preferred site. |

##### Usage Guidelines

None

##### Example

Split the file system-based HyperMetro domain whose ID is "10100".

```text
admin:/>change fs_hyper_metro_domain split domain_id=10100
CAUTION: You are about to split the HyperMetro domain of the file system. This operation may cause service exceptions.
Suggestion: Before performing this operation, ensure that the operation and parameters are correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
