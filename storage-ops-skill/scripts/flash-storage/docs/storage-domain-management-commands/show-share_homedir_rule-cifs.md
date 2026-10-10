# show share_homedir_rule cifs


##### Function

The **show share_homedir_rule cifs** command is used to view the mapping rules of a Homedir share.

##### Format

**show share_homedir_rule cifs** \[ share_id=? \] \[ rule_id=? \] \[ file_system_id=? \] \[ match_user=? \]

##### Parameters

| Parameter        | Description                     | Value                                                                 |
|------------------|---------------------------------|-----------------------------------------------------------------------|
| share_id=?       | Homedir share ID.               | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| rule_id=?        | Mapping rule ID.                | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| file_system_id=? | File system ID.                 | The value is an integer ranging from 0 and 65535.                     |
| match_user=?     | Matched user of a mapping rule. | The value contains 1 to 255 characters.                               |

##### Usage Guidelines

None

##### Example

Query the created mapping rules.

```text

admin:/>show share_homedir_rule cifs

Rule ID       Share ID  Name       FileSystem ID  Priority  Auto Create  Path
------------  --------  ---------  -------------  --------  -----------  -----
304942678150  71        1          0              32        No           /fs0/

```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                                                 |
|---------------|-----------------------------------------------------------------------------------------|
| Rule ID       | Mapping rule ID.                                                                        |
| Share ID      | Homedir share ID.                                                                       |
| Name          | User name.                                                                              |
| FileSystem ID | File system ID.                                                                         |
| Priority      | Priority.                                                                               |
| Auto Create   | Whether the function of creating a home directory automatically is enabled or disabled. |
| Path          | File system path of the user's home directory.                                          |
