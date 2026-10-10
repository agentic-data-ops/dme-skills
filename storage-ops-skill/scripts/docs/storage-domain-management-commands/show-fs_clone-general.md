# show fs_clone general


##### Function

The **show fs_clone general** command is used to query information about a file system's child clone file system, including its ID, name, status, and associated parent file system snapshot name.

##### Format

**show fs_clone general** { parent_file_system_id=? } { parent_file_system_name=? \| parent_file_system_vstore_id=? \| parent_file_system_vstore_name=? } { parent_snapshot_id=? \| parent_snapshot_name=? }

##### Parameters

| Parameter                        | Description                                 | Value                                                                                                              |
|----------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| parent_file_system_id=?          | ID of the parent file system to be queried. | To obtain the value, run "show file_system general".                                                               |
| parent_snapshot_id=?             | Snapshot ID.                                | The value is the ID of the snapshot.                                                                               |
| parent_file_system_name=?        | Parent file system name.                    | To obtain the value, run "show file_system general".                                                               |
| parent_file_system_vstore_name=? | Parent file system vStore name.             | The value contains 1 to 256 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |
| parent_file_system_vstore_id=?   | Parent file system vStore ID.               | The value ranges from 0 to 1023. To obtain the value, run the "show vstore" command without parameters.            |
| parent_snapshot_name=?           | Snapshot name of the parent file system.    | The value is the name of the snapshot.                                                                             |

##### Usage Guidelines

Before performing the operation, check whether the ID of the file system or snapshot ID to be queried is correct.

##### Example

Query information about a file system's child clone file system.

```text
admin:/>show fs_clone general parent_file_system_id=1
ID             Name       vStore Name     Health Status     Running Status    Parent Snapshot   Time Stamp
----------- ------------- -------------- ----------------  ----------------- ----------------- ------------------------------
2             clone1      System_vStore    Normal           Online            snap1             2021-01-06/11:56:42 UTC+08:00
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                                                              |
|-----------------|--------------------------------------------------------------------------------------|
| ID              | Child clone file system ID.                                                          |
| Name            | Child clone file system name.                                                        |
| Health Status   | Health status.                                                                       |
| Running Status  | Running status.                                                                      |
| Parent Snapshot | Name of the parent file system snapshot associated with the child clone file system. |
| vStore Name     | vStore name.                                                                         |
| Time Stamp      | Time when a clone file system is created.                                            |
