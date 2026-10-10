# change consistency_group split


##### Function

The **change consistency_group split** command is used to split consistency groups.

##### Format

**change consistency_group split** consistency_group_id=?

##### Parameters

| Parameter              | Description                | Value                                                      |
|------------------------|----------------------------|------------------------------------------------------------|
| consistency_group_id=? | ID of a consistency group. | To obtain the value, run "show consistency_group general". |

##### Usage Guidelines

-   Running this command destroys the data consistency between the primary logical unit number (LUN) and a secondary LUN.
-   Before running this command, ensure that the selected consistency group is exactly the one you want to split.
-   You cannot split a consistency group if its replication relationship is replication failed.

##### Example

Split consistency group "21008038bc1e70e90000000300000000".

```text
admin:/>change consistency_group split consistency_group_id=21008038bc1e70e90000000300000000
WARNING: You are about to split the primary and secondary resources in all remote replication tasks within consistency group.After this operation,the data on the primary and secondary resources is not synchronized any longer.
Suggestion: Before performing this operation, ensure that the selected consistency group is correct.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
