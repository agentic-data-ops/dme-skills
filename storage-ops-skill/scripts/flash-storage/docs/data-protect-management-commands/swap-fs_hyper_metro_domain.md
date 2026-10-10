# swap fs_hyper_metro_domain


##### Function

The **swap fs_hyper_metro_domain** command is used to perform a primary/secondary switchover for a HyperMetro domain cluster.

##### Format

**swap fs_hyper_metro_domain** domain_id=?

##### Parameters

| Parameter   | Description           | Value                                                                             |
|-------------|-----------------------|-----------------------------------------------------------------------------------|
| domain_id=? | HyperMetro domain ID. | You can run the "show fs_hyper_metro_domain general" command to obtain the value. |

##### Usage Guidelines

None

##### Example

Perform a primary/secondary switchover for the HyperMetro domain cluster. The domain ID is "48ad083e9b9f0100".

```text
admin:/>swap fs_hyper_metro_domain domain_id=48ad083e9b9f0100
WARNING: You are about to perform a primary/secondary switchover for the HyperMetro domain cluster. This operation will exchange the roles of the original primary and secondary file systems.
Suggestion: Before performing this operation, ensure that the correct HyperMetro domain cluster is selected.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
