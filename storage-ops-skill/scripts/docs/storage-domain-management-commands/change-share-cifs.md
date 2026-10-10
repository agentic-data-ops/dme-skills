# change share cifs


##### Function

The **change share cifs** command is used to modify CIFS share configurations.

##### Format

**change share cifs** { share_id=? \| share_name=? } { oplock_enabled=? \| continue_available_enabled=? \| notify_enabled=? \| offline_file_mode=? \| smb2_ca_enabled=? \| ip_control_enabled=? \| abe_enabled=? \| audit_items=? \| file_filter_enable=? \| apply_default_acl=? \| show_previous_versions_enabled=? \| show_snapshot_enabled=? \| browse_enabled=? \| readdir_timeout=? \| lease_enabled=? \| dir_umask=? \| file_umask=? \| description=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_id=? | Share ID. | The value is an integer ranging from 0 to 18446744073709551615. |
| oplock_enabled=? | Switch of the Oplock function. By using the function, a client can lock a file, and a server can cancel the locking. | The value can be "yes" or "no", where: <br>"yes": enables the Oplock function.<br>"no": disables the Oplock function. |
| notify_enabled=? | Switch of the Notify function. | The value can be "yes" or "no", where: <br>"yes": enables the Notify function.<br>"no": disables the Notify function. |
| continue_available_enabled=? | Switch of the resumable transmission function. | The value can be "yes" or "no", where: <br>"yes": enables the resumable transmission function.<br>"no": disables the resumable transmission function. |
| abe_enabled=? | Whether to enable the permission-based directory item enumeration (ABE) function. | The value can be "yes" or "no", where: <br>"yes": enables the ABE function.<br>"no": disables the ABE function. |
| smb2_ca_enabled=? | Switch of the SMB2 failover function. | The value can be "yes" or "no", where: <br>"yes": enables the SMB2 failover function.<br>"no": disables the SMB2 failover function. |
| ip_control_enabled=? | Switch of the IP address access control function. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the IP address access control function.<br>"no": disables the IP address access control function. |
| offline_file_mode=? | Offline cache mode. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "none", "manual", "documents", or "programs", where: <br>"none": disables offline cache.<br>"manual": manual mode.<br>"documents": documents mode.<br>"programs": programs mode. |
| audit_items=? | Audit log option. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The parameter value contains at least one of the following values: "all", "none", "open", "create", "read", "write", "close", "delete", "rename", "get_security", "set_security", "get_attr", "set_attr", "get_xattr", and "set_xattr", where: <br>"all": includes all audit log options from "open" to "set_xattr".<br>"none": excludes all audit log options.<br>"open": opens a file.<br>"create": creates a file.<br>"read": reads a file.<br>"write": writes a file.<br>"close": closes a file.<br>"delete": deletes a file.<br>"rename": renames a file.<br>"get_security": obtains security attributes of a file.<br>"set_security": sets security attributes of a file.<br>"get_attr": obtains file attributes.<br>"set_attr": sets file attributes.<br>"get_xattr": obtains extended attributes of a file.<br>"set_xattr": sets extended attributes of a file.<br> If the parameter value is "all" or "none", no other values can be set. |
| file_filter_enable=? | Switch of the file name extension filtering function. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the file name extension filtering function.<br>"no": disables the file name extension filtering function.<br> The default value is "no". |
| apply_default_acl=? | Switch of applying the default ACL. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": applies the default ACL.<br>"no": does not apply the default ACL.<br> The default value is "yes". |
| show_previous_versions_enabled=? | Switch of showing previous versions. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the function of showing previous versions.<br>"no": disables the function of showing previous versions.<br> The default value is "yes". |
| show_snapshot_enabled=? | Switch of showing snapshots. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the function of showing snapshots.<br>"no": disables function of showing snapshots.<br> The default value is "yes". |
| browse_enabled=? | Switch of allowing Windows clients to browse the share. | The value can be "yes" or "no", where: <br>"yes": enables the function.<br>"no": disables the function. |
| share_name=? | CIFS share name. | The value consists of 1 to 80 characters excluding \"/\\[]:|<>+;,?*=. |
| lease_enabled | Lease lock switch, which allows the client to lock a file with a lease key, and the server can revoke the lock. Lease locks are supported with the SMB 2.1 protocol and later. | The value can be "yes" or "no", where: <br>"yes": enables the function.<br>"no": disables the function. |
| dir_umask=? | Default UNIX umask of a new directory created on the share. | The value ranges from 000 to 777. |
| file_umask=? | Default UNIX umask for new files created on the share. | The value ranges from 000 to 777. |
| description=? | Description. | The value is a string of 0 to 255 characters. |

##### Usage Guidelines

None

##### Example

Enable the Oplock function.

```text
admin:/>change share cifs share_id=8 oplock_enabled=yes
Command executed successfully.
```

Enable the Notify function.

```text
admin:/>change share cifs share_id=8 notify_enabled=yes
Command executed successfully.
```

Enable the resumable transmission function.

```text
admin:/>change share cifs share_id=8 continue_available_enabled=yes
Command executed successfully.
```

Enable the permission-based directory enumeration (ABE) function.

```text
admin:/>change share cifs share_id=8 abe_enabled=yes
Command executed successfully.
```

Enable the IP address access control function.

```text
admin:/>change share cifs share_id=8 ip_control_enabled=yes
Command executed successfully.
```

Set the offline mode to manual.

```text
admin:/>change share cifs share_id=8 offline_file_mode=manual
Command executed successfully.
```

Enable the SMB2 failover function.

```text
admin:/>change share cifs share_id=8 smb2_ca_enabled=yes
Command executed successfully.
```

Modify the audit items of the share.

```text
admin:/>change share cifs share_id=8 audit_items=rename
Command executed successfully.
```

Apply the default ACL.

```text
admin:/>change share cifs share_id=8 apply_default_acl=yes
Command executed successfully.
```

Enable the function of showing previous versions.

```text
admin:/>change share cifs share_id=8 show_previous_versions_enabled=yes
Command executed successfully.
```

Enable the function of showing snapshots.

```text
admin:/>change share cifs share_id=8 show_snapshot_enabled=yes
Command executed successfully.
```

Enable Windows clients to browse the share.

```text
admin:/>change share cifs share_id=8 browse_enabled=yes
Command executed successfully.
```

View the modification results.

```text
admin:/>show share cifs share_id=8
Share ID                       : 8
Name                           : asmb
File System ID                 : 2
Description                    :
Local Path                     : /fs1/
Oplock Enabled                 : Disable
Notify Enabled                 : Disable
Continue Available Enabled     : Disable
Offline File Mode              : none
Smb2 CA Enabled                : Disable
IP Access Control              : Disable
ABE Enabled                    : Disable
Audit Items                    : [0]
File Extenson Filter           : Disable
Apply Default ACL              : Disable
Share Type                     : Normal
Show Previous Versions Enabled : Disable
Show Snapshot Enabled          : Disable
Browse Enabled                 : Enable
Leaselock Enabled              : Enable
Dir Umask                      : 000
File Umask                     : 000
```

Enable the Oplock function.

```text
admin:/>change share cifs share_name=cifs0 oplock_enabled=yes
Command executed successfully.
```

Query the modification results.

```text
admin:/>show share cifs share_id=8
Share ID                       : 8
Name                           : asmb
File System ID                 : 2
Description                    :
Local Path                     : /fs1/
Oplock Enabled                 : Disable
Notify Enabled                 : Disable
Continue Available Enabled     : Disable
Offline File Mode              : none
Smb2 CA Enabled                : Disable
IP Access Control              : Disable
ABE Enabled                    : Disable
Audit Items                    : [0]
File Extenson Filter           : Disable
Apply Default ACL              : Disable
Share Type                     : Normal
Show Previous Versions Enabled : Disable
Show Snapshot Enabled          : Disable
Browse Enabled                 : Enable
Leaselock Enabled              : Enable
Dir Umask                      : 000
File Umask                     : 000
```

Change the default UNIX umask of the directory.

```text

admin:/>change share cifs share_id=8 dir_umask=755
Command executed successfully
```

Modify the default UNIX umask of the file.

```text
admin:/>change share cifs share_id=8 file_umask=744
Command executed successfully.
```

Query the modification result.

```text
admin:/>show share cifs share_id=8
Share ID                       : 8
Name                           : asmb
File System ID                 : 2
Description                    :
Local Path                     : /fs1/
Oplock Enabled                 : Disable
Notify Enabled                 : Disable
Continue Available Enabled     : Disable
Offline File Mode              : none
Smb2 CA Enabled                : Disable
IP Access Control              : Disable
ABE Enabled                    : Disable
Audit Items                    : [0]
File Extenson Filter           : Disable
Apply Default ACL              : Disable
Share Type                     : Normal
Show Previous Versions Enabled : Disable
Show Snapshot Enabled          : Disable
Browse Enabled                 : Enable
Leaselock Enabled              : Enable
Dir Umask                      : 755
File Umask                     : 744
```

##### System Response

None
