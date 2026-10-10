# show dns_server general


##### Function

The **show dns_server general** command is used to check the management DNS server in a disk array.

##### Format

**show dns_server general**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Check the management DNS server in the current disk array.

```text
admin:/>show dns_server general
IP Address List : 192.168.1.8 192.168.1.9
Check Switch : On
Check Period(min) : 2
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                   |
|-------------------|---------------------------|
| IP Address List   | List of DNS IP addresses. |
| Check Switch      | Automatic check switch.   |
| Check Period(min) | Automatic check period.   |
