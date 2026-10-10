# test domain ldap


##### Function

The **test domain ldap** command is used to test the connectivity of an LDAP server.

##### Format

**test domain ldap** \[ address=? \] \[ port=? \] \[ controller=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| address=? | IP address or host name of the LDAP server. | The value can be an IP address or a host name, and contains 1 to 255 characters. <br>IPv4 and IP46 addresses are supported.<br>A host name: <br>Contains 1 to 255 characters, including letters, digits, hyphens (-), periods (.), and underscores (_).<br>Must start with a letter or digit and cannot end with a hyphen (-) or underscore (_).<br>Cannot contain consecutive periods (.), pure digits, or the combination of a period and underscore (._ or _.). |
| port | Listening port number of the LDAP service. | The value is an integer ranging from 1 to 65535. The default LDAP port number is 389, and the default LDAPS port number is 636. |
| controller=? | Controller ID. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0. To obtain the value, run "show controller general". |

##### Usage Guidelines

None

##### Example

Test the connectivity of the LDAP server whose IP address is "10.148.105.124".

```text
admin:/>test domain ldap address=10.148.105.124 port=389 controller=0A
Command executed successfully.
```

##### System Response

None
