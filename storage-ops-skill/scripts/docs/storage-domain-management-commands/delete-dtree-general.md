# delete dtree general


##### Function

The **delete dtree general** command is used to delete a dtree.

##### Format

**delete dtree general** { dtree_id_list=? \| dtree_name_list=? \[ file_system_id=? \| file_system_name=? \] } \[ vstore_id=? \]

##### Parameters

| Parameter          | Description          | Value                                                |
|--------------------|----------------------|------------------------------------------------------|
| dtree_id_list=?    | List of dtree IDs.   | The value is a list of dtree IDs.                    |
| dtree_name_list=?  | List of dtree names. | The value is a list of dtree names.                  |
| file_system_id=?   | File system ID.      | The value is a file system ID.                       |
| file_system_name=? | File system name.    | To obtain the value, run "show file_system general". |
| vstore_id=?        | vStore ID.           | vStore ID. The default value is "0".                 |

##### Usage Guidelines

None

##### Example

Delete a dtree.

```text
admin:/>delete dtree general dtree_name_list=dtname0 file_system_id=1
WARNING: You are about to delete a dtree in the file system.
This operation will delete all files in the dtree.
Suggestion: Before performing this operation, ensure that the files have been backed up or are no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Delete dtree by batch dtname0 successfully.
```

##### System Response

None
