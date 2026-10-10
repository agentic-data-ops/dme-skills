# test smtp_server general


##### Function

The **test smtp_server general** command is used to test the connectivity of an SMTP server.

##### Format

**test smtp_server general** server=?

##### Parameters

| Parameter | Description                 | Value                                                                                                                                                                                                                                                                                                         |
|-----------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server=?  | Address of the SMTP server. | The value can be a domain name or IP address (IPv4 or IPv6 address). The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits, and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |

##### Usage Guidelines

None

##### Example

Test the connectivity of the SMTP server whose IP address is 10.148.105.124.

```text
admin:/>test smtp_server general server=10.148.105.124
Command executed successfully.
```

##### System Response

None
