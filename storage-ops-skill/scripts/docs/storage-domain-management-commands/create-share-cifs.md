# create share cifs


##### Function

The **create share cifs** command is used to create a CIFS share.

##### Format

**create share cifs** name=? local_path=? \[ continue_available_enabled=? \] \[ oplock_enabled=? \] \[ notify_enabled=? \] \[ file_system_id=? \| file_system_name=? \] \[ offline_file_mode=? \] \[ smb2_ca_enabled=? \] \[ ip_control_enabled=? \] \[ abe_enabled=? \] \[ audit_items=? \] \[ file_filter_enable=? \] \[ apply_default_acl=? \] \[ share_type=? \] \[ show_previous_versions_enabled=? \] \[ show_snapshot_enabled=? \] \[ browse_enable=? \] \[ readdir_timeout=? \] \[ lease_enable=? \] \[ dir_umask=? \] \[ file_umask=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | CIFS share name. | The value consists of 1 to 80 characters excluding \"/\\[]:|<>+;,?*=. |
| local_path=? | Local path directory. | The value consists of 1 to 1023 characters. |
| oplock_enabled=? | Oplock switch. By using the Oplock, a client can lock a file. A server can cancel the lock. | The value can be "yes" or "no", where: <br>"yes": enables the Oplock function.<br>"no": disables the Oplock function.<br> The default value is "yes". |
| notify_enabled=? | Switch of the Notify function. | The value can be "yes" or "no", where: <br>"yes": enables the Notify function.<br>"no": disables the Notify function.<br> The default value is "yes". |
| file_system_id=? | ID of the file system to which the CIFS share belongs. | The value is an integer between 0 and 65535. Run "show file_system general" to obtain the value. |
| continue_available_enabled=? | Switch of the continue available function. | The value can be "yes" or "no". By default, this function is enabled. <br>"yes": enables the continue available function.<br>"no": disables the continue available function. |
| smb2_ca_enabled=? | SMB2 failover switch of shares. | The value can be "yes" or "no", where: <br>"yes": enables the SMB2 failover function.<br>"no": disables the SMB2 failover function.<br> The default value is "yes". |
| offline_file_mode=? | Offline cache mode. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "none", "manual", "documents", or "programs", where: <br>"none": disables offline cache.<br>"manual": manual mode.<br>"documents": documents mode.<br>"programs": programs mode. |
| ip_control_enabled=? | IP address access control switch. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the IP address access control function.<br>"no": disables the IP address access control function.<br> The default value is "no". |
| audit_items=? | Audit log option. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The parameter value contains at least one of the following values: "all", "none", "open", "create", "read", "write", "close", "delete", "rename", "get_security", "set_security", "get_attr", "set_attr", "get_xattr", and "set_xattr", where: <br>"all": includes all audit log options from "open" to "set_xattr".<br>"none": excludes all audit log options.<br>"open": opens a file.<br>"create": creates a file.<br>"read": reads a file.<br>"write": writes a file.<br>"close": closes a file.<br>"delete": deletes a file.<br>"rename": renames a file.<br>"get_security": obtains security attributes of a file.<br>"set_security": sets security attributes of a file.<br>"get_attr": obtains file attributes.<br>"set_attr": sets file attributes.<br>"get_xattr": obtains extended attributes of a file.<br>"set_xattr": sets extended attributes of a file.<br> If the parameter value is "all" or "none", no other values can be set. |
| share_type | Share type. | The value can be "normal" or "homedir", where: <br>"normal": normal share.<br>"homedir": homedir share.<br> The default value is "normal". |
| file_filter_enable=? | Switch of the file name extension filtering function. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the file name extension filtering function.<br>"no": disables the file name extension filtering function.<br> The default value is "no". |
| abe_enabled=? | Whether to enable the permission-based directory item enumeration (ABE) function. | The value can be "yes" or "no", where: <br>"yes": enables the ABE function.<br>"no": disables the ABE function.<br> The default value is "no". |
| apply_default_acl=? | Switch of applying the default ACL. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": applies the default ACL.<br>"no": does not apply the default ACL.<br> The default value is "yes". |
| show_previous_versions_enabled=? | Switch of showing previous versions. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the function.<br>"no": disables the function.<br> The default value is "yes". |
| show_snapshot_enabled=? | Whether the function of showing snapshots is enabled. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": The function of showing snapshots is enabled.<br>"no": The function of showing snapshots is disabled.<br> The default value is "yes". |
| browse_enabled=? | Switch of allowing Windows clients to browse the share. | The value can be "yes" or "no", where: <br>"yes": enables the browse_enable function.<br>"no": disables the browse_enable function. |
| file_system_name=? | File system name. | The value consists of 1 to 255 ASCII characters including numbers, letters, and underscores (_). |
| lease_enabled | Lease lock switch, which allows the client to lock a file with a lease key, and the server can revoke the lock. Lease locks are supported with the SMB 2.1 protocol and later. | The value can be "yes" or "no", where: <br>"yes": enables the lease lock function.<br>"no": disables the lease lock function. |
| dir_umask=? | Default UNIX umask of a new directory created on the share. | The value ranges from 000 to 777. |
| file_umask=? | Default UNIX umask for new files created on the share. | The value ranges from 000 to 777. |

##### Usage Guidelines

None

##### Example

Create a CIFS share.

```text
admin:/>create share cifs name=cifs0 local_path=/fs001
Command executed successfully.
```

Query CIFS shares.

```text
admin:/>show share cifs
Share ID  Name   File System ID  Local Path
--------  -----  --------------  ----------
8         cifs0  0               /fs001/
```

Create a CIFS share.

```text
admin:/>create share cifs name=cifs0 local_path=/fs001 file_system_name=fs001
Command executed successfully.
```

Query CIFS shares.

```text
admin:/>show share cifs
Share ID  Name   File System ID  Local Path
--------  -----  --------------  ----------
8         cifs0  0               /fs001/
```

##### System Response

None
