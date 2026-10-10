# create fs_snapshot general


##### Function

The **create fs_snapshot general** command is used to create a file system snapshot.

##### Format

**create fs_snapshot general** name=? \[ description=? \] { file_system_name=? \| file_system_id_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of the snapshot you want to create. | The value contains 1 to 255 ASCII characters, including letters, digits, underscores (_), and hyphens (-). |
| description=? | Description of the snapshot you want to create. | The value contains 1 to 1023 characters. |
| file_system_id_list=? | ID of the file system for which you want to create a snapshot. | To obtain the value, run "show file_system general". You can specify multiple file system IDs separated by commas (,) or by hyphens (-) to represent an ID range, such as: "0,5-8". |
| file_system_name=? | Name of the file system for which you want to create a snapshot. | To obtain the value, run "show file_system general". |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

-   Before running this command, check whether the ID of the file system for which you want to create a snapshot is correct.
-   Before running this command, check whether the name of the snapshot you want to create exists and is correct.
-   Multiple file systems can be created with multiple read-only snapshots with the same name. Separate the IDs of the file systems with comma (,).

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Create a snapshot named "snap1" for the file system whose ID is "1".

```text
admin:/>create fs_snapshot general name=snap1 file_system_id_list=1
Create filesystem snapshot with filesystem 1 successfully.
```

##### System Response

None
