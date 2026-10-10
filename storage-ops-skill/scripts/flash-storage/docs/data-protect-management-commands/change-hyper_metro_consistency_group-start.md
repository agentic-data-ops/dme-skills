# change hyper_metro_consistency_group start


##### Function

The **change hyper_metro_consistency_group start** command is used to forcibly start a HyperMetro consistency group.

##### Format

**change hyper_metro_consistency_group start** consistency_group_id=?

##### Parameters

| Parameter              | Description                  | Value                                                                                                |
|------------------------|------------------------------|------------------------------------------------------------------------------------------------------|
| consistency_group_id=? | ID of the consistency group. | Run the "show hyper_metro_consistency_group general" command without parameters to obtain the value. |

##### Usage Guidelines

None

##### Example

Forcibly start HyperMetro consistency group "21008038bc1e70e90000000100000000".

```text
admin:/>change hyper_metro_consistency_group start consistency_group_id=21008038bc1e70e90000000100000000
DANGER: You are about to forcibly enable host access permissions of member LUNs in the local HyperMetro consistency group.
Ensure that the remote site does not accept host access requests. Otherwise, data loss may occur.
Suggestion: Before performing this operation, disconnect the remote site from hosts.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
