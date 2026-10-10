# remove ntp_server general


##### Function

The **remove ntp_server general** command is used to delete an NTP server used for time synchronization.

##### Format

**remove ntp_server general** server=?

##### Parameters

| Parameter | Description         | Value                                                                                                                                                                                                                                                                                                        |
|-----------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server=?  | NTP server address. | The value can be a domain name or IP address (IPv4 or IPv6 address). The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |

##### Usage Guidelines

None

##### Example

Delete the time synchronization server whose IP address is 192.168.1.2.

```text
admin:/>remove ntp_server general server=192.168.1.2
WARNING: You are about to delete the NTP server. This operation may make the time synchronization function unavailable.
Suggestion: Before performing this operation, ensure that the NTP server needs to be deleted.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
