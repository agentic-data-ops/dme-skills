# Storage System Security Management Commands

The storage system provides multiple storage security functions including the access authentication for Lightweight Directory Application Protocol (LDAP) domains and the whitelist mechanism. This prevents unauthorized access to the storage system for improved system security.

## certificate

- change certificate auto_update: modify the automatic certificate update configuration.
- change certificate password: change the password for encrypting the private key of a certificate.
- change certificate prewarning_time: change the expiration warning days of certificates.
- delete certificate general: delete CA certificate information from an array.
- delete crl general: delete the certificate revocation list.
- export certificate: generate private keys and certificate request files based on application scenarios and export the certificate request files for subsequent signature and certificate import.
- import certificate: import a new private key, certificate, and CA certificate.
- import crl file: import a new certificate revocation list.
- show certificate general: query certificate information on storage arrays in various scenarios.
- show crl general: query certificate revocation list information on storage arrays in various scenarios.

## certificate_management

- change ca_server: modify the CA server configuration.
- show ca_server: query the CA server configuration.
- test ca_server: test the configuration of a CA server.

## domain

- change domain ad_config: change the name, site, and machine account of the domain controller, determine whether to overwrite the existing machine account when the storage array joins the AD domain, as well as determine whether to join or exit the domain.
- change domain ad_prefdc: modify information about the preferred domain controller.
- change domain dns_config: set the IP addresses of a vStore's DNS server.
- change domain ldap_config: modify the LDAP domain authentication configuration.
- change domain ldap_schema: modify LDAP domain authentication advanced configurations.
- change domain monitor: enable or disable the monitoring function for the external domain controller of the vStore and configure the monitoring period when the function is enabled.
- change domain nis_config: modify NIS domain authentication configurations.
- delete domain dns: delete the DNS server of a vStore.
- delete domain ldap: delete the configuration of the LDAP domain.
- delete domain ldap_schema: delete the advanced configuration of the LDAP domain.
- delete domain nis: initialize the configuration of an NIS domain.
- show domain ad: query the configuration of the AD domain controller and check whether the storage array has successfully joined the domain.
- show domain ad_prefdc: check the configuration of the preferred domain controller.
- show domain controller: query the domain controller list.
- show domain dns: query the IP addresses of a vStore's DNS server.
- show domain ldap: query LDAP domain authentication configurations.
- show domain ldap_schema: query LDAP domain authentication advanced configurations.
- show domain monitor: view the monitoring information of a domain controller.
- show domain nis: query NIS domain authentication configurations.
- show domain session: show session information between a storage device and an AD domain.
- test domain ad: test the connectivity of an AD domain server.
- test domain dns: test the connectivity of the DNS server.
- test domain ldap: test the connectivity of an LDAP server.
- test domain nis: test the connectivity of an NIS server.

## ldap

- change ldap configuration: modify the configuration of Lightweight Directory Application Protocol (LDAP) servers.
- create ldap configuration: configure the attributes associated with Lightweight Directory Application Protocol (LDAP) servers.
- delete ldap configuration: delete the configuration information on Lightweight Directory Application Protocol (LDAP) servers.
- show ldap configuration: query the configuration information on Lightweight Directory Application Protocol (LDAP) servers.

## security_rule

- add security_rule: add a security rule to control the maintenance terminals that attempt to access the storage system.
- change nas security: modify the NAS security policy of a vStore.
- change security_rule enabled: enable or disable security rules.
- delete security_rule: delete security rules.
- show nas security: query the security rules of the NAS protocol.
- show security_rule: query the information about security rules. Security rules are used to control the access of the storage system by maintenance terminals.Only the maintenance terminals in the security rules can access the storage system.
