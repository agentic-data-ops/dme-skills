# add consistency_group remote_replication_delay


##### Function

The **add consistency_group remote_replication_delay** command is used to add the remote replication into the consistency group after the initial synchronization of the remote replication is complete.

##### Format

**add consistency_group remote_replication_delay** consistency_group_id=? remote_replication_id=?

##### Parameters

| Parameter               | Description                                                                     | Value                                                       |
|-------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------|
| consistency_group_id=?  | ID of a consistency group.                                                      | To obtain the value, run "show consistency_group general".  |
| remote_replication_id=? | ID of the remote replication tasks that you want to add to a consistency group. | To obtain the value, run "show remote_replication general". |

##### Usage Guidelines

-   This command can be used when: the initial synchronization of an asynchronous consistency group is complete; the asynchronous consistency group is in the cycle mode; and you do not want to affect the RPO of the asynchronous consistency group after adding the remote replication that is in initial synchronization into the asynchronous consistency group.
-   This is an asynchronous command. After you execute this command, operations, such as splitting the remote replication, consistency group, adding the remote replication to the consistency group, and restarting the synchronization of the consistency group, are performed on the background.
-   This command can only be performed when the consistency group having at least one member is in the synchronization or normal state, and the remote replication is in the initial synchronization or spliting or Initialized synchronization.
-   Therefore, after you perform this operation, do not operate the remote replication and consistency group to prevent operation failures.

##### Example

Add remote replication task whose ID is respectively "2100f102030405060000000200000000" to consistency group "2100f102030405060000000300000000" in delayed mode.

```text
admin:/>add consistency_group remote_replication_delay consistency_group_id=2100f102030405060000000300000000 remote_replication_id=2100f102030405060000000200000000
CAUTION: You are about to add a remote replication to a consistency group in delayed mode. Before performing this operation, note that:
1. This operation is an asynchronous operation, and will be executed after the initial synchronization of the remote replication is complete.
2. Before adding a remote replication to a consistency group, do not operate the remote replication and consistency group. Otherwise, this operation may fail, and the remote replication and consistency group will be in split state.
Suggestion: Perform this operation based on customer requirements.
Do you wish to continue?(y/n)y
Asynchronously executing the command (--) in background.
Run the "show task general task_id=7" command to query the execution result.
```

##### System Response

None
