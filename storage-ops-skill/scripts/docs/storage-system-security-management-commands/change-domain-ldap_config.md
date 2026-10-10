# change domain ldap_config


##### Function

The **change domain ldap_config** command is used to modify the LDAP domain authentication configuration.

##### Format

**change domain ldap_config** server_ip_list=? transfer_type=? base_dn=? password_hash=? port=? \[ \[ user_suffix=? \] \| \[ group_suffix=? \] \| \[ shadow_suffix=? \] \| \[ bind_dn=? bind_password=? \] \| \[ timelimit=? \] \| \[ bind_timelimit=? \] \| \[ idle_timelimit=? \] \| \[ netgroup_dn=? \] \| \[ bind_level=? \] \| \[ user_search_scope=? \] \| \[ group_search_scope=? \] \| \[ netgroup_search_scope=? \] \| \[ bind_using_ad_credentials=? \] \| \[ client_session_security=? \] \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| server_ip_list=? | IP address or host name of the LDAP server. | For IP addresses: A maximum of 64 IP addresses (IPv4 or IPv6 addresses) are supported. Use commas (,) to separate IP addresses. It is recommended that the IP address that can be used to connect to the storage device be placed in front of the IP address list. For host names: <br>A host name contains 1 to 255 letters, digits, hyphens (-), periods (.), and underscores (_).<br>A host name must start with a letter or digit and cannot end with a hyphen (-) or underscore (_).<br>A host name cannot contain consecutive periods (..), pure digits, or the combination of a period and underscore (._ or _.). |
| transfer_type=? | LDAP encryption algorithm. | The value can be "LDAP" or "LDAPS", where: <br>"LDAPS": The SSL encryption algorithm is enabled.<br>"LDAP": The SSL encryption algorithm is disabled.<br> NOTE: To ensure secure data transmission, you are advised to use Secure Sockets Layer(SSL) encryption. Before selecting the LDAPS protocol, use the "import certificate" command to import the CA certificate file for the LDAP domain server. |
| base_dn=? | Base distinguished name (DN) of the LDAP directory, that is, the root directory of the LDAP server. | The value is in the format of "cn=?, ou=?, dc=?" and consists of 1 to 1024 characters. |
| password_hash=? | Password encryption method. | The value can be "clear", "md5", or "crypt", where: <br>"clear": clear encryption.<br>"md5": MD5 encryption.<br>"crypt": crypt encryption.<br> NOTE: Because clear and MD5 are unsafe for secure data transmission, you are advised to use crypt encryption. |
| port=? | LDAP listening port. | The value is an integer ranging from 1 to 65,535. The default port number is "389" for LDAP and "636" for LDAPS. |
| user_suffix=? | Filter criteria for querying users. If this parameter is not configured, the querying starts from the root directory. | The value is in the format of "cn=?, ou=?, dc=?" and consists of 1 to 1024 characters. |
| group_suffix=? | Filter criteria for querying groups. If this parameter is not configured, the querying starts from the root directory. | The value is in the format of "cn=?, ou=?, dc=?" and consists of 1 to 1024 characters. |
| shadow_suffix | Filter criteria for querying passwords. If this parameter is not configured, the querying starts from the root directory. | The value is in the format of "cn=?, ou=?, dc=?" and consists of 1 to 1024 characters. |
| bind_dn=? | DN bound with an LDAP server. If anonymous binding is not available for an LDAP server, you must bind DNs before you can retrieve the information on users or user groups. | The value is in the format of "cn=?, ou=?, dc=?" and consists of 1 to 1024 characters. |
| bind_password=? | Password for login. The password must be the same as that for logging in to the LDAP server. | The value consists of 1 to 63 characters. |
| timelimit=? | Timeout threshold of waiting for a response to an LDAP query request. | The value is an integer ranging from 0 to 2147483647. NOTE: Value "0" indicates no timeout limit. |
| bind_timelimit=? | Timeout threshold of setting up connections between a client and server. | The value is an integer ranging from 1 to 2,147,483,647. |
| idle_timelimit=? | Timeout threshold of client connections when the LDAP connection is idle. | The value is an integer ranging from 0 to 2,147,483,647. NOTE: Value "0" means no timeout limit. |
| netgroup_dn=? | Filter criteria for querying netgroups. If this parameter is not configured, the querying starts from the root directory. | The value is in the format of "cn=?, ou=?, dc=?" and consists of 1 to 1024 characters. |
| bind_level=? | Way of binding the storage array with the LDAP server. | The value can be "simple" or "SASL", where: <br>"simple": simple authentication method.<br>"SASL": SASL authentication method. |
| user_search_scope=? | Range for querying the user. | The value can be "subtree", "onelevel", or "base", where: <br>"subtree": queries all items at all levels, including the specified basic DN.<br>"onelevel": queries all items at the next level of the basic DN.<br>"base": only queries items under the basic DN. |
| group_search_scope=? | Range for querying the group. | The value can be "subtree", "onelevel", or "base", where: <br>"subtree": queries all items at all levels, including the specified basic DN.<br>"onelevel": queries all items at the next level of the basic DN.<br>"base": only queries items under the basic DN. |
| netgroup_search_scope=? | Range for querying the netgroup. | The value can be "subtree", "onelevel", or "base", where: <br>"subtree": queries all items at all levels, including the specified basic DN.<br>"onelevel": queries all items at the next level of the basic DN.<br>"base": only queries items under the basic DN. |
| bind_using_ad_credentials | Whether to use the AD domain account to bind. | The value can be "true" or "false", where: <br>"true": uses the AD domain account to bind.<br>"false": does not use the AD domain account to bind. |
| client_session_security=? | LDAP client signing security level. | The value can be "none", "sign", or "seal", where: <br>"none": The LDAP BIND request is not signed.<br>"sign": The LDAP BIND request is signed.<br>"seal": The LDAP BIND request is sealed. |

##### Usage Guidelines

-   If parameter "bind_dn" is specified, parameter "bind_password" is required.
-   When parameters "bind_dn" and "bind_level" are not specified and the value of "bind_using_ad_credentials" is "false", use the anonymous method to connect to the LDAP server.

##### Example

Query LDAP domain authentication configurations before the modification.

```text
admin:/>show domain ldap

IP Address List :
Base DN         :
Port            :
Password Hash   : --
Transfer Type   : --
User Suffix     :
Group Suffix    :
Shadow Suffix   :
Timelimit       : 3
Bind Timelimit  : 3
Idle Timelimit  : 30
Bind DN         :
Netgroup DN :
Bind Using the AD Credentials: True
User Search Scope: Subtree
Group Search Scope: Subtree
Netgroup Search Scope: Subtree
Bind Authentication Level: Simple
Client Session Security: None
```

Modify the LDAPS domain authentication configuration.

```text
admin:/>change domain ldap_config server_ip_list=10.40.25.8 transfer_type=LDAPS base_dn=dc=vendor,dc=com password_hash=md5 port=636 group_suffix=dc=vendor,dc=com shadow_suffix=dc=vendor,dc=com user_suffix=dc=vendor,dc=com bind_dn=cn=root,dc=vendor,dc=com bind_password=********* netgroup_dn=dc=vendor,dc=com bind_level=simple user_search_scope=subtree group_search_scope=subtree netgroup_search_scope=subtree bind_using_ad_credentials=true client_session_security=sign
Command executed successfully.
```

Query the LDAPS domain authentication configuration after the modification.

```text
admin:/>show domain ldap

IP Address List : 10.40.25.8
Base DN         : dc=vendor,dc=com
Port            : 636
Password Hash   : Md5
Transfer Type   : LDAPS
User Suffix     : dc=vendor,dc=com
Group Suffix    : dc=vendor,dc=com
Shadow Suffix   : dc=vendor,dc=com
Timelimit       : 3
Bind Timelimit  : 3
Idle Timelimit  : 30
Bind DN         : cn=root,dc=vendor,dc=com
Netgroup DN :
Bind Using the AD Credentials: True
User Search Scope: Subtree
Group Search Scope: Subtree
Netgroup Search Scope: Subtree
Bind Authentication Level: Simple
Client Session Security: Sign
```

Modify the LDAP domain authentication configuration.

```text
admin:/>change domain ldap_config server_ip_list=10.40.25.8 transfer_type=LDAP base_dn=dc=vendor,dc=com password_hash=md5 port=389 group_suffix=dc=vendor,dc=com shadow_suffix=dc=vendor,dc=com user_suffix=dc=vendor,dc=com bind_dn=cn=root,dc=vendor,dc=com bind_password=*********
netgroup_dn=dc=vendor,dc=com bind_level=simple user_search_scope=subtree group_search_scope=subtree netgroup_search_scope=subtree bind_using_ad_credentials=true client_session_security=none
Command executed successfully.
```

Query the LDAP domain authentication configuration after the modification.

```text
admin:/>show domain ldap

IP Address List : 10.40.25.8
Base DN         : dc=vendor,dc=com
Port            : 389
Password Hash   : Md5
Transfer Type   : LDAP
User Suffix     : dc=vendor,dc=com
Group Suffix    : dc=vendor,dc=com
Shadow Suffix   : dc=vendor,dc=com
Timelimit       : 3
Bind Timelimit  : 3
Idle Timelimit  : 30
Bind DN         : cn=root,dc=vendor,dc=com
Netgroup DN :
Bind Using the AD Credentials: True
User Search Scope: Subtree
Group Search Scope: Subtree
Netgroup Search Scope: Subtree
Bind Authentication Level: Simple
Client Session Security: None
```

##### System Response

None
