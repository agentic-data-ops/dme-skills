# change dtree


##### Function

The **change dtree** command is used to modify dtree information in a file system.

##### Format

**change dtree** dtree_id=? { dtree_new_name=? \| security_style=? \| unix_permissions=? }

**change dtree** dtree_name=? { file_system_id=? \| file_system_name=? } { dtree_new_name=? \| security_style=? \| unix_permissions=? }

**change dtree** dtree_name=? { file_system_id=? \| file_system_name=? } { dtree_new_name=? \| security_style=? \| unix_permissions=? } \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| dtree_id=? | Dtree ID. | The value is a dtree ID. |
| dtree_name=? | Dtree name. | The value contains 1 to 255 characters, including letters, digits, spaces, and special characters (!\"#&%$'()*+-.;<=>?@[]^_`{|}~). On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. |
| file_system_id=? | File system ID. | The value is a file system ID. |
| file_system_name=? | File system name. | To obtain the value, run "show file_system general". |
| dtree_new_name=? | New dtree name. | The value contains 1 to 255 characters, only including letters, digits, spaces, and special characters (!\"#&%$'()*+-.;<=>?@[]^_`{|}~). On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. |
| security_style=? | Security style supported by the dtree directory. | The value can be "NTFS" or "UNIX", where: <br>"NTFS": NTFS security style.<br>"UNIX": UNIX security style. |
| unix_permissions = ? | UNIX permissions of the dtree root directory. | The value consists of three digits, where: The first digit refers to the permission of the owner. The second digit refers to the permission of the user group to which the owner belongs. The last digit refers to the permission of everyone else, ranging from 0 to 7, where: <br>"0": no permission.<br>"1": executable.<br>"2": writable.<br>"3": writable and executable.<br>"4": readable.<br>"5": readable and executable.<br>"6": readable and writable.<br>"7": full permissions (readable + writable + executable). |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

Enter at least one of the following parameters: "dtree_new_name", "security_style", and "unix_permissions".

##### Example

Change the security style of the dtree whose name is "dt_001" to "NTFS".

```text
admin:/>change dtree dtree_name=dt_001 file_system_id=1 security_style=NTFS
Command executed successfully.
```

Change the name of the dtree whose ID is "1@4098" to "dt_00a".

```text
admin:/>change dtree dtree_id=1@4098 dtree_new_name=dt_00a
Command executed successfully.
```

##### System Response

None
