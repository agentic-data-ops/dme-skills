# remove consistency_group remote_replication


##### Function

The **remove consistency_group remote_replication** command is used to delete remote replication pairs from a consistency group.

##### Format

**remove consistency_group remote_replication** consistency_group_id=? \[ remote_replication_id=? \] \[ remote_replication_id_list=? \]

##### Parameters

| Parameter                    | Description                                                | Value                                                                        |
|------------------------------|------------------------------------------------------------|------------------------------------------------------------------------------|
| consistency_group_id=?       | ID of a consistency group.                                 | To obtain the value, run "show consistency_group general".                   |
| remote_replication_id=?      | ID of the remote replication pair that you want to delete. | To obtain the value, run "show remote_replication general".                  |
| remote_replication_id_list=? | List of remote replication pair IDs to be deleted.         | You can run the show remote_replication general command to obtain the value. |

##### Usage Guidelines

-   Running this command destroys the status consistency between the selected remote replication pair and the consistency group.
-   Before running this command, ensure that the selected remote replication pair is exactly the one you want to delete.

##### Example

Delete remote replication pair whose ID is "21008038bc1e70e90000000200000000" from consistency group "21008038bc1e70e90000000300000000".

```text
admin:/>remove consistency_group remote_replication consistency_group_id=21008038bc1e70e90000000300000000 remote_replication_id=21008038bc1e70e90000000200000000
DANGER: You are about to remove remote replication task from consistency group. After this operation, the status of the remote replication task becomes inconsistent with that of the consistency group.
Suggestion: Before performing this operation, ensure that the selected remote replication task is correct.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete remote replications whose IDs are 21008038bc1e70e900000002000000000 and 21008038bc1e70e90000000200000001 from the consistency group whose ID is 21008038bc1e70e90000000300000000.

```text
admin:/>remove consistency_group remote_replication consistency_group_id=21008038bc1e70e90000000300000000 remote_replication_id_list=21008038bc1e70e90000000200000000,21008038bc1e70e90000000200000001
DANGER: You are about to remove remote replication task from consistency group. After this operation, the status of the remote replication task becomes inconsistent with that of the consistency group.
Suggestion: Before performing this operation, ensure that the selected remote replication task is correct.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove remote replication 21008038bc1e70e90000000200000000 from consistency group successfully.
Remove remote replication 21008038bc1e70e90000000200000001 from consistency group successfully.
```

##### System Response

None
