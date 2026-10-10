# swap remote_replication


##### Function

The **swap remote_replication** command is used to implement primary/secondary resource switchover of a remote replication. Use this command when you need to copy the data at the secondary resource to the primary resource using remote replication.

##### Format

**swap remote_replication** remote_replication_id=?

##### Parameters

| Parameter               | Description                      | Value                                                       |
|-------------------------|----------------------------------|-------------------------------------------------------------|
| remote_replication_id=? | ID of a remote replication task. | To obtain the value, run "show remote_replication unified". |

##### Usage Guidelines

-   Running this command swaps the roles of the primary resource and the selected secondary resource.
-   Before performing this operation, ensure that the selected remote replication task is correct.
-   Primary/secondary switchover cannot be performed when the secondary resource is not in Consist state.
-   In a synchronous remote replication, primary/secondary switchover can be performed only in two situations: when it is in Normal state; when it is in Split state and the secondary resource can be written.
-   In an asynchronous remote replication, primary/secondary switchover can be performed only when it is in Split state and the secondary resource can be written.
-   You cannot perform primary/secondary switchover for a remote replication task if the task has been added to a consistency group.

##### Example

To swap the primary Resource and a secondary Resource for remote replication task "9747215445131264", run the following command.

```text
admin:/>swap remote_replication remote_replication_id=9747215445131264
DANGER: You are about to perform a primary-secondary switchover for remote replication. This operation will switch over the roles of the primary and secondary resources. If the primary resource capacity is not equal to the secondary resource capacity, possible risks are as follows:
1. If the primary resource capacity is greater than the secondary resource capacity, remote replication I/Os may become abnormal, remote replication pairs may be in the abnormal interruption state, or data of the primary and secondary resources may be inconsistent.
2. If the primary resource capacity is smaller than the secondary resource capacity, remaining capacity of the secondary resource is not fully used.
Suggestion:Before performing this operation, ensure that the selected primary and secondary resources are correct.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
