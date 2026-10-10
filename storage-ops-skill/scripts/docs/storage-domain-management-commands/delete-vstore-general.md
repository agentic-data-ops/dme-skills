# delete vstore general


##### Function

The **delete vstore general** command is used to delete a vStore.

##### Format

**delete vstore general** { id=? \| name=? }

##### Parameters

| Parameter | Description                                 | Value                                                                                                          |
|-----------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| id=?      | ID of the vStore that you want to delete.   | The value ranges from 1 to 1023. To obtain the value, run the "show vstore" command without parameters.        |
| name=?    | Name of the vStore that you want to delete. | The value contains 1 to 256 characters. To obtain the value, run the "show vstore" command without parameters. |

##### Usage Guidelines

-   Before performing this operation, ensure that the correct vStore is selected.
-   If the vStore contains vStore resources, it cannot be deleted. Before deleting a vStore, you need to delete the vStore resources.
-   This operation will delete vStore information from the storage system.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Delete the vStore whose ID is "11".

```text
admin:/>delete vstore general id=11
WARNING: You are about to delete vStore.
This operation will delete the vStore from the system.
Suggestion: Before performing this operation, ensure that you choose the correct vStore, and the vStore is no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
admin:/>
```

Delete the vStore whose name is "test".

```text
admin:/>delete vstore general name=test
WARNING: You are about to delete vstore.
This operation will delete the vStore from the system.
Suggestion: Before performing this operation, ensure that you choose the correct vStore, and the vStore is no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
admin:/>
```

##### System Response

None
