# test domain ad


##### Function

The **test domain ad** command is used to test the connectivity of an AD domain server.

##### Format

**test domain ad** \[ fqdn=? \] \[ controller=? \]

##### Parameters

| Parameter  | Description                          | Value                                                                                                                                       |
|------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| fqdn=?     | Domain name of the AD domain server. | The value contains of 1 to 127 characters.                                                                                                  |
| controller | Controller ID.                       | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0. To obtain the value, run "show controller general". |

##### Usage Guidelines

None

##### Example

Test the connectivity of the AD domain server whose domain name is "auth2k8.com".

```text
admin:/>test domain ad fqdn=auth2k8.com controller=0A
Command executed successfully.
```

##### System Response

None
