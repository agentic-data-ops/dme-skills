# show domain ldap


##### Function

The **show domain ldap** command is used to query LDAP domain authentication configurations.

##### Format

**show domain ldap**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query LDAP domain authentication configurations.

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

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| IP Address List | IP address or host name of the LDAP server. A maximum of three IP addresses can be specified, and they must be separated from each other using commas (,). |
| Base DN | Base distinguished name (DN) of the LDAP directory, that is, the root directory of the LDAP server. |
| Port | LDAP listening port. |
| Password Hash | Password encryption method. The value can be "clear", "md5", or "crypt". |
| Transfer Type | LDAP encryption algorithm. The value can be "LDAP" or "LDAPS", where: <br>"LDAPS": The SSL encryption algorithm is enabled.<br>"LDAP": The SSL encryption algorithm is disabled. |
| User Suffix | Filter criteria for querying users. If this parameter is not configured, the querying starts from the root directory. |
| Group Suffix | Filter criteria for querying groups. If this parameter is not configured, the querying starts from the root directory. |
| Shadow Suffix | Filter criteria for querying passwords. If this parameter is not configured, the querying starts from the root directory. |
| Timelimit | The parameter specifies the amount of time to wait for a response to an LDAP query. |
| Bind Timelimit | The parameter specifies the amount of time to wait while trying to connect to an LDAP server. |
| Idle Timelimit | Client will close connections if the LDAP server has not been contacted for the number of seconds specified by the parameter. |
| Bind DN | A DN bound with an LDAP server. If anonymous binding is not available for an LDAP server, you must bind DNs before you can retrieve the information on users or user groups. |
| Netgroup DN | Filter criteria for querying netgroups. If this parameter is not configured, the querying starts from the root directory. |
| Bind Using the AD Credentials | Whether to use the AD domain account to bind. |
| User Search Scope | Range for querying the user. |
| Group Search Scope | Range for querying the group. |
| Netgroup Search Scope | Range for querying the netgroup. |
| Bind Authentication Level | Way of binding the storage array with the LDAP serevr. |
| Client Session Security | LDAP client signing security level. |
