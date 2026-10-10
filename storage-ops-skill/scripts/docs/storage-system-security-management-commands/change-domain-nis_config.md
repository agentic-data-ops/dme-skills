# change domain nis_config


##### Function

The **change domain nis_config** command is used to modify NIS domain authentication configurations.

##### Format

**change domain nis_config** domain_name=? server_ip_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_name=? | A domain name contains 1 to 63 characters chosen from letters, digits, underscores (_), and hyphens (-), and cannot start or end with an underscore (_) or a hyphen (-). A domain name at each level can contain a maximum of 63 characters. Domain names at various levels are separated by periods (.). For example, domain.com,domain.net. | The value consists of 1 to 63 characters. |
| server_ip_list=? | NIS server address or host name. A maximum of three IP addresses are supported. Use commas (,) to separate IP addresses. | IP address: A maximum of three IP addresses (IPv4 addresses) are supported. Use commas (,) to separate IP addresses. Host name: <br>Contains 1 to 255 letters, digits, hyphens (-), periods (.), and underscores (_).<br>Must start with a letter or digit and cannot end with a hyphen (-) or underscore (_).<br>Cannot contain consecutive periods (.), pure digits (.), or the combination of a period and underscore (._ or _.). |

##### Usage Guidelines

None

##### Example

Query NIS domain authentication configurations before the modification.

```text
admin:/>show domain nis

IP Address List :
Name           :
```

Modify NIS domain authentication configurations.

```text
admin:/>change domain nis_config domain_name=nisdomain server_ip_list=10.40.25.10,10.40.25.11,10.40.25.12
WARNING:You are about to run the command for configuring the NIS domain. The NIS domain does not support encrypted transmission, which may cause security risks.
Suggestion: Before performing this operation, ensure that the risk is acceptable.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query NIS domain authentication configurations after the modification.

```text
admin:/>show domain nis
IP Address List : 10.40.25.10 10.40.25.11 10.40.25.12
Name            : nisdomain
```

##### System Response

None
