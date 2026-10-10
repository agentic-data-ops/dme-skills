# change share nfs


##### Function

The **change share nfs** command is used to modify the configurations of an NFS share.

##### Format

**change share nfs** { share_id=? \| share_name=? } { charset=? \| lock_type=? \| audit_items=? \| show_snapshot_enabled=? \| description=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_id=? | NFS share ID. | The value ranges from 1 to 18446744073709551615. |
| charset=? | NFS share encoding mode. | The value can be "UTF-8", "JIS", "S-JIS", "EUC-JP", "DE", "ZH", "GBK", "EUC-TW", "BIG5", "PT", "FR", "IT", "ES" or "KO", where: <br>"UTF-8": UTF-8 encoding.<br>"ZH": simplified Chinese.<br>"GBK": simplified Chinese.<br>"EUC-TW": traditional Chinese.<br>"BIG5": traditional Chinese.<br>"EUC-JP": EUC-JP encoding.<br>"JIS": JIS encoding.<br>"S-JIS": Shift-JIS encoding.<br>"DE": German.<br>"PT": Portuguese.<br>"ES": Spanish.<br>"FR": French.<br>"IT": Italian.<br>"KO": Korean.<br> The default value is "UTF-8". |
| lock_type=? | Lock policy type. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "Mandatory" or "Advisory", where: <br>"Mandatory": indicates a mandatory strategy.<br>"Advisory": indicates an advisory strategy.<br> The default value is "Mandatory". |
| audit_items=? | Audit log option. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The parameter value contains at least one of the following values: "none", "all", "open", "create", "read", "write", "close", "delete", "rename", "get_attr", "set_attr", "get_security", and "set_security", where: <br>"none": excludes all audit log options.<br>"all": includes all audit log options from "open" to "set_security".<br>"open": opens a file.<br>"create": creates a file.<br>"read": reads a file.<br>"write": writes a file.<br>"close": closes a file.<br>"delete": deletes a file.<br>"rename": renames a file.<br>"get_security": obtains security attributes of a file.<br>"set_security": sets security attributes of a file.<br>"get_attr": obtains file attributes.<br>"set_attr": sets file attributes.<br> If the parameter value is "all" or "none", no other values can be set. |
| show_snapshot_enabled=? | Whether the function of showing snapshots is enabled. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": the function of showing snapshots is enabled.<br>"no": the function of showing snapshots is disabled.<br> The default value is "yes". |
| share_name=? | NFS share name. | The value must start with a slash (/). Except the first slash, the value contains 1 to 255 characters, only including letters, digits, spaces, and special characters (/!\"#&%$'()*+-,.:;<=>?@[]^_`{|}~). On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. |
| description=? | Description. | The value consists of 0 to 255 characters. |

##### Usage Guidelines

None

##### Example

Modify the encoding mode and lock policy of an NFS share.

```text
admin:/>change share nfs share_id=1 charset=EUC-JP lock_type=Advisory  audit_items=all show_snapshot_enabled=yes
WARNING: You are about to change the NFS share configuration. This operation may cause the following problems:
1.If this operation changes the character coding format of an NFS share, garbled display or service interruption may occur after the language is switched.
2.If this operation changes the lock policy of an NFS share to "Advisory", cross-protocol interworking scenarios may be influenced and data inconsistency or service interruption may occur.
3.If you enable the audit log function of the NFS share in this operation, NFS service performance may decrease.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Modify the encoding mode and lock policy of a specified NFS share.

```text
admin:/>change share nfs share_name=/fs1 charset=EUC-JP lock_type=Advisory  audit_items=all show_snapshot_enabled=yes
WARNING: You are about to change the NFS share configuration. This operation may cause the following problems:
1.If this operation changes the character coding format of an NFS share, garbled display or service interruption may occur after the language is switched.
2.If this operation changes the lock policy of an NFS share to "Advisory", cross-protocol interworking scenarios may be influenced and data inconsistency or service interruption may occur.
3.If you enable the audit log function of the NFS share in this operation, NFS service performance may decrease.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
