# show share cifs


##### Function

The **show share cifs** command is used to query a CIFS share.

##### Format

**show share cifs** \[ share_id=? \| file_system_id=? \| share_type=? \| share_name=? \| file_system_name=? \| share_id_list=? \| share_name_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_id=? | ID of the CIFS share. | The value is an integer ranging from 0 to 18446744073709551615. |
| file_system_id=? | ID of the file system. | The value is an integer ranging from 0 and 65535. |
| share_type=? | CIFS share type. | The value can be "normal", "homedir", or "all". The default value is "normal". <br>"normal": common share.<br>"homedir": homedir share.<br>"all": all. |
| share_name=? | Name of the CIFS share. | The value consists of 1 to 80 characters excluding \"/\\[]:|<>+;,?*=. |
| file_system_name=? | File system name. | The value contains 1 to 255 ASCII characters including numbers, letters, and underscores (_). |
| share_id_list=? | List of CIFS share IDs. | CIFS share IDs are separated by commas (,) or hyphens (-). |
| share_name_list=? | List of CIFS share names. | CIFS share names are separated by commas (,) or a name range is represented by a hyphen (-). For a name range, the names before and after the hyphen (-) must be of the same format and length. CIFS share names cannot contain hyphens (-). |

##### Usage Guidelines

None

##### Example

Query all normal CIFS shares.

```text
admin:/>show share cifs

Share ID  Name                    File System ID  Local Path  Share Type  File System Name  Dir Umask  File Umask
--------  ----------------------  --------------  ----------  ----------  ----------------  ---------  ----------
1         cct1                    1               /fs1/        Normal      fs1               000        000
2         cct2                    1               /fs1/        Normal      fs1               000        000
3         cct3                    1               /fs1/        Normal      fs1               000        000

```

Query all CIFS shares.

```text
admin:/>show share cifs share_type=all

Share ID  Name    File System ID  Local Path  Share Type  File System Name  Dir Umask  File Umask
--------  ------  --------------  ----------  ----------  ----------------  ---------  ----------
4         ctt1    --              /123123     Homedir     --                000        000
5         ctt2    1               /fs1        Normal      fs1               000        000
```

Query a CIFS share with a specified ID.

```text
admin:/>show share cifs share_id=21

Share ID                       : 21
Name                           : abc
File System ID                 : --
Description                    :
Local Path                     : /ctt1
Oplock Enabled                 : Disable
Notify Enabled                 : Disable
Continue Available Enabled     : Disable
Offline File Mode              : none
Smb2 CA Enabled                : Enable
IP Access Control              : Disable
ABE Enabled                    : Disable
Audit Items                    : [0]
File Extension Filter          : Disable
Apply Default ACL              : Disable
Share Type                     : Homedir
Show Previous Versions Enabled : Disable
Show Snapshot Enabled          : Disable
Browse Enabled                 : Enable
File System Name               : --
Leaselock Enabled              : Enable
Dir Umask                      : 000
File Umask                     : 000
```

Query the CIFS share that is associated with a specified file system.

```text
admin:/>show share cifs file_system_id=1

Share ID  Name    File System ID  Local Path  Oplock Enabled  Notify Enabled  Continue Available Enabled  Offline File Mode  Smb2 CA Enabled  IP Access Control  ABE Enabled  Audit Items  File Extension Filter  Apply Default ACL  Share Type  Show Previous Versions Enabled  Show Snapshot Enabled  Browse Enabled  File System Name  Leaselock Enabled  Dir Umask File Umask
--------  ------  --------------  ----------  --------------  --------------  --------------------------  -----------------  ---------------  -----------------  -----------  -----------  --------------------  -----------------  ----------  ------------------------------  ---------------------  --------------  ----------------  -----------------  --------- ----------
1         ctt     1               /ctt/       Disable         Disable         Disable                     none               Enable           Disable            Disable      [0]          Disable               Disable            Normal      Disable                         Disable                Enable          ctt               Enable             000       000
2         share1  1               /ctt/       Disable         Disable         Disable                     none               Enable           Disable            Disable      [0]          Disable               Disable            Normal      Disable                         Disable                Enable          ctt               Enable             000       000
```

Query a CIFS share with a specified name.

```text
admin:/>show share cifs share_name=ctt

Share ID                       : 1
Name                           : ctt
File System ID                 : 1
Description                    :
Local Path                     : /ctt/
Oplock Enabled                 : Disable
Notify Enabled                 : Disable
Continue Available Enabled     : Disable
Offline File Mode              : none
Smb2 CA Enabled                : Enable
IP Access Control              : Disable
ABE Enabled                    : Disable
Audit Items                    : [0]
File Extension Filter           : Disable
Apply Default ACL              : Disable
Share Type                     : Normal
Show Previous Versions Enabled : Disable
Show Snapshot Enabled          : Disable
Browse Enabled                 : Enable
File System Name               : ctt
Leaselock Enabled              : Enable
Dir Umask                      : 000
File Umask                     : 000
```

Query the CIFS share that is associated with a specified file system.

```text
admin:/>show share cifs file_system_name=fs1
Command executed successfully.
No matching records.
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Share ID | Share ID. |
| Name | Share name. |
| File System ID | File system associated with the CIFS share. |
| Local Path | Local path directory. |
| Description | Description. |
| Oplock Enabled | Whether the Oplock function is enabled or disabled. By using the Oplock function, a client can lock a file. A server can cancel the locking. |
| Notify Enabled | Switch of the Notify function. |
| Continue Available Enabled | Whether to enable the resumable download function. |
| ABE Enabled | Whether to enable the permission-based directory item enumeration (ABE) function. |
| IP Access Control | Switch of the IP address access control function. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Smb2 CA Enabled | Switch of the SMB2 failover function. |
| Offline File Mode | Offline cache mode. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Audit Items | Audit log option. NOTE: This field is not supported by the current version. The returned value is invalid. |
| File Extension Filter | Whether to enable file name extension filtering. NOTE: This field is not supported in this version, and the command output is invalid. |
| Apply Default ACL | Switch of applying the default ACL. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Share Type | Type of the CIFS share. |
| Show Previous Versions Enabled | Function of showing previous versions. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Show Snapshot Enabled | Function of showing snapshots. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Browse Enabled | Whether to enable the browse function. |
| File System Name | File system name. |
| Leaselock Enabled | Lease lock switch, which allows the client to lock a file with a lease key, and the server can revoke the lock. Lease locks are supported with the SMB 2.1 protocol and later. |
| Dir Umask | Default UNIX umask of a new directory created on the share. |
| File Umask | Default UNIX umask for new files created on the share. |
