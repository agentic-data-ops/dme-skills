# delete file_system general


##### Function

The **delete file_system general** command is used to delete file systems.

##### Format

**delete file_system general** { file_system_id_list=? \| file_system_name_list=? } \[ delete_parent_snapshot=? \] \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_system_id_list=? | List of file system IDs. | IDs are separated by commas (,). Consecutive IDs can also be represented by a hyphen (-).<br>The ID is an integer ranging from 1 to 65535. |
| file_system_name_list=? | List of file system names. | Multiple names are separated by commas (,).<br>A single name consists of 1 to 255 ASCII characters, including digits, letters, and underscores (_).<br>The value can contain a maximum of 25600 characters. |
| vstore_id | vStore ID. The default value is 0. | - |
| delete_parent_snapshot=? | Whether to delete the snapshot of the parent file system. | The value can be "yes" or "no". The default value is "no". |

##### Usage Guidelines

-   This command will delete information about the file systems from the system, and data in the file systems will be lost.
-   Before running this command, ensure that you have selected correct file systems, and services of the file systems have been stopped.
-   If a file system has been shared, delete the share before running the command. Otherwise, the file system cannot be deleted.

##### Example

Delete a file system.

```text
admin:/>delete file_system general file_system_id_list=3
DANGER: You are going to delete filesystem.This operation deletes the data stored on the filesystem.
Suggestion: Before you perform this operation, ensure that the data on the filesystem has been backed up or is allowed to delete.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete file system 3 successfully.
```

Delete multiple file systems.

```text
admin:/>delete file_system general file_system_id_list=3,4
DANGER: You are going to delete filesystem.This operation deletes the data stored on the filesystem.
Suggestion: Before you perform this operation, ensure that the data on the filesystem has been backed up or is allowed to delete.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete file system 3 successfully.
Delete file system 4 successfully.
admin:/>
```

##### System Response

None
