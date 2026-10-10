# change fs_snapshot general


##### Function

The **change fs_snapshot general** command is used to modify basic attributes of a file system snapshot, including the name and description.

##### Format

**change fs_snapshot general** snapshot_name=? { file_system_name=? \| file_system_id=? } { name=? \| description=? } \[ vstore_id=? \]

**change fs_snapshot general** snapshot_id=? { name=? \| description=? }

##### Parameters

| Parameter          | Description                                          | Value                                                                                                          |
|--------------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| snapshot_name=?    | Name of the file system snapshot you want to modify. | To obtain the value, run "show fs_snapshot general".                                                           |
| snapshot_id=?      | ID of the file system snapshot you want to modify.   | To obtain the value, run "show file_system general".                                                           |
| file_system_id=?   | ID of the file system.                               | To obtain the value, run "show file_system general".                                                           |
| file_system_name=? | Name of the file system.                             | To obtain the value, run "show file_system general".                                                           |
| description=?      | New description of the file system snapshot.         | The value contains 1 to 1023 characters.                                                                       |
| name=?             | New name of the file system snapshot.                | The value consists of 1 to 255 ASCII characters, including letters, digits, underscores (\_), and hyphens (-). |
| vstore_id=?        | vStore ID.                                           | vStore ID. The default value is "0".                                                                           |

##### Usage Guidelines

-   Before running this command, check whether the name or ID of the snapshot is correct.
-   Before running this command, check whether the ID of the file system to which the snapshot belongs is correct.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Change the name of the file system snapshot whose original name is "snap_1" and source file system ID is "1" to "snapshot_1".

```text
admin:/>change fs_snapshot general snapshot_name=snap_1 file_system_id=1 name=snapshot_1
Command executed successfully.
```

Change the description of the file system snapshot whose name is "snap_1" and source file system ID is "1" to "file_system_snap_1".

```text
admin:/>change fs_snapshot general snapshot_id=1@snap_1 description=file_system_snap_1
Command executed successfully.
```

Change the name and description of the snapshot whose original name is "snap_1" and source file system ID is "1" to "snapshot_1" and "file_system_snap_1", respectively.

```text
admin:/>change fs_snapshot general snapshot_name=snap_1 file_system_id=1 name=snapshot_1 description=file_system_snap_1
Command executed successfully.
```

##### System Response

None
