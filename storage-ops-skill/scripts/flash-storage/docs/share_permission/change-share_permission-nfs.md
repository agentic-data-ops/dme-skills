# change share_permission nfs


##### Function

The **change share_permission nfs** command is used to modify NFS share permission settings.

##### Format

**change share_permission nfs** share_permission_id=? { access_type=? \| sync_enabled=? \| all_squash_enabled=? \| root_squash_enabled=? \| secure_enabled=? \| charset=? \| anonymous_user_id=? \| v4_acl_preserve=? \| ntfs_unix_security_ops=? \| security_type=? \| chown_mode=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_permission_id=? | NFS share permission ID. | The value is an integer ranging from 1 to 18446744073709551615. |
| access_type=? | NFS share access permission. | The value can be "read_only" or "read_write", where: <br>"read_only": read-only.<br>"read_write": read and write. |
| sync_enabled=? | Whether NFS share write synchronization is enabled. | The value can be "yes" or "no", where: <br>"yes": NFS share write synchronization is enabled.<br>"no": NFS share write synchronization is disabled. |
| all_squash_enabled=? | Whether the permissions of all users that access the NFS share are compressed. | The value can be "yes" or "no", where: <br>"yes": The permissions of all users are compressed.<br>"no": The permissions of all users are not compressed. |
| root_squash_enabled=? | Whether the permissions of super users that access the NFS share are compressed. | The value can be "yes" or "no", where: <br>"yes": The permissions of super users are compressed.<br>"no": The permissions of super users are not compressed. |
| secure_enabled=? | Whether an NFS share supports security ports. | The value can be "yes" or "no", where: <br>"yes": supports security ports.<br>"no": does not support security ports. |
| charset=? | Encoding mode of the NFS share. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "UTF-8", "JIS", "S-JIS", "EUC-JP", "DE", "ZH", "GBK", "EUC-TW", "BIG5", "PT", "FR", "IT", "ES", "KO" or "default", where: <br>"UTF-8": UTF-8 encoding.<br>"ZH": simplified Chinese.<br>"GBK": simplified Chinese.<br>"EUC-TW": traditional Chinese.<br>"BIG5": traditional Chinese.<br>"EUC-JP": EUC-JP encoding.<br>"JIS": JIS encoding.<br>"S-JIS": Shift-JIS encoding.<br>"DE": German.<br>"PT": Portuguese.<br>"ES": Spanish.<br>"FR": French.<br>"IT": Italian.<br>"KO": Korean.<br>"default": inherits the encoding mode configured for the share. |
| anonymous_user_id=? | Mapping value of the UID and GID of an anonymous NFS share user. | The value is an integer ranging from 0 to 4294967294. |
| v4_acl_preserve=? | NFSv4 ACL protection. | The value can be "enable" or "disable", where: <br>"enable": In UNIX security mode, NFSv4 ACL is preserved during the NFS client permission modification.<br>"disable": In UNIX security mode, NFSv4 ACL is deleted during the NFS client permission modification.<br> The default value is "enable". |
| ntfs_unix_security_ops=? | NTFS UNIX security option. | The value can be "fail" or "ignore", where: <br>"fail": In NTFS security mode, if ACL exists, modifying the permission on the NFS client is not allowed.<br>"ignore": In NTFS security mode, if ACL exists, modifying the permission on the NFS client is ignored.<br> The default value is "fail". |
| security_type=? | The supported security type for the NFS mount. The security type can be configured unix or none or none_unix. | The security type can be "auth_none" or "auth_unix" or both. If both of them are specified, separate them by an underscore (_). For example, security_type="unix" or security_type="none_unix", indicating that the security type is UNIX. |
| chown_mode=? | Ownership (owner or group) change mode. | The value can be "restricted" or "unrestricted", where: <br>"restricted": Only the root user can change the ownership of a file or directory.<br>"unrestricted": The root user, owner, or non-owners with the write owner permission in the ACL can change the ownership of files or directories. |

##### Usage Guidelines

None

##### Example

Query the NFS share permission before the modification.

```text
admin:/>show share_permission nfs share_permission_id=1
Share Permission ID : 1
Access Name      : 10.90.96.90
Share ID       : 1
Access Type      : Read Only
Sync Enabled     : Yes
All Squash Enabled  : Yes
Root Squash Enabled : Yes
Secure Enabled    : Yes
CharSet           : default
Anonymous User ID : 65534
V4 Acl Preserve : Enabled
Ntfs Unix Security Ops: Fail
Security Type         : --
Chown Mode        : Restricted
```

Modify the NFS share permission.

```text
admin:/>change share_permission nfs share_permission_id=1 access_type=read_write sync_enabled=no all_squash_enabled=no root_squash_enabled=no secure_enabled=no charset=GBK anonymous_user_id=65533 v4_acl_preserve=disable ntfs_unix_security_ops=ignore
WARNING: You are about to modify the permission configurations of the NFS share. This operation may cause the following problems:
1. If this operation changes the character encoding mode of the NFS share permission, garbled characters may be displayed or services may be interrupted.
2. If this operation changes the anonymous user ID of the NFS share permission, services may be interrupted.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query the NFS share permission after the modification.

```text
admin:/>show share_permission nfs share_permission_id=1
Share Permission ID : 1
Access Name : 10.90.96.90
Share ID : 1
Access Type : Read Write
Sync Enabled : No
All Squash Enabled : No
Root Squash Enabled : No
Secure Enabled    : No
CharSet           : GBK
Anonymous User ID : 65533
V4 Acl Preserve : Disabled
Ntfs Unix Security Ops: Ignore
Security Type         : --
Chown Mode        : Restricted
```

##### System Response

None
