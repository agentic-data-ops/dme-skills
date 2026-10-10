# change user_mode enabled


##### Function

The **change user_mode enabled** command is used to set the supported views.

##### Format

**change user_mode enabled** user_mode=? enabled=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| user_mode=? | User mode. | The value is "developer". |
| enabled=? | Switch. | The value can be "yes" or "no", where: <br>"yes": supports the current view.<br>"no": does not support the current view. |

##### Usage Guidelines

This command can be executed only when SNMP is running correctly.

##### Example

Disable the support for the developer view.

```text
admin:>change user_mode enabled user_mode=developer enabled=no
Command executed successfully.
```

##### System Response

None
