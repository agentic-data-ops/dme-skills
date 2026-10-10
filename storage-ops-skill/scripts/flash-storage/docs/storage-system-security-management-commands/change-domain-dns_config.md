# change domain dns_config


##### Function

The **change domain dns_config** command is used to set the IP addresses of a vStore's DNS server.

##### Format

**change domain dns_config** address=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| address=? | IP address list of the DNS server. | The value is an IP address list which contains a maximum of three IP addresses separated by commas (,), for example, "address=192.168.1.9,192.168.2.9,192.168.3.9". Both IPv4 and IPv6 addresses are supported and the IP address must be unique. |
| domains=? | Domain name list of the DNS server. | The value is a domain name list which contains a maximum of six domain names separated by commas (,), for example, "domains=domain1,domain2,domain3,domain4,domain5,domain6". Each domain name contains 1 to 255 characters and must be unique. A domain name has the following rules: <br>The domain name is case-insensitive.<br>The domain name contains only letters (a to z and A to Z), digits (0 to 9), periods (.), underscores (-), and hyphens (-). Each label separated by periods (.) must start or end with a letter or digit.<br>Each label separated by periods (.) contains a maximum of 63 characters. |

##### Usage Guidelines

None

##### Example

Set the IP addresses of the vStore's DNS server to "192.168.1.9", "192.168.2.9", and "192.168.3.9".

```text
admin:/>change domain dns_config address=192.168.1.9,192.168.2.9,192.168.3.9
Command executed successfully.
```

##### System Response

None
