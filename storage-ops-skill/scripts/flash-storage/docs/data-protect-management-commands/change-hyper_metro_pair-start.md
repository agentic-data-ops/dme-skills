# change hyper_metro_pair start


##### Function

The **change hyper_metro_pair start** command is used to forcibly start a HyperMetro pair.

##### Format

**change hyper_metro_pair start** pair_id=?

##### Parameters

| Parameter | Description                | Value                                                                |
|-----------|----------------------------|----------------------------------------------------------------------|
| pair_id=? | ID of the HyperMetro pair. | Run the "show hyper_metro_pair general" command to obtain the value. |

##### Usage Guidelines

None

##### Example

Forcibly start HyperMetro pair "1".

```text
admin:/>change hyper_metro_pair start pair_id=1
DANGER: You are going to forcibly start host access of a member LUN in a HyperMetro pair on the local storage array.
Before performing this operation, ensure that host access at the remote site is stopped. Otherwise, data loss may occur.
Suggestion: Before performing this operation, disconnect the storage array at the remote site from hosts.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
