# change domain ad_config


##### Function

The **change domain ad_config** command is used to change the name, site, and machine account of the domain controller, determine whether to overwrite the existing machine account when the storage array joins the AD domain, as well as determine whether to join or exit the domain.

##### Format

**change domain ad_config** { domain_name=? \| organization_unit=? \| system_name=? site_name=? \| ddns_enable=? \| ddns_ttl=? \| join_domain_enabled=? username=? password=? \[ overwrite_same_account=? \] } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| join_domain_enabled=? | Whether to join the domain. | The value can be "yes" or "no", where: <br>"yes": joins the domain.<br>"no": exits the domain. |
| username=? | Domain controller account that has the permission to add a machine account. | The value contains 1 to 63 characters. |
| password=? | Password of the domain controller account that has the permission to add a machine account. | The value contains 1 to 127 characters. |
| domain_name=? | Name of the domain that the storage array joins. | The value contains 1 to 127 characters. |
| organization_unit=? | Organization unit that is added when the storage array joins the domain. | The value contains 1 to 255 characters. |
| system_name=? | Name of the storage array added to the domain. | The name contains 1 to 15 characters, and cannot contain @#*()=+[]|;:",<>\/? or control characters. Characters such as ~!$%^&{}`' are not recommended. |
| site_name=? | Site where the domain controller resides when the storage array joins the domain. | The value contains 1 to 255 characters. |
| overwrite_same_account=? | Whether to overwrite the existing machine account when the storage array joins the domain. | The value can be "yes" or "no", where: <br>"yes": The existing machine account will be overwritten.<br>"no": The existing machine account will not be overwritten. |
| ddns_enable=? | Whether the DNS server update is allowed. | The value can be "yes" or "no", where: <br>"yes": The DNS server update is allowed.<br>"no": The DNS server update is not allowed. |
| ddns_ttl=? | Validity period of the DNS cache. | The value is an integer from 0 to 2592000. |

##### Usage Guidelines

If parameter "join_domain_enable" is specified, parameters "username" and "password" are mandatory and parameter "overwrite_same_account" is optional. If parameter "join_domain_enable" is set to "no", only parameters "username" and "password" can be specified.

##### Example

Query the configuration of the AD domain before the modification.

```text
admin:/>show domain ad
Domain Status : Joined
Full Domain Name : auth2k12.com
Organization Unit : CN=Computers,DC=auth2k12,DC=com
Cluster Name : storage
Site Name : china
Join Domain Error Info : --
DDNS Enabled : Enable
DDNS TTL(s) : 86400
```

Modify the configuration of the AD domain.

```text
admin:/>change domain ad_config system_name=storage site_name=china ddns_enable=yes ddns_ttl=172800 domain_name=auth2k12.com join_domain_enabled=yes username=user1 password=******** organization_unit=ou=test,dc=huawei,dc=com overwrite_same_account=yes
Command executed successfully.
```

Query the configuration of the AD domain after the modification.

```text
admin:/>show domain ad
Domain Status : Joined
Full Domain Name : auth2k12.com
Organization Unit : ou=test,dc=huawei,dc=com
System Name : storage
Site Name : china
Join Domain Error Info : --
DDNS Enabled : Enable
DDNS TTL(s) : 172800
```

Modify the configuration of the AD domain.

```text
admin:/>change domain ad_config join_domain_enabled=no username=test  password=********
WARNING: You are about to exit the AD domain.
After this operation, AD domain users cannot access CIFS share data, and services are interrupted.
Suggestion: Before performing this operation, ensure that:
1. The AD domain is no longer used by the current vStore.
2. Other vStores are not added to the AD domain using the same machine account. For example, if the vStore has been added to a HyperMetro vStore pair, you must check whether the vStore on the remote storage array needs to use the AD domain.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
