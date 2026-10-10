# swap consistency_group


##### Function

The **swap consistency_group** command is used to implement primary/secondary switchover for existing remote replication tasks in a consistency group.

##### Format

**swap consistency_group** consistency_group_id=?

##### Parameters

| Parameter              | Description                                                                        | Value                                                      |
|------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------|
| consistency_group_id=? | ID of a consistency group on which primary/secondary switchover will be performed. | To obtain the value, run "show consistency_group general". |

##### Usage Guidelines

-   Running this command swaps the roles of the primary logical unit number (LUN) and the selected secondary LUN.
-   Before running this command, ensure that the selected consistency group is exactly the one you want to perform primary/secondary switchover for its remote replication tasks.
-   Primary/secondary switchover cannot be performed when the secondary LUN is in Consist state.
-   In a synchronous remote replication, primary/secondary switchover can be performed only in two situations: when it is in Normal state; when it is in Split state and the secondary LUN can be written.
-   In an asynchronous remote replication, primary/secondary switchover can be performed only when it is in Split state and the secondary LUN can be written.

##### Example

To perform primary/secondary switchover for existing remote replication tasks in consistency group "9747215445131234", run the following command.

```text
admin:/>swap consistency_group consistency_group_id=9747215445131234
DANGER: You are about to switch over the primary and secondary resources in all remote replication tasks within consistency group.This operation will switch over roles of primary and secondary resources.
Suggestion: Before performing this operation, ensure that the selected consistency group is correct.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
