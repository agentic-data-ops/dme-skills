# delete fs_hyper_cdp general


##### Function

The **delete fs_hyper_cdp general** command is used to delete a file system HyperCDP object.

##### Format

**delete fs_hyper_cdp general** cdp_name_list=? { file_system_name=? \| file_system_id=? } \[ vstore_id=? \]

**delete fs_hyper_cdp general** cdp_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_name_list=? | Name of the HyperCDP object you want to delete. | To obtain the value, run "show fs_hyper_cdp general". Multiple HyperCDP objects are separated by commas (,). |
| cdp_id_list=? | ID of the HyperCDP object you want to delete. | To obtain the value, run "show fs_hyper_cdp general". Multiple HyperCDP objects are separated by commas (,). |
| file_system_id=? | ID of the file system. | To obtain the value, run "show file_system general". |
| file_system_name=? | Name of the file system. | To obtain the value, run "show file_system general". |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

-   Before running this command, check whether the name or ID of the HyperCDP object is correct.
-   Before running this command, check whether the ID of the file system to which the HyperCDP object belongs is correct.

##### Example

Delete the HyperCDP object whose name is "fssnap" of the file system whose ID is "1".

```text
admin:/>delete fs_hyper_cdp general cdp_name_list=fssnap file_system_id=1
WARNING: You are about to delete the read-only snapshot of the file system.
This operation will delete the data protected by the snapshot.
Suggestion: Before performing this operation, ensure that the correct snapshot is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the HyperCDP object whose name is "fssnap" of the file system whose ID is "1".

```text
admin:/>delete fs_hyper_cdp general cdp_id_list=1@fssnap
WARNING: You are about to delete the read-only snapshot of the file system.
This operation will delete the data protected by the snapshot.
Suggestion: Before performing this operation, ensure that the correct snapshot is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
