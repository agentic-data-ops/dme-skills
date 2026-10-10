# change remote_replication split


##### Function

The **change remote_replication split** command is used to split a remote replication task. During the split of a remote replication task, then data synchronization stops between both resources.

##### Format

**change remote_replication split** remote_replication_id=?

**change remote_replication split** remote_replication_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_replication_id=? | Remote replication pair ID. | To obtain the value, run "show remote_replication unified". |
| remote_replication_id_list=? | Remote replication pair ID list. | You can run the "show remote_replication unified" command to obtain the ID.<br>Use commas (,) to separate multiple pair IDs.<br>A maximum of 100 IDs can be entered. |

##### Usage Guidelines

-   Before running this command, ensure that the selected remote replication task is exactly the one you want to split.
-   You cannot split a remote replication task that has been added to a consistency group. In this condition, you must remove the remote replication task from the consistency group before you can split the task.
-   Exercise caution when you attempt to split an asynchronous remote replication task whose primary and secondary resources are in the initial synchronization state, because both attempts may cause data loss on employed secondary resources.
-   After you split the primary and secondary resources for a remote replication task, the data of the secondary resources will be consistent with that of the primary resource when it was split. A secondary resource is available to serve as a backup of the primary resource only when the status of the secondary resource is "Consistent" or "Synchronized".

##### Example

Split remote replication task "2100f102030405060000000200000000".

```text
admin:/>change remote_replication split remote_replication_id=2100f102030405060000000200000000
DANGER: You are about to split the primary resource from the secondary resource in remote replication. This operation causes the data on the secondary resource to become inconsistent with the data on the primary resource.
Suggestion: Before you perform this operation, determine whether the split is necessary.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Split multiple remote replication pairs whose IDs are 2100f10230405060000000200000000 and 2100f10230405060000000200000001.

```text
admin:/>change remote_replication split remote_replication_id_list=2100f102030405060000000200000000,2100f102030405060000000200000001
DANGER: You are about to split the primary resource from the secondary resource in remote replication. This operation causes the data on the secondary resource to become inconsistent with the data on the primary resource.
Suggestion: Before you perform this operation, determine whether the split is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change remote replication split 2100f102030405060000000200000000 successfully.
Change remote replication split 2100f102030405060000000200000001 successfully.
```

##### System Response

None
