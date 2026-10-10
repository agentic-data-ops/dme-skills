# show system dns_load_balance


##### Function

The **show system dns_load_balance** command is used to query information about DNS load balancing.

##### Format

**show system dns_load_balance**

##### Parameters

None

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query information about DNS load balancing.

```text
admin:/>show system dns_load_balance
Enabled  : Yes
Strategy : Weighted Round Robin
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                                             |
|-----------|-----------------------------------------------------|
| Enabled   | Whether the DNS load balancing function is enabled. |
| Strategy  | DNS load balancing policy.                          |
