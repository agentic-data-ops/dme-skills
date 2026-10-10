# change system dns_load_balance


##### Function

The **change system dns_load_balance** command is used to enable or disable the DNS load balancing function and configure the load balancing policy.

##### Format

**change system dns_load_balance** { enabled=? \| strategy=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled | Options for configuring the DNS load balancing function. | The value can be: <br>"yes": enables the DNS load balancing function.<br>"no": disables the DNS load balancing function. |
| strategy | Options for configuring the DNS load balancing strategy. | The value can be: <br>"weighted_round_robin": weighted round robin.<br>"cpu_usage": CPU usage.<br>"bandwidth_usage": bandwidth usage.<br>"open_connections": number of connections.<br>"overall_load": overall load. |

##### Usage Guidelines

Before performing this operation, determine whether the modification is necessary.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Enable the DNS load balancing function.

```text
admin:/>change system dns_load_balance enabled=yes
Command executed successfully.
```

Disable the DNS load balancing function.

```text
admin:/>change system dns_load_balance enabled=no
WARNING: You are about to disable the DNS load balancing function.
After the operation, you cannot use the domain name resolution service, and file systems cannot use the DNS load balancing function.
Suggestion: Before performing this operation, confirm that you want to disable the function.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Configure the load balancing policy as "weighted_round_robin".

```text
admin:/>change system dns_load_balance strategy=weighted_round_robin
WARNING: You are about to modify the DNS load balancing strategy. This operation will affect DNS load balancing effect.
Suggestion: Before performing this operation, ensure that the modified strategy is more suitable for the current service configuration.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
