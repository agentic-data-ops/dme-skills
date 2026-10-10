# delete dr_star general


##### Function

The **delete dr_star general** command is used to delete DR Star.

##### Format

**delete dr_star general** dr_star_id=? \[ is_local_execute=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| dr_star_id | DR Star ID. | To obtain the value, run "show dr_star general". |
| is_local_execute | Whether local deletion is executed. | The value can be "no" or "yes", where: <br>"no": Local deletion is not executed.<br>"yes": Local deletion is executed.<br> The default value is "no". |

##### Usage Guidelines

-   This operation will remove the DR Star relationship among the three sites and clear the DR Star configuration information from arrays. As a result, the asynchronous DR relationship does not exist when a fault occurs.
-   Before performing an all-end deletion operation, ensure that the replication links between the primary site and the other two sites are normal and the running status of DR Star is "Disable".
-   Before performing a local deletion operation, ensure that the running status of DR Star is "Disable" or "Invalid".
-   If the running status of DR Star is "Invalid", only the local deletion command is available.

##### Example

Delete DR Star "1a212d4a5e6b0000".

```text
admin:/>delete dr_star general dr_star_id=1a212d4a5e6b0001
WARNING: You are about to delete DR Star.This operation will cancel the service relationship between the three members in the DR Star, and the operation cannot be rolled back.
Suggestion: Before performing this operation, ensure that you have selected the correct DR Star.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
