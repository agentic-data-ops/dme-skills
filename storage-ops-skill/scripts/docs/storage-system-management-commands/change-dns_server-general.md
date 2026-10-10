# change dns_server general


##### Function

The **change dns_server general** command is used to modify information about the management DNS server of a disk array.

##### Format

**change dns_server general** \[ address=? \] \[ check_switch=? \] \[ check_period=? \]

##### Parameters

| Parameter      | Description             | Value                                                                                                                                                                                             |
|----------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| address=?      | DNS IP addresses.       | A maximum of three IP addresses are supported. Separate the IP addresses with commas (,), for example, "address=192.168.1.9,192.168.2.9,192.168.3.9." Both IPv4 and IPv6 addresses are supported. |
| check_switch=? | Automatic check switch. | The automatic check switch can be turned on or off. By default, it is turned off.                                                                                                                 |
| check_period=? | Automatic check period. | The automatic check period ranges from 1 to 30, expressed in minutes, and the system default value is "2".                                                                                        |

##### Usage Guidelines

None

##### Example

Set the IP addresses of the DNS server to "192.168.1.9", "192.168.2.9", and "192.168.3.9", turn on the automatic check switch, and set the check period to two minutes.

```text
admin:/>change dns_server general address=192.168.1.9,192.168.2.9,192.168.3.9 check_switch=on check_period=2
Command executed successfully.
```

##### System Response

None
