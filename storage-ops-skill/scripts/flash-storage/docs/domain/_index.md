# domain

Manage authentication domains (AD, LDAP, NIS), including configuration, monitoring, and testing.

| command | function |
|---|---|
| change domain ad_config | change the name, site, and machine account of the domain controller, determine whether to overwrite the existing machine account when the storage array joins the AD domain, as well as determine whether to join or exit the domain. |
| change domain ad_prefdc | modify information about the preferred domain controller. |
| change domain dns_config | set the IP addresses of a vStore's DNS server. |
| change domain ldap_config | modify the LDAP domain authentication configuration. |
| change domain ldap_schema | modify LDAP domain authentication advanced configurations. |
| change domain monitor | enable or disable the monitoring function for the external domain controller of the vStore and configure the monitoring period when the function is enabled. |
| change domain nis_config | modify NIS domain authentication configurations. |
| delete domain dns | delete the DNS server of a vStore. |
| delete domain ldap | delete the configuration of the LDAP domain. |
| delete domain ldap_schema | delete the advanced configuration of the LDAP domain. |
| delete domain nis | initialize the configuration of an NIS domain. |
| show domain ad | query the configuration of the AD domain controller and check whether the storage array has successfully joined the domain. |
| show domain ad_prefdc | check the configuration of the preferred domain controller. |
| show domain controller | query the domain controller list. |
| show domain dns | query the IP addresses of a vStore's DNS server. |
| show domain ldap | query LDAP domain authentication configurations. |
| show domain ldap_schema | query LDAP domain authentication advanced configurations. |
| show domain monitor | view the monitoring information of a domain controller. |
| show domain nis | query NIS domain authentication configurations. |
| show domain session | show session information between a storage device and an AD domain. |
| test domain ad | test the connectivity of an AD domain server. |
| test domain dns | test the connectivity of the DNS server. |
| test domain ldap | test the connectivity of an LDAP server. |
| test domain nis | test the connectivity of an NIS server. |