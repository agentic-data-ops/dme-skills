# show share_permission nfs


##### Function

The **show share_permission nfs** command is used to query information about NFS share permissions.

##### Format

**show share_permission nfs** \[ share_permission_id=? \| share_id=? \| share_name=? access_name=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_permission_id=? | NFS share permission ID. | The value ranges from 1 to 18446744073709551615. |
| share_id=? | NFS share ID. | The value ranges from 1 to 18446744073709551615. |
| share_name | NFS share name. | The value must start with a slash (/). Except the first slash, the value contains 1 to 255 characters, including letters, digits, spaces, and special characters (/!\"#&%$'()*+-,.:;<=>?@[]^_`{|}~). On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. |
| access_name=? | Access object, which can be an IP address, host name, network group, network segment, or asterisk (*). | The value ranges from 1 to 256 characters. If the value is a network group, add the "@" before the name to be different from the host name. Host name: <br>The value can consist of letters, digits, hyphens (-), periods (.), and underscores (_).<br>The value starts with a letter or digit and cannot end with a hyphen (-) or underscore (_).<br>The value cannot contain consecutive periods (.), or combination of a period and hyphen (.- or -.), or the combination of a period and underscore (._ or _.).<br>The value cannot consist of pure digits.<br>The fully qualified domain name (FQDN) is recommended. |

##### Usage Guidelines

Parameters "share_permission_id", "share_name", and "share_id" are mutually exclusive.

##### Example

Query the permission of an NFS share with a specific share ID.

```text

admin:/>show share_permission nfs share_id=2

Share Permission ID  Access Name  Share ID  Access Type  Sync Enabled  All Squash Enabled  Root Squash Enabled  Secure Enabled  Security Type  Share Name
-------------------  -----------  --------  -----------  ------------  ------------------  -------------------  --------------  -------------  ----------
11                   *            2         Read Only    No            Yes                 No                   No              unix           /ctt1
12                   4.5.6.7      2         Read Write   Yes           No                  No                   No              unix           /ctt1

```

Query the permission of an NFS share with a specific share permission ID.

```text

admin:/>show share_permission nfs share_permission_id=12

Share Permission ID    : 12
Access Name            : 4.5.6.7
Share ID               : 2
Access Type            : Read Write
Sync Enabled           : Yes
All Squash Enabled     : No
Root Squash Enabled    : No
Secure Enabled         : No
Charset                : --
Anonymous User ID      : 65534
V4 Acl Preserve        : Enabled
Ntfs Unix Security Ops : Fail
Security Type          : unix
Share Name             : /ctt1
Chown Mode             : Restricted

```

Query the permission of an NFS share with a specific share name.

```text
admin:/>show share_permission nfs share_name=/ctt1
Share Permission ID  Access Name  Share ID  Access Type  Sync Enabled  All Squash Enabled  Root Squash Enabled  Secure Enabled  Security Type  Share Name
-------------------  -----------  --------  -----------  ------------  ------------------  -------------------  --------------  -------------  ----------
11                   *            2         Read Only    No            Yes                 No                   No              unix           /ctt1
12                   4.5.6.7      2         Read Write   Yes           No                  No                   No              unix           /ctt1
```

Query permissions of all the NFS shares.

```text

admin:/>show share_permission nfs

Share Permission ID  Access Name  Share ID  Access Type  Sync Enabled  All Squash Enabled  Root Squash Enabled  Secure Enabled  Security Type  Share Name
-------------------  -----------  --------  -----------  ------------  ------------------  -------------------  --------------  -------------  ----------
3                    1.1.1.1      3         Read Write   Yes           Yes                 No                   No              unix           /ctt2
5                    1.1.1.3      3         Read Write   Yes           Yes                 No                   No              unix           /ctt2
11                   *            2         Read Only    No            Yes                 No                   No              unix           /ctt1
12                   4.5.6.7      2         Read Write   Yes           No                  No                   No              unix           /ctt1
13                   4.5.6.7      3         Read Write   Yes           No                  No                   No              unix           /ctt2
14                   5.5.5.5      10        Read Write   No            No                  No                   No              unix           /fstest2
19                   1.1.1.1      50        Read Only    No            Yes                 Yes                  No              unix           /smbfs4242
20                   1.1.1.2      50        Read Write   No            Yes                 Yes                  No              unix           /smbfs4242
21                   1.1.1.1      51        Read Only    No            Yes                 Yes                  No              unix           /smbfs2942
22                   1.1.1.2      51        Read Write   No            Yes                 Yes                  No              unix           /smbfs2942
23                   1.1.1.1      52        Read Only    No            Yes                 Yes                  No              unix           /smbfs3660
24                   1.1.1.2      52        Read Write   No            Yes                 Yes                  No              unix           /smbfs3660

```

Query the permission of an NFS share with a specific share ID and a share name.

```text
admin:/>show share_permission nfs share_name=/ctt1 access_name=*
Share Permission ID  Access Name  Share ID  Access Type  Sync Enabled  All Squash Enabled  Root Squash Enabled  Secure Enabled  Security Type  Share Name
-------------------  -----------  --------  -----------  ------------  ------------------  -------------------  --------------  -------------  ----------
11                   *            2         Read Only    No            Yes                 No                   No              unix           /ctt1
```

##### System Response

The following table describes the parameter meanings.

| Parameter              | Meaning                                                                                                       |
|------------------------|---------------------------------------------------------------------------------------------------------------|
| Share Permission ID    | NFS share permission ID.                                                                                      |
| Access Name            | Access object. The object can be an IP address, host name, network group, or network segment.                 |
| Share ID               | NFS share ID.                                                                                                 |
| Access Type            | NFS share access type.                                                                                        |
| Sync Enabled           | Whether NFS share write synchronization is enabled.                                                           |
| All Squash Enabled     | Whether the permissions of all users that access the NFS share are compressed.                                |
| Root Squash Enabled    | Whether the permissions of super users that access the NFS share are compressed.                              |
| Secure Enabled         | Whether an NFS share supports security ports.                                                                 |
| Charset                | Encoding mode of the NFS share.                                                                               |
| Anonymous User ID      | Mapping value of the UID and GID of an anonymous NFS share user.                                              |
| V4 Acl Preserve        | NFSv4 ACL protection.                                                                                         |
| Ntfs Unix Security Ops | NTFS UNIX security option.                                                                                    |
| Security Type          | The supported security type for the NFS mount. The security type can be configured unix or none or none_unix. |
| Share Name             | Name of the NFS share.                                                                                        |
| Chown Mode             | Ownership (owner or group) change mode.                                                                       |
