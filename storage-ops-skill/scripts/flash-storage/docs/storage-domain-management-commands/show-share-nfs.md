# show share nfs


##### Function

The **show share nfs** command is used to query information about NFS shares.

##### Format

**show share nfs** \[ share_id=? \| file_system_id=? \| share_name=? \| file_system_name=? \| share_id_list=? \| share_name_list=? \]

##### Parameters

| Parameter          | Description              | Value                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| share_id=?         | NFS share ID.            | The value ranges from 1 to 18446744073709551615.                                                                                                                                                                                                                                                                                                                                                       |
| file_system_id=?   | File system ID.          | The value ranges from 0 to 65535.                                                                                                                                                                                                                                                                                                                                                                      |
| share_name=?       | NFS share name.          | The value must start with a slash (/). Except the first slash, the value contains 1 to 255 characters, only including letters, digits, spaces, and special characters (/!\\"#&%$'()\*+-,.:;\<=\>?@\[\]^\_\`{\|}\~). On the CLI, the following characters need to be represented with escape sequences: "\\\|" indicates "\|", "\\\\" indicates "\\", "\\q" indicates "?", and "\\s" indicates a space. |
| file_system_name=? | File system name.        | The value consists of 1 to 255 ASCII characters including numbers, letters, and underscores (\_).                                                                                                                                                                                                                                                                                                      |
| share_id_list=?    | NFS share ID list.       | NFS share IDs are separated by commas (,) or an ID range is represented by a hyphen (-).                                                                                                                                                                                                                                                                                                               |
| share_name_list=?  | List of NFS share names. | NFS share names are separated by commas (,) or an name range is represented by a hyphen (-). For a name range, the names before and after the hyphen (-) must be of the same format and length. NFS share names cannot contain hyphens (-).                                                                                                                                                            |

##### Usage Guidelines

None

##### Example

Query information about an NFS share.

```text
admin:/>show share nfs share_id=4

Share ID              : 4
File System ID        : 4
Description           :
Local Path            : /ctt3
Alias                 : /ctt3
CharSet               : UTF-8
Lock Type             : Mandatory
Audit Items           : --
show_snapshot_enabled : Disable
File System Name      : ctt3
```

Query information about an NFS share.

```text
admin:/>show share nfs share_name=/ctt1
Share ID              : 2
File System ID        : 2
Description           :
Local Path            : /ctt1
Alias                 : /ctt1
CharSet               : UTF-8
Lock Type             : Mandatory
Audit Items           : --
show_snapshot_enabled : Disable
File System Name      : ctt1
```

Query the NFS share that is associated with a specified file system ID.

```text

admin:/>show share nfs file_system_id=3

Share ID  File System ID  Description  Local Path  Alias  CharSet  Lock Type  Audit Items  show_snapshot_enabled  File System Name
--------  --------------  -----------  ----------  -----  -------  ---------  -----------  ---------------------  ----------------
3         3                            /ctt2       /ctt2  UTF-8    Mandatory  --           Disable                ctt2

```

Query the NFS share that is associated with a specified file system name.

```text
admin:/>show share nfs file_system_name=ctt1
Share ID  File System ID  Description  Local Path  Alias  CharSet  Lock Type  Audit Items  show_snapshot_enabled  File System Name
--------  --------------  -----------  ----------  -----  -------  ---------  -----------  ---------------------  ----------------
2         2                            /ctt1       /ctt1  UTF-8    Mandatory  --           Disable                ctt1
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Share ID | NFS share ID. |
| File System ID | File system ID. |
| Description | NFS share description. |
| Local Path | Absolute path of the NFS share. |
| Alias | NFS share alias. NOTE: This field is not supported by the current version. The returned value is invalid. |
| CharSet | NFS share encoding. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Lock Type | Lock strategy type. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Audit Items | Audit log option. NOTE: This field is not supported by the current version. The returned value is invalid. |
| show_snapshot_enabled | Whether the function of showing snapshots is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| File System Name | File system name. |
