# change weak_password_dictionary switch


##### Function

The **change weak_password_dictionary switch** command is used to enable or disable the weak password dictionary function.

##### Format

**change weak_password_dictionary switch** switch=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| switch=? | Whether to enable the weak password dictionary function. | The value can be "on" or "off", where: <br>"on": Enable the weak password dictionary function.<br>"off": Disable the weak password dictionary function. |

##### Usage Guidelines

After this command is executed successfully, the system changes the status of the weak password dictionary function based on the command parameters.

##### Example

Enable the weak password dictionary function.

```text
admin:/>change weak_password_dictionary switch switch=on
Command executed successfully.
```

Disable the weak password dictionary function.

```text
admin:/>change weak_password_dictionary switch switch=off
Command executed successfully.
```

##### System Response

None
