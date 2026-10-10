# change clone_consistency_group general


##### Function

The **change clone_consistency_group general** command is used to modify clone consistency group settings.

##### Format

**change clone_consistency_group general** { clone_consistency_group_id=? \| clone_consistency_group_name=? } \[ copy_speed=? \] \[ name=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_consistency_group_id=? | Clone consistency group ID. | You can run the show clone_consistency_group general command to obtain the value. |
| clone_consistency_group_name=? | Name of the clone consistency group. | You can run the show clone_consistency_group general command to obtain the value. |
| copy_speed=? | Copy rate. | The value can be "low", "middle", "high", or "highest", where: <br>"low": low speed.<br>"middle": medium speed.<br>"high": high speed.<br>"highest": highest speed. |
| name=? | New name of the clone consistency group. | The value is a string of 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| description=? | Description of the clone CG. | - |

##### Usage Guidelines

None

##### Example

Change the copy speed of clone consistency group "3" to "high".

```text
admin:/>change clone_consistency_group general clone_consistency_group_id=3 copy_speed=high
Command executed successfully.
```

##### System Response

None
