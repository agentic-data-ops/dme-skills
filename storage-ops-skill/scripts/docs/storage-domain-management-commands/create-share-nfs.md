# create share nfs


##### Function

The **create share nfs** command is used to create an NFS share.

##### Format

**create share nfs** local_path=? \[ file_system_id=? \| file_system_name=? \] \[ charset=? \] \[ lock_type=? \] \[ alias=? \] \[ audit_items=? \] \[ show_snapshot_enabled=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_system_id=? | File system ID. | The value ranges from 0 to 65535. |
| local_path=? | Absolute path of the NFS share. | The value consists of 1 to 1023 characters. |
| charset=? | NFS share encoding mode. | The value can be "UTF-8", "JIS", "S-JIS", "EUC-JP", "DE", "ZH", "GBK", "EUC-TW", "BIG5", "PT", "FR", "IT", "ES" or "KO", where: <br>"UTF-8": UTF-8 encoding.<br>"ZH": simplified Chinese.<br>"GBK": simplified Chinese.<br>"EUC-TW": traditional Chinese.<br>"BIG5": traditional Chinese.<br>"EUC-JP": EUC-JP encoding.<br>"JIS": JIS encoding.<br>"S-JIS": Shift-JIS encoding.<br>"DE": German.<br>"PT": Portuguese.<br>"ES": Spanish.<br>"FR": French.<br>"IT": Italian.<br>"KO": Korean.<br> The default value is "UTF-8". |
| lock_type=? | Lock policy type. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "Mandatory" or "Advisory", where: <br>"Mandatory": indicates a mandatory strategy.<br>"Advisory": indicates an advisory strategy.<br> The default value is "Mandatory". |
| alias=? | Alias of the NFS share. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must start with a slash (/). Except the first slash, the value contains 1 to 255 characters, only including letters, digits, spaces, and special characters (!\"#&%$'()*+-,.:;<=>?@[]^_`{|}~). On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. |
| audit_items=? | Audit log option. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The parameter value contains at least one of the following values: "none", "all", "open", "create", "read", "write", "close", "delete", "rename", "get_attr", "set_attr", "get_security", and "set_security", where: <br>"none": excludes all audit log options.<br>"all": includes all audit log options from "open" to "set_security".<br>"open": opens a file.<br>"create": creates a file.<br>"read": reads a file.<br>"write": writes a file.<br>"close": closes a file.<br>"delete": deletes a file.<br>"rename": renames a file.<br>"get_security": obtains security attributes of a file.<br>"set_security": sets security attributes of a file.<br>"get_attr": obtains file attributes.<br>"set_attr": sets file attributes.<br> If the parameter value is "all" or "none", no other values can be set. |
| show_snapshot_enabled=? | Whether the function of showing snapshots is enabled. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": the function of showing snapshots is enabled.<br>"no": the function of showing snapshots is disabled.<br> The default value is "yes". |
| file_system_name=? | File system name. | The value consists of 1 to 255 ASCII characters including numbers, letters, and underscores (_). |
| description=? | Description. | The value consists of 0 to 255 characters. |

##### Usage Guidelines

None

##### Example

Create an NFS share.

```text
admin:/>create share nfs local_path=/fs110 file_system_id=0 charset=UTF-8 lock_type=mandatory alias=/share_alias audit_items=read,write show_snapshot_enabled=yes
WARNING: You are about to create an NFS share. This operation may cause the following problems:
1. If you set the lock policy of the NFS share to "Advisory" in this operation, cross-protocol interworking scenarios may be affected, causing data inconsistency or service interruption.
2. If you enable the audit log function of the NFS share in this operation, NFS service performance may decrease.
Suggestion: Confirm that you want to perform this operation based on the service type.

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
admin:/>create share nfs local_path=/fs111 charset=UTF-8 lock_type=Advisory alias=/fs111 audit_items=rename show_snapshot_enabled=no
WARNING: You are about to create an NFS share. This operation may cause the following problems:
1. If you set the lock policy of the NFS share to "Advisory" in this operation, cross-protocol interworking scenarios may be affected, causing data inconsistency or service interruption.
2. If you enable the audit log function of the NFS share in this operation, NFS service performance may decrease.
Suggestion: Confirm that you want to perform this operation based on the service type.

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query information about an NFS share.

```text

admin:/>show share nfs

Share ID  File System ID  Description  Local Path  Alias     CharSet  Lock Type  Audit Items  show_snapshot_enabled
--------  --------------  -----------  ----------  --------  -------  ---------  -----------  ---------------------
1         1               1111         /fs0        /fs0      UTF-8    Mandatory  --           no
2         1                            /fs0/!\\    /fs0/!\\  UTF-8    Mandatory  --           no
4         3                            /fs110      /fs110    UTF-8    Mandatory  --           no
5         4                            /fs111      /fs111    UTF-8    Mandatory  --           no

```

Create an NFS share.

```text
admin:/>create share nfs local_path=/fs110 file_system_name=fs110 charset=UTF-8 lock_type=mandatory alias=/share_alias audit_items=read,write show_snapshot_enabled=yes
WARNING: You are about to create an NFS share. This operation may cause the following problems:
1. If you set the lock policy of the NFS share to "Advisory" in this operation, cross-protocol interworking scenarios may be affected, causing data inconsistency or service interruption.
2. If you enable the audit log function of the NFS share in this operation, NFS service performance may decrease.
Suggestion: Confirm that you want to perform this operation based on the service type.

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
admin:/>create share nfs local_path=/fs111 charset=UTF-8 lock_type=Advisory alias=/fs111 audit_items=rename show_snapshot_enabled=no
WARNING: You are about to create an NFS share. This operation may cause the following problems:
1. If you set the lock policy of the NFS share to "Advisory" in this operation, cross-protocol interworking scenarios may be affected, causing data inconsistency or service interruption.
2. If you enable the audit log function of the NFS share in this operation, NFS service performance may decrease.
Suggestion: Confirm that you want to perform this operation based on the service type.

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query information about an NFS share.

```text

admin:/>show share nfs

Share ID  File System ID  Description  Local Path  Alias     CharSet  Lock Type  Audit Items  show_snapshot_enabled
--------  --------------  -----------  ----------  --------  -------  ---------  -----------  ---------------------
1         1               1111         /fs0        /fs0      UTF-8    Mandatory  --           no
2         1                            /fs0/!\\    /fs0/!\\  UTF-8    Mandatory  --           no
4         3                            /fs110      /fs110    UTF-8    Mandatory  --           no
5         4                            /fs111      /fs111    UTF-8    Mandatory  --           no

```

##### System Response

None
