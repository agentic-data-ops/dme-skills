# change user_session number


##### Function

The **change user_session number** command is used to change the number of sessions supported by the system.

##### Format

**change user_session number** max_number=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| max_number=? | Number of sessions supported by the system. | The value can be "32" or "256", where: <br>32: The system supports 32 sessions.<br>256: The system supports 256 sessions. |

##### Usage Guidelines

None

##### Example

Change the number of sessions supported by the system to "256".

```text
admin:/>change user_session number max_number=256
Command executed successfully.
```

##### System Response

None
