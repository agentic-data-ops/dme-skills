# show host reachable


##### Function

The **show host reachable** command is used to query whether a host is reachable.

##### Format

**show host reachable** { dest_ipv4=? \| dest_ipv6=? \| hostname=? } \[ count=? \] \[ controller=? \]

##### Parameters

| Parameter    | Description               | Value                                                                                                             |
|--------------|---------------------------|-------------------------------------------------------------------------------------------------------------------|
| count=?      | Count of ping operations. | The value ranges from 1 to 30. The default value is "4".                                                          |
| dest_ipv4=?  | Host IP address.          | The value can be an IPv4.                                                                                         |
| dest_ipv6=?  | Host IP address.          | The value can be an IPv6.                                                                                         |
| hostname=?   | Host name.                | The value contains 1 to 253 characters including letters, digits, hyphens (-), underscores (\_), and periods (.). |
| controller=? | Controller ID.            | For example, 0A or 1C. You can run the "show controller general" command to obtain the value.                     |

##### Usage Guidelines

None

##### Example

Check whether IP address "192.168.90.160" is reachable.

```text
admin:/>show host reachable controller=0A count=5 dest_ipv4=192.168.90.160
Local Controller  :  0A
Remote Host       :  192.168.90.160
Reachable         :  Yes
```

Check whether IP address "fe80::3600:a3ff:fedc:46c2" is reachable.

```text
admin:/>show host reachable controller=0A count=5 dest_ipv6=fe80::3600:a3ff:fedc:46c2
Local Controller  :  0A
Remote Host       :  fe80::3600:a3ff:fedc:46c2
Reachable         :  Yes

```

Check whether IP address "fe80::3600:a3ff:fedc:46c2" is reachable.

```text
admin:/>show host reachable count=5 dest_ipv6=fe80::3600:a3ff:fedc:46c2
Local Controller  :  0A
Remote Host       :  fe80::3600:a3ff:fedc:46c2
Reachable         :  Yes
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                  |
|------------------|--------------------------|
| Reachable        | Reachable.               |
| Local Controller | Local controller.        |
| Remote Host      | Remote host information. |
