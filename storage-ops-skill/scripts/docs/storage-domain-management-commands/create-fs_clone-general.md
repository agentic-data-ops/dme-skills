# create fs_clone general


##### Function

The **create fs_clone general** command is used to create a clone file system.

##### Format

**create fs_clone general** name=? { parent_file_system_id=? \| parent_file_system_id_list=? } { parent_file_system_name=? \| parent_file_system_name_list=? \| parent_file_system_vstore_id=? \| parent_file_system_vstore_name=? } { parent_snapshot_id=? \| parent_snapshot_name=? } { vstore_id=? \| vstore_name=? } \[ file_system_id=? \] \[ number=? \] \[ alloc_type=? \] \[ description=? \] \[ hyper_cdp_schedule_name=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a clone file system. | The value contains 1 to 255 ASCII characters, including letters, digits, and underscores (_). For batch creation, the value contains a maximum of 251 characters. |
| parent_file_system_id=? | Parent file system ID. | To obtain the value, run "show file_system general". |
| parent_file_system_id_list=? | List of parent file system IDs. | To obtain the value, run "show file_system general". |
| parent_snapshot_id=? | Read-only snapshot ID. | The value is the ID of the snapshot. |
| file_system_id=? | ID of a clone file system. | The value is an integer from 1 to 65535. If the value is not specified, the system automatically allocates an ID of the newly created file system. |
| number=? | Number of file systems that are batch created. If this parameter is specified, the "file_system_id=?" parameter cannot be specified. | The value ranges from 2 to 100. The default value is 1. |
| alloc_type=? | Allocation type of the file system. | The value can be "thick" or "thin", where: <br>"thick": When thick file systems are created, fixed capacity is allocated to them.<br>"thin": Capacity of thin file systems will be automatically expanded when the capacity is about to be used up. The capacity cannot exceed the threshold (specified by the "capacity" parameter).<br> The default value is "thin". |
| parent_file_system_name=? | Parent file system name. | To obtain the value, run "show file_system general". |
| parent_file_system_name_list=? | List of parent file system names. | File system names may contain hyphens (-). Therefore, parent file system names can only be separated by commas (,). |
| parent_file_system_vstore_id=? | Parent file system vStore ID. | The value ranges from 0 to 1023. To obtain the value, run the "show vstore" command without parameters. |
| parent_file_system_vstore_name=? | Parent file system vStore name. | The value contains 1 to 256 characters, including letters, digits, underscores (_), periods (.), and hyphens (-). |
| parent_snapshot_name=? | Snapshot name of the parent file system. | The value is the name of the snapshot. |
| vstore_id=? | vStore ID. | The value ranges from 0 to 1023. To obtain the value, run the "show vstore" command without parameters. |
| vstore_name=? | vStore name. | The value contains 1 to 256 characters, including letters, digits, underscores (_), periods (.), and hyphens (-). |
| description=? | Description of the clone file system. | The value is a string of 1 to 255 characters. |
| hyper_cdp_schedule_name | Name of a schedule. | The value contains 1 to 255 ASCII characters, including digits, letters, periods (.), underscores (_), and hyphens (-). |

##### Usage Guidelines

-   Before the operation, check whether the parent file system ID is correct.
-   Before the operation, check whether the clone file system name is correct or exists.
-   Multiple clone file systems can be created for multiple file systems at the same time. Parent file system IDs are separated by commas (,).
-   Multiple clone file systems can be created for a file system.5:OceanStor 2200 V3 (8 GB memory) and 2600 V3 ( for video storage systems) do not support this command.

##### Example

Create a clone file system named "clone1" for the file system whose ID is "1".

```text
admin:/>create fs_clone general name=clone1 parent_file_system_id_list=1
Create clone of file system clone1 successfully.
```

##### System Response

None
