# create dtree general


##### Function

The **create dtree general** command is used to create a dtree.

##### Format

**create dtree general** name=? { file_system_id=? \| file_system_name=? } \[ path=? \] \[ security_style=? \] \[ number=? \] \[ unix_permissions=? \]

**create dtree general** name=? { file_system_id=? \| file_system_name=? } \[ path=? \] \[ security_style=? \] \[ number=? \] \[ unix_permissions=? \] \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Dtree name. | The value contains 1 to 255 characters, including letters, digits, spaces, and special characters (!\"#&%$'()*+-.;<=>?@[]^_`{|}~). On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. |
| file_system_id=? | File system ID. | The value is a file system ID. |
| file_system_name=? | File system name. | To obtain the value, run "show file_system general". |
| path=? | Full path of the parent directory. | The value contains only digits, letters, and underscores (_). |
| security_style=? | Security mode supported by the dtree directory. | The value can be "NTFS" or "UNIX", where: <br>"NTFS": NTFS security style.<br>"UNIX": UNIX security style. |
| number=? | Number of dtrees to be created. | The value ranges from 2 to 100. |
| unix_permissions=? | Permissions of the dtree directory. | The value consists of three digits, where: The first digit refers to the permission of the owner. The second digit refers to the permission of the user group to which the owner belongs. The last digit refers to the permission of everyone else, ranging from 0 to 7, where: <br>"0": no permission.<br>"1": executable.<br>"2": writable.<br>"3": writable and executable.<br>"4": readable.<br>"5": readable and executable.<br>"6": readable and writable.<br>"7": full permissions (readable + writable + executable). |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

None

##### Example

Create a dtree.

```text
admin:/>create dtree general name=dtname file_system_id=1 security_style=UNIX
Create dtree dtname successfully.
```

##### System Response

None
