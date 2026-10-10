# delete fs_snapshot general


##### Function

The **delete fs_snapshot general** command is used to delete a file system snapshot.

##### Format

**delete fs_snapshot general** snapshot_name=? { file_system_name=? \| file_system_id=? } \[ vstore_id=? \]

**delete fs_snapshot general** snapshot_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_name=? | Name of the snapshot you want to delete. | To obtain the value, run "show fs_snapshot general". |
| snapshot_id_list=? | ID of the snapshot you want to delete. | To obtain the value, run "show fs_snapshot general". Multiple snapshot IDs are separated by commas(,). |
| file_system_id=? | ID of the file system. | To obtain the value, run "show file_system general". |
| file_system_name=? | Name of the file system. | To obtain the value, run "show file_system general". |
| vstore_id=? | vStore ID. | vStore ID. The default value is 0. |

##### Usage Guidelines

-   Before performing this operation, check whether the snapshot name or ID is correct.
-   Before performing this operation, check whether the ID of the file system to which the snapshot belongs is correct.
-   To forcibly delete a private snapshot in the normal state in the developer view, use the private mode. The uncomplete mode is used when you need to clear the redo records and mutually exclusive bits of snapshots that fail to be created or deleted.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Delete the snapshot whose name is "fssnap" of the file system whose ID is "1".

```text
admin:/>delete fs_snapshot general snapshot_name=fssnap file_system_id=1
WARNING: You are about to delete the read-only snapshot of the file system.
This operation will delete the data protected by the snapshot.
Suggestion: Before performing this operation, ensure that the correct snapshot is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the snapshot whose name is "fssnap" of the file system whose ID is "1".

```text
admin:/>delete fs_snapshot general snapshot_id_list=1@fssnap
WARNING: You are about to delete the read-only snapshot of the file system.
This operation will delete the data protected by the snapshot.
Suggestion: Before performing this operation, ensure that the correct snapshot is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
