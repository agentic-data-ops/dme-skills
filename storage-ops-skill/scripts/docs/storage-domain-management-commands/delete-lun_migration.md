# delete lun_migration


##### Function

The **delete lun_migration** command is used to delete LUN migration tasks.

##### Format

**delete lun_migration** source_lun_id=? \[ is_delete_target=? \]

##### Parameters

| Parameter          | Description                                                                                                                                                                                                | Value                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| source_lun_id=?    | ID of a source LUN.                                                                                                                                                                                        | Run the "show lun_migration general" command without parameters to obtain the value. |
| is_delete_target=? | Parameter used to decide whether to delete a target LUN. This parameter can only be used in developer mode. For details about how to log in to the developer mode, see the Advanced O&M Command Reference. | The value can be "yes" or "no", and the default value is "yes".                      |

##### Usage Guidelines

None

##### Example

Delete a LUN migration task.

```text
admin:/>delete lun_migration source_lun_id=5
WARNING: You are about to delete the LUN migration task, and the redundant LUN will be deleted in the meantime.
Suggestion: Before performing this operation, ensure that you have correctly selected the LUN migration task whose running status is Migrated. Otherwise, the migration task will be canceled.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete LUN migration successfully.
Delete LUN 7 successfully.
```

Delete a LUN migration task and the redundant LUNs.

```text
developer:/>delete lun_migration source_lun_id=8 is_delete_target=yes
WARNING: You are about to delete the LUN migration task, and the redundant LUN will be deleted in the meantime.
Suggestion: Before performing this operation, ensure that you have correctly selected the LUN migration task whose running status is Migrated. Otherwise, the migration task will be canceled.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete LUN migration successfully.
Delete LUN 18 successfully.
```

Delete a LUN migration task without deleting the redundant LUNs.

```text
developer:/>delete lun_migration source_lun_id=9 is_delete_target=no
WARNING: You are about to delete the LUN migration task.
Suggestion: Before performing this operation, ensure that you have correctly selected the LUN migration task whose running status is Migrated. Otherwise, the migration task will be canceled.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete LUN migration successfully.
```

##### System Response

None
