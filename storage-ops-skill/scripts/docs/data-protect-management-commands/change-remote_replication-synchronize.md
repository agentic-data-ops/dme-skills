# change remote_replication synchronize


##### Function

The **change remote_replication synchronize** command is used to synchronize a specific remote replication. Use this command when you need to synchronize the data at the primary resource to a secondary resource to ensure data consistency.

##### Format

**change remote_replication synchronize** remote_replication_id=?

**change remote_replication synchronize** remote_replication_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_replication_id=? | Remote replication pair ID. | To obtain the values, run "show remote_replication unified". |
| remote_replication_id_list=? | List of remote replication pair IDs. | You can run the show remote_replication Unified command to obtain the value.<br>Use commas (,) to separate multiple pair IDs.<br>A maximum of 100 IDs can be entered. |

##### Usage Guidelines

-   Running this command will cause data of the primary resource to overwrite data of a secondary resource.
-   Before running this command, ensure that the selected secondary resource is exactly the one you want to synchronize with the primary resource, and that the data of the secondary resource is safe to be overwritten.
-   You cannot synchronize the primary and secondary resources for a remote replication task that has been added to a consistency group.
-   When a remote replication task is in synchronizing state, you cannot synchronize between the local and remote resources.

##### Example

Synchronize the primary and secondary resources for remote replication task "2100ef02030405060000000200000000".

```text
admin:/>change remote_replication synchronize remote_replication_id=2100ef02030405060000000200000000
DANGER: You are about to synchronize the data on the primary resource to the secondary resource in remote replication. The secondary resource belongs to storage array. This operation overwrites the data on the secondary resource with the data on the primary resource.
Suggestion: Before you perform this operation, ensure that the correct secondary resource is selected and the data on the secondary resource can be overwritten.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Synchronize multiple remote replication pairs whose IDs are 2100ef020304050600000002000000000 and 2100ef0203040506000000020000000001.

```text
admin:/>change remote_replication synchronize remote_replication_id_list=2100ef02030405060000000200000000,2100ef02030405060000000200000001
DANGER: You are about to synchronize the data on the primary resource to the secondary resource in remote replication. The secondary resource belongs to storage array. This operation overwrites the data on the secondary resource with the data on the primary resource.
Suggestion: Before you perform this operation, ensure that the correct secondary resource is selected and the data on the secondary resource can be overwritten.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change remote replication synchronize 2100f102030405060000000200000000 successfully.
Change remote replication synchronize 2100f102030405060000000200000001 successfully.
```

##### System Response

None
