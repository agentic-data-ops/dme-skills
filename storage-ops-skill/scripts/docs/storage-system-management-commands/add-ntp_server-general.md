# add ntp_server general


##### Function

The **add ntp_server general** command is used to add an NTP server for time synchronization.

##### Format

**add ntp_server general** server=?

##### Parameters

| Parameter | Description         | Value                                                                                                                                                                                                                                                                                                        |
|-----------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server=?  | NTP server address. | The value can be a domain name or IP address (IPv4 or IPv6 address). The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |

##### Usage Guidelines

-   Two NTP servers can be configured for a system. Ensure that the time of the two NTP servers is consistent. If one server fails, you can synchronize the time from the other server to the faulty one.
-   If the time of the two servers is inconsistent, system time-hopping may occur, adversely affecting functions related to user management, alarms, and licenses.
-   Ensure that the time of NTP servers ranges from 2000-01-01/00:00:01 to 2035-12-31/23:59:59.

##### Example

Add the server whose IP address is 192.168.1.2 as a time synchronization server.

```text
admin:/>add ntp_server general server=192.168.1.2
WARNING: You are about to add the NTP server. This operation may make the time synchronization function malfunction if an NTP server already exists in the system and the time of the two NTP servers is different.
Suggestion: If an NTP server already exists in the system, ensure that the time of the two NTP servers is the same.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
