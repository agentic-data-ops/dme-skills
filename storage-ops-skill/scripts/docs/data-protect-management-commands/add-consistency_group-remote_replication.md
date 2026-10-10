# add consistency_group remote_replication


##### Function

The **add consistency_group remote_replication** command is used to add a remote replication pair to a consistency group.

##### Format

**add consistency_group remote_replication** consistency_group_id=? \[ remote_replication_id=? \] \[ remote_replication_id_list=? \]

##### Parameters

| Parameter                    | Description                                                                      | Value                                                                        |
|------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| consistency_group_id=?       | ID of a consistency group.                                                       | To obtain the value, run "show consistency_group general".                   |
| remote_replication_id=?      | ID of the remote replication pair that you want to add to the consistency group. | To obtain the value, run "show remote_replication general".                  |
| remote_replication_id_list=? | ID list of remote replication pairs to be added to the consistency group.        | You can run the show remote_replication general command to obtain the value. |

##### Usage Guidelines

-   Remote replication pairs can be added to a consistency group only when both the remote replication pairs and the consistency group are in the Split state.

 

If the consistency group has no member, the consistency group is in the Normal state. You can add remote replication pairs to the consistency group.

-   This command can be successfully executed only when the replication mode of the remote replication pairs to be added is the same as that of the remote replication consistency group to which the remote replication pairs are added.
-   Only synchronous remote replication pairs can be added to a synchronous consistency group. Asynchronous remote replication pairs cannot be added to a synchronous consistency group.
-   Only asynchronous remote replication pairs can be added to an asynchronous consistency group. Synchronous remote replication pairs cannot be added to an asynchronous consistency group.

##### Example

Add remote replication pair "21008038bc1e70e90000000200000000" to consistency group "21008038bc1e70e90000000300000000".

```text
admin:/>add consistency_group remote_replication consistency_group_id=21008038bc1e70e90000000300000000 remote_replication_id=21008038bc1e70e90000000200000000
Command executed successfully.
```

Add the remote replication pairs whose IDs are "21008038bc1e70e90000000200000000" and "21008038bc1e70e90000000200000001" to the consistency group whose ID is "21008038bc1e70e90000000300000000".

```text
admin:/>add consistency_group remote_replication consistency_group_id=21008038bc1e70e90000000100000000 pair_id_list=21008038bc1e70e90000000200000000,21008038bc1e70e90000000200000001
Add remote replication 21008038bc1e70e90000000200000000 to consistency group successfully.
Add remote replication 21008038bc1e70e90000000200000001 to consistency group successfully.
```

##### System Response

None
