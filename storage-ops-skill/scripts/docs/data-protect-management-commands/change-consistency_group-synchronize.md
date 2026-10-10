# change consistency_group synchronize


##### Function

The **change consistency_group synchronize** command is used to synchronize appointed consistency groups.

##### Format

**change consistency_group synchronize** consistency_group_id=?

##### Parameters

| Parameter              | Description                | Value                                                      |
|------------------------|----------------------------|------------------------------------------------------------|
| consistency_group_id=? | ID of a consistency group. | To obtain the value, run "show consistency_group general". |

##### Usage Guidelines

-   Running this command overwrites the data of a secondary LUN using that of the primary LUN.
-   Before running this command, ensure that the data of the selected secondary LUN is safe to be overwritten.
-   You cannot synchronize a consistency group if its replication mode is synchronous and its replication relationship is normal, synchronizing, or replication failed.
-   You cannot synchronize a consistency group if its replication mode is asynchronous and its replication relationship is synchronizing or replication failed.

##### Example

Synchronize consistency group "9747215445131264".

```text
admin:/>change consistency_group synchronize consistency_group_id=9747215445131264
DANGER: You are about to synchronize the data on the primary resources to the secondary resources in all remote replication tasks within consistency group. After this operation, the data on the secondary resource will be overwritten by the data on the primary resource, and the data on the secondary LUN is unrecoverable.
Suggestion: Before performing this operation, ensure that all data on the secondary resources can be overwritten.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
