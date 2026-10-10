# change clone general


##### Function

The **change clone general** command is used to modify clone pair settings.

##### Format

**change clone general** { clone_id=? \| clone_name=? } \[ copy_speed=? \] \[ name=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_id=? | ID of the clone pair to be modified. | The value is an integer ranging from 0 to 65535. |
| clone_name=? | Name of the clone pair to be modified. | The value is a string of 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| copy_speed=? | Copy rate. | The value can be "low", "middle", "high", or "highest", where: <br>"low": low speed.<br>"middle": medium speed.<br>"high": high speed.<br>"highest": highest speed. |
| name=? | New name of the clone pair. | The value is a string of 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| description=? | Description. | - |

##### Usage Guidelines

None

##### Example

Change the copy speed of clone pair "1" to "high".

```text
admin:/>change clone general clone_id=1 copy_speed=high
Command executed successfully.
```

##### System Response

None
