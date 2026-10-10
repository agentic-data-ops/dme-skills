# delete share nfs


##### Function

The **delete share nfs** command is used to delete an NFS share.

##### Format

**delete share nfs** { share_id=? \| share_name=? }

##### Parameters

| Parameter    | Description     | Value                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| share_id=?   | NFS share ID.   | The value ranges from 1 to 18446744073709551615.                                                                                                                                                                                                                                                                                                                                                       |
| share_name=? | NFS share name. | The value must start with a slash (/). Except the first slash, the value contains 1 to 255 characters, only including letters, digits, spaces, and special characters (/!\\"#&%$'()\*+-,.:;\<=\>?@\[\]^\_\`{\|}\~). On the CLI, the following characters need to be represented with escape sequences: "\\\|" indicates "\|", "\\\\" indicates "\\", "\\q" indicates "?", and "\\s" indicates a space. |

##### Usage Guidelines

In HyperMetro scenarios, if a failure message is prompted when deleting an NFS share, inconsistency between primary and secondary share permission lists may occur. You need to delete again until the operation succeeds to prevent inconsistency between primary and secondary share permission lists.

##### Example

Query NFS shares before the deletion.

```text

admin:/>show share nfs

Share ID  File System ID  Description  Local Path  Alias     CharSet  Lock Type  Audit Items  show_snapshot_enabled
--------  --------------  -----------  ----------  --------  -------  ---------  -----------  ---------------------
1         1               1111         /fs0        /fs0      ZH       Mandatory  --           yes
2         1                            /fs0/!\\    /fs0/!\\  UTF-8    Mandatory  --           yes
3         2                            /fs1        /fs1      UTF-8    Mandatory  --           yes

```

Delete an NFS share.

```text
admin:/>delete share nfs share_id=3
WARNING: You are going to delete protocol share. This operation may interrupt share services or cause access exceptions.
Suggestion: Before you perform this operation, determine whether the delete is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query NFS shares after the deletion.

```text

show share nfs

Share ID  File System ID  Description  Local Path  Alias     CharSet  Lock Type  Audit Items  show_snapshot_enabled
--------  --------------  -----------  ----------  --------  -------  ---------  -----------  ---------------------
1         1               1111         /fs0        /fs0      ZH       Mandatory  --           yes
2         1                            /fs0/!\\    /fs0/!\\  UTF-8    Mandatory  --           yes

```

##### System Response

None
