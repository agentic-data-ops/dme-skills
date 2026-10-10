# delete consistency_group


##### Function

The **delete consistency_group** command is used to delete consistency groups.

##### Format

**delete consistency_group** consistency_group_id=? \[ is_local_delete=? \] \[ is_force_delete=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| consistency_group_id=? | ID of a consistency group. | To obtain the value, run "show consistency_group general". |
| is_local_delete=? | Whether to delete the local consistency group. | The value can be: <br>yes: The local consistency group will be deleted.<br>no: The local consistency group will not be deleted. |

##### Usage Guidelines

-   Running this command deletes the selected consistency group.
-   If the consistency group contains remote replication pairs, remove the pairs by running the "remove consistency_group remote_replication" command.
-   Before running this command, ensure that the selected consistency group is exactly the one you want to delete.
-   If the consistency group contains members, it can be deleted only when it is in the "Split" state or when its "Health Status" is "Fault". If the consistency group contains no members, it can be deleted when it is in the "Normal" state.

##### Example

Delete consistency group "21008038bc1e70e90000000300000000".

```text
admin:/>delete consistency_group consistency_group_id=21008038bc1e70e90000000300000000
DANGER: You are about to delete consistency group. This operation will delete information about the consistency group from the system.
Suggestion: Before performing this operation, ensure that the selected consistency group is correct.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
