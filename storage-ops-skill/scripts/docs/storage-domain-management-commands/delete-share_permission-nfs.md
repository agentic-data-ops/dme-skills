# delete share_permission nfs


##### Function

The **delete share_permission nfs** command is used to delete an NFS share permission.

##### Format

**delete share_permission nfs** { share_permission_id=? \| share_name=? access_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_permission_id=? | NFS share permission ID. | The value ranges from 1 to 18446744073709551615. |
| share_name=? | Name of the NFS share. | The value must start with a slash (/). Except the first slash, the value contains 1 to 255 characters, only including letters, digits, spaces, and special characters (/!\"#&%$'()*+-,.:;<=>?@[]^_`{|}~). On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. |
| access_name=? | Access object. The object can be an IP address, host name, network group, network segment or asterisk (*). Multiple host names or IP addresses are separated by commas (,). | The value ranges from 1 to 256 characters. If the value is a network group, add the "@" before the name to be different from the host name. Host name: <br>The value can consist of letters, digits, hyphens (-), periods (.), and underscores (_).<br>The value starts with a letter or digit and cannot end with a hyphen (-) or underscore (_).<br>The value cannot contain consecutive periods (.), or combination of a period and hyphen (.- or -.), or the combination of a period and underscore (._ or _.).<br>The value cannot consist of pure digits.<br>The fully qualified domain name (FQDN) is recommended. |

##### Usage Guidelines

Parameters "share_permission_id" or "share_name and access_name" must be entered.

##### Example

Query NFS share permissions before the deletion.

```text

admin:/>show share_permission nfs share_id=6

Share Permission ID  Access Name  Share ID  Access Type  Sync Enabled  All Squash Enabled  Root Squash Enabled  Secure Enabled  Security Type  Share Name
-------------------  -----------  --------  -----------  ------------  ------------------  -------------------  --------------  -------------  ----------
11                   *            6         Read Only    No            Yes                 No                   No              unix           /fs_1

```

Delete an NFS share permission.

```text
admin:/>delete share_permission nfs share_permission_id=6
Command executed successfully.
```

Query NFS share permissions after the deletion.

```text
admin:/>show share_permission nfs share_id=6
Command executed successfully.
```

Delete an NFS share permission.

```text
admin:/>delete share_permission nfs share_name=/fs_1 access_name=*
Command executed successfully.
```

Delete NFS share permissions.

```text
admin:/>delete share_permission nfs share_name=/fs_1 access_name=192.168.0.10,192.168.0.0/24,*
Command executed successfully.
```

##### System Response

None
