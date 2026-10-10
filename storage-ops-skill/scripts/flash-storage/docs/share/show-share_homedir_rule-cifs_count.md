# show share_homedir_rule cifs_count


##### Function

The **show share_homedir_rule cifs_count** command is used to view the number of mapping rules of a Homedir share.

##### Format

**show share_homedir_rule cifs_count** \[ share_id=? \] \[ file_system_id=? \] \[ match_user=? \]

##### Parameters

| Parameter        | Description                     | Value                                                                 |
|------------------|---------------------------------|-----------------------------------------------------------------------|
| share_id=?       | Homedir share ID.               | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| file_system_id=? | File system ID.                 | The value is an integer ranging from 0 and 65535.                     |
| match_user=?     | Matched user of a mapping rule. | The value contains 1 to 255 characters.                               |

##### Usage Guidelines

None

##### Example

Query the number of created mapping rules.

```text
admin:/>show share_homedir_rule cifs_count
Number: 9

```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                                     |
|-----------|---------------------------------------------|
| Number    | Number of mapping rules of a Homedir share. |
