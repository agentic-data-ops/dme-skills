# change disk precopy


##### Function

The **change disk precopy** command is used to enable or disable the disk precopy function.

##### Format

**change disk precopy** enabled=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Whether or not to enable the disk precopy function. | The value can be "yes" or "no", where: <br>"yes": The disk precopy function will be enabled.<br>"no": The disk precopy function will be disabled. |

##### Usage Guidelines

The disk precopy function enables the system to back up data to hot spare area in a timely manner in the scenario where a member disk of the disk domain is going to fail. This improves data security.

##### Example

Enable the disk precopy function.

```text
admin:/>change disk precopy enabled=yes
Command executed successfully.

```

##### System Response

None
