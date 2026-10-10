# show dtree general


##### Function

The **show dtree general** command is used to query information about dtrees.

##### Format

**show dtree general** { dtree_id_list=? \| \[ dtree_name_list=? \[ file_system_id=? \| file_system_name=? \] \] } \[ vstore_id=? \]

**show dtree general** { file_system_id_list=? \| file_system_name_list=? } \[ name=? \] \[ quotaConfigured=? \] \[ shareType=? \] \[ limit=? \] \[ index=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| dtree_id_list=? | List of dtree IDs. | The value is a list of dtree IDs. |
| dtree_name_list=? | List of dtree names. | The value is a list of dtree names. |
| file_system_id_list=? | List of file system IDs. | The value is a list of file system IDs. |
| file_system_name_list=? | List of file system names. | The value is a list of file system names. |
| file_system_id=? | File system ID. | The value is a file system ID. |
| file_system_name=? | File system name. | To obtain the value, run "show file_system general". |
| name=? | Fuzzy query of names. | Substring of dtree names. |
| quotaConfigured=? | Whether to enable the function of determining whether to configure a quota in exact matching mode. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the function.<br>"no": disables the function. |
| shareType=? | Share type. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "NFS", "CIFS", or "null", where: <br>"NFS": NFS share.<br>"CIFS": CIFS share.<br>"null": no share is configured. |
| limit=? | Maximum number of dtrees to be queried. | The value is an integer from 0 to 100. |
| index=? | Query offset. | The value is an integer from 0 to 1023. |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

None

##### Example

Query basic information about dtrees.

```text
admin:/>show dtree general dtree_name_list=dtname0 file_system_id=1
Type : Dtree
Dtree ID : 4294971393
Dtree Name : dtname0
File System ID : 1
Path : /
Quota Configured : false
Security Style : Mixed
Share Type : NFS
Need Init : false
Used Capacity : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Type | Type. |
| Dtree ID | Dtree ID. |
| Dtree Name | Dtree name. |
| File System ID | File system ID. |
| Path | Full path of the parent directory. |
| Dtree Dir Name | Name of a dtree. |
| Quota Configured | Whether a quota is configured. |
| Security Style | Security mode supported by a dtree. |
| Share Type | Share type list. The value can be: <br>"NFS": NFS share.<br>"CIFS": CIFS share.<br>"null": no share is configured. |
| Need Init | Whether to initialize a dtree. |
| Used Capacity | Dtree used capacity. |
