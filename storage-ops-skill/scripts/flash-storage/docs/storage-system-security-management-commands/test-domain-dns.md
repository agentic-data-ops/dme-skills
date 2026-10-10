# test domain dns


##### Function

The **test domain dns** command is used to test the connectivity of the DNS server.

##### Format

**test domain dns** \[ address=? \] \[ controller=? \]

##### Parameters

| Parameter    | Description                   | Value                                                                                                                                       |
|--------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| address=?    | IP address of the DNS server. | The value can be an IPv4 address or IPv6 address.                                                                                           |
| controller=? | Controller ID.                | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0. To obtain the value, run "show controller general". |

##### Usage Guidelines

None

##### Example

Test the connectivity of the DNS server whose IP address is "10.148.105.124".

```text
admin:/>test domain dns address=10.148.105.124 controller=0A
Command executed successfully.
```

##### System Response

None
