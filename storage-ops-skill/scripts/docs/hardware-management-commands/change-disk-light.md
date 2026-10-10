# change disk light


##### Function

The **change disk light** command is used to turn on or turn off the location indicator of a specific disk.

##### Format

**change disk light** disk_id=? on_or_off=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disk_id=? | ID of the disk. | To obtain the value, run "show disk general". |
| on_or_off=? | Whether to turn on or turn off the location indicator of a disk. | The value can be "on" or "off", where: <br>"on": The location indicator of a disk will be turned on.<br>"off": The location indicator of a disk will be turned off. |

##### Usage Guidelines

By turning on the location indicator of a disk, you can find the physical location of the disk easily.

##### Example

Turn on the location indicator of the disk whose ID is "DAE000.0". The command output varies depending on a specific product.

```text
admin:/>change disk light disk_id=DAE000.0 on_or_off=on
Command executed successfully.

```

##### System Response

None
