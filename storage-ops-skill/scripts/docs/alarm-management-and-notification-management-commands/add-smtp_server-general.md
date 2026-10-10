# add smtp_server general


##### Function

The **add smtp_server general** command is used to add an email sending server.

##### Format

**add smtp_server general** server=?

##### Parameters

| Parameter | Description                 | Value                                                                                                                                                                                                                                                                                                         |
|-----------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server=?  | Address of the SMTP server. | The value can be a domain name or IP address (IPv4 or IPv6 address). The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits, and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |

##### Usage Guidelines

The system supports a maximum of two email servers. Ensure that the configuration of the two servers are the same.

##### Example

Adding the SMTP server whose IP address is "192.168.1.2".

```text
admin:/>add smtp_server general server=192.168.1.2
Command executed successfully.
```

##### System Response

None
