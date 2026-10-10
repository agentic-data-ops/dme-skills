# change enclosure light


##### Function

The **change enclosure light** command is used to set the status of the location indicator on a specific engine or disk enclosure. You can run this command to query the location of an engine or disk enclosure.

##### Format

**change enclosure light** enclosure_number=? on_or_off=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enclosure_number=? | ID of an engine or disk enclosure. | To obtain the value, run "show enclosure". |
| on_or_off=? | Status of a location indicator. | The value can be "on" or "off", where: <br>"on": The location indicator will be turned on.<br>"off": The location indicator will be turned off. |

##### Usage Guidelines

None.

##### Example

Turn on the location indicator on the disk enclosure whose ID is "DAE000". The command output varies depending on a specific product.

```text
admin:/>change enclosure light enclosure_number=DAE000 on_or_off=on
Command executed successfully.
```

##### System Response

None
