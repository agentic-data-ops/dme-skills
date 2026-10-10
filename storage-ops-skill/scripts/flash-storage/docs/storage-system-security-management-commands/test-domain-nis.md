# test domain nis


##### Function

The **test domain nis** command is used to test the connectivity of an NIS server.

##### Format

**test domain nis** \[ address=? \] \[ controller=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| address=? | IP address or host name of the NIS server. | The value can be an IP address or a host name, and contains 1 to 255 characters. <br>IPv4 and IP46 addresses are supported.<br>A host name: <br>Contains 1 to 255 characters, including letters, digits, hyphens (-), periods (.), and underscores (_).<br>Must start with a letter or digit and cannot end with a hyphen (-) or underscore (_).<br>Cannot contain consecutive periods (.), pure digits, or the combination of a period and underscore (._ or _.). |
| controller=? | Controller ID. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0. To obtain the value, run "show controller general". |

##### Usage Guidelines

None

##### Example

Test the connectivity of the NIS server whose IP address is "10.148.105.124".

```text
admin:/>test domain nis address=10.148.105.124 controller=0A
Command executed successfully.
```

##### System Response

None
