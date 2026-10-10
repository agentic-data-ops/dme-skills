# change icmp switch


##### Function

The **change icmp switch** command is used to set the ICMP function of all ports.You can run this command to turn on or off icmp function of all ports.

##### Format

**change icmp switch** switch=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| switch=? | Status of icmp function switch. | The value can be "on" or "off", where: <br>"on": Enable the icmp function.<br>"off": Disable the icmp function. |

##### Usage Guidelines

None.

##### Example

To disable the icmp function on all ports, run the following command:

```text
admin:/>change icmp switch switch=off
command executed successfully.
```

##### System Response

None
