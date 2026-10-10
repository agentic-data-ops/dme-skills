# add security_rule


##### Function

The **add security_rule** command is used to add a security rule to control the maintenance terminals that attempt to access the storage system.

##### Format

**add security_rule** ip_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip_list=? | IP address white list of the security rule. Only the maintenance terminals whose IP addresses are in the white list can access the storage system. | The value can either be an IP address or an IP address segment. For an IP address segment, the value must be expressed in the following format: start IP address-end IP address. For example: <br>IP address: 192.168.3.5.<br>IP address segment: 192.168.3.5-192.168.3.32. |

##### Usage Guidelines

-   Only the maintenance terminals whose IP addresses are in the white list of the security rule can access the storage system.
-   The white list takes effect only after you enable the security rule by running "change security_rule enabled".

##### Example

Add IP address "192.168.6.5" to the white list of the security rule.

```text
admin:/>add security_rule ip_list=192.168.6.5
CAUTION: You are about to add an IP address white list. This operation will make the IP addresses in this white list able to access the storage system when the IP address security rule is enabled.
Suggestion: Confirm that you need to add this IP address white list and the IP addresses in the white list are correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Add IP address segment "192.168.7.3" to "192.168.7.46" to the white list of the security rule.

```text
admin:/>add security_rule ip_list=192.168.7.3-192.168.7.46
CAUTION: You are about to add an IP address white list. This operation will make the IP addresses in this white list able to access the storage system when the IP address security rule is enabled.
Suggestion: Confirm that you need to add this IP address white list and the IP addresses in the white list are correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
