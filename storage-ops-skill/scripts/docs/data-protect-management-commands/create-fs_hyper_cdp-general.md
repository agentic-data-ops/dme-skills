# create fs_hyper_cdp general


##### Function

The **create fs_hyper_cdp general** command is used to create a file system HyperCDP object.

##### Format

**create fs_hyper_cdp general** name=? \[ description=? \] { file_system_name_list=? \| file_system_id_list=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of the HyperCDP object you want to create. | The value contains 1 to 255 ASCII characters, including letters, digits, underscores (_), and hyphens (-). |
| description=? | Description of the HyperCDP object you want to create. | The value contains 1 to 1023 characters. |
| file_system_id_list=? | ID of the file system for which you want to create a HyperCDP object. | To obtain the value, run "show file_system general". You can specify multiple file system IDs separated by commas (,) or by hyphens (-) to represent an ID range, such as: "0,5-8". |
| file_system_name_list=? | Name of the file system for which you want to create a HyperCDP object. | To obtain the value, run "show file_system general". You can specify multiple file system names separated by commas (,). |

##### Usage Guidelines

-   Before running this command, check whether the ID of the file system for which you want to create a HyperCDP object is correct.
-   Before running this command, check whether the name of the HyperCDP object you want to create exists and is correct.
-   Multiple file systems can be created with multiple HyperCDP objects with the same name. Separate the IDs of the file systems with comma (,).

##### Example

Create a HyperCDP object named "snap1" for the file system whose ID is "1".

```text
admin:/>create fs_hyper_cdp general name=snap1 file_system_id_list=1
Create filesystem snapshot with filesystem 1 successfully.
```

##### System Response

None
