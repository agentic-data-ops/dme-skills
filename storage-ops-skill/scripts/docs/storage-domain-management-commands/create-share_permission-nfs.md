# create share_permission nfs


##### Function

The **create share_permission nfs** command is used to create an NFS share permission.

##### Format

**create share_permission nfs** access_name=? { share_id=? \| share_name=? } access_type=? sync_enabled=? all_squash_enabled=? root_squash_enabled=? \[ secure_enabled=? \] \[ charset=? \] \[ anonymous_user_id=? \] \[ v4_acl_preserve=? \] \[ ntfs_unix_security_ops=? \] \[ security_type=? \] \[ chown_mode=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| access_name=? | Access object. The object can be an IP address, host name, network group, network segment or asterisk (*). Multiple host names or IP addresses are separated by commas (,). | The value ranges from 1 to 256 characters. If the value is a network group, add the "@" before the name to be different from the host name. Host name: <br>The value can consist of letters, digits, hyphens (-), periods (.), and underscores (_).<br>The value starts with a letter or digit and cannot end with a hyphen (-) or underscore (_).<br>The value cannot contain consecutive periods (.), or combination of a period and hyphen (.- or -.), or the combination of a period and underscore (._ or _.).<br>The value cannot consist of pure digits.<br>The fully qualified domain name (FQDN) is recommended. |
| share_id=? | NFS share ID. | The value ranges from 1 to 18446744073709551615. |
| access_type=? | NFS share access type. | The value can be "read_only" or "read_write", where: <br>"read_only": read-only.<br>"read_write": read and write. |
| sync_enabled=? | Whether NFS share write synchronization is enabled. | The value can be "yes" or "no", where: <br>"yes": NFS share write synchronization is enabled.<br>"no": NFS share write synchronization is disabled. |
| all_squash_enabled=? | Whether the permissions of all users that access the NFS share are compressed. | The value can be "yes" or "no", where: <br>"yes": The permissions of all users are compressed.<br>"no": The permissions of all users are not compressed. |
| share_name=? | Name of the NFS share. | The value must start with a slash (/). Except the first slash, the value contains 1 to 255 characters, including letters, digits, spaces, and special characters (/!\"#&%$'()*+-,.:;<=>?@[]^_`{|}~). On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. |
| root_squash_enabled=? | Whether the permissions of super users that access the NFS share are compressed. | The value can be "yes" or "no", where: <br>"yes": The permissions of super users are compressed.<br>"no": The permissions of super users are not compressed. |
| secure_enabled=? | Whether an NFS share supports security ports. | Possible values are "yes" or "no", where: <br>"yes": Secure ports are enabled.<br>"no": Secure ports are not supported. |
| charset=? | Encoding mode of the NFS share. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "UTF-8", "JIS", "S-JIS", "EUC-JP", "DE", "ZH", "GBK", "EUC-TW", "BIG5", "PT", "FR", "IT", "ES", "KO" or "default", where: <br>"UTF-8": UTF-8 encoding.<br>"ZH": simplified Chinese.<br>"GBK": simplified Chinese.<br>"EUC-TW": traditional Chinese.<br>"BIG5": traditional Chinese.<br>"EUC-JP": EUC-JP encoding.<br>"JIS": JIS encoding.<br>"S-JIS": Shift-JIS encoding.<br>"DE": German.<br>"PT": Portuguese.<br>"ES": Spanish.<br>"FR": French.<br>"IT": Italian.<br>"KO": Korean.<br>"default": inherits the encoding mode configured for the share. |
| anonymous_user_id=? | Mapping value of the UID and GID of an anonymous NFS share user. | The value is an integer ranging from 0 to 4294967294. |
| v4_acl_preserve=? | NFSv4 ACL protection. | The value can be "enable" or "disable", where: <br>"enable": In UNIX security mode, NFSv4 ACL is preserved during the NFS client permission modification.<br>"disable": In UNIX security mode, NFSv4 ACL is deleted during the NFS client permission modification.<br> The default value is "enable". |
| ntfs_unix_security_ops=? | NTFS UNIX security option. | The value can be "fail" or "ignore", where: <br>"fail": In NTFS security mode, if ACL exists, modifying the permission on the NFS client is not allowed.<br>"ignore": In NTFS security mode, if ACL exists, modifying the permission on the NFS client is ignored.<br> The default value is "fail". |
| security_type=? | The supported security type for the NFS mount. The security type can be configured unix or none or none_unix. | The security type can be "auth_none" or "auth_unix" or both. If both of them are specified, separate them by an underscore (_). For example, security_type="unix" or security_type="none_unix", indicating that the security type is UNIX. |
| chown_mode=? | Ownership (owner or group) change mode. | The value can be "restricted" or "unrestricted", where: <br>"restricted": Only the root user can change the ownership of a file or directory.<br>"unrestricted": The root user, owner, or non-owners with the write owner permission in the ACL can change the ownership of files or directories. |

##### Usage Guidelines

None

##### Example

Create an NFS share permission.

```text
admin:/>create share_permission nfs access_name=* share_id=1 access_type=read_write sync_enabled=no all_squash_enabled=no root_squash_enabled=no secure_enabled=no charset=GBK anonymous_user_id=65533 v4_acl_preserve=disable ntfs_unix_security_ops=ignore
Command executed successfully.
```

Create an NFS share permission.

```text
admin:/>create share_permission nfs access_name=* share_name=/fs1 access_type=read_write sync_enabled=no all_squash_enabled=no root_squash_enabled=no secure_enabled=no charset=GBK anonymous_user_id=65533 v4_acl_preserve=disable ntfs_unix_security_ops=ignore
Command executed successfully.
```

Create NFS share permissions.

```text
admin:/>create share_permission nfs access_name=192.168.0.10,192.168.0.0/24,* share_id=1 access_type=read_write sync_enabled=no all_squash_enabled=no root_squash_enabled=no secure_enabled=no charset=GBK anonymous_user_id=65533 v4_acl_preserve=disable ntfs_unix_security_ops=ignore
Command executed successfully.
```

##### System Response

None
