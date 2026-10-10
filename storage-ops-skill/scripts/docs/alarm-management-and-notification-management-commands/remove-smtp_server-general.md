# remove smtp_server general


##### Function

The **remove smtp_server general** command is used to delete an email sending server.

##### Format

**remove smtp_server general** server=?

##### Parameters

| Parameter | Description                 | Value                                                                                                                                                                                                                                                                                                         |
|-----------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server=?  | Address of the SMTP server. | The value can be a domain name or IP address (IPv4 or IPv6 address). The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits, and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |

##### Usage Guidelines

None

##### Example

Delete the SMTP server whose IP address is "192.168.1.2".

```text
admin:/>remove smtp_server general server=192.168.1.2
WARNING: You are about to delete the SMTP server. This operation may make the alarm transfer to mailbox function unavailable.
Suggestion: Before performing this operation, ensure that the SMTP server needs to be deleted.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
